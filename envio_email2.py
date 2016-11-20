#!/usr/bin/python
import smtplib
from smtplib import SMTPException

try:
     smtp = smtplib.SMTP('smtp.gmail.com', 587)
     smtp.ehlo()
     smtp.starttls()
     smtp.ehlo()
     smtp.login('seuemail@domain.com', 'suasenha')
 




     de = 'seuemail@gmail.com'
     para = raw_input('Digite o email de quem vai receber: ')
     subject_text = 'Casa comigo?'
     message_text = 'Amor da minha vida!!!\nEu te amo!!!\n\nCasa comigo?'
     msg = 'From: %s\nTo: %s\nSubject: %s\n%s' % (de,para,subject_text, message_text)
    


     smtp.sendmail(de, para, msg)
     print "Email enviado com sucesso"
     smtp.close()
    
except SMTPException, error:
   print "Error: unable to send email: \n", str(error)
