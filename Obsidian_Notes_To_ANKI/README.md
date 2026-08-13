# Obsidian Notes To ANKI

Utilidad de consola en Python para desactivar notas antiguas de Obsidian creadas con el plugin [Obsidian_to_Anki](https://community.obsidian.md/plugins/obsidian-to-anki-plugin).

El script localiza las líneas `TARGET DECK: Nombre del Mazo` o `TARGET DECK` seguido del nombre del mazo (siguiente línea) y las comenta para que esa nota deje de actuar como redirección hacia ANKI. No borra tarjetas ya creadas ni modifica directamente la base de datos de ANKI: solo inutiliza la nota dentro de la bóveda de Obsidian.

El objetivo es práctico y de aprendizaje. Existen alternativas más cómodas o completas, como el propio [Obsidian_to_Anki](https://community.obsidian.md/plugins/obsidian-to-anki-plugin), [AnkiSync+](https://community.obsidian.md/plugins/ObsidianAnkiSync) u otros flujos que permiten excluir carpetas enteras o usar carpetas de archivo/basura para gestionar la sincronización sin editar nota por nota (con validación y respaldo oficial).

## Estado del proyecto

El proyecto está finalizado. Está pensado para manejarse desde consola, mediante un menú interactivo o pasando argumentos con el script ejecutable. Tiene tres opciones de uso:

1. Un fichero concreto.
2. Un directorio completo.
3. Toda la bóveda.

*Cuanto mayor sea la profundidad del árbol de carpetas o el tamaño de la bóveda, más costosa será la ejecución de las opciones 2 y 3.*

Cuenta con tests unitarios y de integración, y con loggings detallados (con un archivo `.log` por cada nota modificada).

## Qué hace

- Busca referencias a `TARGET DECK` en notas de Obsidian.
- Comenta o neutraliza la línea encontrada para que deje de ser interpretada por el flujo de Obsidian hacia ANKI.
- Conserva la nota original dentro de Obsidian, pero sin redirección activa (dejándola inhabilitada).
- **IMPORTANTE:** No elimina mazos ni tarjetas ya importadas en ANKI (internas de la base de datos).

## Tecnologías

Este proyecto usa librerías estándar y externas (externa solo pytest), junto un gestor de paquetes e instalador moderno y un linter y formateador unificado:

- Python 3.13 o superior.
- `pathlib` para manejar rutas y archivos.
- `sys` para salida de proceso y control de ejecución.
- `argparse` para construir la interfaz de consola.
- `pytest` para pruebas unitarias y testing automatizado.
- `logging` para registro de eventos, errores, depuración y control del flujo de ejecución. Con un archivo de log por cada nota modificada en la ruta: `src/obsidian_notes_to_anki/tests/test_files.log`.
- `tempfile` para generar archivos temporales de forma segura y atómica.
- `uv` como gestor de entorno, dependencias y ejecución.
- `ruff` como linter y formateador (configurado para que limpie el código en cada guardado).

## Instalación

1. Instala [`uv`](https://docs.astral.sh/uv/getting-started/installation/) si todavía no lo tienes.
2. Entra en la carpeta del proyecto `Obsidian_Notes_To_ANKI`.
3. Sincroniza el entorno del proyecto con `uv` o corre el script directamente con Python.

Ejemplo:

```bash
uv sync
# ó
uv run src/obsidian_notes_to_anki/main.py
```

## Uso

Correr el archivo `main.py` con `uv` para uso de menú por consola:

```bash
# forma sencilla mediante el script ejectuable (desde cualquier ruta si el entorno está sincronizado):
obsidian-notes-to-anki
# ó con run:
uv run src/obsidian_notes_to_anki/main.py
```

También admite la selección de opción por parámetro:

```bash
# explicación básica de uso por parámetros:
obsidian-notes-to-anki --help 
# ó
obsidian-notes-to-anki -h 

# ejemplo de uso:
uv run src/obsidian_notes_to_anki/main.py -o 1 
uv run src/obsidian_notes_to_anki/main.py --option 1
# con opciones 2 y 3 también disponibles
```

Opciones disponibles:

1. `1 - Limpiar un único fichero.`
2. `2 - Limpiar un directorio completo.`
3. `3 - Limpiar toda la bóveda.`

*Si no indicas una opción por parámetro, el programa muestra un menú interactivo en consola.*

### Opción 1

La opción 1 pide la ruta completa de un archivo y comprueba que exista antes de procesarlo. Si el archivo existe, lo abre, busca las línea `TARGET DECK` y la comenta dejando la nota inhabilitada para su redirección a ANKI.

### Opción 2

La opción 2 pide la ruta completa de un directorio, comprueba que existe y que sea un directorio. Si es un directorio, busca de manera recursiva todos los archivos internos `.md` con la línea `TARGET DECK` y deja todas las notas del directorio inhabilitadas. *Al resto de archivos los ignora.*

### Opción 3

La opción 3 pide la ruta completa de la bóveda (raíz), comprueba que existe y que es un directorio. Si es un directorio procede a realizar el mismo algoritmo recursivo que la opción 2.

*En las 3 opciones se muestra por consola el total de archivos modificados y quedan loggeados en el `test_files.log`.*

## Limitaciones actuales

- No elimina contenidos dentro de ANKI.
- No sustituye una estrategia de exclusión de carpetas bien configurada del plugin original.

## Desarrollo

El repositorio está organizado como un proyecto Python moderno con `src/`, `pytest`, `logging`, `uv` y `ruff`. La intención es mantener el código pequeño, trazable, limpio y fácil de validar con tests y logs.

El proyecto está pensado para uso personal, pero ha sido creado para poder ser usado por cualquier persona que utilice una configuración de ANKI parecida a la que se indica: con `TARGET DECK` para el nombre del mazo, y con preguntas creadas con `#basic` o `START`.

El proyecto genera un `test_files.log` en la ruta `src/obsidian_notes_to_anki/tests/test_files.log` por cada nota que se modifique *(indiferentemente de la opción seleccionada)*. El log contiene información detallada para depuración, búsqueda de errores y cambios realizados. Permitiendo identificar en todo momento que nota/s han sido modificada/s y cuáles no.