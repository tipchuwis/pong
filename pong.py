import pygame, sys
pygame.init

# Colores
BLACK =     (   0,    0,  0) # Estos son colores, los declaramos en mayúsculas para no confundirlos con otras variables.
WHITE =     ( 255,  255,  255)
GREEN =     (   0,  255,    0)
RED =       ( 255,    0,    0)
BLUE =      (   0,    0,  255)

# Definir alto y ancho de jugadores
player_h=100
player_w=15

# Pantalla
screen_size = (800,600) # Variable que me dice cuánto mide la pantalla que vamos a inicializar en pixeles.
screen = pygame.display.set_mode(screen_size) # Aquí decimos que pygame haga un display del modo de screen_size.
clock = pygame.time.Clock() # Este reloj es para que nunca se nos acabe la pantalla, que no se abra y cierre en 1 segundo.

# Coordenadas de los jugadores
player_1_x=50
player_1_y=300 - 50
player_1_speed_y=0

player_2_x=750 - player_w
player_2_y=300 - 50
player_2_speed_y=0

# Definir la velocidad de la pelota
pelota_x=400
pelota_y=300
pelota_speed_y=3
pelota_speed_x=3

# Game over
game_over = False

while not game_over: # Mientras que NO hayamos perdido:
    for event in pygame.event.get(): # Este FOR revisa absolutamente todos los eventos, si movemos el mouse encima,
    #                                   el evento va a registrarse y pasará por todas las condicionales.
        if event.type == pygame.QUIT:
            game_over = True
            sys.exit()

        # Movimiento de Jugadores
        if event.type == pygame.KEYDOWN:
             #P1 avanza
             if event.key == pygame.K_w:
                 player_1_speed_y=-3
             if event.key == pygame.K_s:
                 player_1_speed_y=+3

            #P2 avanza
             if event.key == pygame.K_UP:
                 player_2_speed_y=-3
    
             if event.key == pygame.K_DOWN:
                 player_2_speed_y=+3
        
        if event.type == pygame.KEYUP:
            # P1 para
             if event.key == pygame.K_w:
                player_1_speed_y=0
             if event.key == pygame.K_s:
                player_1_speed_y=0
            
            # P2 para
             if event.key == pygame.K_UP:
                player_2_speed_y=0
             if event.key == pygame.K_DOWN:
                player_2_speed_y=0
        
        # Límites de jugadores
        if player_1_y > 480:
            player_1_y = 480
        if player_1_y < 30:
            player_1_y = 30

        if player_2_y > 480:
            player_2_y = 480
        if player_2_y < 30:
            player_2_y = 30

        # La pelota rebota
        if pelota_y > 550 or pelota_y < 40:
            pelota_speed_y *=-1
        if pelota_x > 730 or pelota_x < 70:
            pelota_speed_x *=-1

        # La pelota reespawnea si se sale de los límites
        if pelota_y > 600 or pelota_y < 20:
            pelota_y=300
            pelota_x=400
            game_over = True
        if pelota_x > 800 or pelota_x < 50:
            pelota_y=300
            pelota_x=400
            game_over = True
        
    
        # La pelota reespawnee después de perder
       # if pelota_x > 480:
        #    pelota_x=400
        #    pelota_y=300
            # Invertir el lado de la pelota
         #   pelota_speed_x*=-1
         #   pelota_speed_y*=-1

       # if pelota_x < 0:
       #     pelota_x=400
        #    pelota_y=300
       #     # Invertir el lado de la pelota
        #    pelota_speed_x*=-1
       #     pelota_speed_y*=-1


    player_1_y+=player_1_speed_y
    player_2_y+=player_2_speed_y

    pelota_x+=pelota_speed_x
    pelota_y+=pelota_speed_y
    
    # Color de fondo
    screen.fill(BLACK)
    #-------------------Zona de dibujo
    player_1=pygame.draw.rect(screen, WHITE, (player_1_x,player_1_y,player_w,player_h))
    player_2=pygame.draw.rect(screen, WHITE, (player_2_x,player_2_y,player_w,player_h))
    pelota=pygame.draw.circle(screen, WHITE,(pelota_x,pelota_y),10)
    #-------------------Zona de dibujo

    # Colisión de la pelota
    if pelota.colliderect(player_1) or pelota.colliderect(player_2):
        pelota_speed_x *=-1

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

    pass