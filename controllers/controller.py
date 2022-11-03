from flask import render_template, request
from app import app
from models.event import Event
from models.event_list import event_list,add_new_event
import datetime




@app.route('/events')
def index():
    return render_template("index.html", event_list= event_list)

@app.route('/events', methods=["POST"])
def add_event():
    date = request.form['date']
    # split the date into a list
    split_date = date.split('-')
    # create a new date object
    date - datetime.date(int(split_date[0])), int(split_date[1]), int([split_date[2]])
    eventName = request.form['name']
    
    eventGuests = request.form['guests']
    eventLocation = request.form['location']
    eventDescription = request.form['description']
    newEvent = Event(name = eventName, date = date, guests = eventGuests, location = eventLocation, description = eventDescription)
    add_new_event(newEvent)
    

    return render_template('index.html', event_list = event_list)
