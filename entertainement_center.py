import media
import fresh_tomatoes

#Instances for the class Movie

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "Fantasy/Science fiction film", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
baahubali = media.Movie("Baahubali", "In the kingdom of Mahishmati, while pursuing his love, Shivudu learns about the conflict-ridden past of his family and his legacy. He must now prepare himself to face his new-found archenemy.", "https://upload.wikimedia.org/wikipedia/en/7/7e/Baahubali_poster.jpg", "https://www.youtube.com/watch?v=3NQRhE772b0")
the_intouchables = media.Movie("The Intouchables","An unlikely friendship develops between a wealthy quadriplegic (François Cluzet) and his caretaker (Omar Sy), just released from prison.", "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg", "https://www.youtube.com/watch?v=0PH6I9h6f3w")
star_wars = media.Movie("Star Wars: The Last Jedi", "Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares to do battle with the First Order.", "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg","https://www.youtube.com/watch?v=Gn0WzX3OcAU")
it = media.Movie("It", "Seven young outcasts in Derry, Maine, are about to face their worst nightmare -- an ancient, shape-shifting evil that emerges from the sewer every 27 years to prey on the town's children. Banding together over the course of one horrifying summer, the friends must overcome their own personal fears to battle the murderous, bloodthirsty clown known as Pennywise.","https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg","https://www.youtube.com/watch?v=fsedSpJ-_a8")

# Creating a HTML file and opening in web browser for list of Latest movies
movies = [toy_story, avatar, baahubali, the_intouchables, star_wars, it]
fresh_tomatoes.open_movies_page(movies)

