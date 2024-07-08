import pygame


pygame.init()


def imprimir_texto(texto,PANTALLA,coordenadas,color):
    fuente = pygame.font.SysFont("Arial",20)
    texto = str(texto)
    texto = fuente.render(texto,False,[255,255,255],color)
    PANTALLA.blit(texto,coordenadas)


def recorrer_textos(min:int,max:int,lista_textos:list,PANTALLA):
    for i in range(min,max):
        imprimir_texto(lista_textos[i]['texto'],PANTALLA,lista_textos[i]['coordenadas'],lista_textos[i]['color'])