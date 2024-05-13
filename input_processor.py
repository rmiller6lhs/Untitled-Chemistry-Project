#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:36:50 2024

@author: richardmiller
"""
import re
class InputProcessor:
    
    def __init__(self,formula):
        #Self declarations
        self.formula = formula
        self.element_counts = {}
        
        #Call preprocesser
        self.input_preprocesser()
        
        #Use result from preprocesser to iterate through dict or pass string to parser
        #Iterator will generate multiple parser calls
        
        if self.formula_metadata['has_parens'] == True:
            self.input_iterator()
        else:
            self.element_parser()
        
    def input_preprocesser(self):
        
        #Check for lower case letters
        if re.search(r"[a-z]",self.formula):
            formula_has_lower = True
        else:
            formula_has_lower = False
            
        #Check for numbers   
        if re.search(r"[0-9]",self.formula):
            formula_has_num = True
        else:
            formula_has_num = False
        
        #Check for parenthesis
        #Split formula string into sub-strings for parsing
        if re.search(r'\(',self.formula):
            formula_has_parens = True
            inside_parens = re.findall(r"\((.*?)\)",self.formula)
            between_parens = re.findall(r"\)(.*?)\(",self.formula)
            before_parens = re.search(r"(.*?)\(", self.formula).group(0)[:-1]
            after_parens = re.findall(r"\)(\w+)",self.formula)
            
            #Ensure parenthesis are followed by a numeric value
            try:
                inside_parens = [(j,int(after_parens[i])) for i,j in enumerate(inside_parens)]
            except:
                raise ValueError('Polyatomic ions or functional groups should only be enclosed in a parenthesis if there are more than 1 of them in your input compound.')
                
        else:
            formula_has_parens = False
            
        #Generate metadata about formula
        self.formula_metadata = {
            'has_parens':formula_has_parens,
            'has_num':formula_has_num,
            'has_lower':formula_has_lower,
        }
        
        #Compile sub-strings from formula for parsing into an iterable (dict)
        if formula_has_parens == True:
            self.formula_preprocessed = {
                    'inside_parens':inside_parens,
                    'between_parens':between_parens,
                    'before_parens':before_parens,
                }
        
    def input_iterator(self):
        if self.formula_metadata['has_parens'] == True:
            for key,value in self.formula_preprocessed.items():
                if type(value) == list:
                    for string in value:
                        self.element_parser(key,string)
                else:
                    self.element_parser(key,value)
        
            
            
    def element_parser(self,key=None,value=None):
        
        #Set element multiplier for elements.
        #Applied to all elements inside parenthesis.
        if key == 'inside_parens':
            multiplier = value[1]
            val = value[0]  
        elif key == 'before_parens':
            multiplier = 1
            val = value
        elif key == 'between_parens':
            multiplier = 1
            val = value
        elif key == None:
            val = self.formula
            
        #Find all elements, put into list of tuples formated as:
        #   (element_name, index_of_element, element_count)
        
        lowers_idxs = [val.index(i) for i in val if i.islower()]
        elements_with_lowers = [[val[i-1]+j,val.index(val[i-1]+j),0] for i,j in enumerate(val) if j.islower()]
        elements_without_lowers = [[j,val.index(j),0] for i,j in enumerate(val) if i+1 not in lowers_idxs and j.isupper()]
        all_elements = elements_with_lowers + elements_without_lowers
        
        #Iterate through all elements and update counts, apply multipliers, etc.
        for idx,element in enumerate(all_elements):
            if key == 'inside_parens':
                if self.formula[element[1]+1].isnumeric():
                    
                    all_elements[idx][2]+= int(val[element[1]+1])*multiplier
                else:
                    all_elements[idx][2] += multiplier
            elif key == 'before_parens' or key == None:
                element_start_idx = self.formula.index(element[0])
                element_end_idx = element_start_idx + len(element[0])
                element_end = self.formula[element_end_idx]
                if element_end.isnumeric():
                    all_elements[idx][2] += int(element_end)
                else:
                    all_elements[idx][2] = 1
                    
                    
        #Check self.element_counts dictionary to see if elements has been counted
        #Insert elements and count OR update element counts
        for symbol,*_,count in all_elements:
            if symbol in self.element_counts.keys():
                self.element_counts[symbol] += count
            else:
                self.element_counts[symbol] = count
                    
                    