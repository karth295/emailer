class bookkeeper:
  timestamp = ""
  user = ""
  days = ""
  assignment = ""

  def __init__(self, timestamp, user, days, assignment):
    self.timestamp = timestamp;
    self.user = user;
    self.days = days;
    self.assignment = assignment;

  def __str__(self):
    return self.user + " requested " + self.days + " lateday(s) on " + self.assignment + " at " + self.timestamp
  
def stringToDate(the_date):
  datetime_string = the_date.strip()
  datetime_list = datetime_string.split(" ")
  date_list = datetime_list[0].split("/")
  date_month = int(date_list[0])
  date_day = int(date_list[1])
  date_year = int(date_list[2])
  time_list = datetime_list[1].split(":")
  time_hour = int(time_list[0])
  time_minute = int(time_list[1])
  time_second = int(time_list[2])
  date = datetime.datetime(date_year, date_month, date_day, time_hour, time_minute, time_second)
  return date

