import json
from .validate import determine_field_type
from rest_framework.views import APIView
from rest_framework.response import Response 
from .db import collection


class GetFormView(APIView):

    def post(self, request):
        try:
            form_data = json.loads(request.body)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=400)

        templates = list(collection.find())

        for template in templates:
            matches = True
            for field_name, field_type in template.items():
                if field_name == "name" or field_name == "_id":
                    continue
                if field_name not in form_data or determine_field_type(form_data[field_name]) != field_type:
                    matches = False
                    break
            if matches:
                return Response({"template_name": template["name"]})

        field_types = {field: determine_field_type(value) for field, value in form_data.items()}
        return Response(field_types, status=200)

