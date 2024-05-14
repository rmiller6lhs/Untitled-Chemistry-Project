import json
import re
import os
import numpy as np
import pandas as pd

if __name__ == '__main__':
    from .processor.input_processor import InputProcessor
    from .calculators.base_calculator import BaseCalculator