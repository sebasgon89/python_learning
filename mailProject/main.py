import smtplib

my_email = "sgonzalezgoetz@gmail.com"
my_password = "uihztddefurzmxgi"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="seba3789@gmail.com", msg="Test")