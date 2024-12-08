from fastapi import FastAPI
from app import collection, router

app = FastAPI()


app.include_router(router)

@app.on_event("startup")
async def populate_templates():
    if collection.count_documents({}) == 0:
        templates = [
            {
                "name": "Order Form",
                "email": "email",
                "phone": "phone",
                "order_date": "date",
            },
            {
                "name": "Contact Form",
                "lead_email": "email",
                "user_phone": "phone",
                "submission_date": "date",
            },
        ]
        collection.insert_many(templates)
        print("Added templates")
