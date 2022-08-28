import pygame
import math

SOURCE_SIZE = 256

def slice_tiles(tileSize, divisions, logoStr):
    tilesArray = []
    lineSizeInBytes = tileSize * 3
    for i in range (divisions): #vert
        for j in range (divisions): #horizontal            
            
            newTile = []            
            newTileHorizontalFlipped = []

            for y in range (tileSize * i, tileSize * i + tileSize):
                vertOffset = y * SOURCE_SIZE * 3 + tileSize * j * 3
                xRange = vertOffset + lineSizeInBytes
                newTileLine = logoStr[slice(vertOffset, xRange, 1)]
                newTile += newTileLine
                newTileHorizontalFlipped += newTileLine[::-1]

            tilesArray += [newTile]
            tilesArray += [newTile[::-1]] #flip vertical
            tilesArray += [newTileHorizontalFlipped]
            tilesArray += [newTileHorizontalFlipped[::-1]] #flip vertical

    tiles = []
    for t in (tilesArray):
        tiles += [pygame.image.frombuffer(bytes(t), (tileSize, tileSize), "RGB")]
    
    return tiles

def main():

    pygame.init()

    sourceImage = pygame.image.load("logo.png")
    pygame.display.set_icon(sourceImage)
    pygame.display.set_caption("Wave Function Collapse")
     
    screen = pygame.display.set_mode((800,800))
     
    running = True
    divisions = 4
    logoStr = pygame.image.tostring(sourceImage, "RGB")
    tileSize = int(SOURCE_SIZE / divisions)

    tiles = slice_tiles(tileSize, divisions, logoStr)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        lineJump = 0
        column = 0
        for i in range (len(tiles)):
            if i % 8 == 0:
                lineJump += 1
                column = 0
            screen.blit(tiles[i], ((tileSize + 5) * column, 100 + (tileSize +5) * lineJump))
            column += 1

        pygame.display.flip()
    
     
if __name__=="__main__":
    main()