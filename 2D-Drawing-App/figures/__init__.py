from .point2d import Point2D
from .circle import Circle
from .rectangle import Rectangle
from .square import Square
from .drawing import Drawing
from .exceptions import InvalidFigureError
# no se importa `Shape` al ser una clase abstracta

# Definimos explícitamente qué clases se exportarán al hacer 'from figures import *'
# o cuáles estarán disponibles directamente desde el paquete 'figures.'
__all__ = [
    'Point2D',
    'Circle',
    'Rectangle',
    'Square',
    'Drawing',
    'InvalidFigureError'
]
