import pandas as pd
import datetime
import smtplib
import os
#os.chdir(r"D:\MyData\Business\code playground\Python Practice Programs\birthday wisher")
# os.mkdir("testing") 

# Enter your authentication details
GMAIL_ID = '21ucs108@lnmiit.ac.in'
#'tester.you256@gmail.com'
#'testing.you758@gmail.com'
GMAIL_PSWD = 'I@mwea1thyforever99'


#qwe!@#asd!@#

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()
    

if __name__ == "__main__":
    #just for testing
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_csv("birthdays.csv")
    # print(df)
    today = datetime.datetime.now().strftime("%d %m").split(" ")
    #month = datetime.datetime.now().strftime("%m")
    yearNow = datetime.datetime.now().strftime("%Y")

    print(today, type(today))
    #print(month, type(month))
    print(yearNow, type(yearNow))

    # print(type(today))
    writeInd = []
    for index, item in df.iterrows():
        print(index, item['Birthday'])
        b_day = item['day']
        b_month = item['month']
        print(b_day, type(b_day))
        print(b_month, type(b_month)) 
        
        # print(b_day == int(today[0]) and (b_month) == int(today[1]))
        # print(type(today[0]))

        if(b_day == int(today[0]) and (b_month) == int(today[1])):
            print("Hello")
            sendEmail(item['email'], "Happy Birthday", "Happy Birthday To You") 
            writeInd.append(index)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'year']
        df.loc[i, 'year'] = str(yr) + ', ' + str(yearNow)
        print(df.loc[i, 'year'])

    #print(df) 
    df.to_csv('data.csv', index=False)   