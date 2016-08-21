import media
import fresh_tomatoes

# We create instances for 6 movies
avatar = media.Movie('Avatar',
    'http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'http://www.youtube.com/watch?v=5PSNL1qE6VY')

theGodfather = media.Movie('The Godfather',
    'http://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg',
    'http://www.youtube.com/watch?v=OfnUvYn6HoM')

pulpFiction = media.Movie('Pulp Fiction',
    'http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg',
    'http://www.youtube.com/watch?v=s7EdQ4FqbhY')

Django = media.Movie('Django Unchained',
    'http://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg',
    'http://www.youtube.com/watch?v=eUdM9vrCbow')

empireStrikesBack = media.Movie('The Empire Strikes Back',
    'http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg',
    'http://www.youtube.com/watch?v=JNwNXF9Y6kY')

theDarkKnight = media.Movie('The Dark Knight',
    'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
    'http://www.youtube.com/watch?v=EXeTwQWrcwY')

# List of movies that will be used by fresh_tomatoes.open_movies_page
movies = [
    avatar,
    theGodfather,
    pulpFiction,
    Django,
    empireStrikesBack,
    theDarkKnight]

# We call fresh_tomatoes.open_movies_page(movies). This will automatically
# generate the html code
fresh_tomatoes.open_movies_page(movies)
