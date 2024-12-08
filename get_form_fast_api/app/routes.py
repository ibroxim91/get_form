from fastapi import APIRouter
from .db import collection
from .models import FormData
from .validate import determine_field_type

router = APIRouter()

@router.post("/get_form")
async def get_form(form_data: FormData):
    # JSON 
    form_data_dict = form_data.root

    # MongoDB-
    templates = list(collection.find())

    for template in templates:
        matches = True
        for field_name, field_type in template.items():
            if field_name == "name" or field_name == "_id":
                continue
            if field_name not in form_data_dict or determine_field_type(form_data_dict[field_name]) != field_type:
                matches = False
                break
        if matches:
            return {"template_name": template["name"]}

    field_types = {field: determine_field_type(value) for field, value in form_data_dict.items()}
    return {"field_types": field_types}
