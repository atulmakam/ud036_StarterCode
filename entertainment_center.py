import fresh_tomatoes
import media         

def main():
    """list of my 5 favorite movies"""
    """In the order of movie_name,storyline,poster_image,youtube_tailer_url"""
    
    deadpool = media.Movie("Deadpool", "A fast-talking mercenary subjected to rogue experiment leaves him with accelerated powers", "http://bit.ly/2eorTC7",
                       "https://www.youtube.com/watch?v=gtTfd6tISfw")
    
    birdbox = media.Movie("Bird Box",
                     "When a mysterious force decimates the population, only one thing is certain -- if you see it, you die.",
                     "https://en.wikipedia.org/wiki/Bird_Box_(film)#/media/File:Bird_Box_(film).png",
                     "https://www.youtube.com/watch?v=o2AsIXSh2xo") 

    horriblebosses = media.Movie("Horrible Bosses",
                     "Nick, Dale and Kurt have personal grudges against their bosses. After a night of drunken revelry, they decide to hire a hitman and assassinate their bosses. However, things don't go quite as planned.",
                     "https://www.google.com/search?tbm=isch&q=Horrible+Bosses#imgrc=nmp7BCjkxusKYM:",
                     "https://www.youtube.com/watch?v=VpUeQV8sdOc")

    thehangover = media.Movie("The Hangover",
                          "The misadventures of a quartet of friends who go on their road trip to attend a bachelor party.",
                          "https://www.google.com/search?tbm=isch&q=The+Hangover#imgrc=k7Wf_1vw_Faq7M:",
                          "https://www.youtube.com/watch?v=tcdUhdOlz9M")
    spectre = media.Movie("Spectre",
                          "James Bond receives an obscure message he uncovers the conspiracy,",
                          "https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",
                          "https://www.youtube.com/watch?v=vBnGxAkdh_k")
    
    """Storing the list of objects to movies"""
    movies = [deadpool,birdbox,horriblebosses,thehangover,spectre]
    """ opening the trailer webpage in user's web browser"""
    
    fresh_tomatoes.open_movies_page(movies)
    

if __name__ == '__main__':
    main()
