 ##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas as pd
import os
from random import randint
from dotenv import load_dotenv, find_dotenv

dotenv_path   = find_dotenv()
load_dotenv(dotenv_path)


my_email = os.getenv("MY_EMAIL")
my_Pass = os.getenv("GMAIL_KEY")

#Get file location
base_dir = os.path.dirname(os.path.abspath(__file__))
birthdays = os.path.join(base_dir, "birthdays.csv")



# 1. Update the birthdays.csv
df = pd.read_csv(birthdays)
data = df.to_dict(orient="records")
ppl_months = [months["month"] for months in data]
ppl_days = [days["day"] for days in data]

# 2. Check if today matches a birthday in the birthdays.csv
date = dt.datetime.now()
today = date.day
month = date.month
year = date.year
bday_person = []
recipient = []
if month in ppl_months and today in ppl_days:
  bday = df["name"][df["month"] == month]
  email_retreived = df["email"][df["month"] == month]
  recipient.append(email_retreived.iloc[0])
  bday_person.append(bday.iloc[0])

  


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
number = randint(1,3)
letters = os.path.join(base_dir,"letter_templates",f"letter_{number}.txt")
# open letter - read then add each name in the list to the [NAME] , then open letters as write and then write it
letter = open(letters)
text = letter.read()
sender = "Zephan"
print(text)

for name in bday_person:
  new_letter = text.replace("[NAME]",name)
  new_letter = new_letter.replace("[sender]",sender)


letter.close()

  


# 4. Send the letter generated in step 3 to that person's email address.



#connect with the server
for people in recipient:
    with smtplib.SMTP("smtp.gmail.com") as file:
      file.starttls()
      file.login(user=my_email,password=my_Pass)
      for name in bday_person:        
        file.sendmail(to_addrs=people,from_addr=my_email,msg=f"Subject:Happy birthday {name} \n\n {new_letter}")



