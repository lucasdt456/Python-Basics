# Simulador de figuras geométricas básicas en 2D

Editor y simulador de figuras geométricas desarrollado en Python. Este proyecto permite crear un lienzo (`Drawing`) y añadir objetos geométricos (`Circle`, `Rectangle`, `Square`) sobre el plano euclidiano mediante el uso de coordenadas 2D. 

El proyecto cuenta con dos implementaciones para interaccionar con el lienzo:
- Una aplicación de consola como demostración programática de los métodos y estructuras.
- Una aplicación web con interfaz gráfica interactiva gracias al ecosistema de Streamlit.

## Tecnologías Utilizadas

- **Python**: Lenguaje base para la implementación de la lógica orientada a objetos (OOP).
- **Streamlit**: Framework empleado para la construcción y levantamiento de la interfaz web interactiva.
- **SVG**: Utilizado por debajo de la interfaz web para renderizar dinámicamente las figuras sobre el canvas 2D.

## Instalación y Configuración

El requisito principal del entorno es disponer de una versión reciente de **Python 3**.

Para ejecutar la aplicación web, es necesario instalar Streamlit. Puedes hacerlo instalando de la siguiente manera:

```bash
pip install streamlit
```

## Cómo Ejecutar y Lanzar la Aplicación

Existen dos formas de ejecutar este proyecto dependiendo de si quieres ver el ejemplo por terminal o interactuar visualmente con la web.

### 1. Ejecutar aplicación de consola

Abre una terminal en este directorio y lanza el archivo `app.py`:

```bash
python app.py
```
Se imprimirán por pantalla los distintos pasos que realiza el script de prueba, como añadir figuras, eliminar duplicados, aplicar traslaciones o sumar el total de sus áreas.

### 2. Lanzar aplicación interactiva web

Asegúrate de haber instalado Streamlit previamente, abre una terminal en esta misma carpeta y ejecuta:

```bash
streamlit run app-web.py
```
Automáticamente, se abrirá una nueva pestaña en tu navegador web por defecto levantando una interfaz visual donde podrás añadir figuras (y rellenar su posición en el gráfico), modificar su profundidad en el canvas (al frente o al fondo), y visualizar todo en tiempo real.
