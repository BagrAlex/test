from bottle import *
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

                      
TEMPLATE_PATH.insert(0,'c:/python/py_server/views')

@route("/")
@view("prediction")
def index():
	now = dt.now()
	x = random()
	return {
		"date": f"{now.year}-{now.month}-{now.day}",
		# "predictions": prophecies_url,	


	"special_date": x > 0.5,
	"x": x,
	}

                      
@route("/api/forecast")
def gener_forecast():

	return {
		"proph": generate_prophecies(6,2)

	}
    
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
