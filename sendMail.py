import smtplib
from email.mime.text import MIMEText

def sendOtp(OTP, email):
    #TODO Crypt the email content and set correct headers
    # can only send to emails like : remi.gasc@etu.unilim.fr
    me = 'dennis@debest.fr'
    print(email)

    msg = MIMEText(str(OTP))
    msg['Subject'] = 'OTP'
    msg['From'] = me
    msg['To'] = email
    s = smtplib.SMTP('smtp.unilim.fr')
    s.set_debuglevel(1)
    s.sendmail(me, email, msg.as_string())
    s.quit()