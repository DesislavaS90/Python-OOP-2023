from math import ceil


class PhotoAlbum:
    PHOTOS_LIMIT = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / cls.PHOTOS_LIMIT))

    def add_photo(self, label):
        for p in range(len(self.photos)):
            if len(self.photos[p]) < self.PHOTOS_LIMIT:
                self.photos[p].append(label)
                return f'{label} photo added successfully on page {p + 1}' \
                       f' slot {len(self.photos[p])}'
        return 'No more free slots'

    def display(self):
        result = ['-' * 11]

        for page in self.photos:
            result.append(('[] ' * len(page)).rstrip())
            result.append('-' * 11)

        return '\n'.join(result)


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())