import tkinter as tk

def Calculate(Operations):
    try:
        Number_1 = float(Entry_1.get())
        Number_2 = float(Entry_2.get())

        if Operations == "+":
            Final = Number_1 + Number_2
        elif Operations == "-":
            Final = Number_1 - Number_2
        elif Operations == "*":
            Final = Number_1 * Number_2
        elif Operations == "/":
            if Number_1 == 0 or Number_2 == 0:
                Answer_Label.config(text="Cannot be divided to zero")
                return
            Final = Number_1 / Number_2
        
        Answer_Label.config(text="Result: " + str(Final))
        
    except ValueError:
       Answer_Label.config(text="Invalid Input")


window = tk.Tk()
window.title("Basic Calculator")
window.geometry("300x300")
window.resizable(False,False)
window.configure(bg="lightblue")

label = tk.Label(window,
                 text = "Calculator",
                 font = ("Arial",12,"bold"),
                 fg = ("black"),
                 bg = ("white"),
                 width = 15,
                 height = 2,
                 anchor = ("center")
                 )

Main_Frame = tk.Frame(window,
                 bg="white",
                 bd=3,
                 relief="groove",
                )


Num_Label_1 = tk.Label(Main_Frame,
                 text = "Enter 1st Number",
                 font = ("Arial",10,"bold"),
                 fg = ("black"),
                 bg = ("white"),
                 width = 15,
                 height = 1,
                 anchor = ("center")
                 )
Num_Label_2 = tk.Label(Main_Frame,
                 text = "Enter 2nd Number",
                 font = ("Arial",10,"bold"),
                 fg = ("black"),
                 bg = ("white"),
                 width = 15,
                 height = 1,
                 anchor = ("center")
                 )

Answer_Label = tk.Label(window,
                 text = " ",
                 font = ("Arial",10,"bold"),
                 fg = ("black"),
                 bg = ("white"),
                 width = 20,
                 height = 1,
                 anchor = ("center")
                 )

Entry_1 = tk.Entry(Main_Frame,
                    width=10,
                    fg="black",
                    bg="white",
                    font="Arial",
                   )
Entry_2 = tk.Entry(Main_Frame,
                    width=10,
                    fg="black",
                    bg="white",
                    font="Arial",
                   )

Addition_Button = tk.Button(Main_Frame,
                            text="Addition",
                            font=("Arial",10,"bold"),
                            width= 8,
                            height= 1,
                            anchor= ("center"),
                            bd= 2,
                            relief="raised",
                            bg="gray",
                            fg="white",
                            activebackground="orange",
                            activeforeground="black",
                            command=lambda:Calculate("+")
                            
                            )
Substraction_Button = tk.Button(Main_Frame,
                            text="Subtract",
                            font=("Arial",10,"bold"),
                            width= 8,
                            height= 1,
                            anchor= ("center"),
                            bd= 2,
                            relief="raised",
                            bg="gray",
                            fg="white",
                            activebackground="orange",
                            activeforeground="black",
                            command =lambda:Calculate("-")
                            )
Multiplication_Button = tk.Button(Main_Frame,
                            text="Multiply",
                            font=("Arial",10,"bold"),
                            width= 8,
                            height= 1,
                            anchor= ("center"),
                            bd= 2,
                            relief="raised",
                            bg="gray",
                            fg="white",
                            activebackground="orange",
                            activeforeground="black",
                            command =lambda:Calculate("*")
                            )
Division_Button = tk.Button(Main_Frame,
                            text="Divide",
                            font=("Arial",10,"bold"),
                            width= 8,
                            height= 1,
                            anchor= ("center"),
                            bd= 2,
                            relief="raised",
                            bg="gray",
                            fg="white",
                            activebackground="orange",
                            activeforeground="black",
                            command =lambda:Calculate("/")
                            )

label.pack(pady = 20, padx= 20)
Main_Frame.pack(pady=5)
Answer_Label.pack(pady=5)

Num_Label_1.grid(column=1, row=1, padx=10, pady=5)
Num_Label_2.grid(column=1, row=2, padx=10, pady=5)

Entry_1.grid(column=2, row=1, padx=10, pady=5)
Entry_2.grid(column=2, row=2, padx=10, pady=5)

Addition_Button.grid(column=1,row=3, padx=10, pady=5)
Substraction_Button.grid(column=2,row=3, padx=10, pady=5)
Multiplication_Button.grid(column=1,row=4, padx=10, pady=5)
Division_Button.grid(column=2,row=4, padx=10, pady=5)

window.mainloop()

