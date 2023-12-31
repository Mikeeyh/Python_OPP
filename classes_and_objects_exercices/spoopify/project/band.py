from project.album import Album


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in [a.name for a in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        for a in self.albums:
            if a.name == album_name:
                if a.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(a)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        band_info = [f"Band {self.name}"]
        for a in self.albums:
            band_info.append(a.details())
        return '\n'.join(band_info)
