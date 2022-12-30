import datetime
import requests
from bs4 import BeautifulSoup

date = datetime.datetime.now()

day = str(date.day - 1)
month = str(date.month)
year = str(date.year)

def getData(rule, days, count):
    html = 'https://rongbachkim.com/thongke.html?days='+str(days)+'&to='+day+'%2F'+month+'%2F'+year+'&range=00-99&sortby=1&mode=0'
    x = requests.get(html)
    html_doc = x.text
    soup = BeautifulSoup(html_doc)
    table = soup.find('table', attrs={'id':'thongketbl'})
    text = 'luat ' + str(rule) + ': ' + str(days) + ' ngay ve <= ' + str(count) + ' lan: '
    for enum, row in enumerate(table.find_all('td')[1:101]):
        if int(row.get_text()) <= count:
            text += str(enum) + ' (' + row.get_text() + ' lan), '
    text += '\n'
    return text

rule1 = getData(1, 25, 0)
rule2 = getData(2, 16, 0)
rule3 = getData(3, 63, 5)
rule4 = getData(4, 28, 1)

import smtplib
import ssl
from email.message import EmailMessage
email_sender = 'automaticemailrbk@gmail.com'
email_password = 'avxidqyoumgxhxgt'
email_receiver = 'nltlam2001@gmail.com'
subject = 'Lo to ngay ' + day + '' + month + '/' + year
body = rule1 + rule2 + rule3 + rule4
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())