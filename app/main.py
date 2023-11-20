# Import and initialize pygame
import pygame
from random import randint
from chicken import Chicken
from duck import Duck
from bird import Bird
from player import Player
from slimeH import SlimeH
from slimeV import SlimeV
from ScoreBoard import ScoreBoard
pygame.init()

clock = pygame.time.Clock()

#configure the screen
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Chicken Rescue')

#Establish background images
background_image = pygame.image.load("background.png")
ready_image = pygame.image.load("readyimage.png")

#Fonts
header_font = pygame.font.SysFont("Roboto", 40)
text_font = pygame.font.SysFont("Roboto", 30)
#Initialize Scoreboard
score = ScoreBoard(30, 30, 0)

def draw_text(text, font, text_col, x, y):
	'''Renders string passed in as an image and display on screen'''
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

#sound
pygame.mixer.init()
pygame.mixer.music.load("./sounds/backgroundmusic.wav")
chicken_sound = pygame.mixer.Sound("./sounds/chicken.wav")
slime_kill = pygame.mixer.Sound("./sounds/slimekill.wav")


# vertical objects
duck = Duck()

#horizontal objects
chicken = Chicken()
bird = Bird()
#player and slimes
player = Player()
slimeH = SlimeH()
slimeV = SlimeV()

vertical_sprites = pygame.sprite.Group()

vertical_sprites.add(duck)


horizontal_sprites = pygame.sprite.Group()
horizontal_sprites.add(chicken)
horizontal_sprites.add(bird)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(score)
all_sprites.add(duck)
all_sprites.add(chicken)
all_sprites.add(bird)
all_sprites.add(slimeH)
all_sprites.add(slimeV)

animal_sprites = pygame.sprite.Group()

animal_sprites.add(duck)
animal_sprites.add(chicken)
animal_sprites.add(bird)

# Creat the game loop
game_state = 'ready'
running = True 
pygame.mixer.music.play(1)
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				elif event.key == pygame.K_LEFT:
					player.left()
				elif event.key == pygame.K_RIGHT:
					player.right()
				elif event.key == pygame.K_UP:
					player.up()
				elif event.key == pygame.K_DOWN:
					player.down()
	# Looks at events
	if game_state == 'ready':
		screen.blit(ready_image, (0, 0))
		game_score = 0
		draw_text('Welcome to Chicken Rescue!', header_font, (244, 244, 244), 115, 40)
		draw_text('THE SLIMES ARE ATTACKING!', text_font, (244, 244, 244), 115, 80)
		draw_text('Use your arrow keys to save', text_font, (244, 244, 244), 115, 120)
		draw_text('your terrified animals!', text_font, (244, 244, 244), 140, 140)
		draw_text('Ready? Hit SPACE to start!', header_font, (244, 244, 244), 120, 180)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			game_state = 'playing'
		pygame.display.flip()

	elif game_state == 'playing':
		screen.blit(background_image, (0, 0))	
		# Draw a circle
		for entity in all_sprites:
			entity.move()
			entity.render(screen)

		pygame.display.flip()
		animals = pygame.sprite.spritecollideany(player, animal_sprites)
		if animals:
			pygame.mixer.Sound.play(chicken_sound)
			for sprite in vertical_sprites:
				sprite.dy += (randint(0, 50) / 100)
			for sprite in horizontal_sprites:
				sprite.dx += (randint(0, 50) / 100)
			slimeH.dx += (randint(0, 25) / 100)
			slimeV.dy += (randint(0, 25) / 100)
			score.update(100)
			game_score += 100
			animals.reset()
		if pygame.sprite.collide_circle(player, slimeH) or pygame.sprite.collide_rect(player, slimeV):
			pygame.mixer.Sound.play(slime_kill)
			game_state = 'game_over'
			for sprite in all_sprites:
				sprite.reset()
			for sprite in vertical_sprites:
				sprite.dy = (randint(0, 200) / 100) + 1
			for sprite in horizontal_sprites:
				sprite.dx = (randint(0, 200) / 100) + 1
			slimeH.dx = (randint(0, 200) / 100) + 1
			slimeV.dy = (randint(0, 200) / 100) + 1

	# Update the display
	elif game_state == 'game_over':
		screen.blit(ready_image, (0, 0))
		draw_text('GAME OVER!', text_font, (244, 244, 244), 190, 100)
		draw_text(f'Your score:{game_score}', text_font, (244, 244, 244), 190, 120)
		draw_text('Play again? Press P!', text_font, (244, 244, 244), 160, 160)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_p]:
			game_state = 'ready'
		pygame.display.flip()
	clock.tick(60)