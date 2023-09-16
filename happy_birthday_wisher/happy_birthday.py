import datetime as dt
import random as rd
import smtplib as sm
import time

import pandas as pd
import schedule

letters = []
my_email = "jvijayabalaji03082002@gmail.com"
password = "rxkaopiplraxrufn"

with open("letter_templates/letter_1.txt") as letter1:
    letters.append(letter1.read())
with open("letter_templates/letter_2.txt") as letter2:
    letters.append(letter2.read())
with open("letter_templates/letter_3.txt") as letter3:
    letters.append(letter3.read())

dataframe = pd.read_csv("birthdays.csv")
data = dataframe.to_dict(orient="records")

today = dt.datetime.now()
today_month = today.month
today_date = today.day


def send_mail():
    for user in data:
        if user['month'] == today_month and user['day'] == today_date:
            letter = rd.choice(letters)
            letter_with_name = letter.replace("[NAME]", user['name'])
            with sm.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=user['email'],
                                    msg=f"Subject:Happy Birthday!\n\n{letter_with_name}")


schedule.every().day.at("11:21").do(send_mail)
while True:
    schedule.run_pending()
    time.sleep(1)
