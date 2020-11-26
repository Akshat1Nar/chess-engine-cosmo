import sys
sys.path.insert(1,'./base')

import aliases
import board
import pieces

from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.graphics.svg import Svg
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.graphics import Color, Ellipse, Triangle, Rectangle, Line
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.clock import Clock 
from kivy.uix.behaviors import DragBehavior
from kivy.uix.checkbox import CheckBox
from kivy.properties import BooleanProperty, ListProperty

import time


Window.size = (1000, 700)
BLACK = (0,0,0,1)
WHITE = (1,1,1,1)


WHITE_PAWN_IMG = './icons/RPawn.png'
WHITE_QUEEN_IMG = './icons/RQueen.png'
WHITE_KING_IMG = './icons/RKing.png'
WHITE_BISHOP_IMG = './icons/RBishop.png'
WHITE_KNIGHT_IMG = './icons/RKnight.png'
WHITE_ROOK_IMG = './icons/RRook.png'

BLACK_PAWN_IMG = './icons/BPawn.png'
BLACK_QUEEN_IMG = './icons/BQueen.png'
BLACK_KING_IMG = './icons/BKing.png'
BLACK_BISHOP_IMG = './icons/BBishop.png'
BLACK_KNIGHT_IMG = './icons/BKnight.png'
BLACK_ROOK_IMG = './icons/BRook.png'
