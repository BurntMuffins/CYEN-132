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
        pygame.mixer.Sound.__init__(self, buffer=self.build_smaples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(MIXER_FREQ / self.frequency))
        amplitude = 2 ** (abs(MIXER_SIZE) - 1) - 1
        samples = array("h", [0] * period)

        # generating notes based on waveform
        for t in range(period):
            if (t < period / 2):
                samples[t] = amplitude
            else:
                samples[t] = -amplitude
        return samples
    


def wait_for_note_start():
    while(not GPIO.input(key)):
        sleep(0.01)

def wait_for_not_stop():
    while(GPIO.input(key)):
        sleep(0.1)

pygame.mixer.pre_init(MIXER_FREQ, MIXER_SIZE, MIXER_CHANS, MIXER_BUFF)
pygame.init()

GPIO.setmode(GPIO.BCM)
key = 20
freq = 261.6 # c note

GPIO.setup(key, GPIO.IN, GPIO.PUD_DOWN)

note = Note(freq, 1)

print("Welcome to the Touch Piano")
print("Press CTRL+C")

try:
    while True:
        wait_for_note_start()
        note.play(-1)
        wait_for_not_stop()
        note.stop()
except KeyboardInterrupt:
    GPIO.cleanup()
