"""
Here are the functions used to read data from the excel file, so it is
easy to modify and build the game without having to change the code to contain
new data.
"""

import pandas as pd

class Excel():
    """ The functions used to read game data from an excel file. """
    @staticmethod
    def read_objects_from_excel(filepath):
        xl = pd.ExcelFile(filepath)
        objects_dict = {}
        for sheet_name in xl.sheet_names:
            df = pd.read_excel(filepath, sheet_name=sheet_name)
            objects_list = []
            for _, row in df.iterrows():
                obj = row #add whatever object you felt like adding
                objects_list.append(obj)
            objects_dict[sheet_name] = objects_list
        return objects_dict
