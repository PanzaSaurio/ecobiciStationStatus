import smtplib
from airflow.models import Variable
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(station, status, email):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login(email, Variable.get('email_password'))

        subject = f'Alerta de estacion {station}'
        body = f'La estacion {station} se paso al estado {status}, verificar'
        
        
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        server.sendmail(email, email, msg.as_string())

        print('Email enviado exitosamente')
    except Exception as e:
        print(f'Error al enviar el email: {e}')