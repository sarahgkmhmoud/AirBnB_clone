#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place  # Import the Place class
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)


print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("___newobject____")
newUser = User()

print(f"new: {storage.new(newUser)}")
print(f"NewUsr: {newUser}")



print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a new State --")
my_State = State()
my_State.name = "Egypt"
my_State.save()
print(my_State)

print("-- Create a new City --")
my_city = City()
my_city.name = "Aswan"
my_city.state_id = my_State.id
my_city.save()
print(my_city)

print("-- Create a new Amenity --")
my_amenity = Amenity()
my_amenity.name = "WiFi"
my_amenity.save()
print(my_amenity)

print("__Create a new Place__")
my_place = Place()
my_place.city_id = my_city.id
my_place.user_id = my_user.id
my_place.name = "Awesome Place"
my_place.description = "A cozy place near the Nile"
my_place.number_rooms = 3
my_place.number_bathrooms = 2
my_place.max_guest = 6
my_place.price_by_night = 100
my_place.latitude = 25.276987
my_place.longitude = 32.539527
my_place.amenity_ids = [my_amenity.id]  # Set the Amenity list

my_place.save()
print(my_place)

print("__Create a new Place__")
my_review = Review()
my_review.place_id = my_place.id
my_review.user_id = my_user2.id
my_review.text = "Great place to stay!"
my_review.save()
print(my_review)