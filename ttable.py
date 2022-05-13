#!/usr/bin/env python3
from bin_permutation import get_bin_permutations 

expr = input("Please leave space left and right of each variable\n")
words = expr.split()
# terms = set(expr) & set('abcdefghijklmnopqrstuvwxyz')
terms = []
for term in 'abcdefghijklmnopqrstuvwxyz':
    if term in words:
        terms+=term

no_variables = len(terms)
permutations = get_bin_permutations(no_variables)
table = []

table.append([list(terms),'Result'])

for permut in permutations:
   exp = expr
   for term,p_value in zip(list(terms),permut):
       exp = exp.split()
       exp = [str(p_value) if i==term else i for i in exp]
       exp = str(" ".join(exp))

   result = eval(exp)
   result = 1 if result else 0 # Converting result to binary
   print(exp,'=',result)
   table.append([[permut],result])



