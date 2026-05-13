import math

class Point2D:
    
    def __init__(self, x=0, y=0):
        if not isinstance(x, (float, int)) and isinstance(y, (float, int)):
            raise ValueError("Error de coordenadas 'x' e 'y' (no float / int)")
        self.x = float(x)
        self.y = float(y)
    
    @staticmethod
    def distance(a, b):
        return math.sqrt(math.pow(a.x - b.x, 2) + math.pow(a.y - b.y, 2))

    def __eq__(self, other):
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        if not isinstance(other, Point2D):
            return False
        return not(self.__eq__(other))

    def __hash__(self):
        return hash((self.x, self.y))
    
    def __getitem__(self, key):
        if key in ("x", "X", 0):
            return self.x
        elif key in ("y", "Y", 1):
            return self.y
        else:
            raise KeyError("Error en la clave ingresada; no válida.")
        
    def __setitem__(self, key, value):
        if key in ("x", "X", 0):
            self.x = value
        elif key in ("y", "Y", 1):
            self.y = value
        else:
            raise KeyError("Error en la clave ingresada; no válida.")

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    a = Point2D(0, 0.0)
    b = Point2D(1.0, 1)

    print(f"a = {a}; b = {b}")
    print(f"> d(a,b) = {Point2D.distance(a, b):.5f}") # ~1.41421
    print(f"> a==b --> {a == b}") # False
    print(f"> a!=b --> {a != b}") # True

    print()
    a = Point2D(1, 1) # re-instanciamos a con el valor de b
    print(f"a = {a}; b = {b}")
    print(f"> d(a,b) = {Point2D.distance(a, b)}") # 0.0
    print(f"> a==b --> {a == b}") # True
    print(f"> a!=b --> {a != b}") # False

    print()
    print(f"> a == tuple(1,1) --> {a == (1,1)}")
    print(f"> a != tuple(1,1) --> {a != (1,1)}")

    print()
    print("Intentando crear un Point2D con valores no numéricos...")
    try:
        Point2D("a", 0)
    except ValueError:
        print("> Se capturó excepción ValueError correctamente")
    try:
        Point2D(0, "CERO")
    except ValueError:
        print("> Se capturó excepción ValueError correctamente")

    # Prueba de conjuntos (sets)
    print()
    lista_puntos = [Point2D(1, 1), Point2D(2, 1), Point2D(1, 2),
                    Point2D(2, 2), Point2D(1, 1), Point2D(2, 2)]
    print(f"Lista de {len(lista_puntos)} puntos: {lista_puntos}") # 6 puntos
    conjunto_puntos = set(lista_puntos)
    print(f"> Conjunto de {len(conjunto_puntos)} puntos únicos de la lista: {conjunto_puntos}") # 4 puntos

    # Pruebas de indexadores
    print()
    p = Point2D(5.0, 10.0)
    print(f"p = {p}")
    print(f"> p[0] = {p[0]};\n> p['x'] = {p['x']}\n> p['X'] = {p['X']}")
    print(f"> p[1] = {p[1]};\n> p['y'] = {p['y']}\n> p['Y'] = {p['Y']}")
    p[0] = 7.0
    p['y'] = -3.0
    print(f"Tras modificar con indexadores:\n> p = {p}")
    print()
    print("Intentando acceder a una clave inválida de p...")
    try:
        print(p[2])
    except KeyError:
        print("> Se capturó excepción KeyError correctamente")
