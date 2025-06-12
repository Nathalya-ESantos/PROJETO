import pygame
import random

class Obstaculo:
    def __init__(self, end_imagem, largura, altura):
        self.largura = largura
        self.altura = altura

#Carregando e alterando o tamanho da imagem
        self.imagem = pygame.image.load(end_imagem)
        self.imagem = pygame.transform.scale(self.imagem,(self.largura, self.altura)) #largura e altura
        self.mascara = pygame.mask.from_surface(self.imagem)

        self.lista_faixas = [100,200,300,400,500]
        self.y_inicial = 0
        self.pos_y = self.y_inicial
        self.pos_x = random.choice(self.lista_faixas)



        #Controlando a velocidade do obstáculo
        self.velocidade = random.randint(1,20)

    def movimentar(self):
        self.pos_y += self.velocidade
        if self.pos_y > 600:
            self.pos_y = self.y_inicial
            self.velocidade = random.randint(1,20)
            self.pos_x = random.choice(self.lista_faixas)