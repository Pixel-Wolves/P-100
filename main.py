class MovieReview:
    def __init__(self,movie,story,actors,music):
        self.movie_name=movie
        self.story_rating=story
        self.actor_rating=actors
        self.music_rating=music
        self.avg=int((self.story_rating+self.actor_rating+self.music_rating)/3)

        self.myreview={
            "Name":self.movie_name,
            "Story Rating":self.story_rating,
            "Actor Rating":self.actor_rating,
            "Music Rating":self.music_rating,
            "Average Rating":self.avg,
        }

        moviereviews.append(self.myreview)

    def avg_star_ratings(self,movie_list):
        for movie in movie_list:
            if (movie["Average Rating"]==1):
                print("You rated this movie:")
                print(movie)
            elif(movie["Average Rating"]==2):
                print("You rated this movie:")
                print(movie)
            elif(movie["Average Rating"]==3):
                print("You rated this movie:")
                print(movie)
            elif(movie["Average Rating"]==4):
                print("You rated this movie:")
                print(movie)
            elif(movie["Average Rating"]==5):
                print("You rated this movie:")
                print(movie)

moviereviews=[]
review1= MovieReview("Sonic The Hedgehog",4,5,5)
review1.avg_star_ratings(moviereviews)


