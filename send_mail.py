import glob
import os
import smtplib
import random
import sys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
gmail_user = 'aidendawes.spammail@gmail.com'
gmail_password = '9meidoring'
imagepath = str(sys.path[0]) + "/images/"
print(imagepath)

imageNames = os.listdir(path=imagepath)
index = random.randint(0, len(imageNames)-1)
name = imageNames[index]
l = len(name)
qname = ""
aname = ""
if(name[l-7: l] == "-ms.png"):
    aname = name
    qname = name[0:l-7] + ".png"
else:
    aname = name[0:l-4] + "-ms.png"
    qname = name
print(aname, qname)


def send_mail(address):
    with open(imagepath+str(qname), 'rb') as f:
        img_data = f.read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Daily Math Question'
    msg['From'] = 'e@mail.cc'
    msg['To'] = address

    text = MIMEText("")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(imagepath+str(qname)))
    msg.attach(image)
    with open(imagepath+str(aname), 'rb') as f:
        img_data = f.read()
    image = MIMEImage(img_data, name=os.path.basename(imagepath+str(aname)))
    msg.attach(image)
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(gmail_user, gmail_password)
    s.sendmail("aidendawes.spammail@gmail.com",
               address, msg.as_string())
    s.quit()


send_mail("aidendawes@gmail.com")
