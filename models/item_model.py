'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
from typing import Union
from pydantic import BaseModel

class Item(BaseModel):
    '''Uma classe Item e dentro (BaseModel) a classe pai'''
    name: str
    price: float
    is_offer: Union[bool, None] = None
    