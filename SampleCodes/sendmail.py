from email.mime.text import MIMEText
from subprocess import Popen, PIPE

msg = MIMEText("Here is the body of my message")
msg["From"] = "young.park"
msg["To"] = "youngspark@outlook.com"
msg["Subject"] = "Testing Result"
p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
p.communicate(msg.as_string())
