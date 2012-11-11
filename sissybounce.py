#! /usr/bin/python

import sys
import os
import sc
import time

import pygame
import pygame.midi
from pygame.locals import *

try:  # Ensure set available for output example
    set
except NameError:
    from sets import Set as set


def input_main(device_id = None):
    
	pygame.init()
	pygame.fastevent.init()
    
	event_get = pygame.fastevent.get
    	event_post = pygame.fastevent.post

    	pygame.midi.init()

    	devices = (pygame.midi.Input(3),pygame.midi.Input(5))
    	pygame.display.set_mode((1,1))
    	print "ready for input"


    	going = True
    	while going:
		events = event_get()
		for i in devices:
			for e in events:
			    if e.type in [QUIT]:
				going = False
			    if e.type == KEYDOWN:
				if e.key in [K_1,K_q,K_a,K_z]:
			    		print "Player 1"
				if e.key in [K_HOME,K_PAGEUP,K_PAGEDOWN,K_END]:
			    		print "Player 2"

			if i.poll():
			    midi_events = i.read(10)
			    if midi_events[0][0][0] == s_keyDown: 
					print midi_events[0][0]
					if i == devices[0]:
						saw = sc.Synth( "saw" )
						saw.freq = midi_events[0][0][1] # midi key pressed
						saw.amp = midi_events[0][0][2]/s_velocityValue

					if i == devices[1]:
						sine = sc.Synth( "sine" )
						sine.freq = midi_events[0][0][1]
						sine.amp = midi_events[0][0][2]/s_velocityValue

    	pygame.midi.quit()



def main(mode='output', device_id=None):

    print_device_info()
                
if __name__ == '__main__':

    	# define global variables
	s_keyDown=144
	s_velocityValue=127.0
    
	# initialize supercollider
	sc.start()
    
	input_main()

