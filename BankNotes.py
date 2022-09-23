# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 10:33:15 2022

@author: rishi
"""


from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
    
