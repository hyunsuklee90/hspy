import smtplib
from email.message import EmailMessage
import os

import psutil

class email_alert():
    def __init__(self, user="alertbot@naver.com", password="GHo@aFf@Mq%z^k"):
        self.user = user
        self.password = password
        
    def send(self, subject, body, to, who=None):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        
        if (type(who) == type(None)):
            msg['from'] = self.user
        else:
            msg['from'] = who
        
        server = smtplib.SMTP('smtp.naver.com', 587)
        server.starttls()
        
        server.login(self.user, self.password)
        
        server.send_message(msg)
        
        server.quit()

def get_task():
    psutil.process_iter(attrs=None, ad_value=None)
    
    msg = ''
    for proc in psutil.process_iter():
        
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            # proc.dir()
            # msg = msg+processName+' ::: '+processID+proc.cmdline()+proc.username()+'\n'
            # msg = msg+processName+' ::: '+proc.username()+'\n'
            msg = msg+proc.username()+'\n'
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    return msg

if __name__ == '__main__' :    
    print (get_task())
    
    import getpass

    username = getpass.getuser()
    
    print (username)
    
    # email_alert().send('Hi', msg, 'hyunsuk.lee90@gmail.com')