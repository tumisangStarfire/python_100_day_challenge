import smtplib

email = "mlamar347@gmail.com"
password = "bqokywyumqwfbabv"

try:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(email, password)
    connection.sendmail(
        from_addr=email,
        to_addrs="tumisangmogotsi@outlook.com",
        msg="Subject:Python Tests\n\n Hello sending from python."
    )
    connection.close()
except smtplib.SMTPException as err:
    print("Could not send email view message below")
    print(err)
