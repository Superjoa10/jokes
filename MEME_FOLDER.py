from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Lol u gay")
# for a  button to quit shit

my_img1 = ImageTk.PhotoImage(Image.open("download.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("lesgo.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("faces.jpeg"))
my_img4 = ImageTk.PhotoImage(Image.open("download (1).jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("3897338.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5]

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

button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit = Button(root, text="Quit", command= root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()