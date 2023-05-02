"""
Object class's used in the game are defined here.
"""

from .ability import *
from .event import *
from .role import *


def read_objects_from_excel(filepath):
    xl = pd.ExcelFile(filepath)
    objects_dict = {}
    for sheet_name in xl.sheet_names:
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        objects_list = []
        for _, row in df.iterrows():
            obj = #add whatever object you felt like adding
            objects_list.append(obj)
        objects_dict[sheet_name] = objects_list
    return objects_dict

print("READ OBJECTS FROM EXCEL FILE " + ead_objects_from_excel(filepath))
