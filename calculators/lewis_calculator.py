from loaders.util_loader import UtilLoader
from processors.input_processor import InputProcessor
import numpy as np
class LewisCalculator:
    def __init__(self,formula):
        #Self declarations
        self.formula = formula
        self.singles = ['H','Li','Na','K','Rb','Cs','Fr','F','Cl','Br','I']
        
        #Process input formula and extract element data
        self.processed_data = InputProcessor(self.formula)
        self.elements = list(self.processed_data.element_counts.keys())
        self.element_data_extracted = UtilLoader(
            util='element_data',
            extract_feats=True,
            feats=[
                'electronegativity',
                'num_valence_electrons',
                'radius',
                'classif'
                ],elements=self.elements)
        self.element_feats = self.element_data_extracted.extracted_element_data
        #Class function calls
        self.lewis_config()
        
    def en_calc(self,en1,en2):
        return abs(en1-en2)
    
    def lewis_config(self):
        
        #Extract specific features of each element's data set
        ele_en = [float(self.element_feats[element]['electronegativity']) for element in self.elements]
        ele_valence_electrons = [int(self.element_feats[element]['num_valence_electrons']) for element in self.elements]
        ele_radii = [self.element_feats[element]['radius'] for element in self.elements]
        ele_classes = [self.element_feats[element]['classif'] for element in self.elements]
        total_electrons = sum(ele_valence_electrons)
        non_single_elements = [element for element in self.elements if element not in self.singles]
        non_single_elements_en = [en for i,en in enumerate(ele_en) if self.elements[i] not in self.singles]
        
        
        
        if len(self.elements) > 2:
            lowest_en_element_symb = non_single_elements[np.argmin(non_single_elements_en)]
            lowest_en_element_idx = self.elements.index(lowest_en_element_symb)
            if ele_classes[lowest_en_element_idx] == 'Transition Metals':
                expanded_octet = True
            
        element_bonds = {}
        
        
        
        
        
        
     