# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 20:56:42 2020

@author: Thinkpad
"""

'''sudoku solver'''
import numpy as np
board = np.array(
        [[1,8,3,0,0,9,0,0,0],
         [0,0,5,0,0,0,0,1,0],
         [0,0,9,0,0,8,7,0,0],
         [0,0,0,0,1,0,0,5,0],
         [0,6,4,0,0,0,0,0,0],
         [0,0,8,0,0,4,6,0,0],
         [0,0,1,0,8,0,3,0,7],
         [4,0,0,0,9,0,1,0,0],
         [0,0,0,0,3,0,4,0,5]])


def valid(bo,num,pos):
    
    # check square
    block_row = pos[0] // 3   
    block_col = pos[1] // 3
    square = bo[(block_row*3):(3*block_row+3),3*block_col:(3*block_col+3)]
    
    if (num not in (board[pos[0],:])) and (num not in (board[:,pos[1]])) and (num not in (square.reshape(1,-1))):
        return True
    else:
        return False


def find_empty(bo):
    
    for i in range(9):
        for j in range(9):
            if bo[i,j] == 0 :
                return (i,j)
    return False
            

def solve(bo):
    
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row,col] = i
            if solve(bo):
                return True
            bo[row,col] = 0
    return False

solve(board)
print(board)






