#! /usr/bin/python

from abc import ABCMeta,abstractmethod 
from metronome import Metronome

NOTE = 1
ACTION = 2

class Level(object):
	__metaclass__ = ABCMeta
		
	@abstractmethod
	def isValidState(tickValue):
		raise NotImplementedError

	@abstractmethod
	def isButtonPressValid(buttonPress,tickValue):
		raise NotImplementedError

	@abstractmethod
	def playBackgroundInstrument():
		raise NotImplementedError
	
	def isComplete(self):
		if (self.metronome.getBeat() > self.numMeasures*self.beatsPerMeasure):			
			return True 
	
	def getActivePlayer(self):
		return self.activePlayer
		
	def start(self):
		pass
		
	def getState(self):
		return self.state
		
	def advanceState(self):
		if (self.state == NOTE):
			self.state = ACTION
		else:
			self.state = NOTE
			self.changeActivePlayer()
			self.notesPlayed[self.activePlayer] = []
			print "Play a note, player " + str(self.activePlayer)
	
	def changeActivePlayer(self):
		if self.activePlayer == 1:
			self.activePlayer = 2
		else:
			self.activePlayer = 1
			
	def failed(self):
		return self.fail
		
	def __init__(self, beatsPerMeasure, numMeasures, bpm, startText, endText, bgInstrument, instrumentList):
		self.beatsPerMeasure = beatsPerMeasure
		self.numMeasures = numMeasures
		self.bpm = bpm
		self.startText = startText
		self.endText = endText
		self.bgInstrument = bgInstrument
		self.instrumentList = instrumentList
		
		self.activePlayer = 1
		self.state = NOTE
		self.fail = False
		self.notesPlayed = {
            1: [],
            2: [],
			}
		self.metronome = Metronome(self.bpm, self.beatsPerMeasure)
		
	def update(self):
		self.metronome.update()
		if(self.metronome.isAtNextBeat()):
			click = sc.Synth( "click" )
			click.amp  = 0.2
			self.advanceState()
			if(not self.isValidState()):
				print "player " + str(self.activePlayer) + " LOSES"
				self.fail = True
	
	def handleMusicInput(self, player, note):
		if(self.isButtonPressValid(player,note)):
			self.notesPlayed[self.getActivePlayer()].append(note)
			
	def playBackgroundInstrument():
		pass
	
	def getOtherPlayer(self):
		if self.activePlayer == 2:
			return 1
		else:
			return 2
