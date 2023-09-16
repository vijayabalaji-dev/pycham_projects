import smtplib

my_email = "jvijayabalaji03082002@gmail.com"
password = "rxkaopiplraxrufn"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="balajigcp23@gmail.com",
                    msg="Subject:hello from vijay\n\nHello someone")
connection.close()
