import tkinter as tk
window = tk.Tk()
window.title("Student Profile")
window.geometry("500x500")
window.resizable(False,False)
window.configure(bg="#faff9c")

img = tk.PhotoImage(file="img.png")
Image_label = tk.Label(window, image=img)
Image_label.pack()

button = tk.Button(window,
    text="Submit",
    font= ("Arial",12,"bold"),
    fg= "black",
    bg= "white",
    state= "normal",
    relief= "raised",
    width= 1,
    height = 2,
    activebackground= "red",
    activeforeground= "white", )
button.pack(side ="top",padx = 50,pady = 20, fill = "x", expand= False)

window.mainloop()
