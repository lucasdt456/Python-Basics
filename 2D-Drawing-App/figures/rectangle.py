#import math
from .shape import Shape
from .exceptions import InvalidFigureError
from .point2d import Point2D

class Rectangle(Shape):
    
    _N_VERTICES = 4
    
    def __init__(
            self, 
            color="red",
            vertices=(
                Point2D(-1.0, 0.5), 
                Point2D(1.0, 0.5), 
                Point2D(1.0, -0.5), 
                Point2D(-1.0, -0.5)
                )
            ):
        super().__init__(color)
        if not Rectangle._check(vertices):
            raise InvalidFigureError(
                    "El rectángulo no es válido."
                )
        self._vertices = vertices

    @staticmethod
    def _check(vertices): 
        if not isinstance(vertices, tuple) or len(vertices) != Rectangle._N_VERTICES:
            return False
        if not all(isinstance(v, Point2D) for v in vertices):
            return False
        distancia1 = Point2D.distance(vertices[0], vertices[1]) #altura1
        distancia2 = Point2D.distance(vertices[2], vertices[3]) #altura2

        distancia3 = Point2D.distance(vertices[1], vertices[2]) #base1
        distancia4 = Point2D.distance(vertices[3], vertices[0]) #base2
        
        if distancia1 != distancia2 or distancia3 != distancia4:
            return False
        return True

    def get_vertex(self, ind):
        if not (0 <= ind <= 3):
            raise IndexError("El índice debe estar en un rango de [0, 3].")
        return self.vertices[ind]

    def __getitem__(self, ind):
        return self.get_vertex(ind)
    
    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        if not Rectangle._check(vertices):  
            raise InvalidFigureError(
                    "Los nuevos rectángulo no es válido."
                    )
        self._vertices = vertices

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self._color == other.color and self._vertices == other.vertices

    def __hash__(self):
        return hash((self._color, self._vertices))

    def __iter__(self):
        self.__valor_actual = 0
        return self

    def __next__(self):
        if self.__valor_actual < len(self._vertices):
            valor = self._vertices[self.__valor_actual]
            self.__valor_actual += 1
            return valor
        else:
            raise StopIteration

    def __str__(self):
        return(
                f"Rectangle(color: {self._color}, "
                f"vertices: {self._vertices})"
              )

    def area(self):
        distancia1 = Point2D.distance(self._vertices[0], self._vertices[1]) # altura1
        distancia3 = Point2D.distance(self._vertices[1], self._vertices[2]) # base1
        return distancia1 * distancia3

    def perimeter(self):
        distancia1 = Point2D.distance(self._vertices[0], self._vertices[1]) # altura1
        distancia3 = Point2D.distance(self._vertices[1], self._vertices[2]) # base1
        return 2 * distancia1 + 2 * distancia3

    def translate(self, incX, incY):
        for v in self._vertices:
            v.x += incX
            v.y += incY

if __name__ == "__main__":
    print("--- Pruebas del Constructor ---")
    r1 = Rectangle()
    print(f"[count: {Rectangle.count()}] r1 = {r1}")
    v_personalizados = (Point2D(0.0, 2.0), Point2D(4.0, 2.0), Point2D(4.0, 0.0), Point2D(0.0, 0.0))
    r2 = Rectangle("blue", v_personalizados)
    print(f"[count: {Rectangle.count()}] r2 = {r2}")

    print()
    print("--- Pruebas del Destructor ---")
    del(r1) # invocamos destructor __del__
    print(f"[count: {Rectangle.count()}] del(r1)")

    print()
    print("--- Pruebas de Comparación ---")
    r_eq_1 = Rectangle("red", v_personalizados)
    r_eq_2 = Rectangle("red", v_personalizados)
    r_diff = Rectangle("blue", v_personalizados)

    print(f"r_eq_1: {r_eq_1}")
    print(f"r_eq_2: {r_eq_2}")
    print(f"r_diff: {r_diff}")

    print(f"  > r_eq_1 == r_eq_2: {r_eq_1 == r_eq_2}")
    print(f"  > r_eq_1 != r_eq_2: {r_eq_1 != r_eq_2}")
    print(f"  > r_eq_1 == r_diff: {r_eq_1 == r_diff}")
    print(f"  > r_eq_1 != r_diff: {r_eq_1 != r_diff}")

    print()
    print("--- Pruebas de Getters, Setters y Métodos ---")
    print(f"r2 antes:\n  > {r2}")
    r2.color = "red"
    # r2 lo trasladamos artificialmente sumando 1 a todo
    v_mas_uno = (Point2D(1.0, 3.0), Point2D(5.0, 3.0), Point2D(5.0, 1.0), Point2D(1.0, 1.0))
    r2.vertices = v_mas_uno
    print(f"r2 modificado:\n  > {r2}")
    print(f"Valores leidos:")
    print(f"  > color={r2.color}")
    print(f"  > vertices={r2.vertices}")
    print(f"  > area={r2.area()}; perimeter={r2.perimeter()}")

    print()
    print("--- Pruebas de Indexación e Iteración ---")
    print(f"Acceso a r2 por get_vertex(0): {r2.get_vertex(0)}")
    print(f"Acceso a r2 por r2[1] (__getitem__): {r2[1]}")

    print("Iterando vértices de r2:")
    for i, v in enumerate(r2):
        print(f"  Iteración {i}: {v}")

    print()
    print("--- Pruebas de Excepciones ---")
    print("Intentando acceder a un índice de vértice inválido (r2[4])...")
    try:
        r2[4]
    except IndexError as e:
        print(f"  > Se capturó excepción IndexError correctamente: {e}")

    print("Intentando instanciar Rectangle con vértices que no forman rectángulo...")
    try:
        v_invalidos = (Point2D(0,0), Point2D(0,0), Point2D(10,5), Point2D(90,90))
        Rectangle("red", v_invalidos)
    except InvalidFigureError as e:
        print(f"  > Se capturó excepción InvalidFigureError correctamente: {e}")

    print("Intentando instanciar Rectangle con una lista en lugar de tupla...")
    try:
        v_lista = [Point2D(0,2), Point2D(4,2), Point2D(4,0), Point2D(0,0)]
        Rectangle("red", v_lista)
    except InvalidFigureError as e:
        print(f"  > Se capturó excepción InvalidFigureError correctamente: {e}")

    print()
    print("--- Pruebas con Conjuntos (Set) ---")
    lista_rectangulos = [Rectangle("red", v_personalizados),
                         Rectangle("blue"),
                         Rectangle("red", v_personalizados)]
    print(f"Lista original con {len(lista_rectangulos)} rectángulos")
    conjunto_rectangulos = set(lista_rectangulos)
    print(f"Conjunto (sin duplicados) con {len(conjunto_rectangulos)} rectángulos")

    print()
    print(f"Figuras vivas (count): {Rectangle.count()}")
