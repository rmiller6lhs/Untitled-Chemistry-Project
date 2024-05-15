from loaders.util_loader import UtilLoader
from processors.input_processor import InputProcessor
class LewisCalculator:
    def __init__(self,formula):
        #Self declarations
        self.formula = formula
        
        #Process input formula and extract element data
        self.processed_data = InputProcessor(self.formula)
        self.element_counts = self.processed_data.element_counts
        self.element_data_extracted = UtilLoader(
            util='element_data',
            extract_feats=True,
            feats=[
                'electronegativity',
                'num_valence_electrons',
                'radius',
                ])
        print(self.element_data_extracted)
        self.element_feats = self.element_data_extracted.extracted_element_data
        #Class function calls
        self.lewis_config()
        
    def en_calc(self,en1,en2):
        return abs(en1-en2)
    
    def lewis_config(self):
        
        ele_symbols = list(self.element_counts.keys())
        ele_en = [self.element_feats[ele]['electronegativity'] for ele in ele_symbols]
        ele_val_elec = [self.element_feats[ele]['num_valence_electrons'] for ele in ele_symbols]
        ele_radii = [self.element_feats['ele']['radius']]
        
        '''print(ele_symbols)
        print(ele_en)
        print(ele_val_elec)'''
        
        
#UtilLoader is returning an empty dictionary...why?
     