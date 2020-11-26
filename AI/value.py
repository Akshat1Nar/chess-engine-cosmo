from aliases import *

HASH_VALUE = 0
MODE = MIDGAME
PREV_MODE = MODE

#------------------------------------------------------------------------------
VLE = { ENDGAME : {
	
	PAWN:[[0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0]],

	KNIGHT:[[0,0,0,0,0,0,0,0,0],
			[0,2,3,4,4,4,4,3,2],
			[0,3,4,6,6,6,6,4,3],
			[0,4,6,8,8,8,8,6,4],
			[0,4,6,8,8,8,8,6,4],
			[0,4,6,8,8,8,8,6,4],
			[0,4,6,8,8,8,8,6,4],
			[0,3,4,6,6,6,6,4,3],
			[0,2,3,4,4,4,4,3,2],
			[0,0,0,0,0,0,0,0,0]],

	BISHOP:[[0,0,0,0,0,0,0,0,0],
			[0,7,7,7,7,7,7,7,7],
			[0,7,9,9,9,9,9,9,7],
			[0,7,9,11,11,11,11,9,7],
			[0,7,9,11,13,13,11,9,7],
			[0,7,9,11,13,13,11,9,7],
			[0,7,9,11,11,11,11,9,7],
			[0,7,7,7,7,7,7,7,7],
			[0,7,9,9,9,9,9,9,7],
			[0,0,0,0,0,0,0,0,0]],

	KING:[[0,0,0,0,0,0,0,0,0],
		  [0,3,5,5,5,5,5,5,3],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,3,5,5,5,5,5,5,3],
		  [0,0,0,0,0,0,0,0,0]],

	ROOK:[[0,0,0,0,0,0,0,0,0],
		  [0,14,14,14,14,14,14,14,14],
		  [0,14,14,14,14,14,14,14,14],
		  [0,14,14,14,14,14,14,14,14],
		  [0,14,14,14,14,14,14,14,14],
		  [0,14,14,14,14,14,14,14,14],
		  [0,14,14,14,14,14,14,14,14],
		  [0,14,14,14,14,14,14,14,14],
		  [0,14,14,14,14,14,14,14,14],
		  [0,0,0,0,0,0,0,0,0]],

	OTHER:[[0 for i in range(9)]for j in range(9)],
	QUEEN:[[20 for i in range(9)]for j in range(9)]
},


#------------------------------------------------------------------------------

MIDGAME : {
	
	PAWN:[[0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,1,2,2,2,2,2,2,1],
		  [0,0,0,0,0,0,0,0,0],
		  [0,0,0,0,0,0,0,0,0]],

	KNIGHT:[[0,0,0,0,0,0,0,0,0],
			[0,2,3,4,4,4,4,3,2],
			[0,3,4,6,6,6,6,4,3],
			[0,4,6,8,8,8,8,6,4],
			[0,4,6,8,8,8,8,6,4],
			[0,4,6,8,8,8,8,6,4],
			[0,4,6,8,8,8,8,6,4],
			[0,3,4,6,6,6,6,4,3],
			[0,2,3,4,4,4,4,3,2],
			[0,0,0,0,0,0,0,0,0]],

	BISHOP:[[0,0,0,0,0,0,0,0,0],
			[0,1,2,2,2,2,2,2,1],
			[0,2,4,4,4,4,4,4,2],
			[0,2,4,4,4,4,4,4,2],
			[0,2,4,4,4,4,4,4,2],
			[0,2,4,4,4,4,4,4,2],
			[0,2,4,4,4,4,4,4,2],
			[0,2,4,4,4,4,4,4,2],
			[0,1,2,2,2,2,2,2,1],
			[0,0,0,0,0,0,0,0,0]],

	KING:[[0,0,0,0,0,0,0,0,0],
		  [0,3,5,5,5,5,5,5,3],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,5,8,8,8,8,8,8,5],
		  [0,3,5,5,5,5,5,5,3],
		  [0,0,0,0,0,0,0,0,0]],

	ROOK:[[0,0,0,0,0,0,0,0,0],
		  [0,2,3,3,3,3,3,3,2],
		  [0,3,4,4,4,4,4,4,3],
		  [0,3,4,4,4,4,4,4,3],
		  [0,3,4,4,4,4,4,4,3],
		  [0,3,4,4,4,4,4,4,3],
		  [0,3,4,4,4,4,4,4,3],
		  [0,3,4,4,4,4,4,4,3],
		  [0,2,3,3,3,3,3,3,2],
		  [0,0,0,0,0,0,0,0,0]],

	OTHER:[[0 for i in range(9)]for j in range(9)],
	QUEEN:[[20 for i in range(9)]for j in range(9)]
}}


#------------------------------------------------------------------------------