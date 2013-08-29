##--Michael duPont (flyinactor91.com)
##--This function creates and sends an email with attachments

import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(sender , password , reciever , subject , text , files=[]):
    if isinstance(reciever, basestring): reciever = [reciever]
    if isinstance(files, basestring): files = [files]

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(reciever)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(f)))
        msg.attach(part)

    smtpserver = smtplib.SMTP('smtp.gmail.com' , 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(sender , password)
    smtpserver.sendmail(sender, reciever, msg.as_string())
    smtpserver.close()
