from pymongo import MongoClient
from django.conf import settings


client = MongoClient(settings.MONGO_URI)
db = client["form_templates"]
collection = db["templates"]

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

if collection.count_documents({}) == 0:
    collection.insert_many(templates)
    

