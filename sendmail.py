import smtplib
from getpass import getpass


def mailfunctie(SUBJECT, TEXT):

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    office365Usr = input("Geef hier je gebruikersnaam op ")
    office365Pass = getpass("Geef hier je Office365 password op ")

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(office365Usr, office365Pass)
    server.sendmail(office365Usr,'toseijs@gmail.com',message)
    server.quit()
