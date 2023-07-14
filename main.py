
import sqlite3
con = sqlite3.connect('callcars.db')
cur = con.cursor()

con.execute("CREATE TABLE IF NOT EXISTs cars (name TEXT, year INTEGER, engine TEXT, transmission TEXT)")
cur.execute("DELETE FROM cars")
data = [('Camry', 2020, '2.5L Inline-4', '8-speed automatic'),
        ('Corolla', 2020, '1.8L Inline-4', 'CVT'),
        ('Prius', 2020, '1.8L Inline-4 + Electric Motor', 'CVT'),
        ('RAV4', 2020, '2.5L Inline-4', '8-speed automatic'),
        ('Highlander', 2020, '3.5L V6', '8-speed automatic'),
        ('Tacoma', 2020, '3.5L V6', '6-speed automatic'),
        ('86', 2020, '2.0L Flat-4', '6-speed manual'),
        ('Supra', 2020, '3.0L Inline-6', '8-speed automatic'),
        ('Camry', 2019, '2.5L Inline-4', '8-speed automatic'),
        ('Corolla', 2019, '1.8L Inline-4', 'CVT'),
        ('Prius', 2019, '1.8L Inline-4 + Electric Motor', 'CVT'),
        ('RAV4', 2019, '2.5L Inline-4', '8-speed automatic'),
        ('Highlander', 2019, '3.5L V6', '8-speed automatic'),
        ('Tacoma', 2019, '3.5L V6', '6-speed automatic'),
        ('86', 2019, '2.0L Flat-4', '6-speed manual'),
        ('Supra', 2019, '3.0L Inline-6', '8-speed automatic'),
        ('Cruze', 2020, '1.4L Turbocharged Inline-4', '6-speed automatic'),
        ('Malibu', 2020, '1.5L Turbocharged Inline-4', 'CVT'),
        ('Impala', 2020, '3.6L V6', '6-speed automatic'),
        ('Equinox', 2020, '1.5L Turbocharged Inline-4', '6-speed automatic'),
        ('Traverse', 2020, '3.6L V6', '9-speed automatic'),
        ('Tahoe', 2020, '5.3L V8', '10-speed automatic'),
        ('Suburban', 2020, '5.3L V8', '10-speed automatic'),
        ('Camaro', 2020, '6.2L V8', '10-speed automatic'),
        ('Altima', 2020, '2.5L Inline-4', 'CVT'),
        ('Sentra', 2020, '2.0L Inline-4', 'CVT'),
        ('Maxima', 2020, '3.5L V6', 'CVT'),
        ('Rogue', 2020, '2.5L Inline-4', 'CVT'),
        ('Murano', 2020, '3.5L V6', 'CVT'),
        ('Pathfinder', 2020, '3.5L V6', 'CVT'),
        ('Frontier', 2020, '3.8L V6', '9-speed automatic'),
        ('370Z', 2020, '3.7L V6', '7-speed automatic')]



cur.executemany('''INSERT INTO cars VALUES (?,?,?,?)''', data)
con.commit()

item = cur.execute("SELECT * FROM cars")

for row in item:
    print(row)

cur.close()
con.close()

