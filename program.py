# MARK: Imports
from fresh_tomatoes import open_movies_page
from movie import Movie

# MARK: Movie Posters Constants
IMAGE_ASSET_BASE = "https://images-na.ssl-images-amazon.com/images/M/"
R1_POSTER = IMAGE_ASSET_BASE +\
  "MV5BMjEwMzMxODIzOV5BMl5BanBnXkFtZTgwNzg3OTAzMDI@._V1_SY1000_SX675_AL_.jpg"

MOANA_POSTER = IMAGE_ASSET_BASE +\
        "MV5BMjI4MzU5NTExNF5BMl5BanBnXkFtZTgwNzY1MTEwMDI" +\
        "@._V1_SY1000_CR0,0,674,1000_AL_.jpg"

FBEASTS_POSTER = IMAGE_ASSET_BASE +\
        "MV5BMjMxOTM1OTI4MV5BMl5BanBnXkFtZTgwODE5OTYxMDI" +\
        "@._V1_SY1000_CR0,0,674,1000_AL_.jpg"

# MARK: Create Movie Instances
# NOTE: You should probably escape your HTML
rogue_one = Movie(
        "Rogue One:<br><small>A Star Wars Story</small>",
        R1_POSTER,
        "https://www.youtube.com/watch?v=sC9abcLLQpI")

moana = Movie(
        "Moana",
        MOANA_POSTER,
        "https://www.youtube.com/watch?v=M5dnZKrUpdA")

f_beasts = Movie(
        "Fantastic Beasts<br><small>And Where To Find Them</small>",
        FBEASTS_POSTER,
        "https://youtu.be/Vso5o11LuGU")

# MARK: Aggregate Movies in List
movies = [rogue_one, moana, f_beasts]

# MARK: Main
open_movies_page(movies)
