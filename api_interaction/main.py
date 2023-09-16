import requests
import smtplib



MY_LAT = 12.971599
MY_LONG = 77.594566
MY_EMAIL = "jvijayabalaji03082002@gmail.com"
MY_PASSWORD = "rxkaopiplraxrufn"

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])

iss = (latitude, longitude)

if latitude <= MY_LAT-5 or latitude >= MY_LAT+5 and longitude <= MY_LONG-5 or longitude >= MY_LONG+5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Satalite!!!!\n\nThe ISS satalaite is above you\nyours{MY_LAT}, {MY_LONG}\nSatalite: {latitude}, {longitude}")
        print("Mail sent successfully")

    
