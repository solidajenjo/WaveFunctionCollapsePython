import pygame

def main():

    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Wave Function Collapse")
     
    screen = pygame.display.set_mode((800,800))
     
    running = True
     
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(logo, (100, 100))

        pygame.display.flip()
    
    print (pygame.image.tostring(logo, "RGB"))
     
     
if __name__=="__main__":
    main()