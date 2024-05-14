import json
import os
from input_processor import InputProcessor

class Calculator:
    def __init__(self,formula,**calculations):
        self.formula = formula
        self.__kwargs__ = calculations
        self.element_counts = InputProcessor(self.formula).element_counts
        if self.__kwargs__['molar_mass'] == True:
            self.molar_mass()
            
        if self.__kwargs__['percent_comp'] == True:
            self.percent_comp()
        
        
    def molar_mass(self):
        self.util_loader()
        molecule_mass = 0
        for element,count in self.element_counts.items():
            element_dict = self.elements_data[element]
            element_mass = element_dict['mass']
            element_contribution = element_mass*count
            molecule_mass += element_contribution
            if self.__kwargs__['percent_comp'] == True:
                self.element_counts[element] = [count,element_contribution]
        self.molecule_mass = molecule_mass
        
    def percent_comp(self):
        
        for element,value in self.element_counts.items():
            #self.element_counts[element] = value.append(100*value[1]/self.molecule_mass)
            print(value)
        print(self.element_counts)
        
    def util_loader(self):
        
        elements_fpath = os.path.dirname(os.path.abspath(__file__)) + '/utils/elements.json'
        with open(elements_fpath,'r') as f:
            self.elements_data = json.load(f)
            
        