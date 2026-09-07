from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

dec_base= declarative_base()

class Products(dec_base): 
    __tablename__ = "fastapi_main"  
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    description = Column(String(500))
    price = Column(String(20))
    quantity = Column(Integer)