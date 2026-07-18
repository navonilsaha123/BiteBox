from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import restaurants_collection, foods_collection
from bson import ObjectId
from database import users_collection
from models import UserRegister, UserLogin
from auth_utils import hash_password, verify_password
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc


@app.get("/restaurants")
def get_restaurants():
    restaurants = restaurants_collection.find()
    return [serialize(r) for r in restaurants]


@app.get("/foods")
def get_foods():
    foods = foods_collection.find()
    return [serialize(f) for f in foods]


@app.get("/restaurants/{restaurant_id}/foods")
def get_foods_by_restaurant(restaurant_id: int):

    restaurant = restaurants_collection.find_one({"id": restaurant_id})

    if not restaurant:
        return {"error": "Restaurant not found"}

    foods = foods_collection.find({"restaurant": restaurant["name"]})

    return [serialize(f) for f in foods]


@app.get("/foods/mood/{mood}")
def get_foods_by_mood(mood: str):

    foods = foods_collection.find({"moods": mood})

    return [serialize(f) for f in foods]


@app.get("/foods/category/{cat}")
def get_foods_by_category(cat: str):

    foods = foods_collection.find({"cats": cat})

    return [serialize(f) for f in foods]


@app.get("/foods/veg/{is_veg}")
def get_foods_veg(is_veg: bool):

    foods = foods_collection.find({"veg": is_veg})

    return [serialize(f) for f in foods]

@app.post("/register")
def register(user: UserRegister):

    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)

    new_user = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "password": hashed_pw,
        "phone": user.phone,
        "created_at": datetime.utcnow()
    }

    users_collection.insert_one(new_user)

    return {"message": "User registered successfully"}


@app.post("/login")
def login(user: UserLogin):

    db_user = users_collection.find_one({"email": user.email})

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email")

    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid password")

    return {
        "message": "Login successful",
        "user": {
            "name": db_user["first_name"] + " " + db_user["last_name"],
            "email": db_user["email"],
            "phone": db_user["phone"]
        }
    }