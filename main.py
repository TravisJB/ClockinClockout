# Dependencies.
import os
import sys
import re
from time import sleep

# Global variables/settings. (You can change these.)
NAME = 'Clock-in/Clock-out' # Name of the program, you can change this if you really want to.
COMPANY = 'Example Inc.' # Company name, change this to your company/business.
VERSION = '1.0-dev' # Current version of the program.
AUTHOR = 'Travis B.' # The author of the program.
ID_FILE = 'ids.txt' # This is the file that all the IDs are in. If you want to change the file name you can do so here. (You must keep the '.txt' extension.)
ADMIN_PASSWORD = 'password' # The administrative password. You can set this to anything you choose. This password is used whenever someone tries to use a command that you set to be admin only.
EXIT_ADMIN = 'true' # Should exiting the program require the admin password? (Recommended: true) [true/false]
# Global variables. (Do not change these as you could break the program if you don't know what you are doing.)
GLOBAL_COMMANDS = ['in', 'out', 'make', 'exit', 'help']


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
	if command not in GLOBAL_COMMANDS:
		print("Unknown command, please type 'help' for a list of all commands.")
		os.system("pause")
		start()


def clockin():
	userid = input('What is your ID: ')
	data = open(ID_FILE).readlines()
	if re.match(r"^[0-9]*$", userid):
		if len(userid) == 4:
			found_line = None
			for data_line in data:
				line = data_line.strip()
				if userid in line:
					found_line = line
					break
		else:
			print('You must have only 4 numbers in your ID, cancelling.')
			os.system("pause")
			start()
	else:
		print('You can only have numbers in your input, cancelling.')
		os.system("pause")
		start()

	if found_line:
		print(found_line)
		os.system("pause")
		start()
	else:
		print('This ID is not registered in the database, cancelling.')
		os.system("pause")
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


os.system('cls')

exitvalues = ['true', 'false']
if EXIT_ADMIN not in exitvalues:
	print('The setting "EXIT_ADMIN" is does not have a valid value, exiting.')
	sys.exit()
else:
	print('EXIT_ADMIN passed.')

if not os.path.isfile(ID_FILE):
	print('ID file "' + ID_FILE + '" does not exist, exiting.')
	sys.exit()
else:
	print('ID_FILE passed.')

if GLOBAL_COMMANDS == '':
	print('Global commands are blank, cannot start the program.')
else:
	print('GLOBAL_COMMANDS passed.')

print()
print('Settings:')
print('Name: '+ NAME)
print('Company: '+ COMPANY)
print('Version: '+ VERSION)
print('Author = '+ AUTHOR)
print('ID File: '+ ID_FILE)
print('Admin Password: '+ ADMIN_PASSWORD)
print('Exit is an admin command: '+ EXIT_ADMIN)
print('Global Commands (string): '+ str(GLOBAL_COMMANDS))
print()
print('Settings have been verified and the program is starting.')
sleep(3)

start()