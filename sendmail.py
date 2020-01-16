import smtplib


def mailfunctie(SUBJECT, TEXT):

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    
    office365Pass = input("Geef hier je Office365 password op")
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login("tobias.seijsener@student.hu.nl", office365Pass)
    server.sendmail('tobias.seijsener@student.hu.nl','toseijs@gmail.com',message)
    server.quit()
