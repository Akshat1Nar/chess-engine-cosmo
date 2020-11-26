
class Node:

	def __init__(self,move):

		self.move = move
		self.Children = []

	def __eq__(self, other):
		return self.move == other.move
