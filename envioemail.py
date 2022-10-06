from email.message import EmailMessage
import smtplib

def enviar_email(email_destino,codigo):
    remitente = "vaccar@uninorte.edu.co"
    destinatario = email_destino
    mensaje = "Codigo de Confirmacion"+codigo
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Codigo de Activacion" + codigo
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

def recuperar_email(email_destino):
    remitente = "vaccar@uninorte.edu.co"
    destinatario = email_destino
    mensaje="<hr>"
    mensaje = "<h2>Recuperacion de Cuenta</h2>"
    mensaje =mensaje+ "<a href='http://localhost:5000/restablecer/"+ email_destino +"'>Ingrese Aqui para restablecer su contraseña</a>" 
    mensaje=mensaje+"<hr>"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Recuperar Contraseña" 
    email.set_content(mensaje, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "_Malex2013_")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()