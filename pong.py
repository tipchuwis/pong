import pygame, sys
pygame.init

# Colores
BLACK =     (   0,    0,  0) # Estos son colores, los declaramos en mayúsculas para no confundirlos con otras variables.
WHITE =     ( 255,  255,  255)
GREEN =     (   0,  255,    0)
RED =       ( 255,    0,    0)
BLUE =      (   0,    0,  255)

# Pantalla
screen_size = (800,600) # Variable que me dice cuánto mide la pantalla que vamos a inicializar en pixeles.
screen = pygame.display.set_mode(screen_size) # Aquí decimos que pygame haga un display del modo de screen_size.
clock = pygame.time.Clock() # Este reloj es para que nunca se nos acabe la pantalla, que no se abra y cierre en 1 segundo.

# Coordenadas del cuadro

cord_x= 400
cord_y= 200

# Definir la velocidad
speed_x=3 # Es decir, que en x (y y), se va a mover cada vez 3 pixeles empezando en 400, luego 403, luego 406, y así sucesivamente.
speed_y=3

# Definir FPS


while True: # Este es para que sí pase algo :3
    for event in pygame.event.get(): # Este FOR imprime en la consola todos los eventos en la ventanita.
    #         print(event) Como realmente no hemos hecho mucho, sólo nos va a imprimir la posición del mouse.
        if event.type == pygame.QUIT:
            sys.exit()

    if (cord_x > 720 or cord_x < 0):
        speed_x*= -1
    if (cord_y > 520 or cord_y < 0):
        speed_y*= -1

    cord_x+=speed_x
    cord_y+=speed_y
    
    # Color de fondo
    screen.fill(BLACK)
    #-------------------Zona de dibujo
    pygame.draw.rect(screen, RED, (cord_x,cord_y,80,80)) # Llamamos a pygame, el método draw y luego rect para hacer
    '''for i in range (100,700,100):               un rectángulo. De ahí le indicamos coordenadas en x, y, base y altura.
        pygame.draw.rect(screen,WHITE,(i,230,50,50))
        pygame.draw.line(screen, GREEN, (i,0), (i,100),5)'''
    #-------------------Zona de dibujo
    '''screen.fill(WHITE) # Le estamos diciendo que ahora, nuestra variable de pantalla se llene de blanco.
    pygame.draw.line(screen, GREEN, [0,100], [200,300], 5)
    pygame.draw.rect(screen, RED, (100,100,80,80))
    pygame.draw.circle(screen, BLACK, (100,100), 10)'''

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

    pass