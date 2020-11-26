from node import Node



class Tree:

	def __init__(self):

		self.root = Node('root')
		self.iter = root
		#levels = []

	def find(self,all,move):

		for each in all.Children:
			if move == each:
				return each

		return Node('None')


	def buildTreeFromFile(self,filename):

		# Assuming each line to contain some value
		# Open file
		file = open(filename)

		# reading value line by line
		number =0
		for each in file:
			number+=1
			temp = each.split(' ')
			
			temp[-1] = temp[-1].replace('\n','')
			# list = [move-number,move,move,...]
			i =0
			iterator = self.root
			final = iterator
			for move in temp:
				move = Node(move)
				
				i = (i+1)%3
				if (i==1):
					continue

				iterator = self.find(iterator,move)

				if (iterator==Node('None')):
					final.Children.append(move)
				else:
					final = iterator
					

	def printWell(self,each,temp):		

		if(len(each.Children)==0):
			print(temp)
			return

		for every in each.Children:
			new_temp = temp+every.move+' '
			self.printWell(every,new_temp)

				