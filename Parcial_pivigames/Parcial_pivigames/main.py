import pygame
import pygame.locals
from esto_aquello.juego_1 import game_start_juego_1

"""Definimos los colores RGB
    """
#COLORES
NEGRO = (0,0,0) 
ROJO = (255,0,0)
AZUL = (0,0,255)
AZUL_CLARO = (0,150,255)
VERDE = (0,255,0)
BLANCO = (255,255,255)

"""Definimos el tamaño de la pantalla
    """

#TAMAÑO DE PANTALLA/VENTANA
ANCHO = 1200
ALTO = 600

"""Inicializamos la pantalla y les pasamos como parametros el ANCHO Y EL ALTO
    """

#DEFINIMOS LA PANTALLA
PANTALLA = pygame.display.set_mode((ANCHO,ALTO))

#SACAMOS LAS IMAGENES QUE USAREMOS EN EL TRABAJO

"""Con el metodo image.load cargamos las imagenes con sus respectivos pads y con el transform para inicializarlas en la pantalla
    """
#BOTONES
boton_start = pygame.image.load("Parcial_pivigames/botones/start.png")
boton_start = pygame.transform.scale(boton_start, (450,500))

boton_configuracion = pygame.image.load("Parcial_pivigames/botones/configuracion.png") 
boton_configuracion = pygame.transform.scale(boton_configuracion, (50,50))

boton_modo_votacion = pygame.image.load("Parcial_pivigames/botones/boton_decicion.jpg")
boton_modo_votacion = pygame.transform.scale(boton_modo_votacion,(150,150))

boton_trivia = pygame.image.load("Parcial_pivigames/botones/imagen_trivia.png")
boton_trivia = pygame.transform.scale(boton_trivia, (150,150))

boton_skin = pygame.image.load("Parcial_pivigames/botones/skins.png")
boton_skin = pygame.transform.scale(boton_skin,(200,100))


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

usuario_skin = pygame.image.load("Parcial_pivigames/botones/usuario.png")
usuario_skin = pygame.transform.scale(usuario_skin,(150,95))

trofeos = pygame.image.load("Parcial_pivigames/botones/trofeos.png")
trofeos = pygame.transform.scale(trofeos,(50,50))

mesa_trofeos = pygame.image.load("Parcial_pivigames/botones/mesa_trofeos.png")
mesa_trofeos = pygame.transform.scale(mesa_trofeos,(200,100))

# MONEDAS

monedas = pygame.image.load("Parcial_pivigames/botones/monedas.png")
monedas = pygame.transform.scale(monedas,(100,100))



# fuente = pygame.font.SysFont("Arial",20)
# texto = fuente.render("Hola Gente",False,NEGRO,ROJO)

# DEFINIMOS COORDENADAS CON LAS QUE TRABAJAREMOS
x,y=400,200

"""Defimnimos con las cordenas que vamos a trabajar
    """

rectangulo_x= 450
rectangulo_y = 200

"""Inicializamos el pygame
    """
pygame.init()

"""Creamos una lista vacía para después agregar con el método append las preguntas que ya fueron realizadas
    """
lista_preguntas_hechas = []

"""Creamos una bandera
    """
transicion = True

"""Creamos una bandera para inicializar la pantalla y cuando quieran darle a la X de la ventana, se cierra automaticamente la ventana del juego. En la línea 124 hacemos un elif para poder detectar los botones que apreten que son convertidos a imagen donde le pasamos como parametros las coordenas del boton
    """
bandera = True
while bandera:

    #ESTABLECIENDO LA SALIDA DE LA PANTALLA
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos_x = evento.pos[0]
            pos_y = evento.pos[1]
            
            #CONVIRTIENDO IMAGENES EN BOTONES
            if pos_x >= x and pos_x <= (x+rectangulo_x) and pos_y >= y and pos_y <= (y+rectangulo_y):
                transicion = False
                    

        if transicion == False:
            
            #CONVIRTIENDO IMAGENES EN BOTONES 2.0
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_x = evento.pos[0]
                pos_y = evento.pos[1]

                if pos_x >= x-50 and pos_x <=(350+150) and pos_y >=y+150 and pos_y <= (350+150):
                    lista_preguntas_hechas = game_start_juego_1(lista_preguntas_hechas)
                elif pos_x >= x+350 and pos_x <=(750+150) and pos_y >=y+150 and pos_y <= (350+150):
                    print("holaaaa 2.0")
                elif pos_x >= x+600 and pos_x <=(1000+200) and pos_y >=y and pos_y <= (200+100):
                    print("holaaaa 3.0")
                elif pos_x >= x-390 and pos_x <=(10+50) and pos_y >=y-190 and pos_y <= (10+50):
                    print("holaaaa 4.0")



    """Con el metodo .blit pegamos las imagenes que le pasamos como primer parametro la imagen y segundo dentro de una tupla las coordenadas que queremos utilizarlas
    """
    #TRANSICION DE PANTALLA START/INICIO
    if transicion:

        #SACAR RECTANGULO
        rectangulo_boton = pygame.draw.rect(PANTALLA,ROJO,(x,y,rectangulo_x,rectangulo_y))
        PANTALLA.blit(sala_de_espera,(0,0))
        PANTALLA.blit(boton_start,(400,50))
    else:
        
        #POSICIONAMIENTOS DE LAS IMAGENES

        PANTALLA.blit(fondo_teatro,(0,0))
        PANTALLA.blit(gradas,(200,0))
        # rectangulo_votacion = pygame.draw.rect(PANTALLA,AZUL_CLARO,(350,350,150,150))

        #MESA_JURADO PRIMERA FILA
        PANTALLA.blit(jurados,(515,145))
        PANTALLA.blit(jurados,(500+espacio_jurados+15,145))

        PANTALLA.blit(mesa_votacion,(500,185))
        PANTALLA.blit(mesa_votacion,(500+espacio_jurados,185))
        
        #2FILA  MESA + JURADOS

        PANTALLA.blit(jurados,(465,235))
        PANTALLA.blit(jurados,(450+espacio_jurados+15,235))
        PANTALLA.blit(jurados,(450+espacio_jurados*2+15,235))

        PANTALLA.blit(mesa_votacion,(450,275))
        PANTALLA.blit(mesa_votacion,(450+espacio_jurados,275))
        PANTALLA.blit(mesa_votacion,(450+espacio_jurados*2,275))

        # PERSONAJE USUARIO

        PANTALLA.blit(usuario,(45,300))
        PANTALLA.blit(mesa_votacion_usuario,(75,420))

        # TROFEOS

        # PANTALLA.blit(mesa_trofeos,(950,420))
        # PANTALLA.blit(trofeos,(750,290))

        # ELEGIR MODO DE JUEGO + AJUSTES + SKIN
        PANTALLA.blit(boton_trivia,(750,350))
        PANTALLA.blit(boton_modo_votacion,(350,350))
        PANTALLA.blit(boton_configuracion,(10,10))
        PANTALLA.blit(boton_skin,(1000,200))

        PANTALLA.blit(usuario_skin,(967,186))

    """Actualizamos la ventana con el metodo update ya que le cargamos imagenes
    """
    pygame.display.update()

"""Cerramos el juego
    """
pygame.quit()