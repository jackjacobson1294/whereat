from flask import *
import extensions
import datetime
import time
import uuid
import hashlib

app = Flask(__name__)

@app.route("/", methods=['GET','POST','PUT'])
def hello():
	if request.method == 'PUT':
		db = extensions.connect_to_database()
		eventName = request.get_json(force=True)['eventName']
		#time = request.get_json(force=True)['time']
		ts = time.time()
		timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		eventCreator = request.get_json(force=True)['eventCreator']
		cur = db.cursor()
		#Reminder: should capitilize the Table Names
		cur.execute('INSERT INTO Events(eventName,time,eventCreator) VALUES ("%s","%s","%s")' % (eventName,timestamp,eventCreator))
		return "Hello World! You Have Inserted into the WhereAt Database"
	if request.method == 'GET':
		return "Hello World"


if __name__ == "__main__":
    app.run()