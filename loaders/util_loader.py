import json
import os
import pathlib
class UtilLoader:
    def __init__(self,util):
        self.util = util
        
        if self.util == 'element_data':
            self.element_data_loader()
        
    def element_data_loader(self):
        #load element data
        elements_fpath = os.getcwd()+'/utils/elements.json'
        with open(elements_fpath,'r') as f:
            self.elements_data = json.load(f)