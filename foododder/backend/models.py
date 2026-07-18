from database import restaurants_collection, foods_collection
from seed_data import restaurants, foods   
from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

restaurants_collection.insert_many(restaurants)

foods_collection.insert_many(foods)

print("Data inserted successfully!")