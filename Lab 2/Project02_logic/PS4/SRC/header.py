import os
import sys
import copy

# tim negative literal
def negation(literal:str):
    if literal[0] == '-':
        return literal[1]
    return '-' + literal[0]

# doi tuong clause chua list literal
class Clause:
    def __init__(self, clause:list):
        self.clause = clause
        self.format()
    
    # operator xuat ra man hinh
    def __str__(self):
        if self.clause == []:
            return '{}'
        return ' OR '.join(self.clause)

    # operator so sanh bang
    def __eq__(self, obj):
        return set(obj.clause) == set(self.clause)

    # method cac literal sap xep theo thu tu chu cai A->Z
    def format(self):
        self.clause = list(set(self.clause))
        return self.clause.sort(key=lambda x: x[-1])

    # method kiem tra menh de vo nghia
    def nonsense(self):
        for literal in self.clause:
            if negation(literal) in self.clause:
                return False
        return True
    
    # ket hop 2 chuoi literal voi nhau sau khi hop giai 2 chuoi
    @staticmethod
    def merge(clause1, clause2): 
        c1 = copy.deepcopy(clause1.clause)
        c2 = copy.deepcopy(clause2.clause)

        for i in range(len(c1)):
            for j in range(len(c2)):
                if i < len(c1) and j < len(c2) and c1[i] == negation(c2[j]):
                    c1.pop(i)
                    c2.pop(j)
                    return Clause(c1 + c2)
        return None