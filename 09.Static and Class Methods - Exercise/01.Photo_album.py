from math import  ceil
class PhotoAlbum:
    MAX_PHOTO_PER_PAGE = 4
    def __init__(self,pages):
        self.pages = pages
        self.photos = self.create_matrix(self.pages)


    def create_matrix(self,pages):
        matrix = []
        for _ in range(pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count):
        result = ceil(photos_count / PhotoAlbum.MAX_PHOTO_PER_PAGE)
        return cls(result)

    def add_photo(self, label):
        for idx, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.MAX_PHOTO_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {idx+1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        sep = "-" * 11
        result = sep + "\n"
        for page in self.photos:
            result += ' '.join(["[]" for _ in page]) + '\n'
            result += sep + '\n'


        return result









