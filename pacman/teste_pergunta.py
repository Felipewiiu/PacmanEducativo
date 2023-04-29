import pygame

# Definindo as cores que serão usadas no jogo
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Definindo a classe para representar as perguntas e respostas
class Pergunta:
    def __init__(self, pergunta, resposta):
        self.pergunta = pergunta
        self.resposta = resposta

    def desenha(self, surface):
        font = pygame.font.Font(None, 36)
        text = font.render(self.pergunta, True, BLACK)
        surface.blit(text, (50, 50))

    def verifica_resposta(self, resposta_usuario):
        return resposta_usuario.lower() == self.resposta.lower()


# Definindo a classe para representar a caixa de texto de entrada
class InputBox:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = ""

    def update(self):
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.color)
        width = max(200, text_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, BLACK)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))


# Inicializando o Pygame
pygame.init()

# Definindo o tamanho da janela e criando a janela
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Perguntas e Respostas")

# Criando a lista de perguntas e respostas
perguntas = [
    Pergunta("Qual é a capital do Brasil?", "Brasília"),
    Pergunta("Qual é o maior planeta do Sistema Solar?", "Júpiter"),
    Pergunta("Quem pintou a Mona Lisa?", "Leonardo da Vinci")
]

# Criando a caixa de texto de entrada
input_box = InputBox(50, 200, 700, 50)

# Iniciando a variável para contar os acertos do usuário
acertos = 0

# Iniciando o loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_box.text = input_box.text[:-1]
            else:
                input_box.text += event.unicode
            if event.key == pygame.K_RETURN:
                resposta = input_box.text
                input_box.text = ""
                pergunta_atual = perguntas.pop(0)
                if pergunta_atual.verifica_resposta(resposta):
                    acertos += 1

                if not perguntas:
                    rodando = False

    screen.fill(WHITE)

    if perguntas:
        pergunta_atual = perguntas[0]
        pergunta_atual.desenha(screen)

        input_box.update()
        input_box.draw(screen)

        pygame.display.flip()
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("Você")
