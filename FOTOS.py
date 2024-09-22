import os
import shutil
from datetime import datetime

# Directorio de origen y destino
source_dir = 'ruta/a/tu/directorio/de/fotos'
destination_dir = 'ruta/a/tu/directorio/ordenado'

# Número máximo de archivos a procesar
max_files_to_process = 100  # Cambia este valor según tus necesidades

# Crear el directorio de destino si no existe
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

# Contador de archivos procesados
files_processed = 0

# Listar todos los archivos en el directorio de origen
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        if files_processed >= max_files_to_process:
            break
        
        file_path = os.path.join(root, filename)
        
        # Obtener la extensión del archivo
        file_extension = os.path.splitext(filename)[1].lower().strip('.')
        
        # Obtener la fecha de creación del archivo
        creation_time = os.path.getctime(file_path)
        creation_date = datetime.fromtimestamp(creation_time)
        
        # Crear la estructura de carpetas
        year_folder = creation_date.strftime('%Y') + '.' + file_extension
        month_folder = creation_date.strftime('%Y%m') + '.' + file_extension
        
        # Ruta completa de la carpeta de destino
        destination_path = os.path.join(destination_dir, file_extension, year_folder, month_folder)
        
        # Crear la carpeta de destino si no existe
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        
        # Mover el archivo a la carpeta correspondiente
        shutil.move(file_path, os.path.join(destination_path, filename))
        
        # Incrementar el contador de archivos procesados
        files_processed += 1

print(f"Archivos ordenados y movidos a la nueva estructura de carpetas. Total archivos procesados: {files_processed}")