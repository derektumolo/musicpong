def main():
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('Apocalypse')

	# Fill background (probably deprecated?)
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))

	# Initialise units
	global ug
	ug = units.UnitGroup() 
	ug.add(units.Unit())
	ug.add(units.Unit(2,4,"frowns"))

	global player
	player = Player()

	global map
	map = maps.Map(10) # 10 is the size, in tiles

	# Initialise sprites
	unitsprites = pygame.sprite.RenderPlain((ug))
	mapsprites = pygame.sprite.RenderPlain(map)

	gamechrome = chrome.Chrome()

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Initialise clock
	clock = pygame.time.Clock()

	running = True

	while running:
	# Make sure game doesn't run at more than 60 frames per second
		clock.tick(60)

		# no events are used, but the remnant pong behavior is still there for ref.
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			elif event.type == MOUSEBUTTONDOWN:
				x = event.pos[0]/32	
				y = event.pos[1]/32
				if event.button == 1:
					# detect collision with a unit, and select it, first deselecting the current
					player.highlight.move(x,y)
					#print player.highlight.rect
					newselect = pygame.sprite.spritecollide(player.highlight, ug, False)
					print newselect
					if newselect != []:
						# we have clicked on a unit.  
						if newselect[0] == player.selection:
							# if we click on it again, we deselect
							player.selection.deselect()
							player.selection = []
						else:
							# drop the current one, and select a new one.
							player.select(newselect[0])
							#player.selection.highlight = player.highlight
					elif player.selection:
						player.selection.move(x, y)

		map.draw(screen)

		# prob wrong
		player.highlight.draw(screen)

		for u in ug:
			screen.blit(background, u.rect, u.rect)
		unitsprites.update()

		unitsprites.draw(screen)

		gamechrome.draw(screen, player)

		pygame.display.flip()

if __name__ == '__main__': main()