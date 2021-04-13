"""
id, title, featured_artist, length, written_by, 
"""
import time

class Song:
  id = 0
  title = ''
  featured_artist = ''
  song_duration = ''
  written_by = ''

  def __init__(self, id, title, featured_artist, song_duration, written_by):
    self.id = id
    self.title = title
    self.featured_artist = featured_artist
    self.song_duration = song_duration
    self.written_by = written_by

  def __str__(self):
    return self.title + "|" + self.artist