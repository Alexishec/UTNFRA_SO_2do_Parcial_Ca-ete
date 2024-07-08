import pygame
import pygame.locals
from modulos.obtener_datos_coordenadas_juego1 import *
from modulos.obtener_datos_imagen import *
from modulos.obtener_cargar_archivoCSV import *
from modulos.obtener_datos import *
from modulos.imprimir_texto import *

sound = pygame.mixer.Sound("Parcial_pivigames/sonidos/Y2meta.app - Sonido de decepción (128 kbps).mp3")

def game_start(lista_preguntas_ya_hechas:list):

    pygame.init()
    # print("Hora del juego!!!")

    ANCHO = 1200
    ALTO = 600
    PANTALLA = pygame.display.set_mode((ANCHO,ALTO))


    # DEFINIMOS LAS LISTAS
    lista_escenario_juego = []
    lista_jurados_vitrinas = []     #
    lista_usuario = []              # ESTAS LAS HICIMOS EN EL MENU PRINCIPAL, PERO LAS REPETIMOS PARA LA COHERENCIA
    lista_botones_operacion = []    # ADEMAS DE DECLARARLAS
    lista_rectangulo_votacion = []
    lista_preguntas = []

        
    # CONVERTIMOS LAS LISTAS EN ALGO QUE PYGAME PUEDA USAR
    lista_escenario_juego = retorno_imagenes("Parcial_pivigames/archivosCSV/lista_escenario_juego_1.csv")
    lista_jurados_vitrinas = retorno_imagenes("Parcial_pivigames/archivosCSV/jurados_vitrinas.csv")
    lista_usuario = retorno_imagenes("Parcial_pivigames/archivosCSV/usuario_votacion.csv")
    lista_botones_operacion = retorno_imagenes("Parcial_pivigames/archivosCSV_interactivos/juego_1/botones_usables.csv")

    # RETORNO DE IMAGENES Y LISTAS DE '.CSV'
    lista_botones_interactivos = leer_archivo_CSV("Parcial_pivigames/archivosCSV_interactivos/lista_botones_interactivos.csv")
    lista_rectangulo_votacion = leer_archivo_CSV("Parcial_pivigames/archivosCSV_interactivos/juego_1/colores_rectangulo.csv")
    lista_preguntas = leer_archivo_CSV("Parcial_pivigames/archivosCSV_interactivos/juego_1/preguntas_para_hacer.csv")
    lista_ultimate_juego = [
            lista_escenario_juego,
            lista_usuario,lista_jurados_vitrinas,
            lista_botones_operacion
        ]
    
    #RETORNO DE AECHIVOS DE '.JSON'
    lista_textos = leer_archivo_json("Parcial_pivigames/archivosCSV_interactivos/juego_1/textos_juego_1.json")
    puntuacion_monedas = leer_archivo_json("Parcial_pivigames/archivosCSV/Puntuacion_usuario.json")
    lista_porcentaje_votos =  [
        {"tamaño":[0,0,0,0],"distancia":50,"color":[0,0,0]},
        {"tamaño":[0,0,0,0],"distancia":50,"color":[0,0,0]},
        {"tamaño":[0,0,0,0],"distancia":50,"color":[0,0,0]},
        {"tamaño":[0,0,0,0],"distancia":50,"color":[0,0,0]},
        {"tamaño":[0,0,0,0],"distancia":50,"color":[0,0,0]},
        ]

    # DECLARAMOS VARIABLES
    BLANCO = (255,255,255)
    NEGRO = (0,0,0)
    ROJO = (255,0,0)
    AZUL = (0,0,255)
    tiempo_inicial = pygame.time.get_ticks()
    tiempo_transcurrido = None
    votos_totales = -1
    votos_rojos = -1
    votos_azules = 0
    ahre=0


    # DECLARAMOS LAS BANDERAS

    cerrar_juego = False
    bandera_game_start = True
    pregunta_en_curso = False
    pregunta_respondida = False
    boton_elegido = False
    comodin_reload = True
    comodin_half = True
    comodin_next = True
    tiempo_limite = False
    mostrar_votos = False
    ganador = None
    racha = None
    racha_emitida = None
    puntuacion_emitida = False
    
    lista_votos_emitidos = conseguir_votos_jurado(5)
    print(lista_votos_emitidos)

    while bandera_game_start:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera_game_start = False
                cerrar_juego = True

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                pos_x = evento.pos[0]
                pos_y = evento.pos[1]

                boton_pulsado = click_bool(pos_x,pos_y,lista_botones_operacion,lista_botones_interactivos)

                if boton_pulsado == "regresar":
                    bandera_game_start = False

                if boton_elegido == False:
                    
                    respuesta = respuesta_rectangulo(pos_x,pos_y,lista_rectangulo_votacion,lista_botones_interactivos)
                    
                    if comodin_reload:
                        if boton_pulsado == "boton_reload":
                            pregunta_en_curso = False
                            print("boton_usado_reload")
                            comodin_reload = False


                    if comodin_half:
                        if boton_pulsado == "boton_half":
                            print("boton_usado_half")
                            lista_rectangulo_votacion = cambiar_color_cuadrados(lista_rectangulo_votacion,lista_votos_emitidos,2)
                            comodin_half = False


                    if comodin_next:
                        if boton_pulsado == "boton_next":
                            print("boton_usado_next")
                            obtener_voto_ganador = conseguir_votos(lista_votos_emitidos)
                            if obtener_voto_ganador == "votantes_rojos":
                                decicion = 1
                            else:
                                decicion = 2
                            comodin_next = False
                            boton_elegido = True
                            mostrar_votos=True
                            pregunta_respondida = True
                            racha = True
                    

                    if respuesta == "boton_rojo_elegido":
                        print("elegi el rojo")
                        decicion = 1
                        pregunta_respondida = True
                        mostrar_votos = True
                        boton_elegido = True
                        
                    elif respuesta == "boton_azul_elegido":
                        print("elegi el azul")
                        decicion = 2
                        pregunta_respondida = True
                        mostrar_votos = True
                        boton_elegido = True


        if mostrar_votos:
            lista_rectangulo_votacion = cambiar_color_cuadrados(lista_rectangulo_votacion,lista_votos_emitidos,5)

        for juegos in lista_ultimate_juego:
            recorrer_listas_imagenes(juegos,PANTALLA)
            recorrer_textos(0,1,puntuacion_monedas,PANTALLA)
            

        for elementos in lista_rectangulo_votacion:
            pygame.draw.rect(PANTALLA,elementos['color'],elementos['coordenadas'])

        # ELEGIMOS LA PREGUNTA A HACER

        tiempo_transcurrido,tiempo_mostrado = conseguir_temporizados(tiempo_inicial)

        if tiempo_limite:
            lista_textos[4]['texto'] = "Tiempo limite:Fallaste"
            recorrer_textos(3,5,lista_textos,PANTALLA)

                
        else:
            

            if pregunta_en_curso:
                    
                    # SE DECIDE SI GANO
                    if pregunta_respondida:
                        votos_finales = conseguir_votos(lista_votos_emitidos)
                        if decicion == 1 :
                            
                            if votos_finales == "votantes_rojos":
                                lista_textos[4]['texto'] = "Gana rojo:Tu Ganaste, Obtuviste 10 monedas"
                                ganador = True
                                racha = True
                                recorrer_textos(3,5,lista_textos,PANTALLA)

                            else:
                                lista_textos[4]['texto'] = "Pierde rojo:Tu Perdiste"
                                ganador = False
                                racha = False
                                recorrer_textos(3,5,lista_textos,PANTALLA)
                                sound.play()

                        elif decicion == 2:

                            if votos_finales == "votantes_azules":
                                lista_textos[4]['texto'] = "Gana azul:Tu Ganaste, Obtuviste 10 monedas"
                                ganador = True
                                racha = True
                                recorrer_textos(3,5,lista_textos,PANTALLA)

                            else:
                                lista_textos[4]['texto'] = "Pierde azul:Tu Perdiste"
                                ganador = False
                                racha = False
                                recorrer_textos(3,5,lista_textos,PANTALLA)
                                sound.play()

                        print("*"*50)
                        for porcentaje in lista_porcentaje_votos:
                            lista_porcentaje_votos = cambiar_color_cuadrados(lista_porcentaje_votos,lista_votos_emitidos,5)
                            # print(porcentaje['color'],"\n")

                            
                            if porcentaje['color'][0] == 255:
                                if votos_rojos <= 5:
                                    votos_rojos+=1
                                valor_rojo = 465
                                votos_totales = votos_rojos
                                ahre+=1
                                posicion = valor_rojo
                                separacion = 50

                            elif porcentaje['color'][0] == 0:
                                if votos_azules <= 5:
                                    votos_azules+=1
                                valor_azul = 715
                                votos_totales = votos_azules
                                ahre+=1
                                posicion = valor_azul
                                separacion = -50

                            if ahre<=5:
                                porcentaje['tamaño'][0]=posicion+(separacion*votos_totales)
                                porcentaje['tamaño'][1]=350
                                porcentaje['tamaño'][2]=45
                                porcentaje['tamaño'][3]=45
                                
                            for porcentaje in lista_porcentaje_votos:
                                pygame.draw.rect(PANTALLA,porcentaje['color'],porcentaje['tamaño'])  

                        if ganador:
                            if puntuacion_emitida == False:
                                puntuacion_monedas[0]['texto']+=10
                                puntuacion_emitida = True
                        
                        if racha_emitida == None:
                            if racha:
                                puntuacion_monedas[1]['texto'] +=1
                            else:
                                puntuacion_monedas[1]['texto'] = 0
                            racha_emitida = True

                        
                    else:

                        lista_textos[1]['texto'] = respuesta_1
                        lista_textos[2]['texto'] = respuesta_2
                        recorrer_textos(0,3,lista_textos,PANTALLA)
                        if tiempo_mostrado <= 14:
                            lista_textos[5]['texto'] = f"{(tiempo_mostrado+1):.00f}"
                            # print(lista_textos[5]['texto'])
                            recorrer_textos(5,6,lista_textos,PANTALLA)
                        else:
                            tiempo_limite = True 


            else:
                respuesta_1,respuesta_2,lista_preguntas_ya_hechas = elegir_pregunta(lista_preguntas,lista_preguntas_ya_hechas)
                print(respuesta_1,respuesta_2)
                pregunta_en_curso = not pregunta_en_curso
        
        pygame.display.update()

    cargar_archivo_json("Parcial_pivigames/archivosCSV/Puntuacion_usuario.json",puntuacion_monedas)     
    if cerrar_juego:
        return cerrar_juego
    return puntuacion_monedas