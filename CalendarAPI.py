from flask import Flask, jsonify, abort, request
import json


app = Flask(__name__)

calendars =  [
	{'cal_ID' : 100, 'entries' : [] },   #Calendar with no entries 
	{'cal_ID' : 101, 'entries' : [ {'entry_ID': 1, 'date': '21st Feb 2014', 'description': 'Going out', 'start-time': '9pm', 'end-time':'1am', 'repeats':'daily',' locations': 'maps.google.ie/bisto'},
				       {'entry_ID': 2, 'date': '13th Mar 2015', 'description': 'My Birthday', 'start-time': '9am', 'end-time': '4pm', 'repeats': 'weekly', 'locations': 'maps.google.ie/dit'},
				     ]   #End of entries list
	}   #End cal_ID 101
	     ]   #End of calendars list
	

#Initially show the calendars
#
@app.route('/')
def start_page():
	return jsonify( { 'calendars':calendars } )


#Working - Returns all calendars in JSON format
# curl = curl http://127.0.0.1:5000/api/calendars -X GET 
@app.route('/api/calendars', methods = ['GET'])
def get_calendars():
	return jsonify( {'calendars' : calendars} ) 

#Working - Returns calendar and events within for provided cal_ID
# curl = curl http://127.0.0.1:5000/api/calendars/100 -X GET 
@app.route('/api/calendars/<int:cal_ID>', methods = ['GET'])
def get_entry(cal_ID):
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			return jsonify( {'calendar': calendar[0] } )
		return "No existing calendar\n\n"

# Get entry from calendar with cal_ID and entry_ID
# curl - 
@app.route('/api/calendars/<int:cal_ID>/<int:entry_ID>', methods = ['GET'])
def get_enrty_from_calendar(cal_ID, entry_ID):
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			for temp_e in temp_c['entries']:
				if temp_e == {}:
					temp_c['entires'].remove({})
				elif temp_e['entry_ID'] == entry_ID:
					return jsonify(temp_e)
	return "No such entry found in calendar\n\n"


#Working -  Create a calendar with provided cal_ID
# curl = curl http://127.0.0.1:5000/api/calendars/102 -X POST
@app.route('/api/calendars/<int:cal_ID>', methods = ['POST'])
def create_calendar(cal_ID):
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			return "Calendar already exists\n\n"
	newCalendar = { 'cal_ID': cal_ID, 'entries': [] }
	calendars.append(newCalendar)
	return "New Calendar Created\n\n"


#Working - Create entry in calendar with provided cal_ID and the provided enrty_ID
# curl -i -H "Content-Type: application/json" -X POST -d '{"date":"31st March 2015"}' http://127.0.0.1:5000/api/calendars/100/4
@app.route('/api/calendars/<int:cal_ID>/<int:entry_ID>', methods = ['POST'])
def create_entry(cal_ID, entry_ID):
	if not request.json or not 'date' in request.json:
		abort(400)
	newEntry = {
		'entry_ID': entry_ID,
		'date': request.json['date'],
		'description': request.json.get('description', ""),
		'start-time': request.json.get('start-time', ""),
		'end-time': request.json.get('start-time', ""),
		'repeat': request.json.get('repeat', ""),
		'location': request.json.get('location', "")
	}
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			for temp_e in temp_c['entries']:
				if temp_e == {}:
					temp_c['entries'].remove({})
					temp_c['entries'].append(newEntry)
					return "Entry Created\n\n"
				if temp_e['entry_ID'] == entry_ID:
					return "Entry ID already exists, please choose a new entry ID\n\n"
			temp_c['entries'].append(newEntry)
			return "Entry Created\n\n"
	return "No existing calendar\n\n"


#Working - Get Calendar with the proived cal_ID
# curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/api/calendars/100

@app.route('/api/calendars/<int:cal_Id>', methods = ['GET'])
def get_calendar(cal_id):
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			return jsonify(temp_c)
		return "The selected calendar does not exist\n\n"


# NOT WORKING -  Update an existing enrty in an existing calendar with the given cal_ID and entry_ID 
# curl = curl -i -H "Content-Type: application.json" -d '{"description":"Updates Description"}' -X PUT http://127.0.0.1:5000/api/calendars/101/1
@app.route('/calendars/<int:cal_ID>/<int:entry_ID>', methods = ['PUT'])
def update_entry(cal_ID,entry_ID):
	if not request.json or not 'cal_ID' in request.json:
		abort(400)
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			for temp_e in temp_c['entries']:
				if temp_e['entry_ID'] == entry_ID:
					if 'date' in request.json:
						temp_e['date'] = request.json.get('date')
					if 'description' in request.json:
						temp_e['description'] = request.json.get('description')
					if 'start-time' in request.json:
						temp_e['start-time'] = request.json.got('start-time') 
					if 'end-time' in request.json:
						temp_e['end-time'] = request.json.got('end-time')
					if 'repeat' in request.json:
						temp_e['repeat'] = request.json.got('repeat')
					if 'location' in request.json:
						temp_e['location'] = request.json.got('location')
					
	return "Entry updated\n\n"

#Working -  Delete and entry in a calendar with the given cal_ID and entry_ID
# curl = curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5dars/101/1
@app.route('/api/calendars/<int:cal_ID>/<int:entry_ID>', methods = ['DELETE'])
def delete_Calendar_Entry(cal_ID, entry_ID):
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			for temp_e in temp_c['entries']:
				if temp_e['entry_ID'] == entry_ID:
					temp_e.clear()
					temp_c['entries'].remove({})
					return "Entry Deleted\n"
			return "Entry does no exist\n\n"
	return "Calendar does no exist\n\n"

#Delete calender with the given cal_ID
# curl = curl -i -X DELETE http://localhost:5000/api/calendars/105 
@app.route('/api/calendars/<int:cal_ID>', methods = ['DELETE'])
def delete_calendar(cal_ID):
	for temp_c in calendars:
		if temp_c['cal_ID'] == cal_ID:
			temp_c.clear()
			calendars.remove({})
			return "Calendar Deleted\n\n"
	return "Calendar does not exist"

if __name__ == '__main__':
	app.run(debug = True)
