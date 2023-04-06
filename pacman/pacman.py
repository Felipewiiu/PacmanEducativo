import pygame
AMARELO = (255, 255, 0)
PRETO = (0,0,0)
VELOCIDADE = 0.2
RAIO = 30

pygame.init()

tela = pygame.display.set_mode((640, 480), 0 )
x = 10
y = 10
velo_x = VELOCIDADE
velo_y = VELOCIDADE
while True:
    # calcula as regras
    x = x +  velo_x
    y = y + velo_y
    if x + RAIO> 640:
        velo_x = -VELOCIDADE
    if x - RAIO< 0:
        velo_x = VELOCIDADE
    if y + RAIO> 480:
        velo_y = -VELOCIDADE
    if y - RAIO< 0:
        velo_y = VELOCIDADE
    # Pinta
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0)
    pygame.display.update()
    # Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()