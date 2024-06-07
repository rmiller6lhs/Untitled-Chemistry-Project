import os.path
import PySimpleGUI as sg
from loaders.util_loader import UtilLoader

class Windows:
    def __init__(self):
        self.gui_utils = UtilLoader('gui_util').utils
        
    def main_window(self):
        
        