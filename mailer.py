from bookkeeping import *
from subprocess import Popen, PIPE

def sendMail(message, subject, to):
  echoed = Popen(['echo', message], stdout=PIPE)
  Popen(['mail', '-s', subject, '-r', 'cse331-staff@cs.washington.edu', to], stdin=echoed.stdout, stdout=PIPE)

def summary(total):
  string = "Summary of all requests: \n"
  for record in total:
    string += str(record) + "\n"
  return string

def sendKidMail(total, accepted):
  days = str(accepted.days)  #easy to concatenate as string
  subject = "Requested " + accepted.days + " lateday(s)"
  message = """Dear """ + accepted.user + """,

  You requested """ + accepted.days + """ lateday(s) for """ + accepted.assignment + """ at """ + accepted.timestamp + """. Please notify us immediately at cse331-staff@cs.washington.edu if this is incorrect.

""" + summary(total) + """ 
  Warning: This email is only to inform you how many latedays you requested on the Google form. Please ensure that you actually have the number of lateday(s) you requested left, and that the requested assignment was still open for latedays at the date/time indicated.
  
  Thanks,
  CSE 331 staff"""
  
  sendMail(message, subject, accepted.user);
  #print(message, subject, accepted.user);

def sendStaffMail(idToInfo, homework, failure_list):
  message = "Late days requested for " + homework + ":\n\n"
  for user, info in idToInfo.items():
    message += str(info) + "\n"
  if len(failure_list) > 0:
    message += "\nCould not send email to these lines in the csv file:\n"
    for fail in failure_list:
      message += fail + "\n"
  else:
    message += "\nNo errors occurred while parsing the file\n"
  
  subject = "Summary of late day requests for " + homework

  sendMail(message, subject, "cse331-staff@cs.washington.edu")
  #print "Called sendMail", message, subject
