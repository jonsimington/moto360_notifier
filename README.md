moto360_notifier
================

Purpose
-------

This script notifies the user at a specified e-mail address when the watch of their choosing is available on Google Play


Usage
-----

This script takes in 5 arguments in this order:

* color of watch you want to be notified about (gray/black)
* e-mail address to send e-mails from (I use my own email for simplicity)
* password for e-mail address entered in argument 2
* e-mail address to send notification e-mail to
* how often you want to check the webpage (in seconds)
    NOTE: IF YOU SET THIS TO A SMALL NUMBER AND THE WATCH IS AVAILABLE, YOU WILL GET A BUNCH OF EMAILS


Example terminal command to run script: ``python moto360_notifier.py black from@from.com <password> to@to.com 600``

The above command will check the availability of the black Moto360 on Google Play every 600 second (10 minutes).  If the watch is available, the e-mail notification will be sent to to@to.com from from@from.com.

Note
----

Currently, this script only supports sending e-mail from gmail accounts, but it can send e-mail to any e-mail account.
