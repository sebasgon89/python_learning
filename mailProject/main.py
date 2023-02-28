import smtplib

my_email = "sgonzalezgoetz@gmail.com"
my_password = "uihztddefurzmxgi"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="seba3789@gmail.com", msg="Test")

# import datetime as dt
# datetime = dt.datetime
# print(datetime.now())

import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open('angela/quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print (quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="seba3789@gmail.com",
            msg=f"Subject: Motivation\n\n{quote}"
        )
