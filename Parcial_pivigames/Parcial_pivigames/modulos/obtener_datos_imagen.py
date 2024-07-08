import pygame
from modulos.obtener_cargar_archivoCSV import leer_archivo_CSV

def recorrer_listas_imagenes(lista:dict,PANTALLA):
    for imagen in lista:
        PANTALLA.blit(imagen['imagen'],imagen['x_y'])
        

def retorno_imagenes(path) -> list[dict]:
    
    lista = leer_archivo_CSV(path)

    lista_datos_cargados_pygame = []
    for imagenes in lista:  
        nombre = imagenes['name']
        path_imagen_cargar = pygame.image.load(imagenes['path_imagen'])
        path_imagen_cargar = pygame.transform.scale(path_imagen_cargar, imagenes['ancho_y_alto'])
        
        ancho_y_alto = imagenes['ancho_y_alto']
        x_y = imagenes['width_height']

        lista_datos_cargados_pygame.append({"name": nombre, "imagen": path_imagen_cargar, "ancho_y_alto": ancho_y_alto, "x_y": x_y})
    
    return lista_datos_cargados_pygame
