# -*- coding: utf-8 -*-
"""
PROGRAM TO GENERATE REVERSE, COMPLEMENT, and REVERSE COMPLEMENT DNA SEQUENCES

NOTE - the input here is a string. These functions would have to be altered slightly to fit other input formats

Created on Mon Nov  5 18:16:52 2018
@author: kmuss
"""

# Simple example sequence to use in the program (in the form of a string)
sequence = 'AATCGGATCTAACGGTAACG'

# Reverse a sequence
# I did not define this as a function since it was so simple
rev_seq = sequence[::-1]

print('Reverse: ')
print(rev_seq)


# Completement a sequence: 

def complement(sequence): 
    # create a variable to store the generated sequence
    comp = []  
    # capitalize everything to make it easier to compare letters
    sequence = sequence.upper()
    for item in sequence: 
        # for unknown bases
        if item not in ['A', 'T', 'C', 'G']: 
            comp.append('N')
        elif item == 'A': 
            comp.append('T')
        elif item == 'T': 
            comp.append('A')
        elif item == 'G': 
            comp.append('C')
        elif item == 'C': 
            comp.append('G')
    return ''.join(comp)
    print('comp as list')
    print(comp)

print('Complement:')
print(complement(sequence))


# Reverse complement: 

print('Reverse Complement:')
print(complement(sequence)[::-1])
