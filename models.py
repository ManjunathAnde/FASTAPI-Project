from pydantic import BaseModel 

class Products (BaseModel): 
    id: int #Using Python Hints to predefine data types
    name:str
    description:str
    price:float
    quantity:int
#Pydantic takes care of the constructor
