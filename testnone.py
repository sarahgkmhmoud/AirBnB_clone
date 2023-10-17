#!/usr/bin/python3
from models.review import Review

print(type(Review.place_id) is str)
print(Review.place_id == "")

print(type(Review.user_id) is str)
print(Review.user_id == "")

print(type(Review.text) is str)
print(Review.text == "")