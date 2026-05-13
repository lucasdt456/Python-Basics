from .shape import Shape
from .circle import Circle
from .square import Square
from .rectangle import Rectangle


class Drawing:

    def __init__(self):
        self.__shapes = []

    def add_front(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError("La figura debe ser una instancia de Shape")
        self.__shapes.insert(0, shape)

    def add_back(self, shape):
        if not isinstance(shape, Shape):
            raise TypeError("La figura debe ser una instancia de Shape")
        self.__shapes.append(shape)

    def print_all(self):
       for indice, forma in enumerate(self.__shapes):
           print(f"{indice}: {forma}")

    def remove_duplicates(self):
        self.__shapes = list(dict.fromkeys(self.__shapes))

    def get_area_all_squares(self):
        return round(sum(sq.area() for sq in self.__shapes if isinstance(sq, Square)), 5)

    def get_area_all_circles(self):
        return round(sum(cir.area() for cir in self.__shapes if isinstance(cir, Circle)), 5)

    def get_area_all_rectangles(self):
        return round(sum(rect.area() for rect in self.__shapes if isinstance(rect, Rectangle)), 5)

    def move_squares(self, incX, incY):
        for square in self.__shapes:
            if isinstance(square, Square):
                square.translate(incX, incY)

    def move_circles(self, incX, incY):
        for circle in self.__shapes:
            if isinstance(circle, Circle):
                circle.translate(incX, incY)

    def move_rectangles(self, incX, incY):
        for rect in self.__shapes:
            if isinstance(rect, Rectangle):
                rect.translate(incX, incY)
