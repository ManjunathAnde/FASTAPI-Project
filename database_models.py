from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

dec_base= declarative_base()

class Products (dec_base): 
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    description=Column(String)
    price=Column(String)
    quantity=Column(String)