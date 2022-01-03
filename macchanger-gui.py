#!/usr/bin/python3
from tkinter import *
from tkinter import simpledialog
import os,subprocess

os.system("touch .log.txt")
#funcs
def follow():
    out = subprocess.call(["firefox","https://github.com/generatorexit"])
    if(out == 0 ):
        print("Author --> https://www.github.com/generatorexit")
    else:
        os.system("chromium --no-sandbox https://github.com/generatorexit")
        print("Author --> https://www.github.com/generatorexit")

def show_mac():
    interface = simpledialog.askstring(title="Interface",prompt="Choose interface")
    check = subprocess.call(["sudo","ifconfig",interface])
    if(check == 0):
        mac = subprocess.check_output(['macchanger','-s',interface])
        test.insert(END,"[+]Curent MAC\n")
        test.insert(END,"--------------\n")
        test.insert(END,mac)
    else:
        test.insert(END,"[-]Interface not found!")

def show_interface():
    os.system("netstat -i | awk '{print $1}' > .log.txt")
    os.system("echo ----------------------- >> .log.txt")
    inter = subprocess.check_output(["tail","-n","+3",".log.txt"]) 
    test.insert(END,"[+] Availabe Interface\n")
    test.insert(END,"-----------------------\n")
    test.insert(END,inter)

def manual_mac():
    interface = simpledialog.askstring(title="Interface",prompt="Choose interface to change MAC")
    check = subprocess.call(["sudo","ifconfig",interface])
    if(check == 0):
        newmac = simpledialog.askstring(title="MAC Address",prompt="Enter New MAC address")
        test.insert(END,"\n\n[+] Changing to New MAC...\n")
        subprocess.call(["sudo","ifconfig",interface,"down"])
        subprocess.call(["sudo","ifconfig",interface,"hw","ether",newmac])
        subprocess.call(["sudo","ifconfig",interface,"up"])
        test.insert(END,"[+] MAC Address changed\n\n")
    else:
        test.insert(END,"\n[-] Interface Not found!\n")

def random_mac():
    interface = simpledialog.askstring(title="Interface",prompt="Choose interface to change MAC")
    check = subprocess.call(["sudo","ifconfig",interface])
    if(check == 0):
        test.insert(END,"\n[+] Changing to Random MAC...\n")
        subprocess.call(["sudo","ifconfig",interface,"down"])
        out = subprocess.check_output(["sudo","macchanger","-r",interface])
        subprocess.call(["sudo","ifconfig",interface,"up"])
        test.insert(END,out)
        test.insert(END,"\n[+] MAC Address Changed\n")
    else:
        test.insert(END,"\n[-] Interface Not found!\n")

def reset_mac():
        interface = simpledialog.askstring(title="Interface",prompt="Choose interface to change MAC")
        check = subprocess.call(["sudo","ifconfig",interface])
        if(check == 0 ):
            test.insert(END,"\n[+] Reseting Your original MAC...\n")
            subprocess.call(["sudo","ifconfig",interface,"down"])
            subprocess.call(["sudo","macchanger","-p",interface])
            subprocess.call(["sudo","ifconfig",interface,"up"])
            test.insert(END,"\n[+] Your MAC Address Reset Success")
        else:
            test.insert(END,"\n[-] Interface Not Found!\n")
            
#gui
gui = Tk()
gui.geometry("600x450")
gui.title("MACCHANGER @ mksec")
gui.resizable(width=False, height=False)
gui.config(bg='black')

#title lable
lable1 = Label(gui, text="MAC CHANGER",font=("courier",42))
lable1.pack(padx=20,pady=10)
lable1.config(bg='black',fg='#00FF00')

#Set Buttons
btn = Button(gui,
            text="Show MAC",
            command=show_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=21,y=66)

btn = Button(gui,
            text="Show Interface",
            command=show_interface,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=141,y=66)
btn = Button(gui,
            text="Set New MAC",
            command=manual_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=291,y=66)
btn = Button(gui,
            text="Set Random MAC",
            command=random_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=431,y=66)
btn = Button(gui,
            text="Reset MAC",
            command=reset_mac,
            bg='black',fg='white',activebackground='white',activeforeground='black').place(x=250,y=114)

socialbtn = Button(gui,
                    text="Author",
                    command=follow,
                    bg='black',fg='white',activebackground='#00FF00',activeforeground='black',borderwidth=0,highlightthickness=0).place(x=540,y=0)
#log lable
log1 = Label(gui, text="Status:",font=("courier",18),bg='black',fg='white').place(x=0,y=129)

#set Log details here
test = Text(fg='#00ff00',bg='black',borderwidth=2,relief="ridge")
test.place(x=0,y=150,height=300,width=600)

#Run GUI In loop
gui.mainloop()