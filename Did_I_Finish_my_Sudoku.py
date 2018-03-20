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
    
    for bacthes in (rows, cols, squares):
        for cluster in clusters:
          if len(set(cluster)) != 9: #set to eliminate duplicates in cluster
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
