from headers import *

sys.path.insert(1,'./AI')
from value import HASH_VALUE

holyMoly = None
rootCanvas = None


class Piece(Widget):

	def __init__(self,image,piece,pos):
		super().__init__(pos=pos)
		with rootCanvas:
			self.keepPiece = piece
			self.keepPiece.keepPiece = self
			self.img = Image(source=image,pos=pos,opacity=1,width=ChessBoardIMG.sqSize[0]-10,height=ChessBoardIMG.sqSize[1]-10)
			Color(rgba=(1,0,0,1))
			self.fpos=pos

			self.possibleMoves=[]
			self.possiblePlaces=[]
			self.previousPos = None


			
	def updateMoves(self):
		self.possibleMoves=[]
		self.possiblePlaces=[]
		for each in self.keepPiece.moves:
			
			self.possibleMoves.append([each.x,each.y])
			with rootCanvas:
				ChessBoard.BOARD_CIRCLES[each.x][each.y].size=(10,10)


	def checkArea(self,cord):
		for each in self.possibleMoves:
			if(cord[0]>ChessBoard.POSSIBLE_AREA[each[0]][each[1]][0][0] and
			   cord[1]>ChessBoard.POSSIBLE_AREA[each[0]][each[1]][0][1] and
			   cord[0]<ChessBoard.POSSIBLE_AREA[each[0]][each[1]][1][0] and
			   cord[1]<ChessBoard.POSSIBLE_AREA[each[0]][each[1]][1][1]
				):
				return [True,ChessBoard.POSSIBLE_AREA[each[0]][each[1]][2]]

		return [False]


	def on_touch_down(self,touch):


		if self.keepPiece.player==board.Board.TURN and self.img.collide_point(*touch.pos):
			self.previousPos = self.fpos

			board.Board.updateMoves()
			self.updateMoves()
			touch.grab(self)
			return True

		return super().on_touch_down(touch)

	def on_touch_move(self, touch):
		
		if touch.grab_current is self:
			self.pos = touch.pos
			self.img.pos = touch.pos
			return True

		return super().on_touch_move(touch)

	def on_touch_up(self, touch):

		for each in self.possibleMoves:
				with rootCanvas:
					ChessBoard.BOARD_CIRCLES[each[0]][each[1]].size=(1,1)

		temp_value = self.checkArea(touch.pos)

		if touch.grab_current is self and temp_value[0]:

			print(HASH_VALUE)
			touch.ungrab(self)
			another_temp_value = ChessBoard.POS_TO_BOARD[tuple(temp_value[1])]
			
			self.pos = temp_value[1]
			self.img.pos = temp_value[1]
			self.fpos = temp_value[1]

			value = self.keepPiece.position
			some_value =  aliases.POSITION._make(another_temp_value)



			if(self.keepPiece.movePlayer(value,some_value)):
				ChessBoard.BOARDPIECES[some_value[0]][some_value[1]].img.width=0
				ChessBoard.BOARDPIECES[some_value[0]][some_value[1]].img.height=0
				holyMoly.remove_widget(ChessBoard.BOARDPIECES[some_value[0]][some_value[1]])


			ChessBoard.BOARDPIECES[some_value[0]][some_value[1]]=self
			
			
			if(isinstance(self.keepPiece,pieces.Pawn) or
				isinstance(self.keepPiece,pieces.Rook)or 
				isinstance(self.keepPiece,pieces.King)):
				self.keepPiece.moved=True

			board.Board.TURN= not board.Board.TURN
			board.Board.updateMoves()


			return True
		elif touch.grab_current is self:
			touch.ungrab(self)
			self.pos = self.previousPos
			self.img.pos = self.previousPos
			return True

		return super().on_touch_up(touch)

	def update(self, dt):
		pass

	def movePlayer(self,pos,another_pos):
		ChessBoard.BOARDPIECES[another_pos[0]][another_pos[1]]=self
		ChessBoard.BOARDPIECES[pos[0]][pos[1]]= None


		pos = ChessBoard.BOARD_PIECES_POS[pos[0]][pos[1]]
		another_pos = ChessBoard.BOARD_PIECES_POS[another_pos[0]][another_pos[1]]
		self.pos = another_pos
		self.img.pos = another_pos
		self.fpos = another_pos

		
	



class ChessBoardIMG(Widget):

	sqSize=[70,70]
		
	def __init__(self):
		super().__init__()
		global rootCanvas

		self.do_rotation=False
		self.do_scale=False
		self.do_translation=False

		self.color = [(1,1,1,1),(0.44,0.68,0.35,1)]


		flag = False
		initialPos=100
		pos = [initialPos,initialPos]
		offset = 27
		for i in range(1,9):
			for j in range(1,9):
				ChessBoard.BOARD_PIECES_POS[i][j]=[pos[0],pos[1]]
				ChessBoard.POS_TO_BOARD[(pos[0],pos[1])] = (i,j)
				ChessBoard.POSSIBLE_AREA[i][j] = []
				# ChessBoard.POSSIBLE_AREA[i][j].append([pos[0],pos[1]])

				ChessBoard.POSSIBLE_AREA[i][j].append([pos[0]-self.sqSize[0],pos[1]-self.sqSize[1]])
				ChessBoard.POSSIBLE_AREA[i][j].append([pos[0]+self.sqSize[0],pos[1]+self.sqSize[1]])
				ChessBoard.POSSIBLE_AREA[i][j].append([pos[0],pos[1]])

				with self.canvas:
					Color(rgba=(self.color[flag]))
					Rectangle(pos=pos,size=self.sqSize)
				flag= not flag
				pos[0]+=self.sqSize[0]



			pos[0]=initialPos
			pos[1]+=self.sqSize[0]
			flag= not flag
		rootCanvas=self.canvas


	@classmethod
	def drawCircles(self):
		initialPos=100
		pos = [initialPos,initialPos]
		offset = 27

		for i in range(1,9):
			for j in range(1,9):
				
				with rootCanvas:
					Color(rgba=(1,0,0,0.7))
					ChessBoard.BOARD_CIRCLES[i][j]=Ellipse(pos=(pos[0]+offset,pos[1]+offset),size=(0,0))
				pos[0]+=self.sqSize[0]


			pos[0]=initialPos
			pos[1]+=self.sqSize[0]

	




class ChessBoard(FloatLayout):

	BOARD_PIECES_POS = [[[0,0] for i in range(9)] for j in range(9)]
	BOARDPIECES = [[None for i in range(9)] for j in range(9)]
	POS_TO_BOARD = {}
	POSSIBLE_AREA = [[None for i in range(9)] for j in range(9)]
	BOARD_CIRCLES = [[None for i in range(9)] for j in range(9)]

	def __init__(self):
		super().__init__()

		self.cb = ChessBoardIMG()
		self.add_widget(self.cb)

		resizeButton = CheckBox(size_hint=(0.03,0.01),pos_hint={'x':0.9,'y':0.01})
		self.add_widget(resizeButton)
		resizeButton.bind(active=self.on_checkbox_active)

		
		self.initializeBoard()


	def on_checkbox_active(self,checkbox,value):
		if(value):
			self.cb.do_scale=BooleanProperty(True)
		else:
			self.cb.do_scale=BooleanProperty(False)

	def initializeBoard(self):

		for i in range(1,9):
			for j in range(1,9):
				
				if(isinstance(board.Board.BOARD[i][j],pieces.Pawn)):

					if(board.Board.BOARD[i][j].player==aliases.BLACK):

						ChessBoard.BOARDPIECES[i][j]=Piece(BLACK_PAWN_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

					else:

						ChessBoard.BOARDPIECES[i][j]=Piece(WHITE_PAWN_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

				elif(isinstance(board.Board.BOARD[i][j],pieces.King)):

					if(board.Board.BOARD[i][j].player==aliases.BLACK):

						ChessBoard.BOARDPIECES[i][j]=Piece(BLACK_KING_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

					else:

						ChessBoard.BOARDPIECES[i][j]=Piece(WHITE_KING_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

				elif(isinstance(board.Board.BOARD[i][j],pieces.Queen)):

					if(board.Board.BOARD[i][j].player==aliases.BLACK):

						ChessBoard.BOARDPIECES[i][j]=Piece(BLACK_QUEEN_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

					else:

						ChessBoard.BOARDPIECES[i][j]=Piece(WHITE_QUEEN_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

				elif(isinstance(board.Board.BOARD[i][j],pieces.Rook)):

					if(board.Board.BOARD[i][j].player==aliases.BLACK):

						ChessBoard.BOARDPIECES[i][j]=Piece(BLACK_ROOK_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])
					else:

						ChessBoard.BOARDPIECES[i][j]=Piece(WHITE_ROOK_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

				elif(isinstance(board.Board.BOARD[i][j],pieces.Bishop)):

					if(board.Board.BOARD[i][j].player==aliases.BLACK):

						ChessBoard.BOARDPIECES[i][j]=Piece(BLACK_BISHOP_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])
					else:

						ChessBoard.BOARDPIECES[i][j]=Piece(WHITE_BISHOP_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])

				elif(isinstance(board.Board.BOARD[i][j],pieces.Knight)):

					if(board.Board.BOARD[i][j].player==aliases.BLACK):

						ChessBoard.BOARDPIECES[i][j]=Piece(BLACK_KNIGHT_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])
					else:

						ChessBoard.BOARDPIECES[i][j]=Piece(WHITE_KNIGHT_IMG,board.Board.BOARD[i][j],ChessBoard.BOARD_PIECES_POS[i][j])
						self.add_widget(ChessBoard.BOARDPIECES[i][j])
				else:
					ChessBoard.BOARDPIECES[i][j]=None


		ChessBoardIMG.drawCircles()


class Interface(App):

	def changeWindow(self,instance):
		self.Capsule.current='Game'


	def changeWindowBack(self,instance):
		self.Capsule.current='Cosmo Chess Engine'
		board.Board.initializeBoard()
		holyMoly.__init__()
		
		
	def build(self):

		global holyMoly
		Window.clearcolor=(0.2,0.2,0.2,1)
		holyMoly = ChessBoard()

		self.Capsule = ScreenManager()

		screen1 = Screen(name = "Cosmo Chess Engine")
		screen2 = Screen(name = "Game")

		SwitchButton1 = Button(text='Go to Game')
		SwitchButton1.bind(on_press=self.changeWindow)


		SwitchButton2 = Button(text='Go Back',pos_hint={'x':0.8,'y':0.9},size_hint=(0.2,0.02))
		SwitchButton2.bind(on_press=self.changeWindowBack)

		holyMoly.add_widget(SwitchButton2)

		screen1.add_widget(SwitchButton1)
		screen2.add_widget(holyMoly)
		
		self.Capsule.add_widget(screen1)
		self.Capsule.add_widget(screen2)

		self.Capsule.current = 'Cosmo Chess Engine'

		return self.Capsule

		
		return holyMoly





CHESSBOARD=board.Board()
board.Board.initializeBoard()

inter = Interface()
inter.run()