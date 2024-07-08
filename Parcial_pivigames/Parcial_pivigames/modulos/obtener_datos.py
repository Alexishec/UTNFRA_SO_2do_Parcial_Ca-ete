import pygame
import random

def numero_aleatorio(min:int,max:int):
    numero = random.randint(min,max)
    return numero

def elegir_pregunta(lista_preguntas:list,lista_preguntas_ya_hechas:list):

    contador=0
    for pregunta in lista_preguntas:
        if pregunta in lista_preguntas_ya_hechas:
            contador += 1

    # Si todas las preguntas ya han sido hechas
    if contador >= len(lista_preguntas):    
        respuesta_1 = "Ya respondiste"
        respuesta_2 = "Todo"
        return respuesta_1, respuesta_2, lista_preguntas_ya_hechas

    # Seleccionar una pregunta no hecha aún
    while True:

        numero = numero_aleatorio(0, len(lista_preguntas) - 1)
        pregunta_seleccionada = lista_preguntas[numero]
        if pregunta_seleccionada not in lista_preguntas_ya_hechas:
            lista_preguntas_ya_hechas.append(pregunta_seleccionada)
            break

    respuesta_1 = pregunta_seleccionada['opcion_1']
    respuesta_2 = pregunta_seleccionada['opcion_2']
    return respuesta_1, respuesta_2, lista_preguntas_ya_hechas


def conseguir_temporizados(tiempo_inicial):
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = tiempo_actual - tiempo_inicial
    tiempo_mostrado = tiempo_transcurrido*0.001

    return tiempo_transcurrido,tiempo_mostrado

    
def conseguir_votos_jurado(min):
    lista = []
    for i in range(min):

        numero = numero_aleatorio(1,2) 
        lista.append(numero)

    return lista

def cambiar_color_cuadrados(lista_rectangulos:list,lista_votos:list,minimo):

    for i in range(minimo):
        if lista_votos[i] == 1 :
            lista_rectangulos[i]['color'] = [255,0,0]
        elif lista_votos[i] == 2:
            lista_rectangulos[i]['color'] = [0,0,255]
        else:
            print("error")

    return lista_rectangulos

def conseguir_votos(lista_votos:list):
    contador_rojos = 0
    contador_azul = 0
    for jurados in lista_votos:
        if jurados == 1:
            contador_rojos += 1
        else:
            contador_azul += 1
    if contador_rojos>contador_azul:
        ganador = "votantes_rojos"
    else:
        ganador = "votantes_azules"
    return ganador

# def retorno_numeros_cuadrado(color):
#     votos_rojos = -1
#     votos_azules = -1
#     contador_de_cuadrados = 0
#     posicion = 0
#     separacion = 0
#     votos_totales =0

#     if color == 255:
#         if votos_rojos <= 5:
#             votos_rojos+=1
#         valor_rojo = 465
#         votos_totales = votos_rojos
#         contador_de_cuadrados+=1
#         posicion = valor_rojo
#         separacion = 50

#     elif color== 0:
#         if votos_azules <= 5:
#             votos_azules+=1
#         valor_azul = 715
#         votos_totales = votos_azules
#         contador_de_cuadrados+=1
#         posicion = valor_azul
#         separacion = -50

#     return posicion,separacion,votos_totales



# def visualizar_cuadrado(lista:list):
#     votos_rojos = -1
#     votos_azules = -1
#     contador_de_cuadrados = 0
#     for porcentaje in lista:
#         posicion,separacion,votos_totales= retorno_numeros_cuadrado(porcentaje['color'])
#         if contador_de_cuadrados<=5:
#             porcentaje['tamaño'][0]=posicion+(separacion*votos_totales)
#             porcentaje['tamaño'][1]=350
#             porcentaje['tamaño'][2]=45
#             porcentaje['tamaño'][3]=45

#     return lista
#     pass