#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:14:11 2024

@author: richardmiller

Creates dictionary with information about each element
"""
#Import packages to namespace
import os
import pandas as pd
import math
import json

#Generate Base Dictionary
element_data = {
    'H':{'name':'Hydrogen','mass':1.008,}, 'He':{'name':'Helium','mass':4.0026,},
    'Li':{'name':'Lithium','mass':6.94,}, 'Be':{'name':'Beryllium','mass':9.0122,},
    'B':{'name':'Boron','mass':10.81,}, 'C':{'name':'Carbon','mass':12.011,},
    'N':{'name':'Nitrogen','mass':14.007,},'O':{'name':'Oxygen','mass':15.999,},
    'F':{'name':'Fluorine','mass':18.998,},'Ne':{'name':'Neon','mass':20.180,},
    'Na':{'name':'Sodium','mass':22.990,},'Mg':{'name':'Magnesium','mass':24.305,},
    'Al':{'name':'Aluminum','mass':26.982,},'Si':{'name':'Silicon','mass':28.085,},
    'P':{'name':'Phosphorus','mass':30.974,},'S':{'name':'Sulfur','mass':32.06,},
    'Cl':{'name':'Chlorine','mass':35.45,},'Ar':{'name':'Argon','mass':39.948,},
    'K':{'name':'Potassium','mass':39.098,},'Ca':{'name':'Calcium','mass':40.078,},
    'Sc':{'name':'Scandium','mass':44.956,},'Ti':{'name':'Titanium','mass':47.876,},
    'V':{'name':'Vanadium','mass':50.942,},'Cr':{'name':'Chromium','mass':51.996,},
    'Mn':{'name':'Manganese','mass':54.938,},'Fe':{'name':'Iron','mass':55.845,},
    'Co':{'name':'Cobalt','mass':58.933,},'Ni':{'name':'Nickel','mass':58.693,},
    'Cu':{'name':'Copper','mass':63.546,},'Zn':{'name':'Zinc','mass':65.38,},
    'Ga':{'name':'Gallium','mass':69.723,},'Ge':{'name':'Germanium','mass':72.630,},
    'As':{'name':'Arsenic','mass':74.922,},'Se':{'name':'Selenium','mass':78.971,},
    'Br':{'name':'Bromine','mass':79.904,},'Kr':{'name':'Krypton','mass':83.798,},
    'Rb':{'name':'Rubidium','mass':85.468,},'Sr':{'name':'Strontium','mass':87.62,},
    'Y':{'name':'Yttrium','mass':88.906,},'Zr':{'name':'Zirconium','mass':91.224,},
    'Nb':{'name':'Niobium','mass':92.906,},'Mo':{'name':'Molybdenum','mass':95.95,},
    'Tc':{'name':'Technetium','mass':98.000,},'Ru':{'name':'Ruthenium','mass':101.07,},
    'Rh':{'name':'Rhodium','mass':102.91,},'Pd':{'name':'Palladium','mass':106.42,},
    'Ag':{'name':'Silver','mass':107.87,},'Cd':{'name':'Cadmium','mass':112.41,},
    'In':{'name':'Indium','mass':114.82,},'Sn':{'name':'Tin','mass':118.71,},
    'Sb':{'name':'Antimony','mass':121.76,},'Te':{'name':'Tellurium','mass':127.60,},
    'I':{'name':'Iodine','mass':126.90,},'Xe':{'name':'Xenon','mass':131.29,},
    'Cs':{'name':'Caesium','mass':132.91,},'Ba':{'name':'Barium','mass':137.33,},
    'La':{'name':'Lanthanum','mass':138.91,},'Ce':{'name':'Cerium','mass':140.12,},
    'Pr':{'name':'Praseodymium','mass':140.91,},'Nd':{'name':'Neodymium','mass':144.24,},
    'Pm':{'name':'Promethium','mass':145.000,},'Sm':{'name':'Samarium','mass':150.36,},
    'Eu':{'name':'Europium','mass':151.96,},'Gd':{'name':'Gadolinium','mass':157.25,},
    'Tb':{'name':'Terbium','mass':158.94,},'Dy':{'name':'Dysprosium','mass':162.50,},
    'Ho':{'name':'Hollmium','mass':164.93,},'Er':{'name':'Erbium','mass':167.26,},
    'Tm':{'name':'Thulium','mass':168.93,},'Yb':{'name':'Ytterbium','mass':173.05,},
    'Lu':{'name':'Lutetium','mass':174.97,},'Hf':{'name':'Hafnium','mass':178.49,},
    'Ta':{'name':'Tantalum','mass':180.95,},'W':{'name':'Tungsten','mass':183.84,},
    'Re':{'name':'Rhenium','mass':186.21,},'Os':{'name':'Osmium','mass':190.23,},
    'Ir':{'name':'Iridium','mass':192.22,},'Pt':{'name':'Platinum','mass':192.08,},
    'Au':{'name':'Gold','mass':196.97,},'Hg':{'name':'Mercury','mass':200.59,},
    'Tl':{'name':'Thallium','mass':204.38,},'Pb':{'name':'Lead','mass':207.2,},
    'Bi':{'name':'Bismuth','mass':208.98,},'Po':{'name':'Polonium','mass':209.000,},
    'At':{'name':'Astatine','mass':210.000,},'Rn':{'name':'Radon','mass':222.000,},
    'Fr':{'name':'Francium','mass':223.000,},'Ra':{'name':'Radium','mass':226.000,},
    'Ac':{'name':'Actinium','mass':227.000,},'Th':{'name':'Thorium','mass':232.04,},
    'Pa':{'name':'Protactinium','mass':231.04,},'U':{'name':'Uranium','mass':238.03,},
    'Np':{'name':'Neptunium','mass':237.000,},'Pu':{'name':'Plutonium','mass':244.000,},
    'Am':{'name':'Americium','mass':243.000,},'Cm':{'name':'Curium','mass':247.000},
    'Bk':{'name':'Berkelium','mass':247.000,},'Cf':{'name':'Californium','mass':251.000,},
    'Es':{'name':'Einsteinium','mass':252.000,},'Fm':{'name':'Fermium','mass':257.000,},
    'Md':{'name':'Mendelevium','mass':258.000,},'No':{'name':'Nobelium','mass':259.000,},
    'Lr':{'name':'Lawrencium','mass':266.000,},'Rf':{'name':'Rutherfordium','mass':267.000,},
    'Db':{'name':'Dubnium','mass':268.000,},'Sg':{'name':'Seaborgium','mass':269.000,},
    'Bh':{'name':'Bhorium','mass':270.000,},'Hs':{'name':'Hassium','mass':277.000,},
    'Mt':{'name':'Meitnnerium','mass':278.000,},'Ds':{'name':'Darmstadtium','mass':281.000,},
    'Rg':{'name':'Roentgenium','mass':282.000,},'Cn':{'name':'Copernicium','mass':285.000,},
    'Nh':{'name':'Nihonium','mass':286.000,},'Fl':{'name':'Flerovium','mass':289.000,},
    'Mc':{'name':'Moscovium','mass':290.000,},'Lv':{'name':'Livermorium','mass':293.000,},
    'Ts':{'name':'Tennessine','mass':294.000,},'Og':{'name':'Oganesson','mass':294.000}
}

#Generate lists of elements for classification
Lanthenides = ['La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu']
Actenides = ['Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr']
Alkalis = ['Li','Na','K','Rb','Cs','Fr']
Alkalines = ['Be','Mg','Ca','Sr','Ba','Ra']
NonMetals = ['H','C','N','O','P','S','Se']
Nobles = ['He','Ne','Ar','Xe','Kr','Rn']
Transitions = [
    'Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn',
    'Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd',
    'Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg',
]

HereThereBeDragonides = ['Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
Metalloids = ['B','Si','Ge','As','Sb','Te','Po','At']
Halogens = ['F','Cl','Br','I']
PostTransitions = ['Al', 'Ga', 'In', 'Sn', 'Tl', 'Pb', 'Bi']

#Generate list of unstable elements
Unstable = [
    'Fr','Ra','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn',
    'Nh','Fl','Mc','Lv','Ts','Og','Pm','Ac','Np','Pu','Am','Cm',
    'Bk','Cf','Es','Fm','Md','No','Lr','Rd','At','Po',
]

#Iterate through dictionary, enter classification and stability of each element.
for key,val in element_data.items():
    if key in Lanthenides:
        val['classif'] = 'Lanthenides'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in Actenides:
        val['classif'] = 'Actenides'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in Alkalis:
        val['classif'] = 'Alkali Metals'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in Alkalines:
        val['classif'] = 'Alakaline Earth Metals'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in Transitions:
        val['classif'] = 'Transition Metals'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in Metalloids:
        val['classif'] = 'Metalloids'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in Halogens:
        val['classif'] = 'Halogens'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in Nobles:
        val['classif'] = 'Noble Gasses'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in NonMetals:
        val['classif'] = 'Non-Metals'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in HereThereBeDragonides:
        val['classif'] = 'Exotics'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    elif key in PostTransitions:
        val['classif'] = 'Post Transition Metals'
        if key in Unstable:
            val['stable'] = False
        else:
            val['stable'] = True
    element_data[key] = val


#Pull electronegativity data from csv
data_dirpath = os.getcwd()+'/Documents/GitHub/Untitled-Chemistry-Project/element_data_sets/'
electronegativity_fpath = data_dirpath+'electronegativity_table.csv'
electronegativity_chart = pd.read_csv(electronegativity_fpath)
element_symbols = electronegativity_chart['symbol']

#Insert electronegativity data to dictionary
for idx,en in enumerate(electronegativity_chart['electronegativity']):
    if math.isnan(en):
        element_data[element_symbols[idx]]['electronegativity'] = None
    else:
        element_data[element_symbols[idx]]['electronegativity'] = en
        
#Iterate through dictionary, check for missing classifications and stabilities.
missing_classifications = []
missing_stability = []
for key,val in element_data.items():
    try:
        a = val['classif']
    except:
        missing_classifications.append(key)
    
    try:
        b = val['stable']
    except:
        missing_stability.append(key)
    
utils_dirpath = os.getcwd()+'/Documents/GitHub/Untitled-Chemistry-Project/utils/'
json_fpath = utils_dirpath+'elements.json'
print(json_fpath)
with open(json_fpath,'w') as f:
    json.dump(element_data,f)