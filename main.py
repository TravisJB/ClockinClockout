# Dependencies.
import os
import sys
from time import sleep

# Global variables/settings. (You can change these.)
NAME = 'Clock-in/Clock-out' # Name of the program, you can change this if you really want to.
COMPANY = 'Example Inc.' # Company name, change this to your company/business.
VERSION = '1.0-dev' # Current version of the program.
AUTHOR = 'Travis B.' # The author of the program.
ADMIN_PASSWORD = 'password' # The administrative password. You can set this to anything you choose. This password is used whenever someone tries to use a command that you set to be admin only.
EXIT_ADMIN = 'true' # Should exiting the program require the admin password? (Recommended: true) [true/false]


# Definitions.
def start():
	os.system('cls')
	print()
	print(COMPANY + " | " + NAME + " | Version: " + VERSION)
	print()
	command = input("What would you like to do?\n>> ")
	if command == 'in':
		clockin()
	if command == 'make':
		make()
	if command == 'exit':
		exit()
	if command == 'help':
		help()
	else:
		print("Unknown command, please type 'help' for a list of all commands.")
		os.system("pause")
		start()


def clockin():
	with open('ids.txt', 'r') as file:
		for line in file:
			userid = input('What is your ID: ')
			if userid in line:
				matchedLine = line
				print(line)
				sleep(1)
			else:
				print('error')
				sleep(2)
				start()


def make():
	print('test')
	start()


def exit():
	if EXIT_ADMIN == 'true':
		password = input("Enter admin password: ")
		if password == ADMIN_PASSWORD:
			print('Exiting program.')
			sys.exit()
		else:
			start()
	else:
			print('Exiting program.')
			sys.exit()

def help():
	print()	
	print('Command List:')
	print('in - Prompts the clock-in command.')
	print('out - Prompts the clock-out command.')
	print()
	os.system("pause")
	start()



exitvalues = ['true', 'false']

if EXIT_ADMIN not in exitvalues:
	print('Error in the settings, please check the code.')
	sys.exit()
else:
	pass

start()