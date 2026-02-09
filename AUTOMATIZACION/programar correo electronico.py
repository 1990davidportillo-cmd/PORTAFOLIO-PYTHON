import time
from datetime import datetime
from email.message import EmailMessage
import smtplib

def tarea():
    msg = EmailMessage()
    msg.set_content("Hola, este es un mensaje automatico de python")

    msg['Subject'] = 'Mensaje Automático'
    msg['From'] = '1990david.portillo@gmail.com'
    msg['To'] = 'acfibonnacci@gmail.com, compras.gt90@gmail.com'

    # Adjuntar archivo PDF
    with open('documento.pdf', 'rb') as archivo:
        contenido = archivo.read()
        msg.add_attachment(
            contenido,
            maintype='application',
            subtype='pdf',
            filename='documento.pdf'
        )

    with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
        smtp.login(
            user='acfibonnacci@gmail.com',
            password='swgp lvmu bvaf bsbo'
        )
        smtp.send_message(msg)

    print("correo enviado automáticamente")

hora_objetivo = "20:43"

while True:
    hora_actual = datetime.now().strftime("%H:%M")

    if hora_actual == hora_objetivo:
        tarea()
        break

    time.sleep(30)
