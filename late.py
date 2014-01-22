from subprocess import Popen, PIPE
import csv
import sys

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

time_index = 0
user_index = 1
days_index = 2
assign_index = 3

errors = 0

if len(sys.argv) != 2 or (not sys.argv[1].endswith(".csv")):
  print "Usage: python late.py <file.csv>"
else:
  f = csv.reader(open(sys.argv[1]))
  print "Sending mail now..."
  for line in f:
    if len(line) != 4:
      print "Error: malformed line:", line
      errors += 1
      continue
    print sendMail(line[time_index], line[user_index], line[days_index], line[assign_index])
  print "Done sending mail..."
  print "Error summary:"
  print "\t" + str(errors) + " errors"
