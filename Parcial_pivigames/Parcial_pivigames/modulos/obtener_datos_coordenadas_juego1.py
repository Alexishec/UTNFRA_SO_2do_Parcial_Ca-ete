import pygame

def boton_volver_atras():
    regresar = "regresar"
    return regresar


def boton_reload():
    eleccion = "boton_reload"
    return eleccion
    pass
    

def boton_half():
    eleccion = "boton_half"
    return eleccion
    pass


def boton_next():
    eleccion = "boton_next"
    return eleccion
    pass


def boton_rojo():
    eleccion = "boton_rojo_elegido"
    return eleccion
    pass


def boton_azul():
    eleccion = "boton_azul_elegido"
    return eleccion
    pass


def boton_usado(boton_presionado):

    opcion = None

    match boton_presionado:
        case "boton_volver_atras":
            print("*"*50)
            print("boton_volver_atras\n")
            opcion = boton_volver_atras()
             

        case "boton_reload":
            print("*"*50)
            # print("boton_reloaded\n")
            opcion = boton_reload()

        case "boton_half":
            print("*"*50)
            # print("boton_half\n")
            opcion = boton_half()
            
        case "boton_next":
            print("*"*50)
            # print("boton_next\n")
            opcion = boton_next()

        case "boton_rojo":
            print("*"*50)
            # print("boton_rojo\n")
            opcion = boton_rojo()
            
        case "boton_azul":
            print("*"*50)
            # print("boton_azul\n")
            opcion = boton_azul()
        
        case _:
            print("*"*50)
            print("error")

    if opcion != None:
        return opcion
    
def click_bool(pos_x,pos_y,lista_botones:dict,lista_botones_presionados:dict)->bool|str:

    resultado = None


    for botones in lista_botones:
        for botones_presionados in lista_botones_presionados:

            if botones['name'] == botones_presionados['name']:
                
                if pos_x >= botones["x_y"][0] and pos_x <= (botones["x_y"][0]+botones["ancho_y_alto"][0]) and pos_y >= botones["x_y"][1] and pos_y <= (botones["x_y"][1]+botones["ancho_y_alto"][1]): 
                    resultado = boton_usado(botones['name'])
                    break

    return resultado


def respuesta_rectangulo(pos_x,pos_y,rojo_o_azul,lista_botones_presionados):
    resultado = None

    for botones in rojo_o_azul:
        for botones_presionados in lista_botones_presionados:
            if botones['name'] == botones_presionados['name']:

                if pos_x >= botones["coordenadas"][0] and pos_x <= (botones["coordenadas"][0]+botones["coordenadas"][2]) and pos_y >= botones["coordenadas"][1] and pos_y <= (botones["coordenadas"][1]+botones["coordenadas"][3]): 
                    resultado = boton_usado(botones['name'])
                    
    return resultado

