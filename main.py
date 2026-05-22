import smtplib

my_email = "testchoudhury05@gmail.com"
password = "ixlgyccxapzezxop"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="paranchoudhury25@outlook.com",msg="Hello Dear")
connection.close()