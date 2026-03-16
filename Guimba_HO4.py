import tkinter as tk

window = tk.Tk()
window.title("hi")
window.geometry("600x300")
window.configure(bg="lightblue")

Window_Title = tk.Label(window,
text="Profile Builder",
font=("Arial",10,"bold"),
)

Main_Frame = tk.Frame(window)

First_Entry = tk.Entry(Main_Frame,
width=20
)
Last_Entry = tk.Entry(Main_Frame,
width=20
)
Initial_Entry = tk.Entry(Main_Frame,
width=20
)
Year_Entry = tk.Entry(Main_Frame,
width=20
)

First_Label = tk.Label(Main_Frame,
text="First Name",
font=("Arial",10)
)
Last_Label = tk.Label(Main_Frame,
text="Last Name",
font=("Arial",10)
)
Initial_Label = tk.Label(Main_Frame,
text="Middle Name",
font=("Arial",10)
)
Year_Label = tk.Label(Main_Frame,
text="Birth Year",
font=("Arial",10)
)
Age_Label = tk.Label(Main_Frame,
text="Your Age is...",
font=("Arial",14,"bold")
)
Gender_Label = tk.Label(Main_Frame,
text="Gender",
font=("Arial",10)
)

Gender_Radio = tk.Radiobutton(Main_Frame,
text="Male",
font=("Arial",10)
)
Gender_Radio.deselect()

Window_Title.pack(pady=5)
Main_Frame.pack(pady=5)

First_Entry.grid(column=0,row=0,pady=5,padx=20)
Last_Entry.grid(column=1,row=0,pady=5,padx=20)
Initial_Entry.grid(column=2,row=0,pady=5,padx=20)
Year_Entry.grid(column=0,row=3,pady=5,padx=20)

First_Label.grid(column=0,row=1,padx=20)
Last_Label.grid(column=1,row=1,padx=20)
Initial_Label.grid(column=2,row=1,padx=20)
Year_Label.grid(column=0,row=4,padx=20)
Age_Label.grid(column=1,columnspan=2,row=3,padx=20)
Gender_Label.grid(column=0,row=5,padx=20)

Gender_Radio.grid(column=1,row=5,padx=20)




window.mainloop()

