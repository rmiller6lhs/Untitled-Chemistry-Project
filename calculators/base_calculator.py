from processors.input_processor import InputProcessor
from loaders.util_loader import UtilLoader

class BaseCalculator:
    
    def __init__(self,formula):
        #Self declarations
        self.formula = formula
        self.molecule_data = InputProcessor(self.formula).element_counts
        
        #Call simple calculators
        self.molar_mass()
        self.percent_comp()

    def molar_mass(self):
        #Call util_loader to get element data
        self.util_data = UtilLoader(util='element_data')
        self.elements_data = self.util_data.elements_data
        
        #Calculate molar mass
        molecule_mass = 0
        for element,count in self.molecule_data.items():
            element_dict = self.elements_data[element]
            element_mass = element_dict['mass']
            element_contribution = element_mass*count
            molecule_mass += element_contribution
            
            #Add molar mass to element data lists
            self.molecule_data[element] = [count,element_contribution]
            
        #Set molar mass to its own variable
        self.molecule_mass = molecule_mass
        
    def percent_comp(self):
        #Calculate percent composition for each element
        for element,value in self.molecule_data.items():
            value.append(100*value[1]/self.molecule_mass)
            self.molecule_data[element] = value
     

    
    
            
        