import pygame

# Initialize the mixer
pygame.mixer.init()


SOUND_CORRECT = 'sound_correct'
SOUND_WRONG = 'sound_wrong'

class SoundManager:
    sounds = {}  # Dictionary to store loaded sounds

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
