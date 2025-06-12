import pygame
from personagem import Personagem
from obstaculo import Obstaculo

#inicializar as configurações padrão
pygame.init()

cores = {"Azul":(67,103,248),
        "Ciano":(68,247,220),
        "Rosa":(252,148,234),
        "Roxo":(216,122,252),
        "Verde":(197,254,120)}

#criar  a tela
tela = pygame.display.set_mode((800,600))
tela.fill((cores["Ciano"])) #Cores

#Clock regular fps(frequência com que os quadros de imagem são exibidos)
clock = pygame.time.Clock()

#criar objetos

macaco = Personagem ("imagens/macaco.png", 200, 200, 150, 150)

fundo = pygame.image.load("imagens/selva-1.png")
fundo = pygame.transform.scale(fundo,(800,600))

lista_obstaculos = [Obstaculo("Imagens/fruta-que-gosta1.png", 100, 100),
                    Obstaculo ("Imagens/fruta-que-gosta2.png", 100, 100),
                    Obstaculo ("Imagens/fruta-que-gosta3.png", 100, 100),
                    Obstaculo ("Imagens/fruta-que-gosta4.png", 100, 100),
                    Obstaculo ("Imagens/fruta-que-gosta5.png", 100, 100),
                    Obstaculo ("Imagens/fruta-que-nao-gosta1.png", 100, 100),
                    Obstaculo ("Imagens/fruta-que-nao-gosta2.png", 100, 100),
                    Obstaculo ("Imagens/fruta-que-nao-gosta3.png", 100, 100)]

#loop infinito
estado = "JOGANDO"
fim_jogo = False
while not fim_jogo :

    #tratar de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True

    if estado == "JOGANDO":
        tela.blit(fundo,(0,0))


        for obstaculo in lista_obstaculos:
            obstaculo.movimentar()
            tela.blit(obstaculo.imagem,(obstaculo.pos_x,obstaculo.pos_y))
            if macaco.mascara.overlap(obstaculo.mascara,(obstaculo.pos_x-macaco.pos_x,obstaculo.pos_y-macaco.pos_y)):
                macaco.pos_x = macaco.x_inicial
                macaco.pos_y = macaco.y_inicial
                macaco.pontuacao +=1
                print(macaco.pontuacao)


                #Criando o placar
        #placar_macaco = fonte_placar.render(f"macaco: {macaco.pontuacao}",True,cores["Azul"])
        tela.blit(placar_macaco,(10,0))

        
        if macaco.pontuacao == 3:
            estado ="FIM_JOGO"

        tela.blit(macaco.imagem,(macaco.pos_x,macaco.pos_y))
        
        macaco.movimentar(pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a)
        
        tela.blit(macaco.imagem,(macaco.pos_x,macaco.pos_y))
        macaco.movimentar(pygame.K_RIGHT,pygame.K_LEFT)

    #atualizar página
    pygame.display.update()