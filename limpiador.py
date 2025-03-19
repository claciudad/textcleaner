import re

# Nombre del archivo original y el de salida
input_file = "📖 Desarrollo de Apps con Python De 0 a Experto 🚀📱.md"
output_file = "limpio7.md"

# Expresiones regulares para limpieza
markdown_img_pattern = r"!\[.*?\]\(.*?\)"  # Eliminar imágenes Markdown
html_img_pattern = r"<img[^>]+>"  # Eliminar imágenes HTML
emoji_pattern = r"[\U0001F300-\U0001F6FF\U0001F900-\U0001F9FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U00002600-\U000026FF]"  # Eliminar emojis Unicode
markdown_double_asterisk_fix = r"\*\*"  # Eliminar "**" en cualquier parte
checkmark_to_bullet = r"✅"  # Reemplazar "✅" por "•"

# Diccionario para reemplazar los números emoji por números normales
emoji_numbers = {
    "0️⃣": "0", "1️⃣": "1", "2️⃣": "2", "3️⃣": "3", "4️⃣": "4",
    "5️⃣": "5", "6️⃣": "6", "7️⃣": "7", "8️⃣": "8", "9️⃣": "9"
}

# Variables para manejar tablas y estructuras de carpetas
inside_table = False
inside_structure = False
table_buffer = []
structure_buffer = []

# Leer el archivo y limpiar el contenido
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        stripped_line = line.strip()

        # Detectar si es una tabla (contiene "|") y manejarla correctamente
        if "|" in stripped_line:
            inside_table = True
            table_buffer.append(line)
            continue
        elif inside_table and stripped_line == "":
            inside_table = False
            outfile.writelines(table_buffer)
            outfile.write("\n")
            table_buffer = []

        # Detectar si es una estructura de carpetas (contiene ├── o └──)
        if "├──" in stripped_line or "└──" in stripped_line:
            inside_structure = True
            structure_buffer.append(line)
            continue
        elif inside_structure and stripped_line == "":
            inside_structure = False
            outfile.writelines(structure_buffer)
            outfile.write("\n")
            structure_buffer = []

        # Si estamos dentro de una tabla o una estructura de carpetas, no modificar nada
        if inside_table:
            table_buffer.append(line)
            continue
        if inside_structure:
            structure_buffer.append(line)
            continue

        # Reemplazar imágenes y emojis
        clean_line = re.sub(markdown_img_pattern, "", line)
        clean_line = re.sub(html_img_pattern, "", clean_line)
        clean_line = re.sub(emoji_pattern, "", clean_line)
        clean_line = re.sub(markdown_double_asterisk_fix, "", clean_line)  # Eliminar "**"
        clean_line = re.sub(checkmark_to_bullet, "•", clean_line)  # Reemplazar "✅" por "•"

        # Reemplazar los números emoji por números normales
        for emoji_num, num in emoji_numbers.items():
            clean_line = clean_line.replace(emoji_num, num)

        # Escribir solo las líneas que no quedaron vacías
        if clean_line.strip():
            outfile.write(clean_line + "\n")

print(f"✅ Proceso completado. Se ha generado '{output_file}' con las tablas y estructuras de carpetas intactas.")
