
import smtplib as smtp

connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
    
email_addr = 'kaldaterohit2611@gmail.com'
email_passwd = 'wxwg zicw tqeo ubnr'
connection.login(email_addr, email_passwd)
connection.sendmail(from_addr=email_addr, to_addrs='gmaheswaranmca@gmail.com', msg="Sent from my Rohit ")
connection.close()
print('Mail sent successfully')