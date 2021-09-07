#import modules
import os
from colorama import init,Fore,Back
from random import randint

#logo
def logo():
	print(Fore.GREEN)
	print("""

	██████╗░░█████╗░██╗░░██╗░░░░░░██████╗░░█████╗░░██████╗
	██╔══██╗██╔══██╗██║░░██║░░░░░░██╔══██╗██╔══██╗██╔════╝
	██████╔╝███████║███████║█████╗██║░░██║██║░░██║╚█████╗░
	██╔══██╗██╔══██║██╔══██║╚════╝██║░░██║██║░░██║░╚═══██╗
	██║░░██║██║░░██║██║░░██║░░░░░░██████╔╝╚█████╔╝██████╔╝
	╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░╚═════╝░░╚════╝░╚═════╝░
		""")
	time.sleep(3)
	main_menu()

#main menu
def main_menu():
	print("""
DDos[1]       bomber[2]      fishing[3]
		""")
	vib_menu = input()
	if vib_menu == "1":
		ddos()
	elif vib_menu == "2":
		bomber()
	elif vib_menu == "3":
		fishing()
#ddos
def  ddos():
	password = 'test'
	pas = input("password: ")
def  bomber():
	password = 'test'
	pas = input("password: ")
def  fishing():
	password = 'test'
	pas = input("password: ")
