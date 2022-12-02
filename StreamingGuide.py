#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 11/30/22
#This code is designed to

class Movie: #defines class movie
    def __init__(self, title, genre, director, year):
        """initializes objects while accepting parameters"""
        self._title= title
        self._genre= genre
        self._director= director
        self._year= year

    def get_title(self):
        """returns title"""
        return self._title

    def get_genre(self):
        """returns genre"""
        return self._genre

    def get_director(self):
        """returns director"""
        return self._director

    def get_year(self):
        """returns year"""
        return self._year

class StreamingService: #defines class streaming service
    def __init__(self, name):
        """initialized name and sets catalog to an empty dictionary"""
        self._name= name
        self._catalog= {}

    def get_name(self):
        """returns name"""
        return self._name

    def get_catalog(self):
        """returns catalog"""
        return self._catalog

    def add_movie(self, movie):
        """returns addition of a movie"""
        self._catalog[movie.get_title()]=movie

    def delete_movie(self, movie_title):
        """deletes movie if title is in catalog"""
        del self._catalog[movie_title]


class StreamingGuide:
    def __init__(self):
        """initializes data to empty list"""
        self._stream_serve_list=[]

    def add_streaming_service(self, stream_serve):
        """takes streaming services as argument and adds it to a list"""
        self._stream_serve_list.append(stream_serve)

    def delete_streaming_service(self, stream_serve):
        """takes streaming service name, and if it exists in the list, removes it"""
        if stream_serve in self._stream_serve_list:
                self._stream_serve_list.remove(stream_serve)

    def where_to_watch_movie(self, movie_title):
        """takes movie title as an argument and returns a list"""
        element_0=None #sets elements of list to none
        for services in self._stream_serve_list:
            if movie_title in services.get_catalog():
                movie= services.get_catalog()[movie_title]
                if element_0==None:
                    element_0= [movie.get_title () +" ("+ str (movie.get_year ()) +")"] #concatenates name and year of movie

                element_0.append(services.get_name()) #if movie not available on any streaming service, return none
        return element_0

#testing
#movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
#movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
#movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
#movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

#stream_serv_1 = StreamingService('Netflick')
#stream_serv_1.add_movie(movie_2)

#stream_serv_2 = StreamingService('Hula')
#stream_serv_2.add_movie(movie_1)
#stream_serv_2.add_movie(movie_4)
#stream_serv_2.delete_movie('The Seventh Seal')
#stream_serv_2.add_movie(movie_2)

#stream_serv_3 = StreamingService('Dizzy+')
#stream_serv_3.add_movie(movie_4)
#stream_serv_3.add_movie(movie_3)
#stream_serv_3.add_movie(movie_1)

#stream_guide = StreamingGuide()
#stream_guide.add_streaming_service(stream_serv_1)
#stream_guide.add_streaming_service(stream_serv_2)
#stream_guide.add_streaming_service(stream_serv_3)
#stream_guide.delete_streaming_service('Hula')
#search_results = stream_guide.where_to_watch_movie('Little Women')

#print(search_results)
