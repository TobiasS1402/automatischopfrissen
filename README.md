# automatischopfrissen
PTW project automatisch opfrissen. Een repository door Tobias.
Op dit moment zijn er enkele files, die ga ik hieronder toelichten.

dbconnect.py: standard database verbinding voor SELECT queries.

dbconnect_insert.py: standard database verbinding voor INSERT queries.

dbconnect_update.py: stanard database verbinding voor UPDATE queries.

sendmail.py: functie voor het verzenden van mail, deze mailberichten kunnen een custom header en body hebben. Afhankelijk van de reden van de mail.

mainprogram.py: het hoofdprogramma. Deze roept de bovenstaande functies aan en zal verder het geheel laten draaien.
