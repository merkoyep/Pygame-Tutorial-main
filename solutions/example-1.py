# Example 1

# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Creat the game loop
running = True
while running: 
	# Looks at events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# Draw a circle
	screen.fill((255, 255, 255))

	for i in range(0, 9):
		color = (255, 0, 255)
		x = ((i % 3) * 175) + 75
		y = (int(i / 3) * 175) + 75
		position = (x, y)
			
		pygame.draw.circle(screen, color, position, 75)

	pygame.display.flip()
