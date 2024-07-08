import ast
import json

def cargar_archivo_json(path:str,lista:list):

    with open(path, 'w', encoding='utf-8') as archivo_json:
        json.dump(lista, archivo_json, ensure_ascii=False, indent=4)

def leer_archivo_json(path):       
    # lista = []
    with open(path, 'r', encoding='utf-8') as archivo_json:
        lista = json.load(archivo_json)
    
    return lista

def cargar_archivo_CSV(path, lista:list):

    with open(path, "w", encoding="utf8") as archivo:
        for botones in lista:
            linea = f"{botones}\n"
            archivo.write(linea)

def leer_archivo_CSV(path) -> list[dict]:
    lista = []
    with open(path, "r", encoding="utf8") as archivo:
        for linea in archivo:

            # Eliminar espacios en blanco y nuevas líneas
            linea = linea.strip()
            if linea:  
                
                # Verificar que la línea no esté vacía
                # Convertir la línea en un diccionario
                
                diccionario = ast.literal_eval(linea)
                lista.append(diccionario)
    return lista

