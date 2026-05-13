from abc import ABC, abstractmethod
from .exceptions import InvalidFigureError


class Shape(ABC):

    __count = 0

    def __init__(self, color="red"):
        Shape.__count += 1
        if color.lower() not in ("red", "green", "blue"):
            raise InvalidFigureError(
                    'Color inválido. No es ("red", "green" o "blue")'
                    )
        self._color = color.lower()

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        if new_color not in ("red", "green", "blue"):
            raise InvalidFigureError(
                    'Color nuveo inválido.  No es ("red", "green" o "blue")'
                    )
        self._color = new_color

    def __del__(self):
        Shape.__count -= 1
    
    @staticmethod
    def count():
        return Shape.__count
    
    @abstractmethod
    def area(self):
        # cada clase hija (figura) deberá implementar su método
        # de cálculo de área
        pass
    
    @abstractmethod
    def perimeter(self):
        # cada clase hija (figura) deberá implementar su método
        # de cálculo de perímetro
        pass

    @abstractmethod
    def translate(self, incX, incY):
        # cada clase hija (figura) deberá implementar su método
        # de incremento en X e Y (desplazamiento de figura sobre el espacio)
        pass
    
    @abstractmethod
    def __eq__(self, other):
        # cada clase hija (figura) deberá implementar su método
        # para combrobar si dos figuras son lógicamente iguales 
        pass
    
    def __ne__(self, other):
        if type(self) != type(other):
            return True
        return not( self.__eq__(other))

    @abstractmethod
    def __hash__(self):
        # cada clase hija (figura) deberá implementar su método
        # hasheable
        pass
    
    @abstractmethod
    def __str__(self):
        # cada clase hija (figura) deberá implementar su método
        # de representación por texto
        pass

    def __repr__(self):
        return f"Figura: {str(self)}"


if __name__ == "__main__":
    try:
        sh = Shape()
    except TypeError as e:
        print(e)
