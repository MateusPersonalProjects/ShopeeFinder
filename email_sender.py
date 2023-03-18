import smtplib
import time


my_email = "your email"
password = "your password"


def send_email(data):

    for item in data:
        message = f"New Item alert!!!!\n{item['title']} for R${item['price']}\nGet it in here: {item['url']}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="amateussteam@gmail.com",
                msg=f"Subject: Shopee Item Alert!!! \n\n{message}"
            )
        time.sleep(5)
        