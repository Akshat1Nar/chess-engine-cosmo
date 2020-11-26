import sys
sys.path.insert(1,'./AI')

import score
from aliases import *
import pieces
import tree

'''

This will contain specification of a 8*8 chess board

'''


class Board:

	COMPUTER = BLACK

	POSITION_FOR_WHITE=1
	POSITION_FOR_BLACK=-1

	TURN = WHITE

	CHECK = [False,False]
	KING_POS = [None,None]
	CHECKMATE = [False,False]

	BOARD = [[None for i in range(9)] for j in range(9) ]
	CHECK_SQUARES = [[[0 for i in range(9)] for j in range(9) ]
					,[[0 for i in range(9)] for j in range(9) ]]
	CHECK_TO = -1

	MOVES = [None,None]


	
	def __init__(self):



		treeObj = tree.Tree()
		treeObj.buildTreeFromFile('AI/openings/book.txt')


		x=1
		if(x==1):
			Board.COMPUTER=BLACK
		elif(x==2):
			Board.COMPUTER=WHITE
			Board.POSITION_FOR_WHITE=-1
			Board.POSITION_FOR_BLACK=1
		else:
			raise NameError("PLAYER INVALID")


	@classmethod
	def initializeBoard(cls):

		print("ADDING ALL THE PIECES TO THE BOARD")
		pos = POSITION._make(ChessToNumber('a7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)
		pos = POSITION._make(ChessToNumber('c7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)
		pos = POSITION._make(ChessToNumber('e7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)
		pos = POSITION._make(ChessToNumber('g7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)

		pos = POSITION._make(ChessToNumber('b7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)
		pos = POSITION._make(ChessToNumber('d7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)
		pos = POSITION._make(ChessToNumber('f7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)
		pos = POSITION._make(ChessToNumber('h7'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,BLACK)


		pos = POSITION._make(ChessToNumber('a2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)
		pos = POSITION._make(ChessToNumber('c2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)
		pos = POSITION._make(ChessToNumber('e2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)
		pos = POSITION._make(ChessToNumber('g2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)

		pos = POSITION._make(ChessToNumber('b2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)
		pos = POSITION._make(ChessToNumber('d2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)
		pos = POSITION._make(ChessToNumber('f2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)
		pos = POSITION._make(ChessToNumber('h2'))
		Board.BOARD[pos.x][pos.y] = pieces.Pawn(pos,WHITE)

		
		pos = POSITION._make(ChessToNumber('a8'))
		Board.BOARD[pos.x][pos.y] = pieces.Rook(pos,BLACK)
		pos = POSITION._make(ChessToNumber('a1'))
		Board.BOARD[pos.x][pos.y] = pieces.Rook(pos,WHITE)

		pos = POSITION._make(ChessToNumber('h8'))
		Board.BOARD[pos.x][pos.y] = pieces.Rook(pos,BLACK)
		pos = POSITION._make(ChessToNumber('h1'))
		Board.BOARD[pos.x][pos.y] = pieces.Rook(pos,WHITE)



		pos = POSITION._make(ChessToNumber('b8'))
		Board.BOARD[pos.x][pos.y] = pieces.Knight(pos,BLACK)
		pos = POSITION._make(ChessToNumber('b1'))
		Board.BOARD[pos.x][pos.y] = pieces.Knight(pos,WHITE)

		pos = POSITION._make(ChessToNumber('g8'))
		Board.BOARD[pos.x][pos.y] = pieces.Knight(pos,BLACK)
		pos = POSITION._make(ChessToNumber('g1'))
		Board.BOARD[pos.x][pos.y] = pieces.Knight(pos,WHITE)


		pos = POSITION._make(ChessToNumber('c8'))
		Board.BOARD[pos.x][pos.y] = pieces.Bishop(pos,BLACK)
		pos = POSITION._make(ChessToNumber('c1'))
		Board.BOARD[pos.x][pos.y] = pieces.Bishop(pos,WHITE)

		pos = POSITION._make(ChessToNumber('f8'))
		Board.BOARD[pos.x][pos.y] = pieces.Bishop(pos,BLACK)
		pos = POSITION._make(ChessToNumber('f1'))
		Board.BOARD[pos.x][pos.y] = pieces.Bishop(pos,WHITE)

		pos = POSITION._make(ChessToNumber('d8'))
		Board.BOARD[pos.x][pos.y] = pieces.Queen(pos,BLACK)
		pos = POSITION._make(ChessToNumber('d1'))
		Board.BOARD[pos.x][pos.y] = pieces.Queen(pos,WHITE)

		pos = POSITION._make(ChessToNumber('e8'))
		Board.BOARD[pos.x][pos.y] = pieces.King(pos,BLACK)
		Board.KING_POS[BLACK] = Board.BOARD[pos.x][pos.y]
		pos = POSITION._make(ChessToNumber('e1'))
		Board.BOARD[pos.x][pos.y] = pieces.King(pos,WHITE)
		Board.KING_POS[WHITE] = Board.BOARD[pos.x][pos.y]

		Board.updateMoves()
		score.initializeHash()




	@classmethod
	def instanceOf(cls,value):
		if(isinstance(value,pieces.Pawn)):
			return PAWN
		elif(isinstance(value,pieces.Knight)):
			return KNIGHT
		elif(isinstance(value,pieces.Bishop)):
			return BISHOP
		elif(isinstance(value,pieces.King)):
			return KING
		elif(isinstance(value,pieces.Rook)):
			return ROOK
		elif(isinstance(value,pieces.Queen)):
			return QUEEN
		else:
			return OTHER

		
	@classmethod
	def isPieceAt(cls,pos):
		if(cls.BOARD[pos.x][pos.y]!=None):
			return True
		return False

	@classmethod
	def getPiece(cls,pos):
		return cls.BOARD[pos.x][pos.y]

	@classmethod
	def checkCheck(cls):
		
		cls.TURN = not cls.TURN
		cls.MOVES[cls.TURN] = []
		cls.updateMoves(False)
		cls.TURN = not cls.TURN

		for each in cls.MOVES[not cls.TURN]:
			if(cls.KING_POS[cls.TURN].position==each):
				return True

		return False

	@classmethod
	def updateMoves(cls,flag=True):

		if (flag==True):
			cls.updatePins()

		cls.MOVES[cls.TURN] = []
		for i in range(1,9):
			for j in range(1,9):
				if(cls.BOARD[i][j]!=None and cls.BOARD[i][j].player==cls.TURN):
					if isinstance(cls.BOARD[i][j],pieces.Pawn):
						cls.BOARD[i][j].updateMoves(flag)

						if(not flag):
							cls.MOVES[cls.TURN].extend(cls.BOARD[i][j].movesD)


					else:
						cls.BOARD[i][j].updateMoves(flag)

						if(not flag):
							cls.MOVES[cls.TURN].extend(cls.BOARD[i][j].moves)
					

	@classmethod
	def updatePins(cls):

		# Reset Pins
		for i in range(1,9):
			for j in range(1,9):
				if cls.BOARD[i][j]!=None:
					cls.BOARD[i][j].isPinned = False

		# We will put rays from King in every direction
		# and check for pins

		cls.kingPin(cls.TURN)


	# Updates pin for a respective King 
	@classmethod
	def kingPin(cls,player): 

		Kingposition = cls.KING_POS[player]
		x,y = Kingposition.position
		
		# Horizontal

		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x+1,y

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,HORIZONTAL))
			if(flag==False):
				break
			x_+=1


		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x-1,y

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,HORIZONTAL))
			if(flag==False):
				break
			x_-=1

		#----------------------------------------------------------

		# Vertical

		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x,y+1

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,VERTICAL))
			if(flag==False):
				break
			y_+=1


		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x,y-1

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,VERTICAL))
			if(flag==False):
				break
			y_-=1

		#----------------------------------------------------------

		# Diagonal

		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x+1,y+1

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,DIAGONAL))
			if(flag==False):
				break
			x_+=1
			y_+=1


		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x+1,y-1

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,DIAGONAL))
			if(flag==False):
				break
			x_+=1
			y_-=1

		#----------------------------------------------------------

		# Diagonal

		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x-1,y+1

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,DIAGONAL))
			if(flag==False):
				break
			x_-=1
			y_+=1


		samePieceFlag = False
		samePiece = None
		flag = True
		x_,y_ = x-1,y-1

		while isValid((x_,y_)):
			flag,samePiece,samePieceFlag = (cls.checkThisPin(x_,y_,player,samePiece,samePieceFlag,DIAGONAL))
			if(flag==False):
				break
			x_-=1
			y_-=1

		#----------------------------------------------------------





	@classmethod
	def checkThisPin(cls,x_,y_,player,samePiece,samePieceFlag,MOVEMENT):


		if(cls.BOARD[x_][y_]!=None):

			if (samePieceFlag == True):
				if(cls.BOARD[x_][y_].player == player):
					return False,samePiece,samePieceFlag
				else:
					if(cls.BOARD[x_][y_].movement[MOVEMENT]==True):
						samePiece.isPinned = True
					else:
						samePiece.isPinned = False
					
					return False,samePiece,samePieceFlag
			else:
				if(cls.BOARD[x_][y_].player== (not player)):
					return False,samePiece,samePieceFlag
				else:
					samePieceFlag = True
					samePiece = cls.BOARD[x_][y_]
					

		return True,samePiece,samePieceFlag



	@classmethod
	def updateCheck(cls,player):
		pass
		



	@classmethod		
	def CheckMate(cls):
		pass
				

