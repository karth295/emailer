from subprocess import Popen, PIPE
import csv
import sys
import datetime
from bookkeeping import *
from mailer import *

time_index = 0
user_index = 1
days_index = 2
assign_index = 3

errors = 0
error_list = []

if len(sys.argv) != 3 or (not sys.argv[1].endswith(".csv")):
  print "Usage: python late.py <file.csv> <homework_number>"
  exit()

target_hw = sys.argv[2]
cur_map = {}
f = csv.reader(open(sys.argv[1]))
print "Parsing file..."
for line in f:
  if len(line) != 4:
    error_list.append(line)
    errors += 1
    continue
  #while iterating over the lines, add to map (check if it exists before)
  date = line[time_index]
  net_id = line[user_index]
  homework_num = line[assign_index]
  lateday_num = line[days_index]
  if homework_num != target_hw:
    continue
  cur_info = bookkeeper(date, net_id, lateday_num, homework_num)

  sendKidMail(cur_info)
  #print "Called sendKidMail", cur_info

  #Only keep the latest submission in the map
  if net_id in cur_map and date <= cur_map[net_id].timestamp:
    continue
  else:
    cur_map[net_id] = cur_info

print "Sending results to course staff..."
sendStaffMail(cur_map, target_hw, error_list)

print "Done sending mail..."
print "Error summary:"
print "\t" + str(errors) + " errors"
