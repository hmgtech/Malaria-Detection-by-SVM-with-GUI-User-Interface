import re
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox  

from sklearn.externals import joblib 
import skimage
from skimage.io import imread
from skimage.transform import resize
import numpy as np

from PIL import ImageTk, Image

clf = joblib.load('file_1000_40x40.pkl') 
global a

regex = '^\w([\.-]?\w+)*@\w([\.-]?\w+)*(\.\w{2,3})+$'

def filedreq():
	if Fname.get() == "":
		print("First Name Field is Empty!!")
		user = "First Name Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=460)


	elif Lname.get() == "":
		print("Last Name Field is Empty!!")
		user = "Last Name Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=460)

	elif Email.get() == "":
		print("Email Field is Empty!!")
		user = "Email Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=460)

	elif Phone.get() == "":
		print("Phone Field is Empty!!")
		user = "Phone Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=460)

	elif entry_Address.compare("end-1c", "==", "1.0"):     # or else  if len(text.get("1.0", "end-1c")) == 0:
		print("Address Field is Empty!!")
		user = "Address Field is Empty!!"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=460)
	else:
		checkemail()

def checkemail():
	email = Email.get()

	if(re.search(regex,email)):
		# print("Valid Email")
		user = "Valid Email!!"
		# Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=460)
		test()
	else:
		print("Invalid Email!!")
		user = "Invalid Email-Type!! Type Correct Mail: Format: xyz@abc.com"
		Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 12 bold")).place(x=12,y=460)


def browse():
	filename = filedialog.askopenfilename(filetypes = (("All Files","*.*"),("File","*.py")))
	path.config(text = filename)
	
	a = filename
	global file 
	file = a
	# print(a)


def test():
	print("Testing...")
	# Test code will go here....

	dimension=(40, 40)
	images = []
	flat_data = []

	# print("file",file)
	# file = 'data/test/Uni/y.png'
	img = skimage.io.imread(file)
	# print(img)
	img_resized = resize(img, dimension, anti_aliasing=True, mode='reflect')
	flat_data.append(img_resized.flatten()) 
	images.append(img_resized)
	flat_data = np.array(flat_data)
	# print(flat_data)

	result = clf.predict(flat_data)
	# print(result)
	if result[0] == 0:
	    print("Infected")
	    person = Fname.get()
	    user = person + ' is Infected By Malaria!!!'
	    a = user
	    Label(win,text="                                                              ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=460)
	    Label(win,text=user,fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=460)
	    MsgBox = tk.messagebox.showwarning ('warning','Parasite Found!! \nEat Vegetables, Fruits, Milk Products, Fish, Sugar With Honey!!',icon = 'warning')
	else:
	    print("Uninfected")
	    person = Fname.get()
	    user = person + ' is NOT  Infected By Malaria!!!'
	    a = user
	    Label(win,text=". ",fg="red",bg="white",font = ("Calibri 12 bold")).place(x=12,y=460)
	    Label(win,text=user,fg="blue",bg="yellow",font = ("Calibri 12 bold")).place(x=12,y=460)
	    MsgBox = tk.messagebox.showinfo ('information','Parasite Not Found!! \nPateint is at Less Risk!! \nEat Vegetables, Fruits, Milk Products, Fish, Sugar With Honey!!')

	# After Test, save() will execute
	save(a)

def save(a):
	
	First = Fname.get()
	Last = Lname.get()
	email = Email.get()
	address = entry_Address.get(1.0,END)
	phone = Phone.get()
	gender = str(radio.get())
	save_name = First+".txt"  
	
	file = open(save_name,"a")
	file.write("\n\nFirst Name: "+First+"\n")
	file.write("Last Name: "+Last+"\n")
	file.write("Phone: "+phone+"\n")
	file.write("Email: "+email+"\n")
	file.write("Address "+address)
	file.write("Gender: "+gender+"\n")
	file.write("Report: "+ a +"\n")
	file.close()
	report = First + "'s Health Detection have successfully done and Report is saved in "+First+".txt"
	Label(win,text=report,fg="blue",bg="yellow",font = ("Calibri 10 bold")).place(x=12,y=500)
	# print("Printing Data: ")
	# print(First,Last,phone,email,address,gender)

def reset():
	Fname.set("")
	Lname.set("")
	Email.set("")
	Phone.set("")
	entry_Address.delete(1.0,END)


win =  Tk()

win.geometry("420x520")
win.configure(background="cyan")
win.title("Malaria Detector By Hitesh")
win.iconbitmap('icon.ico')

title = Label(win,text="Unmask The Malaria",bg="gray",width="300",height="2",fg="White",font = ("Calibri 20 bold italic underline")).pack()

my_img = ImageTk.PhotoImage(Image.open("image.png"))
my_label = Label(image=my_img)
my_label.place(x=340,y=0)

Fname = Label(win, text="First name: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=100)
gap = Label(win,text="",bg="cyan").pack()

Lname = Label(win, text="Last name: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=140)
gap = Label(win,text="",bg="cyan").pack()

email = Label(win, text="Email ID: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=180)
gap = Label(win,text="",bg="cyan").pack()

Phone = Label(win, text="Phone: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=220)
gap = Label(win,text="",bg="cyan").pack()

Address = Label(win, text="Address: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=260)
gap = Label(win,text="",bg="cyan").pack()

Gender = Label(win, text="Gender: ",bg="cyan",font = ("Verdana 12")).place(x=12,y=300)
radio = StringVar()
Male = Radiobutton(win, text="Male",bg="cyan",variable=radio,value="Male",font = ("Verdana 12")).place(x=12,y=340)
Female = Radiobutton(win, text="Female",bg="cyan",variable=radio,value="Female",font = ("Verdana 12")).place(x=120,y=340)
gap = Label(win,text="",bg="cyan").pack()


Fname = StringVar()
Lname = StringVar()
Email = StringVar()
Phone = StringVar()
Address  = StringVar()
Gender = StringVar()
Courses  = StringVar()


entry_Fname = Entry(win,textvariable = Fname,width=30)
entry_Fname.place(x=120,y=100)
entry_Lname = Entry(win,textvariable = Lname,width=30)
entry_Lname.place(x=120,y=140)
entry_email = Entry(win,textvariable = Email,width=30)
entry_email.place(x=120,y=180)
entry_Phone = Entry(win,textvariable = Phone,width=30)
entry_Phone.place(x=120,y=220)
entry_Address = Text(win,height=2,width=23)
entry_Address.place(x=119,y=260)

path = Label(win,bg="cyan",font = ("Verdana 8"))
path.place(x=140,y=380)
upload = Button(win, text="Load", width="12",height="1",activebackground="blue", bg="Pink",font = ("Calibri 12 "),command = browse).place(x=20, y=380)

reset = Button(win, text="Reset", width="12",height="1",activebackground="red", bg="Pink",font = ("Calibri 12 "),command = reset).place(x=20, y=420)
submit = Button(win, text="Test", width="12",height="1",activebackground="violet", bg="Pink",command = filedreq,font = ("Calibri 12 ")).place(x=240, y=420)

win.mainloop()


