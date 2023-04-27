########################################
# Name: Aidan Schaubhut
# Date: 4/26/23
# Description: Paper piano (v3).
########################################

import RPi.GPIO as GPIO
from time import sleep, time
import pygame
from array import array

MIXER_FREQ = 44100
MIXER_SIZE = -16
MIXER_CHANS = 1
MIXER_BUFF = 1024

# the note generator class
class Note(pygame.mixer.Sound):
    def __init__(self, frequency, volume):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, buffer=self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        samples = array("h", [0] * period)

        # generating notes based on waveform
        for t in range(period):
            if self.waveform == "sine":
                if t < period / 2:
                    samples[t] = amplitude
                else:
                    samples[t] = -amplitude
            elif self.waveform == "sawtooth":
                samples[t] = int((-amplitude + (2 * amplitude / period) * t))
            elif self.waveform == "square":
                if t < period / 2:
                    samples[t] = amplitude
                else:
                    samples[t] = -amplitude
            elif self.waveform == "triangle":
                samples[t] = int((amplitude - (2 * amplitude / period) * abs(t - period/2)))

        return samples
    


def wait_for_note_start():
    while True:
        # first, check for notes
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
            # next, check for the play button
            if (GPIO.input(play)):
                # debounce the switch
                while (GPIO.input(play)):
                    sleep(0.01)
                return "play"
            # finally, check for the record button
            if (GPIO.input(record)):
                # debouce the switch
                while (GPIO.input(record)):
                    sleep(0.01)
                return "record"
            sleep(0.01)

def wait_for_note_stop(key):
    while(GPIO.input(key)):
        sleep(0.1)

def play_song():
    for part in song:
        note, duration = part
        if (note == "SILENCE"):
            sleep(duration)
        else:
            notes[note].play(-1)
            sleep(duration)
            notes[note].stop()

pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

# setup the pins and frequencies for the notes (C, E, G, B)
GPIO.setmode(GPIO.BCM)
keys = [20, 16, 12, 26]
freqs = [261.6, 329.6, 392.0, 493.9]
notes = [] 

# setup the button pins
play = 19
record = 21

# setup thhe LED pins
red = 27
green = 18
blue = 17

# setup the input pins
GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(play, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(record, GPIO.IN, GPIO.PUD_DOWN)

# setup the output pins
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# create the actual notes
for n in range(len(freqs)):
    notes.append(Note(freqs, 1)) # sound for all loops

# begin a non-recording state and init the song
recording = False
song = []

print("Welcome to the Touch Piano")
print("Press CTRL+C")

try:
    while True:
        start = time()
        key = wait_for_note_start()
        duration = time() - start
        if (recording):
            song.append(["SILENCE", duration])
        if (key == "record"):
            if (not recording):
                song = []
            recording = not recording
            GPIO.output(red, recording)
        elif (key == "play"):
            if (recording):
                recording = False
            GPIO.output(red, False)
            GPIO.output(green, True)
            play_song()
            GPIO.output(green, False)
        else:
            start = time()
            notes[key].play(-1)
            wait_for_note_stop(keys[key])
            notes[key].stop()
            duration = time() - start
            if (recording):
                song.append([key, duration])

except KeyboardInterrupt:
    GPIO.cleanup()
