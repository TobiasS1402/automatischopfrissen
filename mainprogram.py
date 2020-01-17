import time
import RPI.GPIO as GPIO
from dbconnect import connector
from sendmail import mailfunctie
from datetime import datetime
from dbconnect_insert import connectorinsert
from dbconnect_update import connectorupdate

def gettime():
	time = datetime.now()
	return time.strftime("%H:%M")

def getdate():
	date = datetime.today()
	return date.strftime("%Y:%m:%d")	

def voorraadcontrole():
	voorraad = connector("SELECT * FROM voorraad")
	for x in voorraad:
		product_id = x[0]
		product_naam = x[1]
		product_aantal = x[2]
		product_prijs = x[3]
		if product_aantal < 4:
			mailfunctie("Product bijna op: "+product_naam, "Beste gebruiker,\n uw "+ product_naam +" is bijna op.\n Er zijn nog maar "+ str(product_aantal) +" over. Vul deze zo snel mogelijk bij.\n Dit is een automatisch gegenereerde e-mail.")

			
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

	
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
        if GPIO.input(8) == True:
                voorraadcontrole()
                time.sleep(1)

        elif GPIO.input(10) == True:
                cocacolaRegular()
                time.sleep(1)

        elif GPIO.input(12) == True:
                cocacolaLight()
                time.sleep(1)

        elif GPIO.input(16) == True:
                cocacolaZero()
                time.sleep(1)

        elif GPIO.input(18) == True:
                #cocacolaLight()
                time.sleep(1)

        elif GPIO.input(22) == True:
                #cocacolaZero()
                time.sleep(1)
