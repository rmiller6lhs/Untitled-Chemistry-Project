import json
import os

class UtilLoader:
    def __init__(self,util,extract_feats=False,feats=[],elements=[]):
        self.util = util
        self.extract_feats = extract_feats
        if self.extract_feats == True:
            self.feats = feats
            self.elements = elements
        
        if self.util == 'element_data':
            self.element_data_loader()
            
        if self.extract_feats == True:
            self.element_extractor()
        
    def element_data_loader(self):
        #load element data
        elements_fpath = os.getcwd()+'/utils/elements.json'
        with open(elements_fpath,'r') as f:
            self.elements_data = json.load(f)
            
    def element_extractor(self):
        '''
        Extracts an element and the desired data from the element's entry from 
        the json file.
        
        the __args__ variable will contain
        '''
        
        self.extracted_element_data = {
            element:{feat:self.elements_data[element][feat] 
                     for feat in self.feats
                } 
            for element in self.elements
            }