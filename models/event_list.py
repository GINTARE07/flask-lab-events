from models.event import Event
import datetime 

event1 = Event("Tech meet up",datetime.date(2022, 11, 3), 15, "Voodoo Rooms", "Cool event for tech indutry enthusiasts")
event2 = Event("Masquerade Ball",datetime.date(2022, 11, 14 ) ,45, "George house", "Bring a pink dress and falafels")
event3 = Event("Halloween party",datetime.date(2022, 10, 31), 25, "Gintares house", "Falafels fiesta and more")

event_list =[event1, event2, event3]


def add_new_event(event):
    event_list.append
    