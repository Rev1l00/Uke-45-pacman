import pygame

BLACK = (0,0,0)

# Lager en powerup klasse 
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        # Save The image
        self.powerUp_image = pygame.image.load(filename).convert()
        self.powerUp_image.set_colorkey(BLACK)