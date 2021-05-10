from icalendar import Calendar, Event
import tempfile, os
import pytz
from datetime import datetime

cal = Calendar()
cal.add('version', '0.1')

event = Event()

event.add('summary', 'Hello World')
event.add('dtstart', datetime(2021, 5, 11, 0,0,tzinfo=pytz.utc))
event.add('dtend', datetime(2021, 5, 12, 0,0,tzinfo=pytz.utc))
event.add('dtstamp', datetime(2021,5,1,0,0,0,tzinfo=pytz.utc))

cal.add_component(event)

directory = tempfile.mkdtemp()
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()