account_sid = "-"
auth_token = "-"

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import smtplib
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_text(self, dep_city, dep_airport, ar_city, ar_airport, price, first_day, last_day):
        proxy_client = TwilioHttpClient()
        # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Important message! The flight from {dep_city}-{dep_airport} to {ar_city}-{ar_airport} has a new lowest price of ${price}. From {first_day} to {last_day}",
            from_="-",
            to="-"
        )
        print(message.status)

    def send_email(self, dest_email, my_email, password, dep_city, dep_airport, ar_city, ar_airport, price, first_day, last_day):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=dest_email,
            msg=f"Subject: Get ready to fly!\n\nGOOD NEWS! The flight from {dep_city}-{dep_airport} to {ar_city}-{ar_airport} has a new lowest price of ${price}. From {first_day} to {last_day}"
        )
