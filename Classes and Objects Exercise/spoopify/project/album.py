from project.song import Song


class Album:

    def __init__(self, name, song=None):
        self.name = name
        self.songs = song
        self.published = False
        self.songs = [song] if song else []

    def add_song(self, song: Song):

        if self.published:
            return 'Cannot add songs. Album is published.'
        if song in self.songs:
            return 'Song is already in the album.'
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name):
        if self.published:
            return 'Cannot remove songs. Album is published.'
        for s in self.songs:
            if s.name == song_name:
                self.songs.remove(s)
                return f'Removed song {song_name} from album {self.name}.'
        return 'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        details = '\n'.join([f'== {song.get_info()}' for song in self.songs])
        return f"Album {self.name}\n{details}\n"