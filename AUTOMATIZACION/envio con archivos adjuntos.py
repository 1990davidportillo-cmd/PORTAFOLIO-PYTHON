import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg.set_content("Hola, este es un mensaje automatico de python")

msg['Subject'] = 'Mensaje Automático'
msg['From'] = 'acfibonnacci@gmail.com'
msg['To'] = 'salazarboris957@gmail.com, jjpumg@gmail.com, rojemarro@gmail.com'

# Adjuntar archivo PDF
with open('documento.pdf', 'rb') as archivo:
    contenido = archivo.read()
    msg.add_attachment(
        contenido,
        maintype='application',
        subtype='pdf',
        filename='documento.pdf'
    )

# Envío del correo
with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.login(
        user='acfibonnacci@gmail.com',
        password='swgp lvmu bvaf bsbo'
    )
    smtp.send_message(msg)

print("correo enviado automáticamente")
