class Metronome:
	
	ticksPerMinute = 3600
		
	def __init__(self, bpm, timeSig, screen):
		self.beat = 1
		self.bpm = bpm
		self.tickerPerBeat = ticksPerMinute/bpm
		self.timeSig = timeSig
		self.screen = screen
		self.tick = 0
	
	def update(self):
		tick = tick + 1 

	def	atNextMeasure():
		if (tick > self.ticksPerBeat * self.beat):
			self.beat = self.beat + 1
			if (self.beat%self.timeSig == 1):
				return True
		return False

