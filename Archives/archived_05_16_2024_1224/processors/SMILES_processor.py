import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from input_processor import InputProcessor
from loaders.util_loader import UtilLoader

class Smiles:
    def __init__(self,formula):
        self.formula = formula
        self.formula_processed = InputProcessor(self.formula)
        self.element_counts = self.formula_processed.element_counts
        
    def covionic_processor(self):
        self.elements_data = UtilLoader(
            util='element_data',
            extract_feats=True,
            feats=['classif'],
            elemenets=self.formula_processed.keys(),
            ).extracted_elements_data
        