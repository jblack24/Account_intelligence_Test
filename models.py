import app
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import Column, Integer, String
#from flask_sqlalchemy import SQLAlchemy

from base import Base
#db = SQLAlchemy(app.app)
#metadata=metadata

class MovieData(Base):
    __tablename__ = 'movie_metadata2'

    id = Column(Integer, primary_key=True)
    color=Column(String(16))
    director_name=Column(String(32))
    num_critic_for_reviews=Column(Integer)
    duration=Column(Integer)
    director_facebook_likes=Column(Integer)
    actor_3_facebook_likes=Column(Integer)
    actor_2_name=Column(String(28))
    actor_1_facebook_likes=Column(Integer)
    gross=Column(Integer)
    genres=Column(String(64))
    actor_1_name=Column(String(27))
    movie_title=Column(String(88))
    num_voted_users=Column(Integer)
    cast_total_facebook_likes=Column(Integer)
    actor_3_name=Column(String(30))
    facenumber_in_poster=Column(Integer)
    plot_keywords=Column(String(149))
    movie_imdb_link=Column(String(52))
    num_user_for_reviews=Column(Integer)
    language=Column(String(10))
    country=Column(String(20))
    content_rating=Column(String(9))
    budget=Column(String(20))
    title_year=Column(Integer)
    actor_2_facebook_likes=Column(Integer)
    imdb_score=Column(Integer)
    aspect_ratio=Column(Integer)
    movie_facebook_likes=Column(Integer)

    # def __init__(self url result_all result_no_stop_words):
    #     self.url = url
    #     self.result_all = result_all
    #     self.result_no_stop_words = result_no_stop_words

    # def __repr__(self):
    #     return '<id {}>'.format(self.id)