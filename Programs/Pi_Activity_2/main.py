import RPi.GPIO as GPIO
from time import sleep
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
            # homework changes
            # sine
            if (t < period / 2):
                samples[t] = amplitude
            else:
                samples[t] = -amplitude

            # sawtooth
            # square
            # triangle
            
        return samples
    


def wait_for_note_start():
    while(True):
        for key in range(len(keys)):
            if (GPIO.input(keys[key])):
                return key
        sleep(0.01)

def wait_for_not_stop(key):
    while(GPIO.input(key)):
        sleep(0.1)

pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

GPIO.setmode(GPIO.BCM)
keys = [20, 16, 12, 26]
freqs = [261.6, 329.6, 392.0, 493.9]
notes = [] 

GPIO.setup(keys, GPIO.IN, GPIO.PUD_DOWN)

for n in range(len(freqs)):
    notes.append(Note(freqs, 1)) # sound for all loops

print("Welcome to the Touch Piano")
print("Press CTRL+C")

try:
    while True:
        key = wait_for_note_start()
        notes[key].play(-1)
        wait_for_not_stop(keys[key])
        notes[key].stop()
except KeyboardInterrupt:
    GPIO.cleanup()
