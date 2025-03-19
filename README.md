
```md
# 🧹 Lipiador - Limpieza Avanzada de Archivos Markdown  

**Lipiador** es una herramienta en Python diseñada para limpiar archivos Markdown de manera automática, eliminando imágenes, emojis y otros elementos no deseados, mientras mantiene intacta la estructura del documento, incluyendo tablas y esquemas de carpetas.  

## ✨ Características  

✔️ **Elimina imágenes** en formato Markdown (`![texto](url)`) y HTML (`<img src="..." >`).  
✔️ **Elimina emojis** sin afectar el contenido del texto.  
✔️ **Corrige asteriscos sueltos (`**`)** que pueden quedar tras la eliminación de contenido.  
✔️ **Reemplaza `✅` por `•`** para mejorar la presentación de listas.  
✔️ **Convierte números emoji (`0️⃣-9️⃣`) en números normales (`0-9`).**  
✔️ **Preserva tablas Markdown** sin alterar su estructura.  
✔️ **Mantiene intactas las estructuras de carpetas** con caracteres como `├──` y `└──`.  

## 🚀 Instalación  

Para utilizar **Lipiador**, necesitas **Python 3.x** instalado en tu sistema.  

1. **Clonar el repositorio**  
   ```sh
   git clone https://github.com/tu-usuario/lipiador.git
   cd lipiador
   ```

2. **Ejecutar el script**  
   ```sh
   python limpiador.py
   ```

## 🔧 Uso  

1. **Coloca el archivo Markdown que deseas limpiar** en la misma carpeta que el script.  
2. **Modifica el archivo `limpiador.py`** y cambia `input_file` para indicar el nombre del archivo Markdown que deseas procesar.  
3. **Ejecuta el script** y generará un archivo limpio llamado `limpio.md` con todo el contenido formateado correctamente.  

## 📌 Ejemplo de Entrada  

Archivo original con emojis, imágenes y estructura de carpetas:  

```md
# Desarrollo de Apps con Python 🚀📱

![Ejemplo](imagen.png)

Python tiene múltiples tipos de datos:

| Tipo    | Descripción                 | Ejemplo                         |
| ------- | --------------------------- | ------------------------------- |
| `int`   | Números enteros             | `10, -5, 1000`                  |
| `float` | Números decimales           | `3.14, -2.5, 100.0`             |

Estructura del proyecto:

mi_proyecto/
├── `main.py` (Código principal de la app)
├── `kv_file.kv` (Diseño de la interfaz)
└── `assets/` (Imágenes, íconos y otros recursos)
```

## ✅ Resultado después de la limpieza  

```md
# Desarrollo de Apps con Python

Python tiene múltiples tipos de datos:

| Tipo    | Descripción                 | Ejemplo                         |
| ------- | --------------------------- | ------------------------------- |
| `int`   | Números enteros             | `10, -5, 1000`                  |
| `float` | Números decimales           | `3.14, -2.5, 100.0`             |

Estructura del proyecto:

mi_proyecto/
├── `main.py` (Código principal de la app)
├── `kv_file.kv` (Diseño de la interfaz)
└── `assets/` (Imágenes, íconos y otros recursos)
```

## 📜 Licencia  

Este proyecto está bajo la licencia **MIT**, lo que significa que puedes utilizarlo, modificarlo y compartirlo libremente.  

---

### **🔗 Contribuciones**  
Si tienes sugerencias, mejoras o encuentras un error, ¡no dudes en hacer un pull request o abrir un issue en GitHub!  

---

