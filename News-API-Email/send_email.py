import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 445

    username = "@gmail.com"
    password = "gmail password"

    receiver = "@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)