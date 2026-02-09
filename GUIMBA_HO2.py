import tkinter as tk
window = tk.Tk()
window.title("Student Profile")
window.geometry("500x300")
window.resizable(False,False)
window.configure(bg="#faff9c")

label = tk.Label(window,text="Student Profile",font = ("Arial",20,"bold"),fg = "black",bg = "#faff9c",width=20,height=2,anchor="center")
label.pack(side="top",padx=10,pady=10,fill="x",expand=False)

name = tk.Label(window,text="Name: Guian Esteebean A. Guimba",font = ("Arial",12),fg = "black",bg = "#faff9c",width=20,height=1,anchor="w")
name.pack(side="top",padx=10,pady=7,fill="x",expand=False)

course = tk.Label(window,text="Course and Section: BSIT-1C",font = ("Arial",12),fg = "black",bg = "#faff9c",width=20,height=1,anchor="w")
course.pack(side="top",padx=10,pady=7,fill="x",expand=False)

birthday = tk.Label(window,text="Birthday: Januray 31, 2007",font = ("Arial",12),fg = "black",bg = "#faff9c",width=20,height=1,anchor="w")
birthday.pack(side="top",padx=10,pady=7,fill="x",expand=False)

motto = tk.Label(window,text="Motto:",font = ("Arial",12),fg = "black",bg = "#faff9c",width=20,height=1,anchor="w")
motto.pack(side="top",padx=10,pady=7,fill="x",expand=False)

motto1 = tk.Label(window,text="It is what it is",font = ("Arial",12,"bold","italic"),fg = "black",bg = "#faff9c",width=20,height=1,anchor="center")
motto1.pack(side="top",padx=10,pady=3,fill="x",expand=False)

window.mainloop()
