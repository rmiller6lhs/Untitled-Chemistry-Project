import json
import pathlib
import os
from input_processor import InputProcessor

class Calculator:
    def __init__(self,formula,**calculations):
        self.formula = formula
        self.__kwargs__ = calculations
        self.element_counts = InputProcessor(self.formula).element_counts
        self.molar_mass()
    def molar_mass(self):
        self.util_loader()
        
        
    def util_loader(self):
        
        elements_fpath = os.path.dirname(os.path.abspath(__file__))
        print(elements_fpath)
        
        with open(elements_fpath,'r') as f:
            elements_data = json.open(f)
            
        print(elements_data)
        

        