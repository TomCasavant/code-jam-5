import pyglet
from config import location_sound, location_music

class Sound():
    def __init__(self):
        self.player = pyglet.media.Player()
        self.current_background = ""

    def play_music(self, song_title):
        '''Load song up and play on a loop'''
        self.current_background = song_title
        song = pyglet.media.load(location_music+song_title) #Load up the song
        self.player.next_source()
        self.player.queue(song) #Add the song to the queue
        self.player.eos_action = pyglet.media.SourceGroup.loop #Loop the song
        self.player.play()

    def play_sound(self, sound_title):
        '''Temporarily pause background music, play sound and restart background music'''
        sound = pyglet.media.load(location_sound+sound_title) #Load up the sound effect
        self.player.queue(sound)
        self.player.next_source() #Play the sound effect
        song = pyglet.media.load(location_music+self.current_background)
        self.player.queue(song) #Add the background music to the queue
