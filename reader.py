# Libs
import pandas as pd

"""
Universidad del Valle de Guatemala
Author: Oliver Milian
Purpose: CSV loader
"""
class reader(object):
    # Loads the CSV doc
    def __init__(self, csvDoc):
        self.fuel = pd.read_excel(csvDoc, index_col=0)

