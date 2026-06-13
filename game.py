import customtkinter as ctk

# CTK settings
root = ctk.CTk()
root.title("Rules :3")
root.geometry("1500x750")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# stats
points = 0

pt_up = 1
pt_multiplier = 1
pt_power = 1

cl_up = 50
cl_multiplier = 1
cl_power = 1

math_multiplier = 1
math_power = 1

def buttons():
    # add points to top left and an upgrade menu with labels & buttons on the right
    # make a math menu that required you to do math on two numbers & then gives you the result in points if you do it right (start w/ 0-10 w/ addition then upgrade)
    # make a randomly appearing clicker event that's an actual clicker and gives base 10 points but can give more
    # 
    # add visuals eventually bc trying to train a puppy... so like https://www.youtube.com/watch?v=E_2HaiqRcjY 


    def info_print(to_print):
       disp = ctk.CTkLabel(root, text=f"{to_print}", font=("Ariel", 20))
       disp.grid(row=1, column=0, padx= 10) # fix location

    def click1():
       points = ((points + pt_up)* pt_multiplier) ** pt_power

       # check win con
       if points > 1000000:
           print("puppy trained")

    # interact with
    g1 = ctk.CTkButton(root, text=":3", command= click1 , font=("Ariel", 20), height=150, width=150)  # actual buttons that do above commands
    g1.grid(row=2, column=2, padx=10,pady=10)
    
    # upgrades
    g2 = ctk.CTkButton(root, text="upgrade button", command= click1 , font=("Ariel", 20), height=150, width=150)  # actual buttons that do above commands
    g2.grid(row=2, column=2, padx=10,pady=10)




# start
def start():
    buttons()
    root.mainloop()

if __name__ == "__main__":
    start()