import sqlite3
carData= [
    (1,'Audi',52642),
    (2,'Mercedes',57127),
    (3,'Nano',52134),
    (4,'Mahendhra',54231),
    (5,'Volvo',900023),
    (6,'Hummer',414000),
    (7,'Bentley',3500000)
    ]
con = sqlite3.connect('mtica.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT,Name TEXT,Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)",carData)
con.commit()
con.close()
print("Values inserted.")
    
