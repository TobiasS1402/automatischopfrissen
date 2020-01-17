import smtplib

def mailfunctie(SUBJECT, TEXT, office365Usr, office365Pass):

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(office365Usr, office365Pass)
    server.sendmail(office365Usr,'frisdrankautomaat@hogeschoolutrecht.onmicrosoft.com',message)
    server.quit()
