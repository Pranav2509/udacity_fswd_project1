import media
import fresh_tomatoes

#adding movies

independence_day =media.Movie("Independence Day", "http://artofvfx.com/wp-content/uploads/2015/12/IndependenceDay2.jpg", "https://www.youtube.com/watch?v=NCe_JshWOZ0")

dead_pool =media.Movie("Dead Pool", "http://static.srcdn.com/wp-content/uploads/Deadpool-Poster-Dec1st.jpg", "https://www.youtube.com/watch?v=ZIM1HydF9UA")

captain_america =media.Movie("Captain America", "http://geekactually.com/wp-content/uploads/2011/04/CA-TEASER-1-SHEET_localised.jpg", "https://www.youtube.com/watch?v=JerVrbLldXw")
#print(independence_day.title)

movie_list = [independence_day, dead_pool, captain_america]
fresh_tomatoes.open_movies_page(movie_list)

