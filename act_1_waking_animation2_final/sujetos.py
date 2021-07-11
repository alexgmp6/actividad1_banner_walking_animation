import pygame

class sujeto(pygame.sprite.Sprite):
     
    def __init__(self, imagenes):        
        self.imagenes = imagenes        
        self.frame = 0   
        self.indicador = 30     
        self.rect = self.imagenes[self.frame].get_rect()
        self.rect.top = 300
        self.rect.left = 0        
    def move(self, vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self, superficie):
        superficie.blit(self.imagenes[self.frame],self.rect)   
    def nextFrame(self):  
        self.frame = self.indicador % len(self.imagenes) #controla los indices de las imagenes
        print(self.frame)
        self.indicador+=1   #sigue a la imagen siguiente
    def setNewSprites(self,imagenes):
        self.imagenes = imagenes    
        
class Player(sujeto):
    """Clase del heroe"""
    def __init__(self, imagenes):        
        sujeto.__init__(self,imagenes)        
   