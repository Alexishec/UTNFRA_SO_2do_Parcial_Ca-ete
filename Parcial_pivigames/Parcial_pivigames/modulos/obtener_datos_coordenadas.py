import pygame
from modo_de_juegos.esto_aquello_juego import game_start

def accion_boton_trivia():
    print("\n")
    print("-"*50)
    return print("trivia\n")


def accion_boton_esto_aquello(lista_vacia:list):
    print("\n")
    print("-"*50)
    print("esto o aquello\n")
    terminar_juego = game_start(lista_vacia)
    return terminar_juego
    

def accion_boton_configuracion():
    print("\n")
    print("-"*50)
    print("confirguracion\n")


def accion_boton_skin():
    print("\n")
    print("-"*50)
    print("skins\n")


def boton_usado(boton_presionado):

    opcion_booleana = None
    lista_vacia = []

    match boton_presionado:
        case "boton_inicio":
            opcion_booleana = False
            print("\n")
            print("-"*50)
            print("boton_inicio/start\n")

        case "boton_trivia":
            accion_boton_trivia()

        case "boton_decicion":
            opcion_booleana = accion_boton_esto_aquello(lista_vacia)

        case "boton_configuracion":
            accion_boton_configuracion()

        case "boton_skins":
            accion_boton_skin()

        case "usuario_skins":
            accion_boton_skin()        
        case _:
            print("error")


    if opcion_booleana != None:
        return opcion_booleana
    
def click_botones_booleanos(pos_x,pos_y,lista_botones:dict,lista_botones_presionados:dict):

    resultado = None

    for botones in lista_botones:
        for botones_presionados in lista_botones_presionados:

            if botones['name'] == botones_presionados['name']:
                if pos_x >= botones["x_y"][0] and pos_x <= (botones["x_y"][0]+botones["ancho_y_alto"][0]) and pos_y >= botones["x_y"][1] and pos_y <= (botones["x_y"][1]+botones["ancho_y_alto"][1]): 
                    resultado = boton_usado(botones['name'])
                    break

    return resultado

