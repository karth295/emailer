from bookkeeping import *

def sendMail(message, subject, to):
  echoed = Popen(['echo', message], stdout=PIPE)
  Popen(['mail', '-s', subject, '-r', 'cse331-staff@cs.washington.edu', to], stdin=echoed.stdout, stdout=PIPE)

def sendKidMail(info):
  days = str(info.days)  #easy to concatenate as string
  subject = "Requested " + info.days + " lateday(s)"
  message = """Dear """ + info.user + """,

  You requested """ + info.days + """ lateday(s) for """ + info.assignment + """ at """ + info.timestamp + """. Please notify us immediately at cse331-staff@cs.washington.edu if this is incorrect.

  Warning: This email is only to inform you how many latedays you requested on the Google form. Please ensure that you actually have the number of lateday(s) you requested left, and that the requested assignment was still open for latedays at the date/time indicated.
  
  Thanks,
  CSE 331 staff"""
  
  sendMail(message, subject, info.user);

def sendStaffMail(idToInfo, homework, failure_list):
  message = "Late days requested for " + homework + ":\n"
  for user, info in idToInfo.items():
    message += str(info) + "\n"
  if len(failure_list) > 0:
    message += "Could not send email to these lines in the csv file:\n"
    for fail in failure_list:
      message += fail + "\n"
  else:
    message += "No errors occurred while parsing the file\n"
  
  subject = "Summary of late day requests for " + homework

  sendMail(message, subject, "cse331-staff@cs.washington.edu")
