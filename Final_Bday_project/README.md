Birthday Wishing Application

This file contains the details on how to run the application and how to debug if any problem arises during the runtime

------------------------------------------------------------------------------------------------

Setup the enviornment for running the file

------------------------------------
Download the file from the github -:
GitHub link -:

****************************
$git clone <link>
$cd Birthday_Wishing_Script
****************************

On Linux System -:
****************************
$pip install -r requirements.txt
****************************

On Linux System -:
The file is running using CRON JOB

Commond for Cronjob
****************************
$crontab -l  # To check if any previous task is pending
$crontab -e  # To edit the cron file and add a new task
****************************
In the file

****************************
>> 01 00 * * * ../python3 ../final.py
****************************
# The Above code of make the script run at 00:01 daily
# Here ../ defines the address of the file, here we address link for both executable file and the Python interpreter

Consult website for more option regarding setting time -: https://crontab.guru/


To Manually run this file on terminal
****************************
$ python final.py
****************************

-------------------------------------------------------------------------------------------------------------------------
Possible Error-: 

1. Google Less Secure Application Service Policy Change -: Google can change the policy due to security reasons, then we need to reconfig the file to find the best optimum solution provided by the Google for using SMTP server.
    * Check for 2-factor Authentication and App Password Avaiability

2. SMTPLIB gets outdated, so one need to update the file manually.

$ pip install secure-smtplib --upgrade

# This will update the lirary to the lastest version
# Also then we need to check if there is any sort of changes in the syntax of the library, if error sustains.

3. If the file is unable to run, then there might be problem of internet connectivity, troubleshoot it and then again run the file.


-----------------------------------------------------------------------------------

Maintiance of Data in the EXCEL sheets

------------------------------------------------------------------

There are total of three files to be maintained for handling the college Data.
1. Faculty_Employees_List.xlsx
    * The Details of faculties is divided according to the branch

    Data should be of form-:

    --------------------------------------------------------------------------
    |S.No.	| Name | Gender | Email | Date of Birth | Birth_Date |Department |
    --------------------------------------------------------------------------


2. NTS_Emplpoyees_List.xlsx
    * Details of NTS Employees is divided according to the Regaular staff and Contractual Staff

    Data should be of form -:

    ----------------------------------------------------
    |S. No.	| Name | Gender | Email | DOB | Birth_Date |
    ----------------------------------------------------

3. Student_List.xlsx
    * Details of Students is divided according to their year of admission

    Data should be of form -:

    -----------------------------------------------------------
    |ROLLNO| Name| Gender | DOB | Birth_Date | Email | BRANCH |
    -----------------------------------------------------------

Important

1. Here, "Birth_date" = TEXT(<Cell of "DOB">,"dd-mm") in all the excel sheets
2. If "Name" is not in regular form, Use **=PROPER(<Cell Number>)** to make it into normal form.