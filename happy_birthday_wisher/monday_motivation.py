import datetime as dt
import random as rd
import smtplib as sm
quotes = []
my_email = "jvijayabalaji03082002@gmail.com"
password = "rxkaopiplraxrufn"

with open("quotes.txt") as data_file:
    quotes = data_file.readlines()

today = dt.datetime.now()
weekday = today.weekday()
if weekday == 2:
    random_quote = rd.choice(quotes)
    with sm.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Monday motivation\n\n{random_quote}")


