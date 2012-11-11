#! /usr/bin/python

from abc import ABCMeta,abstractmethod 

NOTE = 1
ACTION = 2

class Level(object):
	__metaclass__ = ABCMeta
	
	import metronome
		
	@abstractmethod
	def getStartText():
		raise NotImplementedError

	@abstractmethod
	def getEndText():
		raise NotImplementedError

	@abstractmethod
	def getTempo():
		raise NotImplementedError

	@abstractmethod
	def getBackgroundInstrument():
		raise NotImplementedError

	@abstractmethod
	def getInstrumentList():
		raise NotImplementedError

	@abstractmethod
	def isValidState(tickValue):
		raise NotImplementedError

	@abstractmethod
	def isButtonPressValid(buttonPress,tickValue):
		raise NotImplementedError

	@abstractmethod
	def playBackgroundInstrument():
		raise NotImplementedError
	
	@abstractmethod
	def update():
		raise NotImplementedError
	
	@abstractmethod
	def handleMusicInput(input):
		raise NotImplementedError
		
	def isComplete(self):
		if (self.metronome.getBeat() > self.numberOfBeats):			
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
			self.changeActivePlayer
	
	def changeActivePlayer(self):
		if self.activePlayer == 1:
			self.activePlayer = 2
		else:
			self.activePlayer = 1