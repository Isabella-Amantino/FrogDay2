import pygame

# Inicializa o Pygame
pygame.init()
LEVEL_HEIGHT = 1800
# Define as dimensões da tela
largura_tela = 600
altura_tela = 900
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Mover Imagem com Setas")
background_image = pygame.image.load(".\\img\\LevelBackgound.png").convert()
# Carrega a imagem
imagem = pygame.image.load(".\\img\\froggy.png").convert_alpha() # Substitua por seu caminho de imagem
retangulo_imagem = imagem.get_rect()  # Obtém o retângulo da imagem para controle da posição
waterLilyImage = pygame.image.load(".\\img\\waterLilly.png").convert_alpha()
waterLily = waterLilyImage.get_rect()
startPosition = (218, LEVEL_HEIGHT)
currentPosition = list(startPosition)
retangulo_imagem.center = currentPosition
# Variável para controlar se a imagem deve se mover
mover = False
def start_level_one():
    global mover, rodando
    tela.blit(background_image, (0, 0))
    water_lily_positions = [
        (218, LEVEL_HEIGHT - 203),
        (374, LEVEL_HEIGHT - 359),
        (218, LEVEL_HEIGHT - 359),
        (55, LEVEL_HEIGHT - 359),
        (55, LEVEL_HEIGHT - 515),
        (55, LEVEL_HEIGHT - 671),
        (224, LEVEL_HEIGHT - 671),
        (224, LEVEL_HEIGHT - 827),
        (224, LEVEL_HEIGHT - 983),
        (55, LEVEL_HEIGHT - 983),
        (55, LEVEL_HEIGHT - 1139),
        (55, LEVEL_HEIGHT - 1295),
        (374, LEVEL_HEIGHT - 983),
        (374, LEVEL_HEIGHT - 1139),
        (374, LEVEL_HEIGHT - 1295),
        (224, LEVEL_HEIGHT - 1295),
        (224, LEVEL_HEIGHT - 1451),
    ]
    for wlpos in water_lily_positions:
        tela.blit(waterLilyImage, wlpos)
    
    tela.blit(imagem, retangulo_imagem)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            pygame.quit()
         # Verifica as teclas pressionadas
        if evento.type == pygame.KEYDOWN:
            mover = True
            if evento.key == pygame.K_LEFT:
                retangulo_imagem.x -= 150
            elif evento.key == pygame.K_RIGHT:
                retangulo_imagem.x += 150
            elif evento.key == pygame.K_UP:
                retangulo_imagem.y -= 156
            elif evento.key == pygame.K_DOWN:
                retangulo_imagem.y += 156
                
    if mover:
        # Previne a imagem de sair da tela
        retangulo_imagem.clamp_ip(tela.get_rect())

        # Preenche a tela com uma cor
        tela.fill((255, 255, 255))  # Branco

        # Desenha a imagem na tela
        tela.blit(imagem, retangulo_imagem)

        # Atualiza a tela
        pygame.display.flip()

        # Reseta a flag 'mover' para o próximo clique
        mover = False    
    if retangulo_imagem.colliderect(waterLily):
        retangulo_imagem.center = waterLily.center
    pygame.display.flip()    
    pygame.display.update()

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
            
    start_level_one()
    # Move a imagem apenas se a flag 'mover' estiver ativa
    

# Finaliza o Pygame
pygame.quit()