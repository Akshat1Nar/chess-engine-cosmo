from collections import namedtuple

BOARD_ENUM ={
	'a1':'11',  'a2':'21',  'a3':'31',  'a4':'41',  'a5':'51',  'a6':'61',  'a7':'71',  'a8':'81',  
	'b1':'12',  'b2':'22',  'b3':'32',  'b4':'42',  'b5':'52',  'b6':'62',  'b7':'72',  'b8':'82',  
	'c1':'13',  'c2':'23',  'c3':'33',  'c4':'43',  'c5':'53',  'c6':'63',  'c7':'73',  'c8':'83',  
	'd1':'14',  'd2':'24',  'd3':'34',  'd4':'44',  'd5':'54',  'd6':'64',  'd7':'74',  'd8':'84',  
	'e1':'15',  'e2':'25',  'e3':'35',  'e4':'45',  'e5':'55',  'e6':'65',  'e7':'75',  'e8':'85',  
	'f1':'16',  'f2':'26',  'f3':'36',  'f4':'46',  'f5':'56',  'f6':'66',  'f7':'76',  'f8':'86',  
	'g1':'17',  'g2':'27',  'g3':'37',  'g4':'47',  'g5':'57',  'g6':'67',  'g7':'77',  'g8':'87',  
	'h1':'18',  'h2':'28',  'h3':'38',  'h4':'48',  'h5':'58',  'h6':'68',  'h7':'78',  'h8':'88',  
}

BLACK = 1
WHITE = 0

KING   = '13'
QUEEN  = '14'
PAWN   = '15'
ROOK   = '16'
BISHOP = '17'
KNIGHT = '18'
OTHER  = '19'

MIDGAME = '100'
ENDGAME = '101'

HORIZONTAL     = 0
VERTICAL       = 1
DIAGONAL       = 2
PAWN_MOVEMENT  = 3
KING_MOVEMENT  = 4

POSITION = namedtuple('POSITION',['x','y'])

def ChessToNumber(pos):
	pos_ = BOARD_ENUM[pos]
	return (int(pos_[0]),int(pos_[1]))

def getCoordinates(pos):
	x,y = int(pos[0]),int(pos[1])
	return (x,y)

def isValid(pos):
	x,y=pos
	return (x>0 and x<9 and y>0 and y<9)