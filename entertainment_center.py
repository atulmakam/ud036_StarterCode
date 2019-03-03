import fresh_tomatoes
import media         

def main():
    """list of my 5 favorite movies"""
    """In the order of movie_name,storyline,poster_image,youtube_tailer_url"""
    
    deadpool = media.Movie("Deadpool", "A fast-talking mercenary subjected to rogue experiment leaves him with accelerated powers", "http://bit.ly/2eorTC7",
                       "https://www.youtube.com/watch?v=gtTfd6tISfw")
    
    toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/\
                        en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    
    mad_max = media.Movie("Mad Max: Fury Road", 
                       " A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.",
                       "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                       "https://www.youtube.com/watch?v=hEJnMQG9ev8")
    
    inception = media.Movie("Inception",
                       "A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.",
                       "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                       "https://youtu.be/8hP9D6kZseM")
    
    spectre = media.Movie("Spectre",
                        "James Bond receives an obscure message he uncovers the conspiracy,",
                        "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                        "https://www.youtube.com/watch?v=vBnGxAkdh_k")
    
    interstellar = media.Movie("Interstellar",
                        "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life."
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                        "https://youtu.be/0vxOhd4qlnA")

    
    """Storing the list of objects to movies"""
    movies = [deadpool, toy_story, mad_max, inception, spectre, interstellar]
    """ opening the trailer webpage in user's web browser"""
    
    fresh_tomatoes.open_movies_page(movies)
    

if __name__ == '__main__':
    main()
