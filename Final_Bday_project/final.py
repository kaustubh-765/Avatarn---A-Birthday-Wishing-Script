# Copyright (C) 2023 LNMIIT
# This file is a property of The LNM Insitute of Infomation Technology, Jaipur, Rajasthan

# Required Libraries 
import smtplib                          # For mailing and mail session
import datetime as dtime                # For fetching Date and Time received from API
import pandas as pd                     # For handling the Data
import time                             # For handling the date and time 
from email.mime.text import MIMEText    # For making the Structure of the E-Mail
import pytz                             # For accurate calculation of the TimeZone
import requests                         # For API Fetch request


# Class for defining Mail Structure and sending Mails
class Email:
    
    # Constructor
    def __init__(self, gmail_username, gmail_password):
        self.gmail_username = gmail_username
        self.gmail_password = gmail_password
        pass
    
    # Function to give shape and structure to the Mail
    # Taking DataFrame as the parameter of People with Birthday on present day 
    def letter(self, new_df):

        # Opening the HTML template for mail
        with open(f"./bday_letter/letter.html") as letter_file:
            # reading the file
            letter_contents = letter_file.read()

            # replace [NAME] with actual name on the data
            # Checking for Number of names in the DataFrame
            if len(new_df["Name"]) > 1:
                name = ""
                end_name = (new_df["Name"].split())

                # Checking if the person is Professor or not
                if ((end_name[0] != "Dr." and end_name[0] != "Prof.")):    
                    # If the person is Student or NTS Employees
                    if(new_df['Gender'] == "Male" or new_df['Gender'] == 'M'):
                        name ="Mr. " + new_df["Name"]
                    elif (new_df['Gender'] == "Female" or new_df['Gender'] == 'F'):
                        name = "Ms. " + new_df['Name']
                else :
                        name = new_df['Name']

                # Extracting Details for the [FNAME] in the HTML template    
                if(end_name[0] != "Dr." and end_name[0] != "Prof."):
                    the_letter = letter_contents.replace("[NAME]", name).replace("[FNAME]", end_name[0])
                else:
                    the_letter = letter_contents.replace("[NAME]", name).replace("[FNAME]", end_name[1])
                
                # Extracting the Mail from the List of people (DataFrame) 
                the_email = new_df["Email"]
            else:

                # Replacing the [NAME] and [FNAME] from the HTML mail template 
                the_letter = letter_contents.replace("[NAME]", new_df["Name"].item()).replace("[FNAME]", new_df["Name"].item())
                the_email = new_df["Email"].item()

        # Returning the E-Mail Address, The Letter and the Name of the Person
        return the_email, the_letter, name

    # Function to send E-Mail and handling user log-in session
    def send_message(self, the_email, the_letter, name):
        # Using SMTP to connect to Google SMTP Server using port number 587
        with smtplib.SMTP("smtp.gmail.com", 587) as con:
                    # secure the mail
                    con.starttls()
                    # Login as the sending E-Mail user
                    con.login(user=self.gmail_username, password=self.gmail_password)

                    # Finalizing the structure of the E-Mail 
                    msg = MIMEText(the_letter, 'html')
                    msg["From"] = "sender_mail@xyz.com"
                    msg["To"] = the_email
                    msg["Subject"] = "Happy Birthday " + name 

                    # Sending the E-Mail and then Quitting the Session
                    con.send_message(msg)
                    con.quit()
                    time.sleep(10)

    # The Main Function Handling all the above tasks simultaneously 
    def Happy_Birthday(self, new_df, current_date):
        #print(new_df)
        # Checking if there are People who have birthday on the present day
        if len(new_df.loc[new_df['Birth_Date'] == current_date]) > 0:
            # Iterrating through each row in the DataFrame 
            for index, item in new_df.iterrows():      
                #print(index, item)
                
                # Finalizing the E-Mail Address, letter and the Name of the Person to send E-Mail
                the_email, the_letter, name =  self.letter(new_df=item)
                
                #print(the_letter)
                # Calling the send_message function to handle the session and send E-Mail and printing the confirmation
                self.send_message(the_email=the_email, the_letter=the_letter, name=name)
                print("Mail Sent!")
        return 
    

if (__name__ == "__main__"):


    # Define filepath for Students file, Faculties and NTS Employees
    filepath_1 = 'Excel_file_1.xlsx'
    filepath_2 = 'Excel_file_2.xlsx'
    filepath_3 = 'Excel_file_3.xlsx'

    # Load Excel file using Pandas
    f1 = pd.ExcelFile(filepath_1)
    f2 = pd.ExcelFile(filepath_2)
    f3 = pd.ExcelFile(filepath_3)

        
    # Define an empty list to store individual DataFrames
    list_of_dfs = []

    # Iterate through each worksheet 
    for sheet in f1.sheet_names:
        
        # Parse data from each worksheet as a Pandas DataFrame
        df = f1.parse(sheet)

        # And append it to the list
        list_of_dfs.append(df)
        
    for sheet in f2.sheet_names:
        
        # Not include the Master sheet
        if sheet == "Master":
            continue

        # Parse data from each worksheet as a Pandas DataFrame
        df = f2.parse(sheet)

        # And append it to the list
        list_of_dfs.append(df)

    for sheet in f3.sheet_names:

        # Parse data from each worksheet as a Pandas DataFrame
        df = f3.parse(sheet)

        # And append it to the list
        list_of_dfs.append(df)



    # using World Time API
    url = "http://worldtimeapi.org/api/timezone/Asia/Kolkata"

    # Requesting for the response from API and getting Data in JSON Format
    response = requests.get(url)
    data = response.json()

    # Extracting the Time in Unix-Time Format and Timezone
    timestamp = data['unixtime']
    timezone = data['timezone']

    # Calculating the exact timezone as per requirement and storing current time
    tz = pytz.timezone(timezone)
    tme = dtime.datetime.fromtimestamp(timestamp, tz)

    #time.strftime("%Y-%m-%d %H:%M:%S")
    # Extracting the current time in String format
    current_date = (tme.strftime("%d-%m")) 

    # Concatinating all the DataFrames from all the excel sheets 
    data = pd.concat(list_of_dfs, ignore_index=True)

    # Creating a DataFrame with people having birthday on present day
    list_date = data.loc[data['Birth_Date'] == current_date]

    # Gmail App Login Credentials 
    GMUSER = ''
    GMPASS = ''

    # Creating Object for the Class
    em = Email(gmail_username=GMUSER,gmail_password=GMPASS)
    # Sending Happy Birthday E-Mail 
    em.Happy_Birthday(new_df=list_date, current_date=current_date)
