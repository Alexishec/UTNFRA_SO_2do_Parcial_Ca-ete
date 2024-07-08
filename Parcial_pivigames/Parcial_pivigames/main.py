import pygame
from os import system
from modulos.obtener_datos_coordenadas import *
from modulos.obtener_datos_imagen import *
from modulos.obtener_cargar_archivoCSV import *
from modulos.imprimir_texto import recorrer_textos
# from modulos.recorrer_datos import recorrer_listas_imagenes
system("cls")
ANCHO = 1200
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))


# DEFINIMOS LAS LISTAS A UTILIZAR
lista_imagenes_sala_inicio = []
lista_imagenes_menu = []
lista_botones = []
lista_jurados = []
lista_botones_presionados = []
lista_usuario = []
lista_preguntas_ya_hechas = []
lista_puntuacion_usuario = []




# CONVERTIMOS LAS LISTAS EN ALGO QUE PYGAME PUEDA USAR

# RETORNO DE IMAGENES Y LISTAS DE '.CSV'
lista_imagenes_sala_inicio = retorno_imagenes("Parcial_pivigames/archivosCSV/imagenes_sala_inicio.csv")
lista_imagenes_menu = retorno_imagenes("Parcial_pivigames/archivosCSV/imagenes_menu.csv")
lista_usuario = retorno_imagenes("Parcial_pivigames/archivosCSV/usuario_votacion.csv")
lista_jurados = retorno_imagenes("Parcial_pivigames/archivosCSV/jurados_vitrinas.csv")
lista_botones = retorno_imagenes("Parcial_pivigames/archivosCSV/lista_botones_menu.csv")
lista_botones_presionados = leer_archivo_CSV("Parcial_pivigames/archivosCSV_interactivos/lista_botones_interactivos.csv")

#RETORNO DE AECHIVOS DE '.JSON'
# lista_puntuacion_usuario = leer_archivo_json("Parcial_pivigames/archivosCSV/Puntuacion_usuario.json")


# ENCAPSULAMOS TODAS LAS LISTAS PARA SU USO EN RAPIDA SUCESION
lista_ultimate = [
    lista_imagenes_menu,
    lista_usuario,
    lista_botones,
    lista_jurados
]


# DECLARAMOS BANDERAS
bandera=True
transicion = True
terminar_juego = False


while bandera:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
            break


        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos_x = evento.pos[0]
            pos_y = evento.pos[1]


            if transicion==True:
                transicion_efectuada = click_botones_booleanos(pos_x,pos_y,lista_imagenes_sala_inicio,lista_botones_presionados)


                if transicion_efectuada != None:
                    transicion=transicion_efectuada


            else:
                terminar_juego = click_botones_booleanos(pos_x,pos_y,lista_botones,lista_botones_presionados)
                



    if transicion:           
        recorrer_listas_imagenes(lista_imagenes_sala_inicio,PANTALLA)


    else:
        for elementos in lista_ultimate:
            lista_puntuacion_usuario = leer_archivo_json("Parcial_pivigames/archivosCSV/Puntuacion_usuario.json")
            recorrer_listas_imagenes(elementos,PANTALLA)
            recorrer_textos(0,len(lista_puntuacion_usuario),lista_puntuacion_usuario,PANTALLA)


    if terminar_juego == True:
        bandera = False


    pygame.display.update()
pygame.quit()