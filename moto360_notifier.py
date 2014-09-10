import urllib
import urllib2
import smtplib
from sys import argv
import socket
import threading
import time

username = argv[2]
password = argv[3]

# Flags to represent what color the user wants to be notified about
BLACK_FLAG = False
GRAY_FLAG = False

# URLs to the product page
black_url = "https://play.google.com/store/devices/details/Moto_360_Black_Leather?id=motorola_moto_360_leather_black"
gray_url = "https://play.google.com/store/devices/details/Moto_360_Gray_Leather?id=motorola_moto_360_leather_gray"

# HTML element only present when the watch is NOT available
not_available = '<div class="not-available">'

sender = username
receivers = argv[4]
black_available_message = """Subject: Black Moto360 is Available!

Hello, {0} the Moto360 in black is currently available!!!!!!

Grab it here: goo.gl/Vm6pzw""".format(argv[2])

gray_available_message = """Subject: Gray Moto360 is Available!

Hello, {0} the Moto360 in gray is currently available!!!!!!

Grab it here: goo.gl/1FJM8p""".format(argv[2])


if argv[1] == "black" or argv[1] == "Black":
  req = urllib2.Request(black_url)
  BLACK_FLAG = True

if argv[1] == "gray" or argv[1] == "Gray":
  req = urllib2.Request(gray_url)
  GRAY_FLAG = True


# Check page for availability
while True:
  response = urllib2.urlopen(req)

  page = response.read()

  # If available (not-available div is NOT on page), send the user an
  # email to notify them.
  if not not_available in page:

    # watch is available, change message to correspond with the right color
    if BLACK_FLAG: message = black_available_message
    if GRAY_FLAG: message = gray_available_message

    # send email
    try:
      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(username,password)
      server.sendmail(sender, receivers, message)
      server.quit()

      print "Successfully sent email"
    except smtplib.SMTPException:
      print "Error: unable to send email"
    except socket.error:
      print "Socket Error: unable to send email"

    print "{0} Moto360 is available right now!".format(argv[1])
  else:
    print "{0} Moto360 not available right now".format(argv[1])

  # Repeat every x seconds
  time.sleep(float(argv[5]))
