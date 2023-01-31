import smtplib
import datetime as dtime
import pandas as pd
import time
from email.mime.text import MIMEText
import pytz
import requests


class Email:
    
    def __init__(self, gmail_username, gmail_password, ):
        self.gmail_username = gmail_username
        self.gmail_password = gmail_password
        pass

    def letter(self, new_df):
        with open(f"./bday_letter/letter.html") as letter_file:
            # reading the file
            letter_contents = letter_file.read()
            # replace [NAME] with actual name on the data
            if len(new_df["name"]) > 1:
                name = new_df['salutation'] + " " + new_df["name"]
                the_letter = letter_contents.replace("[NAME]", name)
                the_email = new_df["email"]
            else:
                the_letter = letter_contents.replace("[NAME]", new_df["name"].item())
                the_email = new_df["email"].item()

        return the_email, the_letter, name


    def send_message(self, the_email, the_letter, name):
        with smtplib.SMTP("smtp.gmail.com", 587) as con:
                    # secure the mail
                    con.starttls()
                    con.login(user=self.gmail_username, password=self.gmail_password)

                    msg = MIMEText(the_letter, 'html')
                    msg["From"] = "21ucs108@lnmiit.ac.in"
                    msg["To"] = the_email
                    msg["Subject"] = "Happy Birthday " + name + "!!"

                    con.send_message(msg)
                    con.quit()
                    time.sleep(10)

    
    def Happy_Birthday(self, new_df, current_month):
        #print(new_df)
        if len(new_df.loc[new_df['month'] == current_month]) > 0:
            for index, item in new_df.iterrows():      #i in range(len(new_df.loc[new_df['month'] == current_month])):
                #print(index, item)
                
                the_email, the_letter, name =  self.letter(new_df=item)
                
                self.send_message(the_email=the_email, the_letter=the_letter, name=name)
                print("Mail Sent!")
        return 
    

if (__name__ == "__main__"):

    df = pd.read_csv("birthdays.csv")

    # using World Time API
    url = "http://worldtimeapi.org/api/timezone/Asia/Kolkata"

    response = requests.get(url)
    data = response.json()

    timestamp = data['unixtime']
    timezone = data['timezone']

    tz = pytz.timezone(timezone)
    tme = dtime.datetime.fromtimestamp(timestamp, tz)

    #time.strftime("%Y-%m-%d %H:%M:%S")

    current_day = int(tme.strftime("%d"))           
    current_month = int(tme.strftime("%m"))       

    new_df = df.loc[df['day'] == current_day]
    new_df = new_df.loc[new_df['month'] == current_month]

    #print(new_df)

    GMUSER = '21ucs108@lnmiit.ac.in'
    GMPASS = 'I@mwea1thyforever99'

    em = Email(gmail_username=GMUSER,gmail_password=GMPASS)

    em.Happy_Birthday(new_df=new_df, current_month=current_month)
