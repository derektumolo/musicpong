#! /usr/bin/python

import Level
import sc
from metronome import Metronome

NOTE = 1
ACTION = 2

class TimingLevel(Level.Level):
	from logicBlocks.halfNote import getStartText,getEndText,getTempo,\
					 getBackgroundInstrument,getInstrumentList,isValidState,\
					 isButtonPressValid,playBackgroundInstrument,update, handleMusicInput

	def __init__(self):
		
		self.beatsPerMeasure = 4
		self.numMeasures = 6
		self.bpm = 140
		self.activePlayer = 1
		self.elapsedTurns = 0
		self.numFailures = 0
		
		self.state = NOTE
		self.fail = False
		self.notesPlayed = { 1: [], 2: [] }
		
		self.metronome = Metronome(self.bpm, self.beatsPerMeasure)
		
	def getEndText(self):
		print "Level 1 end text"
		
	def update(self):
		self.metronome.update()
		if(self.metronome.isAtNextBeat()):
			sine = sc.Synth( "click" )
			sine.amp  = 0.2
			self.advanceState()
			if(not self.isValidState()):
				self.fail = True
				
	def isValidState(self):
		print self.state
		if self.state == NOTE:
			return True
		else:
			if self.notesPlayed[self.activePlayer]:
				sine = sc.Synth( "sine" )
				sine.freq = 60+ (self.activePlayer * 3) + self.elapsedTurns 
				sine.amp  = 0.9
				return True
		#return False
		if (self.numFailures > 4):
			return False
		else:
			self.numFailures = self.numFailures + 1
			sine = sc.Synth( "saw" )
			sine.freq = 36 + (self.numFailures * 12) 
			sine.amp  = 0.6
			return True
	
	def advanceState(self):
		if (self.state == NOTE):
			self.state = ACTION
		else:
			self.state = NOTE
			self.changeActivePlayer()
			self.notesPlayed[self.activePlayer] = []
			self.elapsedTurns = self.elapsedTurns + 2
	


if __name__ == '__main__':
	test = TimingLevel()
	test.getEndText()
	test.getStartText()
	test.getTempo()
