# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import math
import numpy as np
global image_path

image_size = 300, 300

def ifClicked():
    
    global image_path

    image_path = filedialog.askopenfilename()
    loaded_image = Image.open(image_path)
    loaded_image.thumbnail(image_size)
    disp_image = ImageTk.PhotoImage(loaded_image)
    img = Label(window, image=disp_image)
    img.image = disp_image
    img.place(x=20, y=50)


def encrypt_data():
    
    global image_path

    data = txt.get(1.0,"end-1c")
    img = cv2.imread(image_path)
    data = [format(ord(i),'08b') for i in data]
    encrypted_name = txt1.get(1.0, "end-1c")
    encrypted_name += ".png"

    _, width, _ = img.shape

    PixReq = len(data) * 3
    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0

    for i in range(RowReq+1):

        while count < width and charCount < len(data):

            char = data[charCount]
            charCount += 1

            for index, k in enumerate(char):

                if (k == '1' and img[i][count][index % 3] % 2 == 0) or (k == '0' and img[i][count][index % 3] % 2 == 1):
                    img[i][count][index % 3] -= 1

                if index % 3 == 2:
                    count += 1

                if index == 7:

                    if charCount * 3 < PixReq and img[i][count][2] % 2 == 1:
                        img[i][count][2] -= 1

                    if charCount * 3 >= PixReq and img[i][count][2] % 2 == 0:
                        img[i][count][2] -= 1

                    count += 1

        count = 0

    cv2.imwrite(encrypted_name, img)

    success = Label(window, text="Encryption Successful!", bg='lavender', font=("Times New Roman", 20))
    success.place(x=160, y=400)


window = Tk()
window.configure(background='lavender')
window.title("Encryption")
window.geometry('600x600')

ifClicked_button = Button(window, text="Choose Image", bg='white', fg='black', command=ifClicked)
ifClicked_button.place(x=250, y=10)

txt = Text(window, wrap=WORD, width=30)
txt.place(x=340, y=55, height=165)

label = Label(window, text="Enter the name to be given to the encrypted image:", bg='white', fg='black')
txt1 = Text(window, wrap=WORD, width=30)

label.place(x=50, y=275)
txt1.place(x=330, y=275, height=35)

encrypt_button = Button(window, text="Encode", bg='white', fg='black', command=encrypt_data)
encrypt_button.place(x=250, y=450)
window.mainloop()

def decrypt_data():
    
    global image_path
    
    load=Image.open("./encrypted_image.png")
    load.thumbnail(image_display_size,Image.ANTIALIAS)
    load=np.array(load);
    load=Image.fromarray(np.uint8(load))
    render=ImageTk.PhotoImage(load)
    img=Label(app,image=render)
    img.image=render
    img.place(x=100,y=50)
    
    img=cv2.imread("./encrypted_image.png")
    data=[]
    stop=False
    for index_i,i in enumerate(img):
        i.tolist()
        for index_j,j in enumerate(i):
            if((index_j)%3==2):
                data.append(bin(j[0][-1]))
                data.append(bin(j[1][-1]))
                if(bin(j[2][-1]=='1')):
                    stop=True
                    break
                else:
                    data.append(bin(j[0][-1]))
                    data.append(bin(j[1][-1]))
                    data.append(bin(j[2][-1]))
                if(stop):
                    break
                
                messeage=[]
                
               for i in range(int((len(data)+1)/8)):
                   message.append(data[i*8:(i*8+8)])
               message = [chr(int(''.join(i), 2)) for i in message]
               message = ''.join(message)
               message_label = Label(app, text=message, bg='lavender', font=("Times New Roman", 10))
               message_label.place(x=30, y=400)    
                   
    

# Defined the TKinter object app with background lavender, title Decrypt, and app size 600*600 pixels.
app = Tk()
app.configure(background='lavender')
app.title("Decrypt")
app.geometry('600x600')
# Add the button to call the function decrypt.
main_button = Button(app, text="Start Program", bg='white', fg='black', command=decrypt)
main_button.place(x=250, y=10)
app.mainloop()

def main():
    print("What do you want to perform??")
    print("1.Encryption")
    print("2.Decryption")
    print("3.Exit")
    print("Enter your choice:")
    n=int(input())
    if(n==1):
        encrypt_data()
    elif(n==2):
        decrypt_data()
    elif(n==3):
        break
    elif(n>3 or n<=0):
        print("Invalid choice!!Please enter a valid choice")
        main()
        
    return 0

main()


        
     
    
    
    

    
