# Agregar Marca de Agua a PDF

Este proyecto contiene un script de Python para agregar una marca de agua de texto a un archivo PDF. El script utiliza las bibliotecas `PyPDF2` y `reportlab`.

## Requisitos

- Python 3.x
- Las bibliotecas `PyPDF2` y `reportlab`.

## Configuración del Entorno

1.  **Clona o descarga el repositorio.**

2.  **Instala las dependencias necesarias.**
    Abre una terminal o línea de comandos en el directorio del proyecto y ejecuta el siguiente comando para instalar las bibliotecas requeridas:

    ```bash
    pip install PyPDF2 reportlab
    ```

## Uso

1.  **Coloca tu archivo PDF.**
    Asegúrate de que el archivo PDF al que deseas agregar la marca de agua esté en el mismo directorio que el script `add_watermark.py`. Por defecto, el script busca un archivo llamado `Registro PC Jorge Ávila 2025.pdf`.

2.  **Ejecuta el script.**
    Abre una terminal en el directorio del proyecto y ejecuta el siguiente comando:

    ```bash
    python add_watermark.py
    ```

3.  **Encuentra el resultado.**
    El script generará un nuevo archivo PDF con la marca de agua aplicada. El archivo de salida se llamará `Registro PC Jorge Ávila 2025_watermarked.pdf` por defecto.

## Personalización

Puedes modificar el script `add_watermark.py` para cambiar el texto de la marca de agua, así como los nombres de los archivos de entrada y salida. Abre el archivo y edita las siguientes variables al final del script:

```python
if __name__ == "__main__":
    # Archivo PDF de entrada
    INPUT_FILE = "tu_archivo_de_entrada.pdf"
    
    # Archivo PDF de salida
    OUTPUT_FILE = "tu_archivo_de_salida_con_marca.pdf"
    
    # Texto de la marca de agua (usa '\n' para saltos de línea)
    WATERMARK_TEXT = "Línea 1\nLínea 2\nLínea 3"
    
    print(f"Adding watermark to {INPUT_FILE}...")
    add_watermark(INPUT_FILE, WATERMARK_TEXT, OUTPUT_FILE)
```
