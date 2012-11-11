#! /usr/bin/python

ticksPerMinute = 3600

class Metronome:
		
	def __init__(self, bpm, timeSig):
		self.beat = 1
		self.bpm = bpm
		self.ticksPerBeat = ticksPerMinute/bpm
		self.timeSig = timeSig
		self.tick = 0
	
	def update(self):
		self.tick = self.tick + 1 

	def	isAtNextBeat(self):
		if (self.tick > self.ticksPerBeat * self.beat):
			self.beat = self.beat + 1
			return True
		return False
	
	def getBeat(self):
		return self.beat

