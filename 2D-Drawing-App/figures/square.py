from .rectangle import Rectangle
from .exceptions import InvalidFigureError
from .point2d import Point2D

class Square(Rectangle):
    
    def __init__(
            self,
            color="red",
            vertices=(
                Point2D(-1, 1),
                Point2D(1, 1),
                Point2D(1, -1),
                Point2D(-1, -1)
                )
            ):
        super().__init__(color)
        if not Square.__check(vertices):
            raise InvalidFigureError(
                    "El cuadrado no es válido."
                )
        self._vertices = vertices
    
    @staticmethod
    def __check(vertices):
        verificar_rectangulo = Rectangle._check(vertices)
        if not verificar_rectangulo:
            return False
        
        distancia1 = Point2D.distance(vertices[0], vertices[1]) # altura1
        distancia3 = Point2D.distance(vertices[1], vertices[2]) # base1
        
        return distancia1 == distancia3
    
    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, vertices):
        if not Square.__check(vertices):
            raise InvalidFigureError(
                    "El nuevo cuadrado no es válido."
                    )
        self._vertices = vertices

    def __str__(self):
        return (f"Square(color: {self._color}, "
                f"vertices: {self._vertices})")

if __name__ == "__main__":
    from .point2d import Point2D
    from .exceptions import InvalidFigureError

    print("--- Pruebas del Constructor ---")
    s1 = Square()
    print(f"[count: {Square.count()}] s1 = {s1}")
    v_cuadrado = (Point2D(-2.0, 2.0), Point2D(2.0, 2.0), Point2D(2.0, -2.0), Point2D(-2.0, -2.0))
    s2 = Square("blue", v_cuadrado)
    print(f"[count: {Square.count()}] s2 = {s2}")
    
    print()
    print("--- Pruebas del Destructor ---")
    del(s1) # invocamos destructor __del__
    print(f"[count: {Square.count()}] del(s1)")
    
    print()
    print("--- Pruebas de Comparación ---")
    s_eq_1 = Square("red", v_cuadrado)
    s_eq_2 = Square("red", v_cuadrado)
    s_diff = Square("blue", v_cuadrado)
    
    print(f"s_eq_1: {s_eq_1}")
    print(f"s_eq_2: {s_eq_2}")
    print(f"s_diff: {s_diff}")
    
    print(f"  > s_eq_1 == s_eq_2: {s_eq_1 == s_eq_2}")
    print(f"  > s_eq_1 != s_eq_2: {s_eq_1 != s_eq_2}")
    print(f"  > s_eq_1 == s_diff: {s_eq_1 == s_diff}")

    print()
    print("--- Pruebas de Getters, Setters y Métodos ---")
    print(f"s2 antes:\n  > {s2}")
    s2.color = "red"
    v_cuad_nuevo = (Point2D(0.0, 4.0), Point2D(4.0, 4.0), Point2D(4.0, 0.0), Point2D(0.0, 0.0))
    s2.vertices = v_cuad_nuevo
    print(f"s2 modificado:\n  > {s2}")
    print(f"Valores leidos:")
    print(f"  > area={s2.area()}; perimeter={s2.perimeter()}")

    print()
    print("--- Pruebas de Indexación e Iteración ---")
    print(f"Acceso a s2 por s2.get_vertex(0): {s2.get_vertex(0)}")
    print(f"Acceso a s2 por s2[1] (__getitem__): {s2[1]}")
    
    print("Iterando vértices de s2:")
    for i, v in enumerate(s2):
        print(f"  Iteración {i}: {v}")

    print()
    print("--- Pruebas de Excepciones ---")
    print("Intentando instanciar Square con vértices de rectángulo (no cuadrado)...")
    try:
        # Vértices de un rectángulo 4x2
        v_rectangulo = (Point2D(0.0, 2.0), Point2D(4.0, 2.0), Point2D(4.0, 0.0), Point2D(0.0, 0.0))
        Square("red", v_rectangulo)
    except InvalidFigureError as e:
        print(f"  > Se capturó excepción InvalidFigureError correctamente: {e}")

    print("Intentando modificar un cuadrado con vértices completamente inválidos...")
    try:
        v_invalidos = (Point2D(0,0), Point2D(0,0), Point2D(10,5), Point2D(90,90))
        s2.vertices = v_invalidos
    except InvalidFigureError as e:
        print(f"  > Se capturó excepción InvalidFigureError correctamente: {e}")

    print()
    print("--- Pruebas con Conjuntos (Set) ---")
    lista_cuadrados = [Square("red", v_cuadrado),
                       Square("blue"),
                       Square("red", v_cuadrado)]
    print(f"Lista original con {len(lista_cuadrados)} cuadrados")
    conjunto_cuadrados = set(lista_cuadrados)
    print(f"Conjunto (sin duplicados) con {len(conjunto_cuadrados)} cuadrados")
    
    print()
    print(f"Figuras vivas (count): {Square.count()}")
