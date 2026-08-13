from fastapi import FastAPI
from models import Products
app = FastAPI() #creating an instance of FASTAPI

@app.get("/") # using GET HTTP method to see information in homepage
def greet():
    return "Welcome to MJ APP"

products = [  #Instantiating the classes
    Products(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Products(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Products(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Products(id=4, name="Table", description="A wooden table", price=199.99, quantity=20)
]

@app.get("/products") #usinf GET method to display information when the user routes to 'skills' in the web app. 
def get_products():
    return products

sno:int=1
@app.get("/products/{sno}") #A dynamic URL to fetch products by ID
def get_single_product(sno:int): 
    for product in products: #Looking up the product roster to find matching ID
        if product.id == sno:
            return{'message': 'Hurray! Product found',
                   'prod_details': product
                   } #If found, return the instance.