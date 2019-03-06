import webbrowser


class Movie():    
    def __init__(self, movie_title, movie_storyline, 
                 poster_image, trailer_youtube):
        """ movie name"""
        self.title = movie_title
        """movie storyline"""
        self.storyline = movie_storyline
        """movie poster image url to access"""
        self.poster_image_url = poster_image
        """movie trailer url to access"""
        self.trailer_youtube_url = trailer_youtube   
        
    def show_trailer(self):
        """self refers to a variable field within the class 
        this function shows the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)

