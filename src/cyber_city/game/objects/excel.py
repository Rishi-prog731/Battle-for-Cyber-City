"""
Here are the functions used to read data from the excel file, so it is
easy to modify and build the game without having to change the code to contain
new data.
"""

import pandas as pd

'''
class Excel:
    """The functions used to read game data from an excel file."""
    This is an old version that does not use the CyberCityGameRules. It is a general read in structure.
    @staticmethod
    def read_objects_from_excel(filepath):
        xl = pd.ExcelFile(filepath)
        objects_dict = {}
        for sheet_name in xl.sheet_names:
            df = pd.read_excel(filepath, sheet_name=sheet_name)
            objects_list = []
            for _, row in df.iterrows():
                obj = row  # add whatever object you felt like adding
                objects_list.append(obj)
            objects_dict[sheet_name] = objects_list
        return objects_dict
'''
 """Import statements"""  
import pandas as pd
"""Main class variables"""
class CyberCityGameRules:
    def __init__(self, turns, budget, actions_per_turn, defender_turn, attacker_turn, compromise_threshold):
        self.turns = turns
        self.budget = budget
        self.actions_per_turn = actions_per_turn
        self.defender_turn = defender_turn
        self.attacker_turn = attacker_turn
        self.compromise_threshold = compromise_threshold

"""
Reading in file using pandas
"""
df = pd.read_excel('game_rules.xlsx')
"""
Getting values of variables from excel file
"""
turns = df.loc[df['Rule'] == 'Turns', 'Description'].values[0]
budget_defender = df.loc[df['Rule'] == 'Budget', 'Defender'].values[0]
budget_attacker = df.loc[df['Rule'] == 'Budget', 'Attacker'].values[0]
actions_per_turn = df.loc[df['Rule'] == 'Action per turn', 'Description'].values[0]
defender_turn_desc = df.loc[df['Rule'] == "Defender's turn", 'Description'].values[0]
defender_turn_success_rate = df.loc[df['Rule'] == "Defender's turn", 'Success rate'].values[0]
attacker_turn_desc = df.loc[df['Rule'] == "Attacker's turn", 'Description'].values[0]
attacker_turn_success_rate = df.loc[df['Rule'] == "Attacker's turn", 'Success rate'].values[0]
compromise_threshold = df.loc[df['Rule'] == 'Compromise Threshold', 'Description'].values[0]

"""Creating object using the variables from excel"""
game_rules = CyberCityGameRules(turns=turns, 
                                budget={'defender': budget_defender, 'attacker': budget_attacker},
                                actions_per_turn=actions_per_turn,
                                defender_turn={'description': defender_turn_desc, 'success_rate': defender_turn_success_rate},
                                attacker_turn={'description': attacker_turn_desc, 'success_rate': attacker_turn_success_rate},
                                compromise_threshold=compromise_threshold)
