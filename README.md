# Grocery Store API Tests using Python

This is an API automation testing project built with Python using the Simple Grocery Store API.

API Documentation:
[simple-grocery-store-api.md
](https://github.com/vdespa/Postman-Complete-Guide-API-Testing/blob/main/simple-grocery-store-api.md)

## Project Overview

This project covers several API testing scenarios such as:

- GET all products
- GET product by ID
- GET invalid product
- POST create cart
- POST add item to cart
- POST create order
- GET all orders

The project includes:
- status code validation
- response body validation
- data type validation
- negative testing
- authentication with Bearer Token
- chained API requests
- dynamic test data generation

---

## Dependencies
Install the following libraries:

- pip install requests
- pip install pytest

## How to run the tests
Run the following command in your terminal:

pytest APItestsWithPython.py -v
