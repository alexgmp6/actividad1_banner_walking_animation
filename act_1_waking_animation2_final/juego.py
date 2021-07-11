import pygame
import sujetos
import os

# Constantes
__ANCHO = 640
__ALTO = 480

# Inicializaciones y variables globales
pygame.init()
screen = pygame.display.set_mode((__ANCHO,__ALTO))
pygame.display.set_caption("walking animation")
reloj = pygame.time.Clock()

# Carga las imagenes
imagen=pygame.image.load("Res/walking.png").convert_alpha()   

imagenesPlayerDer=[
imagen.subsurface((64,0),(64,128)),
imagen.subsurface((128,0),(64,128)),
imagen.subsurface((192,0),(64,128)),
imagen.subsurface((256,0),(64,128)),
imagen.subsurface((320,0),(64,128)),
imagen.subsurface((384,0),(64,128)),
imagen.subsurface((448,0),(64,128)),
imagen.subsurface((512,0),(64,128)),
imagen.subsurface((576,0),(64,128))] 
  
imagenesPlayerIzq=[
imagen.subsurface((64,128),(64,128)),
imagen.subsurface((128,128),(64,128)),imagen.subsurface((192,128),(64,128)),
imagen.subsurface((256,128),(64,128)),imagen.subsurface((320,128),(64,128)),
imagen.subsurface((384,128),(64,128)),imagen.subsurface((448,128),(64,128)),
imagen.subsurface((512,128),(64,128)),imagen.subsurface((576,128),(64,128))] 

                     
# Pinta las imagenes en la pantalla                     
def paint(player):
    screen.fill((0,0,0))
    player.update(screen)
    pygame.display.update()
    player.nextFrame()

def main():   
        
    spritesRight = True
                            
    player = sujetos.Player(imagenesPlayerDer)    
    exit = False   
    vx = 15
    
    while exit != True:     # Bucle principal
        paint(player)        
        player.move(vx,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                
                exit = True                
        # control de los limites   
        if player.rect.right >= __ANCHO or player.rect.left <= 0:
            vx=-vx
            if spritesRight == True:  #si mira hacia la derecha
                player.setNewSprites(imagenesPlayerIzq)
                spritesRight = False
            else: #si mira hacia la izquierda
                player.setNewSprites(imagenesPlayerDer)
                spritesRight = True     
        reloj.tick(12)
       
 

# INICIO
if __name__ == '__main__':
    main()
