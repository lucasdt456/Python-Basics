class InvalidFigureError(Exception):
    """
    Excepción lanzada cuando una figura intenta instanciarse o
    tales como colores no permitidos o vértices incorrectos.
    """
    pass

if __name__ == "__main__":
    try:
        raise InvalidFigureError("Mensaje Error Prueba.")
    except InvalidFigureError as e:
        print(f"Se ha detecatado un error, figura inválida. {e}")


    
