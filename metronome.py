class Metronome:
	def __init__(self, bpm, timeSig, screen):
		self.beat = 1
		self.ticksPerBeat = bpm
		self.timeSig = timeSig
		self.screen = screen
	
	def circle(self,tick,gap):
		x = tick*gap*self.ticksPerBeat/60/60
		pygame.draw.circle(self.screen, (255,0,0), (x + 10,70),5)
	
	def update(self, tick):
		self.circle()
		if (tick > self.ticksPerBeat * self.beat):
			self.beat = self.beat + 1
			if (self.beat%self.timeSig == 1):
				return True
		return False