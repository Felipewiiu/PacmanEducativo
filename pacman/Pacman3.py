import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1100, 600), 0)



fonte = pygame.font.SysFont("arial", 28, True, False)
subtitulo = pygame.font.SysFont("arial", 20, True, False)

# pygame.mixer.music.load("actiontheme-v3.mp3")
# pygame.mixer.music.play(-1)


AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VELOCIDADE = 1

class Cenario:
    def __init__(self, tamanho, pac):#isso é um construtor
        self.tamanho = tamanho
        self.pacman = pac
        self.tempo_inicio = time.time()
        self.tempo = int(time.time() - self.tempo_inicio)
        self.segundo = 0
        self.minuto = 0
        self.pontos = 0
        self.questoes = ["Quanto é 7 x 7?", "Quanto é 6 x 3?", "Quanto é 3 x 9?", "Quanto é 45 + 7?", "Quanto é 30 - 27?", ""]
        self.gabarito = ["49","18","27","52","3"]
        self.resultado = ''
        self.texto_resposta = ''
        self.pontuacao = 0
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

        ]
     # Código desenvolvido por Felipe

    def relogio(self):
        self.tempo  += 1
        if self.tempo == int(20):
            self.tempo = 0
            self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
        if self.minuto == 1 and self.segundo == self.pontuacao:
            exit()




# Aqui onde são geradas as perguntas
    def questionario(self, tela, numero):
           posicao_x = 30 * self.tamanho

           pergunta = subtitulo.render(self.questoes[numero], True, AMARELO)
           resposta = subtitulo.render(self.texto_resposta, True, AMARELO)

           tela.blit(pergunta, (posicao_x, 150))
           tela.blit(resposta, (posicao_x, 250))


    # Aqui fica a função que passa o resultado para a tela
    def passa_resultado(self, tela, index):
        if self.texto_resposta == self.gabarito[index]:
            print("Resposta correta")
            self.resultado = "Resposta correta"
            self.texto_resposta = ''
            self.pontuacao += 5
            print(self.pontuacao)



        elif self.texto_resposta != self.gabarito[index] and self.texto_resposta != "":
            print("Resposta errada")
            self.resultado = "Resposta errada"
            self.texto_resposta = ''

        posicao_x = 30 * self.tamanho
        mostra_resultado = subtitulo.render(self.resultado, True, AMARELO)
        tela.blit(mostra_resultado, (posicao_x, 270))
        pygame.display.update()
        pygame.time.delay(1000)





    def pintar_pontos(self, tela):
        pontos_x = 28 * self.tamanho
        posicao_x = 30 * self.tamanho
        img_pontos = fonte.render(f"Tempo: 0{self.minuto}: {self.segundo}", True, AMARELO)
        chamada = subtitulo.render("Acerte e ganhe mas tempo!", True, AMARELO)
        tela.blit(chamada, (posicao_x, 100))
        tela.blit(img_pontos, (posicao_x, 50))

        input_box = pygame.Rect(100, 100, 140, 32)
        text = ''
        #Essa parte é a lógica das perguntas****************************************
        #
        if self.pontos > 10 and self.pontos < 60:
            self.questionario(tela,0)
            # self.passa_resultado(tela,0)

        if self.pontos > 60 and self.pontos < 90:
            self.questionario(tela, 1)
            # self.passa_resultado(tela, 1)

        if self.pontos > 90 and self.pontos < 120:
            self.questionario(tela, 2)
            # self.passa_resultado(tela, 2)

        if self.pontos > 120 and self.pontos < 160:
            self.questionario(tela, 3)
            # self.passa_resultado(tela, 3)

        if self.pontos > 160 and self.pontos < 200:
            self.questionario(tela, 4)
            # self.passa_resultado(tela, 4)

    def processar_eventos(self, eventos, tela):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    # Se a tecla de retrocesso for pressionada, remove o último caractere
                    self.texto_resposta = self.texto_resposta[:-1]
                elif e.unicode.isprintable():
                    # Se um caractere imprimível for pressionado, adiciona-o ao texto
                    self.texto_resposta += e.unicode
                if e.key == pygame.K_RETURN:

                    if self.pontos > 10 and self.pontos < 60:

                        self.passa_resultado(tela, 0)

                    if self.pontos > 60 and self.pontos < 90:

                        self.passa_resultado(tela, 1)

                    if self.pontos > 90 and self.pontos < 120:

                        self.passa_resultado(tela, 2)

                    if self.pontos > 120 and self.pontos < 160:


                        self.passa_resultado(tela, 3)

                    if self.pontos > 160 and self.pontos < 200:

                        self.passa_resultado(tela, 4)






    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            half = self.tamanho // 2
            cor = PRETO
            if coluna == 2:
                cor = AZUL
            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if coluna == 1:
                pygame.draw.circle(tela, AMARELO, (x + half, y + half), self.tamanho // 10, 0)

    def pintar (self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_pontos(tela)

    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao
        if 0 <= col <= 27 and 0 <= lin <= 29:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[lin][col] == 1:
                    self.pontos += 1
                    self.matriz[lin][col] = 0

class Pacman:
    def __init__(self, tamanho):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.raio = int(self.tamanho / 2)
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.velocidade_x
        self.linha_intencao = self.linha + self.velocidade_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)


    def pintar(self, tela):
        # Desenhar o corpo do pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenho da boca
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # desenho do olho
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

        # controle movimentação
    def processar_evento(self, eventos):
        for e in eventos:# isso lê uma fila de eventos
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = -VELOCIDADE
                elif e.key == pygame.K_UP:
                    self.velocidade_y = -VELOCIDADE
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = VELOCIDADE

            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_UP:
                    self.velocidade_y = 0
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0

    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

if __name__ == "__main__":
    size = 600 // 30
    Pacman = Pacman(size)# aqui se cria uma instância de pacman
    cenario = Cenario(size, Pacman)

    while True:
        # calcular as regras
        Pacman.calcular_regras()
        cenario.calcular_regras()
        cenario.relogio()

        # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        Pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(45)


        # Captura os eventos
        eventos = pygame.event.get()
        for e in eventos:# isso lê uma fila de eventos
            if e.type == pygame.QUIT:
                exit()


        Pacman.processar_evento(eventos)
        cenario.processar_eventos(eventos, screen)





