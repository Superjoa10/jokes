from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Lol u gay")
root.iconbitmap("C:/Users/João/Pictures/lesgo.ico")
# for a  button to quit shit

my_img1 = ImageTk.PhotoImage(Image.open("images_n_files/minidrake.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images_n_files/lesgo.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images_n_files/faces.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("images_n_files/old.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images_n_files/guts_sama.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

#status bar:
status = Label(root, text= "image 1 of "+ str(len(image_list)), bd=1, relief= SUNKEN, anchor=E)
#anchor stiks texts and content to one side using W E S N

my_label = Label(image=my_img1)
my_label.grid(row=0,column=0, columnspan=3)

#grid_forget() closes image or label in general depending
def forward(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command= lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda: back(img_num-1))

    if img_num == 5:
        button_forward = Button(root, text=">>", state= DISABLED)

    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    #update status bar
    status = Label(root, text= "image "+ str(img_num) +" of "+ str(len(image_list)), bd=1, relief= SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)

def back(img_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1])
    button_forward = Button(root, text=">>", command= lambda: forward(img_num+1))
    button_back = Button(root, text="<<", command=lambda: back(img_num-1))

    if img_num == 1:
        button_back = Button(root, text="<<", state= DISABLED)
    
    my_label.grid(row=0,column=0, columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    #update status bar
    status = Label(root, text= "image "+ str(img_num) +" of "+ str(len(image_list)), bd=1, relief= SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky= W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Quit", command= root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky= W+E)
#sticky stretches, but uses West East North South (W E N S)

root.mainloop()
