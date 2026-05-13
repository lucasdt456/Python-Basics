import math
from .shape import Shape
from .point2d import Point2D
from .exceptions import InvalidFigureError

class Circle(Shape):

    def __init__(self, color="red", center=Point2D(0,0), radius=1):
        super().__init__(color)
        if not isinstance(center, Point2D):
            raise TypeError(
                    "El centro del circulo debe ser una instancia de Point2D."
                    )
        if not isinstance(radius, (float, int)):
            raise ValueError(
                    "El radio debe ser un valor númerico."
                    )
        if not radius >= 0:
            raise ValueError(
                    "El radio debe ser mayor o igual que 0 (positivo)."
                    )
        self.__center = center
        self.__radius = float(radius)
    
    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, p):
        if not isinstance(p, Point2D):
            raise TypeError(
                    "El nuevo centro del circulo debe ser una instancia de Point2D."
                    )
        self.__center = p

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, r):
        if not isinstance(r, (float, int)):
            raise ValueError(
                    "El nuevo radio debe ser un valor númerico."
                    )
        if not r >= 0:
            raise ValueError(
                    "El nuevo radio debe ser mayor o igual que 0 (positivo)."
                    )
        self.__radius = r

    def __eq__(self, other):
        if not type(self) == type(other):
                return False
        return (self._color == other.color
               and self.__center == other.center
                and self.__radius == other.radius)

    def __hash__(self):
        return hash((self._color, self.__center, self.__radius))

    def __str__(self):
        return(
                f"Circle(color: {self._color},"
                f" center: {(self.__center)},"
                f" radius: {self.__radius})"
               )

    def area(self):
        area_calculada = math.pi * self.__radius**2
        return area_calculada

    def perimeter(self):
        perimetro_calculado = 2 * math.pi * self.__radius
        return perimetro_calculado

    def translate(self, incX, incY):
        self.__center.x += incX
        self.__center.y += incY

if __name__ == "__main__":
    print("--- Pruebas del Constructor ---")
    c1 = Circle()
    print(f"[count: {Circle.count()}] c1 = {c1}")
    c2 = Circle(color="blue")
    print(f"[count: {Circle.count()}] c2 = {c2}")
    c3 = Circle(center=Point2D(3, 3))
    print(f"[count: {Circle.count()}] c3 = {c3}")
    c4 = Circle(radius=4)
    print(f"[count: {Circle.count()}] c4 = {c4}")
    c5 = Circle(center=Point2D(5, 5), radius=5)
    print(f"[count: {Circle.count()}] c5 = {c5}")
    c6 = Circle("green", Point2D(6, 6), 6)
    print(f"[count: {Circle.count()}] c6 = {c6}")

    print()
    print("--- Pruebas del Destructor ---")
    del(c1) # invocamos destructor __del__
    print(f"[count: {Circle.count()}] del(c1)")
    
    print()
    print("--- Pruebas de Comparación ---")
    c_eq_1 = Circle("red", Point2D(1, 1), 2.0)
    c_eq_2 = Circle("red", Point2D(1, 1), 2.0)
    c_diff = Circle("blue", Point2D(1, 1), 2.0)
    
    print(f"c_eq_1: {c_eq_1}")
    print(f"c_eq_2: {c_eq_2}")
    print(f"c_diff: {c_diff}")
    
    print(f"  > c_eq_1 == c_eq_2: {c_eq_1 == c_eq_2}")
    print(f"  > c_eq_1 != c_eq_2: {c_eq_1 != c_eq_2}")
    print(f"  > c_eq_1 == c_diff: {c_eq_1 == c_diff}")
    print(f"  > c_eq_1 != c_diff: {c_eq_1 != c_diff}")
    print(f"  > c_eq_1 == tuple(1,1):  {c_eq_1 == (1,1)}")
    print(f"  > c_eq_1 != tuple(1,1):  {c_eq_1 != (1,1)}")

    print()
    print("--- Pruebas de Getters y Setters ---")
    print(f"c2 antes:\n  > {c2}")
    c2.color = "red"
    c2.center = Point2D(8.0, 8.0)
    c2.radius = 8.0
    print(f"c2 modificado:\n  > {c2}")
    print(f"Valores leidos con getters:")
    print(f"  > color={c2.color}")
    print(f"  > center={c2.center}")
    print(f"  > radius={c2.radius}")

    print()
    print("--- Pruebas de Excepciones ---")
    print("Intentando instanciar Circle con color inválido...")
    try:
        Circle("yellow", Point2D(0,0), 1.0)
    except InvalidFigureError as e:
        print(f"  > Se capturó excepción InvalidFigureError correctamente: {e}")

    print("Intentando instanciar Circle con centro inválido (no Point2D)...")
    try:
        Circle("red", (0, 0), 1.0)
    except TypeError as e:
        print(f"  > Se capturó excepción TypeError correctamente: {e}")

    print("Intentando instanciar Circle con radio no numérico...")
    try:
        Circle("red", Point2D(0, 0), "1.0")
    except ValueError as e:
        print(f"  > Se capturó excepción ValueError correctamente: {e}")

    print("Intentando instanciar Circle con radio negativo...")
    try:
        Circle("red", Point2D(0, 0), -1.0)
    except ValueError as e:
        print(f"  > Se capturó excepción ValueError correctamente: {e}")

    print("Intentando modificar el centro con un valor inválido...")
    try:
        c2.center = (0, 0)
    except TypeError as e:
        print(f"  > Se capturó excepción TypeError correctamente: {e}")

    print("Intentando modificar el radio con un valor no numérico...")
    try:
        c2.radius = "2.0"
    except ValueError as e:
        print(f"  > Se capturó excepción ValueError correctamente: {e}")

    print("Intentando modificar el radio con un valor negativo...")
    try:
        c2.radius = -5.0
    except ValueError as e:
        print(f"  > Se capturó excepción ValueError correctamente: {e}")
    
    # Pruebas con conjuntos
    print()
    print("--- Pruebas con Conjuntos (Set) ---")
    lista_circulos = [Circle("red", Point2D(1.0, 1.0), 2.0),
                      Circle("blue", Point2D(3.0, 3.0), 4.0),
                      Circle("red", Point2D(1.0, 1.0), 2.0)]
    
    print(f"Lista original con {len(lista_circulos)} círculos:")
    for i, c in enumerate(lista_circulos):
        print(f"  {i}: {c}")
        
    conjunto_circulos = set(lista_circulos)
    
    print(f"\nConjunto (sin duplicados) con {len(conjunto_circulos)} círculos:")
    for i, c in enumerate(conjunto_circulos):
        print(f"  {i}: {c}")
    
    # Pruebas de número de figuras globales
    print()
    print(f"Figuras vivas (count): {Shape.count()}")
