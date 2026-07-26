from tkinter import *
import os
from tkinter import messagebox
import random
import json 

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



def generate_password():
    input_pass.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)
    password = "".join(password_list)
    input_pass.insert(0, password)

  	

  

# ---------------------------- SAVE PASSWORD ------------------------------- #

path_dir = os.path.dirname(os.path.abspath(__file__))



file_path = os.path.join(path_dir,"emails.json")


def save_pass():
    website = input_website.get()
    email = input_email.get()
    password = input_pass.get() 
    # .get() takes the data inputted into the Entry() field. 
    new_data = {
        website.lower(): {
            "email": email,
            "password": password
        }
    }

    if "" in [website,email,password]:
        messagebox.showerror(title="Error",message="One field is missing")
    else:
        save_data = messagebox.askokcancel(title=website,message=f"These are the details: \n Website: {website} \n Email: {email} \n Pass: {password} \n Save info??")

        if save_data:
            try:
                with open(file_path, "r") as file: #We are opening the file in read mode before it even exists. 
                    #Error seen: FileNotFoundError: [Errno 2] No such file or directory: './password-manager-start/emails.json'
                    data = json.load(file)
                 # not new_data, since the data present if file exits needs to be updated.
                    # if we say json.dump(new_data,....) that would cause errors since structure would be
                    # (exisiting data) 
                    #     Flipcart: {
                    #         "email": jojo@gmail.com,
                    #         "password": Howdydoing
                    #     }
                    # (new_data added then)
                    #     Amazon: {
                    #         "email": jogo@gmail.com,
                    #         "password": thisisbezos
                    #     }
                    # This results in an error of 2 separate {...} {...} Amazon and flipcart, whereas json requires only one main {...} with sub-divided into it.
            except FileNotFoundError:
                with open(file_path, "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
              data.update(new_data)
              with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
                # else runs code if the try block succeeds. 
            finally:
              input_website.delete(0,END)
              input_pass.delete(0,END)
              

# ---------------------------- Search Password ------------------------------- #

# user types in website - look up website from emails.json Display the email and password - messagebox display "OK" - if not found "Crediantials for this website does not exist" - NotFoundError. try , error "KeyError" Else store

def find_pass() :
  website = input_website.get() #reteives the value user types in that Entry box. 
  with open(file_path,"r") as file:
    data = json.load(file)
    
    
    
    try:
      data_got = data[website.lower()]
    except KeyError:
      messagebox.showerror(title="Error",message=f"{website} has no user data")
      input_website.delete(0,END)
    else:
      messagebox.showinfo(title=f"{website.lower()} User Data", message=f"Email: {data_got["email"]} \nPassword: {data_got["password"]}")
    

    
  
  




  

# ---------------------------- UI SETUP ------------------------------- #



base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir , "logo.png")

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas( width=200, height=200)
canvas.grid(row=0,column=1)


label = Label(text="Website:", font=(FONT_NAME,12))
label.grid(row=1,column=0)

label = Label(text="Email/username:", font=(FONT_NAME,12))
label.grid(row=2,column=0)

label = Label(text="Password:", font=(FONT_NAME,12))
label.grid(row=3,column=0)

btn_generate_pass = Button(text="Generate Password", font=(FONT_NAME,10), width=15, padx=10, command=generate_password)
btn_generate_pass.grid(row=3,column=2)

btn_add_pass = Button(text="Add Password", font=(FONT_NAME,10), width=36, command=save_pass)
btn_add_pass.grid(row=4,column=1,columnspan=2)

btn_find_pass = Button(text="Search", font=(FONT_NAME,10),width=15, command=find_pass)
btn_find_pass.grid(row=1,column=2)

input_website = Entry(width=28)
input_website.focus()
input_website.grid(row=1,column=1)


input_email = Entry(width=60)
input_email.insert(0,"bobthebuilder@gmail.com")
input_email.grid(row=2,column=1,columnspan=2)

input_pass = Entry(width=28)
input_pass.grid(row=3,column=1)

lock_image = PhotoImage(file=image_dir) #loads the image file into python memory. creates an object
canvas.create_image(100,100,image=lock_image) #draws the image at specific pos. 
if __name__ == "__main__":
	window.mainloop()
