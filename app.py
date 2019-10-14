from flask import Flask, Response, jsonify, request
import os
from movieView import MovieView
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/actor/<string:actor>')
def actor_info(actor):
	data=MovieView.data_by_actor(actor)
	return jsonify(data), 200

@app.route('/topGenres')
def top_ten_genres():
	data=MovieView.top_ten_genres()
	return jsonify(data), 200

@app.route('/topActors')
def top_ten_actors():
	data=MovieView.top_ten_actors()
	return jsonify(data), 200


if __name__ == "__main__":
	app.run()