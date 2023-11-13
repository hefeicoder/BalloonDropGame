import pygame

# Initialize the mixer
pygame.mixer.init()


SOUND_CORRECT = 'sound_correct'
SOUND_WRONG = 'sound_wrong'
SOUND_GREAT = 'sound_guaguagua'
SOUND_OHNO = 'sound_ohno'

class SoundManager:
    sounds = {
    }  # Dictionary to store loaded sounds
    @staticmethod
    def init():
        SoundManager.load_sound(SOUND_CORRECT, 'resource/correct.wav')
        SoundManager.load_sound(SOUND_WRONG, 'resource/wrong.wav')
        SoundManager.load_sound(SOUND_GREAT, 'resource/guaguagua.wav')
        SoundManager.load_sound(SOUND_OHNO, 'resource/ohno.wav')

    @staticmethod
    def load_sound(sound_name, file_path):
        """Load a sound from a given file path and store it with a name."""
        SoundManager.sounds[sound_name] = pygame.mixer.Sound(file_path)

    @staticmethod
    def play_sound(sound_name):
        """Play a sound by its name."""
        if sound_name in SoundManager.sounds:
            SoundManager.sounds[sound_name].play()
        else:
            print(f"Sound '{sound_name}' not found.")
