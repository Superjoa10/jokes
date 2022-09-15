from tkinter import *
from PIL import ImageTk,Image
from winsound import *
root = Tk()
root.title("mini drake, the menece")
root.iconbitmap("images_n_files/lesgo.ico")
# for a  button to quit shit
def image_open():
    global my_img
    global play
    my_img = ImageTk.PhotoImage(Image.open("images_n_files/minidrake.jpg"))
    my_label = Label(image=my_img)
    corno = my_label.pack()
    play =  PlaySound('images_n_files/bruh_soudeffect.wav', SND_FILENAME)
    return corno, play
    
def sound():
    global play
    play = lambda: PlaySound('images_n_files/bruh_soudeffect.wav', SND_FILENAME)
    return play

button_2 = Button(root, text = 'open', command=lambda: image_open())
button_bruh = Button(root, text = 'bruh.sound_effect', command = sound())
button_quit = Button(root, text="Quit", command=root.quit)


button_2.pack()
button_bruh.pack()
button_quit.pack()
root.mainloop()
