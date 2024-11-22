import sys
import pygame as py
# Pygame setup
py.init()
py.display.set_caption("FrogDay")
# Frame settings
FrameHeight = 900
FrameWidth = 600
screen = py.display.set_mode((FrameWidth, FrameHeight))

background_image = py.image.load(".\\img\\LevelBackgound.png").convert()
LEVEL_HEIGHT = background_image.get_height() # Altura total do nível a partir da imagem
LEVEL_WIDTH = background_image.get_width()  # Largura do nível, igual à largura do FrameWidth
scroll_y = 0  # Posição inicial da câmera no eixo Y

# Classe Button
class Button:
    def __init__(self, image, position, action=None):
        """
        Inicializa um botão.
        :param image: Superfície do botão (imagem)
        :param position: Posição (x, y) para posicionar o botão
        :param action: Função para executar ao clicar no botão
        """
        self.image = image
        self.rect = image.get_rect(topleft=position)
        self.action = action

    def draw(self, screen):
        """Renderiza o botão na tela."""
        screen.blit(self.image, self.rect.topleft)

    def check_click(self, mouse_pos):
        """
        Verifica se o botão foi clicado.
        :param mouse_pos: Posição do mouse no momento do clique
        :return: True se o botão foi clicado; False caso contrário
        """
        return self.rect.collidepoint(mouse_pos)

    def execute_action(self):
        """Executa a ação associada ao botão, se houver."""
        if self.action:
            self.action()

# Carregar imagens
paginaInicial = py.image.load(".\\img\\StartPage.png").convert()
btnJogar_image = py.image.load(".\\img\\jogarBtn.png").convert_alpha()
btnComoJogar_image = py.image.load(".\\img\\comoJogarBtn.png").convert_alpha()
btnSair_image = py.image.load(".\\img\\sairBtn.png").convert_alpha()



paginaNiveis = py.image.load(".\\img\\levelSelectionBackground.png").convert() 
btnLvl1_image = py.image.load(".\\img\\levelOneButton.png").convert_alpha()
btnLvl2_image = py.image.load(".\\img\\levelTwoButton.png").convert_alpha()
btnLvl3_image = py.image.load(".\\img\\levelThreeButton.png").convert_alpha()

waterLily = py.image.load(".\\img\\waterLilly.png").convert_alpha()
froggyImage = py.image.load(".\\img\\froggy.png").convert_alpha()
froggy = froggyImage.get_rect()

def start_game():
    """Muda para a tela de seleção de níveis."""
    global game_state
    game_state = "level_select"

def show_how_to_play():
    print("Mostrando instruções!")
    # Adicione aqui a lógica para exibir as instruções do jogo

def quit_game():
    print("Saindo do jogo...")
    py.quit()
    sys.exit()

def play_level_one():
    global game_state
    game_state = "level_one"

def play_level_two():
    global game_state
    game_state = "level_two"
    
def play_level_three():
    global game_state
    game_state = "level_three"

# Criar botões
buttons = [
    Button(btnJogar_image, (221, 460), start_game),
    Button(btnComoJogar_image, (221, 548), show_how_to_play),
    Button(btnSair_image, (221, 607), quit_game),
]


# Botões da seleção de níveis
level_buttons = [
    Button(py.transform.smoothscale(btnLvl1_image, (221, 221)), (190, 125), play_level_one),
    Button(py.transform.smoothscale(btnLvl2_image, (221, 221)), (190, 346), play_level_two),
    Button(py.transform.smoothscale(btnLvl3_image, (221, 221)), (190, 594), play_level_three),
]


def show_initial_page():
    """Renderiza a página inicial e os botões."""
    screen.blit(paginaInicial, (0, 0))
    for button in buttons:
        button.draw(screen)

def show_level_select_page():
    """Renderiza a tela de seleção de níveis."""
    screen.blit(paginaNiveis, (0, 0))
    for button in level_buttons:
        button.draw(screen)

froggy_start_pos = (FrameWidth // 2 - froggyImage.get_width() // 2, LEVEL_HEIGHT)
froggy_pos = list(froggy_start_pos)
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
def move_froggy(keys):
    global froggy_pos
    step = 156  # Distância padrão do pulo

    # Detectar direção do movimento
    if keys[py.K_UP]:
        froggy_pos[1] -= step
    elif keys[py.K_DOWN]:
        froggy_pos[1] += step
    elif keys[py.K_LEFT]:
        froggy_pos[0] -= step
    elif keys[py.K_RIGHT]:
        froggy_pos[0] += step

    # Limitar o movimento do sapo dentro do nível
    froggy_pos[0] = max(0, min(froggy_pos[0], FrameWidth - froggyImage.get_width()))
    froggy_pos[1] = max(0, min(froggy_pos[1], LEVEL_HEIGHT - froggyImage.get_height()))

# Inicialização de variáveis globais necessárias
lives = 3  # Número inicial de vidas do jogador
froggy_pos = [FrameWidth // 2, LEVEL_HEIGHT - 100]  # Posição inicial do sapo
froggy_start_pos = froggy_pos.copy()

# Função corrigida
def start_level_one():
    global froggy_pos, scroll_y, lives, game_state

    # Limitar o movimento da câmera para manter o sapo visível
    scroll_y = max(0, min(scroll_y, LEVEL_HEIGHT - FrameHeight))

    # Desenhar o fundo (ajustado com a rolagem)
    screen.blit(background_image, (0, -scroll_y))

    # Desenhar as vitórias-régias
    for pos in water_lily_positions:
        screen.blit(waterLily, (pos[0], pos[1] - scroll_y))

    # Desenhar o sapo
    screen.blit(froggyImage, (froggy_pos[0], froggy_pos[1] - scroll_y))

    # Desenhar as vidas
    font = py.font.SysFont(None, 36)
    lives_text = font.render(f"Vidas: {lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))

    # Lógica adicional para verificar colisões e condições de vitória
    # (Essa parte foi comentada no trecho original)

    
    # Verificar se o sapo caiu na água
    #if not check_collision(froggy_pos, water_lily_positions, scroll_y):
    #    lives -= 1
    #    froggy_pos = list(froggy_start_pos)  # Reiniciar posição
    #    scroll_y = 0  # Reiniciar câmera
    #    if lives <= 0:
    #        print("Game Over!")
    #        game_state = "menu"  # Retornar ao menu inicial

    # Verificar se o sapo alcançou o topo do nível (objetivo)
    #if froggy_pos[1] <= 156:
    #    print("Você venceu o nível 1!")
    #    game_state = "menu"  # Retornar ao menu ou carregar próximo nível

    

# Estado inicial do jogo
game_state = "menu"

# Main loop
running = True
while running:
    keys = py.key.get_pressed()  # Captura as teclas pressionadas
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
            sys.exit()
        elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_pos = event.pos
            if game_state == "menu":
                for button in buttons:
                    if button.check_click(mouse_pos):
                        button.execute_action()
            elif game_state == "level_select":
                for button in level_buttons:
                    if button.check_click(mouse_pos):
                        button.execute_action()
        if event.type == py.KEYDOWN:
            mover = True
            if event.key == py.K_LEFT:
                froggy.x -= 10
            elif event.key == py.K_RIGHT:
                froggy.x += 10
            elif event.key == py.K_UP:
                froggy.y -= 10
            elif event.key == py.K_DOWN:
                froggy.y += 10

        
        
        
        
        
    if game_state == "level_one" and keys:
        move_froggy(keys)
    # Renderização baseada no estado do jogo
    if game_state == "menu":
        show_initial_page()
    elif game_state == "level_select":
        show_level_select_page()
    elif game_state == "level_one":
        start_level_one()
    

    py.display.update()

py.quit()

