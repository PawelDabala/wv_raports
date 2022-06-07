import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)

email_addr = 'reportswvmd@gmail.com'
email_passwd = 'vvbyicqzkayveghe'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='pdabala@gmail.com', msg="Sent from my IDE. Hehe")

connection.close()