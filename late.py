from subprocess import Popen, PIPE
import csv
import sys
import datetime

def sendMail(timestamp, user, days, assignment):
  days = str(days)  #easy to concatenate as string
  subject = "Requested " + days + " lateday(s)"
  message = """Dear """ + user + """,

  You requested """ + days + """ lateday(s) for """ + assignment + """ at """ + timestamp + """. Please notify us immediately at cse331-staff@cs.washington.edu if this is incorrect.

  Warning: This email is only to inform you how many latedays you requested on the Google form. Please ensure that you actually have the number of lateday(s) you requested left, and that the requested assignment was still open for latedays at the date/time indicated.
  
  Thanks,
  CSE 331 staff"""
  
  echoed = Popen(['echo', message], stdout=PIPE)
  Popen(['mail', '-s', subject, '-r', 'cse331-staff@cs.washington.edu', user], stdin=echoed.stdout, stdout=PIPE)

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


time_index = 0
user_index = 1
days_index = 2
assign_index = 3

errors = 0

if len(sys.argv) != 2 or (not sys.argv[1].endswith(".csv")):
  print "Usage: python late.py <file.csv>"
else:
  cur_map = {}
  f = csv.reader(open(sys.argv[1]))
  print "Sending mail now..."
  for line in f:
    if len(line) != 4:
      print "Error: malformed line:", line
      errors += 1
      continue
    #while iterating over the lines, add to map (check if it exists before)
    date = line[time_index]
    net_id = line[user_index]
    homework_num = line[assign_index]
    lateday_num = line[days_index]

    #(net_id, date, homeowork number, number of latedays)
    cur_tuple = date, net_id, lateday_num, homework_num

    if net_id in cur_map:
      old_date = cur_map[net_id][1]
    if date - old_date > 0:
        cur_map[net_id] = cur_tuple
    else:
      cur_map[net_id] = cur_tuple

for key in cur_map:    
  print sendMail(cur_map[key][time_index], cur_map[key][user_index], cur_map[key][days_index], cur_map[key][assign_index])
  print "Done sending mail..."
  print "Error summary:"
  print "\t" + str(errors) + " errors"
