# 1. Configuración para que Jupyter recargue los archivos .py automáticamente
%load_ext autoreload
%autoreload 2

# 2. Añadir la ruta al sistema para poder importar desde la carpeta src
import sys
sys.path.append("../") # Esto sube un nivel para encontrar 'src'

# 3. Importar tus funciones
import src.soporte as sp


