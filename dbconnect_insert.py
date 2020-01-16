import mysql.connector


def connectorinsert(query, values):
    mydb = mysql.connector.connect(
      host="localhost",
      user="frisdrank",
      passwd="V8WDra*57ANz",
      database="frisdrankautomaat"
    )
    cursor = mydb.cursor()
    cursor.execute(query, values)
    mydb.commit()
    mydb.close()

