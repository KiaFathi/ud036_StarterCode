class Movie:
    """ Movie Class

    Attributes:
        title (str): Title of the movie
        poster_image_url (str): URL of the movie's poster image
        trailer_youtube_url (str): URL of the movie's trailer
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
