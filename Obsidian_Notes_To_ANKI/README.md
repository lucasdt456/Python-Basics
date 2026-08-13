# Obsidian Notes To ANKI

Utilidad de consola en Python para desactivar notas antiguas de Obsidian creadas con el plugin [Obsidian_to_Anki](https://community.obsidian.md/plugins/obsidian-to-anki-plugin).

El script localiza las líneas `TARGET DECK: Nombre del Mazo` o `TARGET DECK` seguido del nombre del mazo y las comenta para que esa nota deje de actuar como redirección hacia ANKI. No borra tarjetas ya creadas ni modifica directamente la base de datos de ANKI: solo inutiliza la nota dentro de la bóveda de Obsidian.

El objetivo es práctico y de aprendizaje. Existen alternativas más cómodas o completas, como el propio [Obsidian_to_Anki](https://community.obsidian.md/plugins/obsidian-to-anki-plugin), [AnkiSync+](https://community.obsidian.md/plugins/ObsidianAnkiSync) u otros flujos que permiten excluir carpetas enteras o usar carpetas de archivo/basura para gestionar la sincronización sin editar nota por nota.

## Estado del proyecto

El proyecto todavía está en desarrollo. Ya existe una base funcional para trabajar desde consola, pero todavía faltan archivos, ajustes de comportamiento y tests.

En este momento el flujo principal está pensado para:

1. Un fichero concreto.
2. Un directorio completo.
3. Toda la bóveda.

*Cuanto mayor sea la profundidad del árbol de carpetas o el tamaño de la bóveda, más costosa será la ejecución de las opciones 2 y 3.*

## Qué hace

- Busca referencias a `TARGET DECK` en notas de Obsidian.
- Comenta o neutraliza la línea encontrada para que deje de ser interpretada por el flujo de Obsidian hacia ANKI.
- Conserva la nota original dentro de Obsidian, pero sin redirección activa.
- **IMPORTANTE:** No elimina mazos ni tarjetas ya importadas en ANKI.

## Tecnologías

Este proyecto usa librerías estándar y externas (solo pytest), junto un gestor de paquetes e instalador moderno y un linter y formateador unificado:

- Python 3.13 o superior.
- `pathlib` para manejar rutas y archivos.
- `sys` para salida de proceso y control de ejecución.
- `os` para tipado y utilidades de rutas.
- `argparse` para construir la interfaz de consola.
- `pytest` para pruebas unitarias y testing automatizado.
- `logging` para registro de eventos, errores, depuración y control del flujo de ejecución.
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
uv run src/obsidian_notes_to_anki/main.py -o 1 
uv run src/obsidian_notes_to_anki/main.py --option 1
# con opciones 2 y 3 también disponibles
```

Opciones disponibles:

1. `1 - Limpiar un único fichero.`
2. `2 - Limpiar un directorio completo.`
3. `3 - Limpiar toda la bóveda.`

Si no indicas una opción por parámetro, el programa muestra un menú interactivo en consola.

### Opción 1

La opción 1 pide la ruta completa de un archivo y comprueba que exista antes de procesarlo.

### Opción 2 y 3

Estas opciones forman parte del objetivo del proyecto y están pensadas para ampliar el alcance a carpetas y bóvedas enteras. Al ser recorridos más amplios, su coste depende directamente de la cantidad de archivos y de la profundidad de los directorios.

## Limitaciones actuales

- No elimina contenidos dentro de ANKI.
- No sustituye una estrategia de exclusión de carpetas bien configurada en el plugin original.
- El proyecto aún está en evolución y puede cambiar la forma exacta de tratar archivos y directorios.

## Desarrollo

El repositorio está organizado como un proyecto Python moderno con `src/`, `pytest`, `logging`, `uv` y `ruff`. La intención es mantener el código pequeño, trazable, limpio y fácil de validar con tests y logs *(sin archivo `app.log`)*.
