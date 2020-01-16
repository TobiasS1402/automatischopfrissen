import mysql.connector


def connectorupdate(query):
    mydb = mysql.connector.connect(
      host="localhost",
      user="frisdrank",
      passwd="V8WDra*57ANz",
      database="frisdrankautomaat"
    )
    cursor = mydb.cursor()
    cursor.execute(query)
    mydb.commit()
    mydb.close()

