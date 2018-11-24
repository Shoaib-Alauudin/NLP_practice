# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

sens = ["This is a wolf #scary",
       "Welcome to the jungke #missing",
       "12443 the number to know",
       "Remeber the name s  jordan",
       "I     Love             you"]

for i in range(len(sens)):
    sens[i] = re.sub(r"\W"," ", sens[i])
    sens[i] = re.sub(r"\d","",sens[i])
    sens[i] = re.sub(r"\s+[a-z]\s+"," ",sens[i], flags=re.I)
    sens[i] = re.sub(r"\s+"," ",sens[i])
    sens[i] = re.sub(r"^\s+","",sens[i])
    print(sens[i])