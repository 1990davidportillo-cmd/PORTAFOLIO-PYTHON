import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Hola, este es un mensaje automatico de python")

msg['Subject'] = 'Mensaje Automático'
msg['From'] = '1990david.portillo@gmail.com'
msg['To'] = 'acfibonnacci@gmail.com, compras.gt90@gmail.com'

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.login(
        user='acfibonnacci@gmail.com',
        password='swgp lvmu bvaf bsbo'
    )
    smtp.send_message(msg)

print("correo enviado automaticamente")
