import pygame
class Personagem:

    def __init__(self,figura,largura,altura,x_inicial,y_inicial): #,largura,altura
        self.imagem = pygame.image.load(figura)
        self.imagem = pygame.transform.scale(self.imagem,(largura,altura))#largura,altura
        self.mascara = pygame.mask.from_surface(self.imagem)

        self.x_inicial  = x_inicial
        self.y_inicial = y_inicial
        
        self.pos_x = x_inicial
        self.pos_y = y_inicial

        self.pontuacao = 0 


    def movimentar(self,tecla_direita,tecla_esquerda):
        teclas = pygame.key.get_pressed()
        if teclas[tecla_direita]:
            if self.pos_x < 650:
                self.pos_x +=0.5

        if teclas[tecla_esquerda]:
            if self.pos_x > 0:
                self.pos_x -=0.5
                
                
                #poder 
                #if teclas [tecla_espaco]: