import socket
import subprocess
import pyfiglet 
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier 

def ping():
	text = pyfiglet.figlet_format("Web Ping")
	print(text)

	i = input("Enter an IP or Website name : ")
	subprocess.call("ping "+i ,shell=True)

def port():
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	text = pyfiglet.figlet_format("Port Scanner")
	print(text)

	host = input("Enter the IP : ")
	port = int(input("Enter the port number : "))

	def portScanner(port):
		if s.connect_ex((host, port)):
			print("The port is closed .")
		else:
			print("The port is open ")

	portScanner(port)

def phone():
	text = pyfiglet.figlet_format("Phone Tracker")
	print(text)

	number = str(input("Enter the number with country code : "))
	ch_number = phonenumbers.parse(number,"CH")
	print ("This number is from : "+geocoder.description_for_number(ch_number, "en"))

	service_number = phonenumbers.parse(number, "RO")
	print("Service Provider of this number is : "+carrier.name_for_number(service_number,"en"))


loop = True
while loop:

	text = pyfiglet.figlet_format("EHTOOLS PYTHON")
	print(text)

	print("1.Web Ping")
	print("2.Port Scanner")
	print("3.Phone Tracker")
	print("4.Exit")
	option = int(input("\nEnter Your Choice : "))

	if option == 1:
		ping()
	elif option == 2:
		port()
	elif option == 3:
		phone()
	elif option == 4:
		print("EXIT")
		loop = False
	else:
		print("Please Enter a Valid Input!")




