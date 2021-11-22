import pygame


class Sound:
    def __init__(self, audio: str = 'sounds/default.mp3'):
        self.audio = audio
        self.sound = pygame.mixer.Sound(self.audio)
        pygame.mixer.Sound.set_volume(self.sound, 0.01)

    def play(self):
        pygame.mixer.Sound.play(self.sound)
