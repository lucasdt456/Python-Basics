#!/usr/bin/env python3
from pathlib import Path
import time
import subprocess
from datetime import datetime

def comprobar_archivos_directorios():

    directorio_descargas=Path.home()/"Descargas"
    tiempo_ahora=time.time()
    LIMITE_SEGUNDOS=86400 # 24h
    LIMITE_TAMANIO=3*(1024**3) # 3GB
    fecha=datetime.now().strftime("%Y-%m-%d")
    archivos_procesados=0
    archivos_sin_mover=0

    archivo_log=directorio_descargas/"Logs_Novedades"
    archivo_log.mkdir(parents=True, exist_ok=True) 

    try:
        if not directorio_descargas.exists():
            print(f"Error. No se encuentra {directorio_descargas}")
            return

        for archivo in directorio_descargas.iterdir():

            if archivo.is_dir() or archivo.name.startswith("."):
                continue

            tiempo_archivo = archivo.stat().st_mtime
            tamanio_archivo = archivo.stat().st_size
            antiguedad = tiempo_ahora - tiempo_archivo

            if antiguedad > LIMITE_SEGUNDOS:
                extension=archivo.suffix
                nombre_carpeta=f"Archivos_Antiguos/Extension_{extension.upper().replace(".","")}"
                directorio_antiguedad=directorio_descargas/nombre_carpeta

                if not directorio_antiguedad.exists():
                    directorio_antiguedad.mkdir(parents=True, exist_ok=True)

                if tamanio_archivo>=LIMITE_TAMANIO:
                    ruta_zip_destino=directorio_descargas/"Comprimidos"
                    if not ruta_zip_destino.exists():
                        ruta_zip_destino.mkdir(parents=True, exist_ok=True)
                    archivo_comprimido=ruta_zip_destino/f"{archivo.stem}.zip"
                    subprocess.run([
                        "zip",
                        "-j", # zip -j (junk paths) no guarda la estructura de carpetas dentro del zip
                        str(archivo_comprimido),
                        str(archivo),
                        ], check=True, capture_output=True) # Para que no ensucie la consola del cron
                        
                    archivo.unlink() # Borramos el original

                else:
                    print(f"Moviendo {archivo.name}...")
                    subprocess.run(["mv", str(archivo), str(directorio_antiguedad)])
                    
                archivos_procesados+=1

            else:
                archivos_sin_mover+=1

    except Exception as e:
        print(f"Error durante la ejecución: {e}")

    ruta_final_log = archivo_log / f"logs_{fecha}.log"
    with open(ruta_final_log,"a") as logs:
        logs.write("=========================================================\n")
        logs.write(f"Ejecución el día: {fecha}\n")
        logs.write("---------------------------------------------------------\n")
        logs.write(f"Total de archivos procesados (movidos/zip): {archivos_procesados}\n")
        logs.write("---------------------------------------------------------\n")
        logs.write(f"Total de archivos ignorados (recientes): {archivos_sin_mover}\n")
        logs.write("=========================================================\n")

    print(f"Fin del script. Procesados: {archivos_procesados}")

if __name__ == '__main__':
    comprobar_archivos_directorios()
