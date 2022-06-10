#  Python project to hide data in images (Steganography)
# Coded by Srivatsan.R
# Code for decrypting the data


#rom tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog,Button,Label,Tk,Entry
import cv2
import numpy as np


image_display_size = 500, 350


def valid_entry():
    uname = username.get()
    pword = password.get()
    if (uname == "Srivatsan" and pword == "admin2") :

        def decrypt():
            
           
            path = filedialog.askopenfilename()

            load = Image.open(path)
            load.thumbnail(image_display_size)
            load = np.asarray(load)
            load = Image.fromarray(np.uint8(load))
            render = ImageTk.PhotoImage(load)
            img = Label(app, image=render)
            img.image = render
            img.place(x=100, y=50)

            # Algorithm to decrypt the data from the image
            img = cv2.imread(path)
            data = []
            stop = False
            for index_i, i in enumerate(img):

                i.tolist()
                for index_j, j in enumerate(i):
                
                    if ((index_j) % 3 == 2):
                        # first pixel
                        data.append(bin(j[0])[-1])
                        # second pixel
                        data.append(bin(j[1])[-1])
                        # third pixel
                        if (bin(j[2])[-1] == '1'):
                            stop = True
                            break
                    else:
                        # first pixel
                        data.append(bin(j[0])[-1])
                        # second pixel
                        data.append(bin(j[1])[-1])
                        # third pixel
                        data.append(bin(j[2])[-1])
                if (stop):
                    break
            
            message = []
            for i in range(int((len(data) + 1) / 8)):
                message.append(data[i * 8:(i * 8 + 8)])
            # join all the letters to form the message.
            message = [chr(int(''.join(i), 2)) for i in message]
            message = ''.join(message)
            message_label = Label(app, text=message, bg='lavender', font=("Segoe Script", 11))
            message_label.place(x=30, y=400)

        
        window.destroy()
        app = Tk()
        app.configure(background='Orange')
        app.title("Decrypt")
        app.geometry('600x600')
        # Add the button to call the function decrypt.
        main_button = Button(app, text="Start Program", bg='white', fg='black', command=decrypt)
        main_button.place(x=250, y=10)
        app.mainloop()


    else:
        window.destroy()
        print("Invalid Login")

window=Tk()
window.title("Login")
window.geometry("300x200")
username_label = Label(window,text="Username").place(x=10,y=10)
username = Entry(window)
username.place(x=140,y=10)
password_label = Label(window,text="Password").place(x=10,y=40)
password = Entry(window,show="*")
password.place(x=140,y=40)
Button(window,text="Login",command=valid_entry).place(x=10,y=100)
window.mainloop()
