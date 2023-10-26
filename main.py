# Importazione librerie
from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv

# Configurazione informazioni
mittente = "emaildiprova@diobrando.com"

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'indirizzo_email@prova.com'
smtp_password = 'password_birichina'
from_email = 'indirizzo_email@prova.com'
subject = 'Happy birthday!'

# Lettura file CSV
with open('esercizio.csv', 'r') as filecsv:
    file = csv.reader(filecsv,delimiter=",")
    next(file)
    data_oggi = date.today()
    # print(file)
    for row in file:
        nome = row[1]
        data_di_nascita = row[2]
        destinatario = row[3]
        giorno_nascita = data_di_nascita.split('/')
        # print(giorno_nascita)

        if str(data_oggi.day) == giorno_nascita[2]:
        # print(f"Happy Birthday, dear{nome}")


        # Creazione messaggio e corpo messaggio
        messaggio = MIMEMultipart()
        messaggio['From'] = mittente
        messaggio['To'] = destinatario
        messaggio['Subject'] = "Happy Birthday"
        corpo_testo = f"Happy Birthday, dear{nome}"
        messaggio.attach(MIMEText(corpo_testo))




        # Connessioni al server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Invio email
        server.sendmail(from_email, destinatario, messaggio.as_string())

        # Chiudi la connessione SMTP per questa email
        server.quit()



    # Svolgimento precedente
    # for riga in file:
    #     #print(riga[1])
    #     first_name = riga[1]
    #     #print(riga[3])
    #     email = riga[3]
    #     print(f"Happy birthday, dear {first_name}!")









