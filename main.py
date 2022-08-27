import pygame
import math

SOURCE_SIZE = 32

def main():

    pygame.init()

    sourceImage = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(sourceImage)
    pygame.display.set_caption("Wave Function Collapse")
     
    screen = pygame.display.set_mode((800,800))
     
    running = True
    
    logoStr = pygame.image.tostring(sourceImage, "RGB")
    tileSize = int(SOURCE_SIZE / 2)

    newTile = []
    lineSizeInBytes = tileSize * 3
    for y in range (0, tileSize):
        vertOffset = y * SOURCE_SIZE * 3
        xRange = vertOffset + lineSizeInBytes
        print(vertOffset, xRange)
        newTileLine = logoStr[slice(vertOffset, xRange, 1)]
        newTile += newTileLine

    newTile = bytes(newTile)

    tile = pygame.image.frombuffer(newTile, (tileSize, tileSize), "RGB")

    print (len(logoStr))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(sourceImage, (100,100))
        screen.blit(tile, (150,100))

        pygame.display.flip()
    
     
if __name__=="__main__":
    main()