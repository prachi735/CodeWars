##Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as parameter.
##If the board is valid return 'Finished!', otherwise return 'Try again!'
##
##Sudoku rules:
##
##Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.
##
##There are 9 rows in a traditional Sudoku puzzle.
##Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9.
##There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.
##
##For those who don't know the game, here are some information about rules and how to play Sudoku:
##http://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com/


import collections
import numpy as np
import unittest

def done_or_not(board):
    rows = board #group of rows
    cols = map(list, zip(*board)) #transposing to get columns from rows
    squares = [
    board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
      for i in range(0, 9, 3)
      for j in range(0, 9, 3)]   #squares of len 3 within board
    
    for batches in (rows, cols, squares):
        for batche in batches:
          if len(set(batche)) != 9: #set to eliminate duplicates in cluster
            return 'Try again!' #duplicate found hence len less than 9 
    return 'Finished!' #no duplicates found

class TestStringMethods(unittest.TestCase):
    def test_1(self):
        self.assertEqual(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');
    def test_2(self): 
        self.assertEqual(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');


if __name__ == '__main__':
    unittest.main()
