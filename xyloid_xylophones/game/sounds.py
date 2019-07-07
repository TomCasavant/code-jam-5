import pyglet
from config import location_sound, location_music

class Sound():
    def __init__(self):
        self.player = pyglet.media.Player()

    def play_music(self, song_title):
        song = pyglet.media.load(location_music+song_title)
        self.player.queue(song)
        self.player.eos_action = pyglet.media.SourceGroup.loop
        self.player.play()
