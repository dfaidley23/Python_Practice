import smtplib, ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465


    username = "dmaxar3@gmail.com"
    password = "1q2w3e4r!Q@W#E$R"

    receiver = "dmaxar3@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)