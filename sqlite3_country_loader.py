# import countries data from csv file to sqlite database
import csv, sqlite3

con = sqlite3.connect("country.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS country (country_name, capital, capital_population integer);")

with open('country.csv', encoding='utf-8-sig') as f:
    to_db = [(i['country_name'], i['capital'], i['capital_population']) for i in csv.DictReader(f)]

cur.executemany("INSERT INTO country (country_name, capital, capital_population) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()