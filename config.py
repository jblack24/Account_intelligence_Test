import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
	host='127.0.0.1'
	port='5432'
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	engine_url='postgresql://localhost:5432/assessments'