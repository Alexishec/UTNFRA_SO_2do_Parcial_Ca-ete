import pygame
import pygame.locals
import random

def game_start_juego_1(lista_preguntas_ya_hechas:list)->list|None:

    #COLORES
    NEGRO = (0,0,0)
    ROJO = [255,0,0]
    AZUL = (0,0,255)
    BLANCO = (255,255,255)

    lista_rectangulos = [[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255]]

    #TAMAÑO DE PANTALLA/VENTANA
    ANCHO = 1200
    ALTO = 600

    #DEFINIMOS LA PANTALLA
    PANTALLA = pygame.display.set_mode((ANCHO,ALTO))

    #SACAMOS LAS IMAGENES QUE USAREMOS EN EL TRABAJO

    #BOTONES
    boton_start = pygame.image.load("Parcial_pivigames/botones/start.png")
    boton_start = pygame.transform.scale(boton_start, (450,500))

    boton_volver_atras = pygame.image.load("Parcial_pivigames/botones/volver_atras.png") 
    boton_volver_atras = pygame.transform.scale(boton_volver_atras, (50,50))

    boton_rojo = pygame.image.load("Parcial_pivigames/botones/botones_rojo.png")
    boton_rojo = pygame.transform.scale(boton_rojo,(150,150))

    boton_azul = pygame.image.load("Parcial_pivigames/botones/botones_azul.png")
    boton_azul = pygame.transform.scale(boton_azul, (150,150))



    #PALCO DE VOTACION + USUARIO
    fondo_teatro = pygame.image.load("Parcial_pivigames/botones/Fondo_pantalla.png")
    fondo_teatro = pygame.transform.scale(fondo_teatro,(ANCHO,ALTO))

    sala_de_espera = pygame.image.load("Parcial_pivigames/botones/sala_de_espera.png")
    sala_de_espera = pygame.transform.scale(sala_de_espera,(ANCHO,ALTO))

    gradas = pygame.image.load("Parcial_pivigames/botones/escaleras_sin_fondo.png")
    gradas = pygame.transform.scale(gradas,(800,600))

    mesa_votacion = pygame.image.load("Parcial_pivigames/botones/mesa_votacion.png")
    mesa_votacion = pygame.transform.scale(mesa_votacion,(80,50))

    mesa_votacion_usuario = pygame.image.load("Parcial_pivigames/botones/mesa_votacion.png")
    mesa_votacion_usuario = pygame.transform.scale(mesa_votacion_usuario,(160,100))

    jurados = pygame.image.load("Parcial_pivigames/botones/jurado.png")
    jurados = pygame.transform.scale(jurados,(50,50))

    espacio_jurados = 120

    usuario = pygame.image.load("Parcial_pivigames/botones/usuario.png")
    usuario = pygame.transform.scale(usuario,(250,155))

    trofeos = pygame.image.load("Parcial_pivigames/botones/trofeos.png")
    trofeos = pygame.transform.scale(trofeos,(50,50))

    mesa_trofeos = pygame.image.load("Parcial_pivigames/botones/mesa_trofeos.png")
    mesa_trofeos = pygame.transform.scale(mesa_trofeos,(200,100))

    # MONEDAS

    monedas = pygame.image.load("Parcial_pivigames/botones/monedas.png")
    monedas = pygame.transform.scale(monedas,(100,100))


    # COMODINES

    comodin_reload = pygame.image.load("Parcial_pivigames/botones/comodin_reloaded.png")
    comodin_reload = pygame.transform.scale(comodin_reload,(45,45))
   
    comodin_half = pygame.image.load("Parcial_pivigames/botones/comodin_half.png")
    comodin_half = pygame.transform.scale(comodin_half,(45,45))
 
    comodin_next = pygame.image.load("Parcial_pivigames/botones/comodin_next.png")
    comodin_next = pygame.transform.scale(comodin_next,(45,45))

    #PREGUNTAS

    fuente = pygame.font.SysFont("Arial",20)

    lista_preguntas = ["café,té",
                    "Perros,gatos",
                    "Ciudad,campo",
                    "Playa,montaña",
                    "Libros,películas",
                    "Cocinar en casa,comer en un restaurante",
                    "Música clásica,el rock", 
                    "Volar,invisible", 
                    "Invierno,verano", 
                    "leer un libro emocionante,película fascinante",
                    "viajar al pasadoviajar al futuro"]


    texto = fuente.render("¿Prefieres cocinar en casa o salir a comer en un restaurante?",False,BLANCO,NEGRO)
    #GESTION DE PREGUNTAS POR TIEMPO

    """Inicializamos el metodo time.clock para saber el tiempo inicial desde donde arranca y al finalizar 
    """  
    clock = pygame.time.Clock()
    tiempo_inicial = pygame.time.get_ticks()

    # DEFINIMOS COORDENADAS CON LAS QUE TRABAJAREMOS
    x,y=400,200


    rectangulo_x= 450
    rectangulo_y = 200

    pygame.init()

    def jurado_elecicon()->list:
        lista = []
        for i in range(cant_jurados):
            voto = random.randint(1,2)
            if voto == 1:
                votos = 1
            else:
                votos = 2

            lista.append(votos)

        return lista

    contador_jurados_votos=0

    lista_posiciones = []
    transicion = False
    eleccion_hecha = False
    bandera_pregunta_en_curso = True
    tiempo_de_votacion = True
    bandera_next = True
    bandera_reload=True
    bandera_half=False
    uso_comodin_reloaded=True
    uso_comodin_half = True
    uso_comodin_next = True

    recurecu = pygame.draw.rect(PANTALLA,ROJO,(585,340,50,50))

    bandera = True
    while bandera:

        #ESTABLECIENDO LA SALIDA DE LA PANTALLA
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera = False
                pygame.quit()
            elif transicion == False:
                
                #CONVIRTIENDO IMAGENES EN BOTONES 2.0
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    pos_x = evento.pos[0]
                    pos_y = evento.pos[1]

                    if eleccion_hecha == False:

                        if pos_x >= x+20 and pos_x <=(x+190) and pos_y >=y+340 and pos_y <= (y+340+30):
                            print("boton rojo")
                            decicion = 1
                            tiempo_de_votacion=False
                            lista_votos_jurados = jurado_elecicon()
                            eleccion_hecha = True

                        elif pos_x >= x+220 and pos_x <=(x+400) and pos_y >=y+340 and pos_y <= (y+340+30):
                            print("boton azul")
                            decicion = 2
                            tiempo_de_votacion=False
                            lista_votos_jurados = jurado_elecicon()
                            eleccion_hecha = True


                        if uso_comodin_reloaded:
                            if pos_x >= 700 and pos_x <=(700+45) and pos_y >=450 and pos_y <= (450+45):
                                print("Gol")
                                bandera_pregunta_en_curso=True
                                bandera_reload=False
                                uso_comodin_reloaded=False
                        if uso_comodin_half:
                            if pos_x >= 755 and pos_x <=(755+45) and pos_y >=450 and pos_y <= (450+45):
                                print("Gol2")
                                lista_votos_jurados = jurado_elecicon()
                                bandera_half=True
                                uso_comodin_half = False
                        if uso_comodin_next:
                            if pos_x >= 805 and pos_x <=(805+45) and pos_y >=450 and pos_y <= (450+45):
                                print("Gol3")
                                decicion = 3
                                lista_votos_jurados = jurado_elecicon()
                                tiempo_de_votacion=False
                                eleccion_hecha = True
                                uso_comodin_next = False
                            
                            


                    if pos_x >= x-390 and pos_x <=(10+50) and pos_y >=y-190 and pos_y <= (10+50):
                        bandera = False
                        print("Volver al lugar anterior")
            


        # PANTALLA.fill(BLANCO)

        #TRANSICION DE PANTALLA START/INICIO
        
        #POSICIONAMIENTOS DE LAS IMAGENES

        PANTALLA.blit(fondo_teatro,(0,0))
        PANTALLA.blit(gradas,(200,0))
        # rectangulo_votacion = pygame.draw.rect(PANTALLA,AZUL_CLARO,(350,350,150,150))

        #MESA_JURADO PRIMERA FILA
        PANTALLA.blit(jurados,(515,145))
        PANTALLA.blit(jurados,(500+espacio_jurados+15,145))

        PANTALLA.blit(mesa_votacion,(500,185))
        PANTALLA.blit(mesa_votacion,(500+espacio_jurados,185))

        pygame.draw.rect(PANTALLA,lista_rectangulos[0],(500+30,200,20,20))
        pygame.draw.rect(PANTALLA,lista_rectangulos[1],(500+espacio_jurados+30,200,20,20))
        
        
        #2FILA  MESA + JURADOS

        PANTALLA.blit(jurados,(465,235))
        PANTALLA.blit(jurados,(450+espacio_jurados+15,235))
        PANTALLA.blit(jurados,(450+espacio_jurados*2+15,235))

        PANTALLA.blit(mesa_votacion,(450,275))
        PANTALLA.blit(mesa_votacion,(450+espacio_jurados,275))
        PANTALLA.blit(mesa_votacion,(450+espacio_jurados*2,275))

        pygame.draw.rect(PANTALLA,lista_rectangulos[2],(450+30,290,20,20))
        pygame.draw.rect(PANTALLA,lista_rectangulos[3],(450+espacio_jurados+30,290,20,20))
        pygame.draw.rect(PANTALLA,lista_rectangulos[4],(450+espacio_jurados*2+30,290,20,20))

        # PERSONAJE USUARIO

        PANTALLA.blit(usuario,(45,300))
        PANTALLA.blit(mesa_votacion_usuario,(75,420))

        # TROFEOS

        # PANTALLA.blit(mesa_trofeos,(950,420))
        # PANTALLA.blit(trofeos,(750,290))

        # botones de eleccion + volver atras
        # PANTALLA.blit(boton_azul,(750,350))
        # PANTALLA.blit(boton_rojo,(350,350))
        PANTALLA.blit(boton_volver_atras,(10,10))


        # PREGUNTAS

        votos_rojos = 0
        votos_azules=0
        cant_jurados = 5


        
        if bandera_pregunta_en_curso:
            numero_pregunta = random.randint(0,10)
            for preguntas in lista_preguntas:

                if preguntas in lista_preguntas_ya_hechas:
                    numero_pregunta = random.randint(0,10)
                else:
                    break


        if lista_preguntas[numero_pregunta] not in lista_preguntas_ya_hechas:
            lista_preguntas_ya_hechas.append(lista_preguntas[numero_pregunta])
            print("-.-"*50)
            bandera_while=False

            bandera_pregunta_en_curso = False




        # TEMPORIZADOR 
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        # print(f"{(tiempo_transcurrido*0.001):.00f}")
        tiempo_mostrado = tiempo_transcurrido*0.001

        if tiempo_de_votacion:

            if tiempo_transcurrido*0.001 >= 14:
                texto = fuente.render("HAS FALLADO",False,BLANCO,NEGRO)
                eleccion_hecha=True
                if tiempo_actual%10==0 and contador_jurados_votos<5:
                        lista_rectangulos[contador_jurados_votos] =[0,0,0]
                        contador_jurados_votos+=1
            
            else:
                texto = fuente.render("¿Que Prefieres?",False,BLANCO,NEGRO)
                contador_tiempo = fuente.render(f"{(tiempo_mostrado):.00f}",False,BLANCO,None)  
                PANTALLA.blit(contador_tiempo,(ANCHO//2,475))


        # ESULTADO DEL JUEGO + CAMBIO DE COLOR DE VOTOS

        else:
            if tiempo_actual%10==0 and contador_jurados_votos<5:
                if lista_votos_jurados[contador_jurados_votos] == 1:
                    lista_rectangulos[contador_jurados_votos] =[255,0,0]
                else:
                    lista_rectangulos[contador_jurados_votos] = [0,0,255]        
                contador_jurados_votos+=1
                time_time = tiempo_actual*1.5


            if contador_jurados_votos == 5 :
                for i in range(len(lista_votos_jurados)):
                    if lista_votos_jurados[i]==1:
                        lista_posiciones.append((465+(50*votos_rojos),350,45,45))
                        votos_rojos +=1
                        # print("ojo")

                    elif lista_votos_jurados[i]==2:
                        lista_posiciones.append((715-(50*votos_azules),350,45,45))
                        votos_azules+=1
                        # print("azul")
                        
                
                for i in range(len(lista_votos_jurados)):
                    if lista_votos_jurados[i] == 1:
                        pygame.draw.rect(PANTALLA,ROJO,lista_posiciones[i])  
                    else:
                        pygame.draw.rect(PANTALLA,AZUL,lista_posiciones[i])  

        
        if bandera_half: 
            if tiempo_actual%10==0 and contador_jurados_votos<2:
                if lista_votos_jurados[contador_jurados_votos] == 1:
                    lista_rectangulos[contador_jurados_votos] =[255,0,0]
                else:
                    lista_rectangulos[contador_jurados_votos] = [0,0,255]        
                contador_jurados_votos+=1
                time_time = tiempo_actual*1.5

            if contador_jurados_votos == 1 :
                for i in range(len(lista_votos_jurados)-3):
                    if lista_votos_jurados[i]==1:
                        lista_posiciones.append((465+(50*votos_rojos),350,45,45))
                        votos_rojos +=1
                        
                        # 465
                        # print("ojo")
                    elif lista_votos_jurados[i]==1:
                        lista_posiciones.append((715-(50*votos_azules),350,45,45))
                        votos_azules+=1
                        # print("azul")
                        # 715
   

                        
        if contador_jurados_votos == 5 :
                    
            if votos_rojos>=3:
                ganador = "Gana el Rojo"
                if decicion == 1 or decicion == 3:
                    usuario_gano = "Has ganado"
                else:
                    usuario_gano = "Has perdido"

            elif votos_azules>=3:
                ganador = "Gana el Azul"
                if decicion == 2 or decicion == 3:
                    usuario_gano = "Has ganado"
                else:
                    usuario_gano = "Has perdido"

        
            texto = fuente.render(f"{ganador}",False,BLANCO,NEGRO)
            texto_usuario_decicion = fuente.render(f"{usuario_gano}",False,BLANCO,NEGRO)
            PANTALLA.blit(texto_usuario_decicion,(555,525))
                    

            # print(f"time: {tiempo_actual}")

        PANTALLA.blit(texto,(550,500))


        if contador_jurados_votos != 5:


            if bandera_reload:
                texto_comodin_reloaded = fuente.render("Reload",False,NEGRO,BLANCO) 
                PANTALLA.blit(texto_comodin_reloaded,(705,420))
                PANTALLA.blit(comodin_reload,(700,450))

            if bandera_half == False: 
                texto_comodin_half = fuente.render("Half",False,NEGRO,BLANCO) 
                PANTALLA.blit(texto_comodin_half,(755,420))
                PANTALLA.blit(comodin_half,(755,450))

            if bandera_next:
                texto_comodin_next = fuente.render("Next",False,NEGRO,BLANCO) 
                PANTALLA.blit(texto_comodin_next,(755,420))
                PANTALLA.blit(comodin_next,(805,450))

                
            respuesta = lista_preguntas[numero_pregunta].split(",")

            base_1 = 420
            base_2 = 620


            pygame.draw.rect(PANTALLA,ROJO,(420,545,170,30))
            pygame.draw.rect(PANTALLA,AZUL,(620,545,180,30))

            opcion_uno = respuesta[0]
            opcion_dos = respuesta[1]


            
            

            respuesta1 = fuente.render(f"{opcion_uno}",False,BLANCO,ROJO)
            respuesta2 = fuente.render(f"{opcion_dos}",False,BLANCO,AZUL)
            
            PANTALLA.blit(respuesta1,(420,540))
            PANTALLA.blit(respuesta2,(620,540))
        pygame.display.update()
    
    # print(lista_preguntas_ya_hechas)
    # return lista_preguntas_ya_hechas


