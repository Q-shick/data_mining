"""
'parent': parent node objects
'prob': series of probabilities by conditions of the node or its parents
'cond': binary condition (Yes or No)
"""
class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.table_size = 2**len(self.parent)
        self.prob = []
        self.cond = ""
