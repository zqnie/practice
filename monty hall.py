# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 12:08:27 2020

@author: Thinkpad
"""

import numpy as np
import pandas as pd

def sim():
    car =  np.random.choice([1,2,3],1)[0]
    choice = np.random.choice([1,2,3],1)[0]
    if (car == choice):
        
        opendoor = np.random.choice(list(set([1,2,3])-set([car])),1)[0]
    else:
        
        opendoor = list(set([1,2,3])-set([car,choice]))[0]
        
    lockdoor = list(set([1,2,3])-set([opendoor,choice]))[0]
    
    choice = lockdoor
    
    if choice == car:
        
        return 1
    else:
        return 0
    
    
if __name__ == '__main__':
    win = 0
    n = 100000
    for i in range(n):
        win += sim()
       
    print('The probability of winning the game is ',win/n)
        
