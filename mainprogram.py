import time
import RPi.GPIO as GPIO
from getpass import getpass
from multiprocessing import Process
from dbconnect import connector
from sendmail import mailfunctie
from datetime import datetime
from dbconnect_insert import connectorinsert
from dbconnect_update import connectorupdate

#RASPBERRY PI GPIO PIN SETTINGS
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def gettime():
	time = datetime.now()
	return time.strftime("%H:%M:%S")

def getdate():
	date = datetime.today()
	return date.strftime("%Y:%m:%d")	

def maintenance():
	mailfunctie("Maintenance herinnering frisdrankautomaat " + getdate(), "Beste gebruiker,/n er is een maand verstreken. Wij willen u aanraden om uw frisdrankautomaat te reinigen / onder maintenance te nemen.\nVoor de nieuw onderdelen kunt u op onze website terecht.\nDeze mail is automatisch gegenereerd", office365Usr, office365Pass)

def voorraadcontrole():
	voorraad = connector("SELECT * FROM voorraad")
	for x in voorraad:
		product_id = x[0]
		product_naam = x[1]
		product_aantal = x[2]
		product_prijs = x[3]
		if product_aantal < 4:
			mailfunctie("Product bijna op: "+product_naam, "Beste gebruiker,\n uw "+ product_naam +" is bijna op.\n Er zijn nog maar "+ str(product_aantal) +" over. Vul deze zo snel mogelijk bij.\n Dit is een automatisch gegenereerde e-mail.", office365Usr, office365Pass)

			
def cocacolaLight():
	connectorinsert("INSERT INTO mutatie (productid, datum, tijd) VALUES (%s, %s, %s)", (123457, getdate(), gettime()))
	voorraad = connector("select voorraadaantal FROM voorraad WHERE productid = 123457")
	for x in voorraad:
		y = int(''.join(map(str,x)))
	updatevoorraad = y-1
	print(updatevoorraad)
	connectorupdate("UPDATE voorraad SET voorraadaantal = '%s' WHERE productid = 123457" % (updatevoorraad))
		
def cocacolaRegular():
	connectorinsert("INSERT INTO mutatie (productid, datum, tijd) VALUES (%s, %s, %s)", (123456, getdate(), gettime()))
	voorraad = connector("select voorraadaantal FROM voorraad WHERE productid = 123456")
	for x in voorraad:
		y = int(''.join(map(str,x)))
	updatevoorraad = y-1
	print(updatevoorraad)
	connectorupdate("UPDATE voorraad SET voorraadaantal = '%s' WHERE productid = 123456" % (updatevoorraad))

def cocacolaZero():
	connectorinsert("INSERT INTO mutatie (productid, datum, tijd) VALUES (%s, %s, %s)", (123458, getdate(), gettime()))
	voorraad = connector("select voorraadaantal FROM voorraad WHERE productid = 123458")
	for x in voorraad:
		y = int(''.join(map(str,x)))
	updatevoorraad = y-1
	print(updatevoorraad)
	connectorupdate("UPDATE voorraad SET voorraadaantal = '%s' WHERE productid = 123458" % (updatevoorraad))

def fantaOrange():
	connectorinsert("INSERT INTO mutatie (productid, datum, tijd) VALUES (%s, %s, %s)", (123459, getdate(), gettime()))
	voorraad = connector("select voorraadaantal FROM voorraad WHERE productid = 123459")
	for x in voorraad:
		y = int(''.join(map(str,x)))
	updatevoorraad = y-1
	print(updatevoorraad)
	connectorupdate("UPDATE voorraad SET voorraadaantal = '%s' WHERE productid = 123459" % (updatevoorraad))

def fantaCassis():
	connectorinsert("INSERT INTO mutatie (productid, datum, tijd) VALUES (%s, %s, %s)", (123460, getdate(), gettime()))
	voorraad = connector("select voorraadaantal FROM voorraad WHERE productid = 123460")
	for x in voorraad:
		y = int(''.join(map(str,x)))
	updatevoorraad = y-1
	print(updatevoorraad)
	connectorupdate("UPDATE voorraad SET voorraadaantal = '%s' WHERE productid = 123460" % (updatevoorraad))

def iceteaSparkling():
	connectorinsert("INSERT INTO mutatie (productid, datum, tijd) VALUES (%s, %s, %s)", (123461, getdate(), gettime()))
	voorraad = connector("select voorraadaantal FROM voorraad WHERE productid = 123461")
	for x in voorraad:
		y = int(''.join(map(str,x)))
	updatevoorraad = y-1
	print(updatevoorraad)
	connectorupdate("UPDATE voorraad SET voorraadaantal = '%s' WHERE productid = 123461" % (updatevoorraad))

office365Usr = input("Geef hier je gebruikersnaam op: ")
office365Pass = getpass("Geef hier je Office365 password op: ")

def voorraadloop():
	while True:
		if GPIO.input(8) == True:
			cocacolaRegular()
			time.sleep(1)

		elif GPIO.input(10) == True:
			cocacolaLight()
			time.sleep(1)

		elif GPIO.input(12) == True:
			cocacolaZero()
			time.sleep(1)

		elif GPIO.input(16) == True:
			fantaOrange()
			time.sleep(1)

		elif GPIO.input(18) == True:
			fantaCassis()
			time.sleep(1)

		elif GPIO.input(22) == True:
			iceteaSparkling()
			time.sleep(1)
	
def controleloop():
	while True:
		voorraadcontrole()
		time.sleep(1800)

def maintenanceloop():
	while True:
		maintenance()
		time.sleep(2592000)
		#sleep timer van een maand, na deze timer wordt er een mail verstuurd ter herinnering van maintenance.
		
if __name__ == '__main__':
	Process(target=voorraadloop).start()
	Process(target=controleloop).start()
	Process(target=maintenanceloop).start()
