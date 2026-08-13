from fastapi import FastAPI
from models import Products
app = FastAPI() #creating an instance of FASTAPI

@app.get("/") # using GET HTTP method to see information in homepage
def greet():
    return "Welcome to MJ APP"

products = [  #Instantiating the classes
    Products(1, "CRICKET BAT", "ADIDAS", 2000, "5"),
    Products(2, "OPPO PHONE", "256 GB", 55000, "12")
]

@app.get("/products") #usinf GET method to display information when the user routes to 'skills' in the web app. 
def get_products():
    return products
