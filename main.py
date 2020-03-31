
# Date : Mon Mar 30 20:25:08 2020
# Author : Naveen Kumar
# This class defines a recursive solver for Sudoku

import numpy as np
import sys
import time

class Sudoku:
	
	def __init__(self, mat=None):

		if mat:
			self.matrix = mat
		else:
			self.matrix = np.zeros((9,9),dtype=int)

		self.solved = False

	def read_grid(self,filename):

		r=0
		with open(filename,'r') as fin:
			for line in fin:
				row = list(map(int,line.rstrip()))
				self.matrix[r,:] = np.array(row)
				r+=1

		self.solved=False

		print("Finished loading sudoku grid from file")
		self.print_grid()

	def print_grid(self):
		print(self.matrix)

	def possible(self,y,x,n):
		#Find the cell in which this location is
		r = y//3
		c = x//3

		if n in self.matrix[y,:]:
			return False
		elif n in self.matrix[:,x]:
			return False
		elif np.isin(n, self.matrix[r*3:r*3+3, c*3:c*3+3]):
			return False
		else:
			return True

	def solve(self):

		if self.solved:
			return

		for y in range(9):
			for x in range(9):
				if self.matrix[y][x] == 0:
					for n in range(1,10):
						if self.possible(y,x,n):
							self.matrix[y][x] = n
							self.solve()
							if self.solved:
								return
							self.matrix[y][x] = 0
					return 
		#If we reached here we probably solved it?
		self.solved = True

if __name__== '__main__':
	s = Sudoku()
	s.read_grid(sys.argv[1])

	s.solve()

	print("\n\nThe first solution is:")
	s.print_grid()
