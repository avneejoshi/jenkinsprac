from datetime import datetime,timedelta
today=datetime.now()
print("Today\'s date and time is : ",today)
before=today-timedelta(weeks=1)
print("Date and time before 1 week was : ",before)