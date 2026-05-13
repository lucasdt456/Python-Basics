from figures import Circle, Rectangle, Square, Point2D, Drawing

def main():
    print("--- Inicializando el dibujo con un Círculo y un Cuadrado ---")
    dibujo1 = Drawing()
    circulo1 = Circle()
    cuadrado1 = Square(color = "blue")
    dibujo1.add_front(circulo1)
    dibujo1.add_back(cuadrado1)
    
    print()
    print("--- Mostrando todo el contenido ---")
    dibujo1.print_all()

    print()
    print("--- Introduciendo duplicados intencionadamente ---")
    circulo_duplicado = Circle()
    cuadrado_duplicado = Square(color = "blue")
    dibujo1.add_front(cuadrado_duplicado)
    dibujo1.add_back(circulo_duplicado)

    print()
    print("--- Mostrando todo el contenido (con duplicados) ---")
    dibujo1.print_all()

    print()
    print("--- Eliminando duplicados ---")
    dibujo1.remove_duplicates()

    print()
    print("--- Mostrando todo el contenido (limpio) ---")
    dibujo1.print_all()

    print()
    print("--- Añadiendon un Rectángulo y un Círculo ---")
    rectangulo1 = Rectangle(color = "green")
    circulo2 = Circle(color = "blue", center = Point2D(2.5, 2.5), radius = 2)
    dibujo1.add_front(rectangulo1)
    dibujo1.add_back(circulo2)

    print()
    print("--- Mostrando todo el contenido ---")
    dibujo1.print_all()

    print()
    print("--- Añadiendo uin Círculo y un Cuadrado ---")
    cuadrado2 = Square(color = "blue", vertices = (
                           Point2D(2, 4), Point2D(4, 4),
                           Point2D(4, 2), Point2D(2, 2)
                           ))
    circulo3 = Circle(color = "green", center = Point2D(-1, 5), radius = 1.5)
    dibujo1.add_front(cuadrado2)
    dibujo1.add_back(circulo3)

    print()
    print("--- Mostrando todo el contenido ---")
    dibujo1.print_all()

    print()
    print("--- Calculando área total de círculos ---")
    
    print(" > Suma de áreas:", dibujo1.get_area_all_circles())

    print()
    print("--- Trasladando todos los cuadrados con incremento (+10, +10) ---")
    dibujo1.move_squares(10, 10)

    print()
    print("--- Mostrando contenidos tras la trasladación ---")
    dibujo1.print_all()


if __name__ == "__main__":
    main()
