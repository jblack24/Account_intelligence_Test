import pandas as pd
import json
from models import *
from base import session
from sqlalchemy import or_


class MovieView:
	@classmethod
	def data_by_actor(self, actor_name):
		#finding the actors movie_title, budget and gross from the actor name
		actor_movies=session.query(MovieData.movie_title, MovieData.actor_1_name, MovieData.actor_2_name, MovieData.actor_3_name, MovieData.budget, MovieData.gross)\
		.filter(or_(MovieData.actor_1_name==actor_name, MovieData.actor_2_name==actor_name, MovieData.actor_3_name==actor_name)).all()
		print(actor_movies)
		actor_dict={}
		actor_dict['movies']=[]
		#generating list of movies and detail for the actor
		for movie in actor_movies:
			#'movie_title': str(movie.movie_title).replace('\\u00c2','')
			temp_dict={'movie_title': movie.movie_title.encode('utf-8').replace('\\u00c2',''),
						'actor_1_name': movie.actor_1_name,
						'actor_2_name': movie.actor_2_name,
						'actor_3_name': movie.actor_3_name,
						'budget': movie.budget,
						'gross': movie.gross}
			actor_dict['movies'].append(temp_dict)
		return actor_dict

	@classmethod
	def top_ten_genres(self):
		#querying the database for all movies
		query=session.query(MovieData)
		df=pd.read_sql(query.statement, query.session.bind)
		#getting unique genres 
		unique_genres=pd.unique(df['genres'].str.split('|', expand=True).stack())
		#converting budget to decimal and calculating net profit
		df['budget_decimal']=df['budget'].apply(pd.to_numeric)
		df['Profit']=df['gross']-df['budget_decimal']
		finaldf=pd.DataFrame(columns=['Genre', 'Gross', 'Budget', 'Profit'])
		#iterating over the unique genres and finding which movies have that genre
		#if so adding the movie to the genre and calculating the totals
		for genre in unique_genres:
			#print('genre', genre.encode('ascii'))
			temp_df=df.loc[df['genres'].str.contains(genre.encode('ascii'))]
			#print(temp_df)
			temp_dict={'Genre': genre,
						'Gross': temp_df['gross'].sum(),
						'Budget': temp_df['budget_decimal'].sum(),
						'Profit': temp_df['Profit'].sum()}
			tdf=pd.DataFrame.from_records(temp_dict, index=[0])
			finaldf=finaldf.append(tdf)
		#taking top 10 based on profit
		top_10_df=finaldf.sort_values(['Profit'], ascending=False).iloc[0:10]
		#print(top_10_df)
		return top_10_df.to_dict('records')

	@classmethod
	def top_ten_actors(self):
		#querying the database for all movieData
		query=session.query(MovieData)
		df=pd.read_sql(query.statement, query.session.bind)	
		#getting unique actor names
		unique_actors=pd.unique(df[['actor_1_name', 'actor_2_name', 'actor_3_name']].values.ravel('K'))
		print('hehrere: ', any(i is None for i in unique_actors))
		print(unique_actors)
		unique_actors=[i for i in unique_actors if i]
		print('hehrere: ', any(i is None for i in unique_actors))
		#calculating profit and converting budget to decimal
		df['budget_decimal']=df['budget'].apply(pd.to_numeric)
		df['Profit']=df['gross']-df['budget_decimal']
		finaldf=pd.DataFrame(columns=['Actor', 'Gross', 'Budget', 'Profit'])
		# df['actor_1_name'].fillna('', inplace=True)
		# df['actor_2_name'].fillna('', inplace=True)
		# df['actor_3_name'].fillna('', inplace=True)
		df['actors_encoded']=df['actor_1_name'].str.encode('ascii', 'ignore')+'|'+df['actor_2_name'].str.encode('ascii', 'ignore')+'|'+df['actor_3_name'].str.encode('ascii', 'ignore')
		for actor in unique_actors:
			print(type(actor))
			print(actor)
			#temp_df=df.loc[df['actor_1_name'].str.contains(actor.encode('ascii', ))|df['actor_2_name'].str.contains(actor.encode('ascii'))|df['actor_3_name'].str.contains(actor.encode('ascii'))]
			temp_df=df.loc[df['actors_encoded'].str.contains(actor.encode('ascii', 'ignore'), na=False)]
			temp_dict={'Actor': actor,
						'Gross': temp_df['gross'].sum(),
						'Budget': temp_df['budget_decimal'].sum(),
						'Profit': temp_df['Profit'].sum()}
			tdf=pd.DataFrame.from_records(temp_dict, index=[0])
			finaldf=finaldf.append(tdf)
		#taking top 10 based on profit
		top_10_df=finaldf.sort_values(['Profit'], ascending=False).iloc[0:10]
		#print(top_10_df)
		return top_10_df.to_dict('records')







