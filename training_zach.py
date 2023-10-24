import pygame
import math

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
screen_width = 800
screen_height = 600

# Couleurs
WHITE = [(255, 255, 255](callto:(255, 255, 255))
RED = (255, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Atterrissage sur Mars")

# Position initiale du vaisseau
ship_x = screen_width // 2
ship_y = 50
ship_angle = 0  # Angle initial
ship_power = 0  # Puissance initiale

# Gravité
gravity = 0.1

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gestion des contrôles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship_power += 0.1  # Augmente la puissance de propulsion
    if keys[pygame.K_LEFT]:
        ship_angle += 1  # Tourne vers la gauche
    if keys[pygame.K_RIGHT]:
        ship_angle -= 1  # Tourne vers la droite

    # Mettre à jour la position du vaisseau
    ship_power -= gravity  # Applique la gravité
    ship_x += ship_power * math.sin(math.radians(ship_angle))
    ship_y += ship_power * -math.cos(math.radians(ship_angle))

    # Dessine la planète
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [(200, 500, 400, 20](callto:(200, 500, 400, 20)))  # Surface de la planète

    # Dessine le vaisseau
    pygame.draw.polygon(screen, WHITE, [(ship_x, ship_y), (ship_x - 10, ship_y + 20), (ship_x + 10, ship_y + 20)])

    # Mise à jour de l'affichage
    pygame.display.flip()

# Libération des ressources Pygame
pygame.quit()
