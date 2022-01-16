import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(os.getenv("USER_EMAIL"), os.getenv("USER_PASSWORD"))
server.sendmail("ccy786@gmail.com", "ccy786@gmail.com", "Testing python code")

server.quit()
