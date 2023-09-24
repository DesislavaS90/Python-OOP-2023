from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user = [n for n in self.users_collection if n.username == username]
        if user:
            raise Exception('User already exists!')
        user = User(username, age)
        self.users_collection.append(user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        user = [n for n in self.users_collection if n.username == username]
        if not user:
            raise Exception('This user does not exist!')
        if user[0].username != movie.owner.username:
            raise Exception(f'{user[0].username} is not the owner of the movie {movie.title}!')
        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        self.movies_collection.append(movie)
        user[0].movies_owned.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        if movie.owner.username != username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if movie.owner.username != username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        self.movies_collection.remove(movie)
        movie.owner.movies_owned.remove(movie)
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        user = [s for s in self.users_collection if s.username == username][0]
        if movie.owner.username == user.username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')
        if movie in user.movies_liked:
            raise Exception(f'{username} already liked the movie {movie.title}!')
        movie.likes += 1
        user.movies_liked.append(movie)
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        user = [s for s in self.users_collection if s.username == username][0]
        if movie not in user.movies_liked:
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        return '\n'.join([movie.details() for movie in movies]) if movies else 'No movies found.'

    def __str__(self):
        return f"All users: {', '.join([u.username for u in self.users_collection])if self.users_collection else 'No users.'}\n"\
               f"All movies: {', '.join([m.title for m in self.movies_collection])if self.movies_collection else 'No movies.'}"



