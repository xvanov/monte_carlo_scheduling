from datetime import datetime
from dateutil.rrule import *

dtstart = datetime(2021, 8, 4)
weekdays = rrule(WEEKLY, byweekday=(MO, TU, WE, TH, FR), dtstart=dtstart)
workdays = rrule(DAILY, dtstart=dtstart)
laborday = rrule(DAILY, dtstart=datetime(2021, 9, 7), count=1)
offsite_training = rrule(DAILY, dtstart=datetime(2021, 9, 10), count=4)
learning = rrule(DAILY, dtstart=dtstart)

rules = [
        (laborday,  0),
        (offsite_training, 3),
        (learning, 3),
]
