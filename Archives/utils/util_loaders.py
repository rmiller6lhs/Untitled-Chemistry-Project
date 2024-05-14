class UtilLoader:
    
    def __init__(self,loader_call):
        self.loader_call = loader_call
        
        
    def element_data_loader(self):
        #load element data
        elements_fpath = os.path.dirname(os.path.abspath(__file__)) + '/utils/elements.json'
        with open(elements_fpath,'r') as f:
            self.elements_data = json.load(f)