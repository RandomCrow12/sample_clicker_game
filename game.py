import customtkinter as ctk
import random

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

cl_up = 100

num_one = 2
num_two = 3

up_cost_pt = 30
up_cost_mult = 20
up_cost_power = 40
up_cost_math = 50

math_upg_num = 0



        

def buttons():
    # add points to top left and an upgrade menu with labels & buttons on the right
    # make a math menu that required you to do math on two numbers & then gives you the result in points if you do it right (start w/ 0-10 w/ addition then upgrade)
    # make a randomly appearing clicker event that's an actual clicker and gives base 100 points but can give more
    # 
    # add visuals eventually... so like https://www.youtube.com/watch?v=E_2HaiqRcjY 
    # and have a random event for a clicker which gives a ton of points and make the sound?? -> that's if I actually cared enough

    def check_win_con():
        global points
        if points > 1000000:
            print("victory")
            info_print("victory")

    score_label = ctk.CTkLabel(root, text="0", font=("Arial", 20))
    score_label.grid(row=1, column=0, padx=10)

    def info_print(to_print):
        score_label.configure(text=str(to_print))

    def click1():
       global points
       global pt_multiplier
       global pt_up
       global pt_power

       points = points + (((pt_up)* pt_multiplier) ** pt_power)
       info_print(points)
       check_win_con()
    
    def add():
        global num_one
        global num_two
        global pt_multiplier
        global pt_power
        global points

        try:
            inp = int(entry.get())
        except ValueError:
            return

        if (num_one + num_two == inp):
            points = points + (((inp)* pt_multiplier) ** pt_power)
            info_print(points)
            check_win_con()

            num_one = random.randint(0, 9) + (math_upg_num*random.randint(0, 9))
            num_two = random.randint(0, 9) + (math_upg_num*random.randint(0, 9))

            math1.configure(text=f"{num_one} + {num_two} =")
            entry.delete(0, "end")

    def upg_button():
        global up_cost_pt
        global pt_up
        global points

        if (up_cost_pt <= points):
            points = points - up_cost_pt
            pt_up += 1
            up_cost_pt += 30*pt_up
            info_print(points)
            u2.configure(text=f"button: {up_cost_pt}")
        
    def upg_mult():
        global up_cost_mult
        global pt_multiplier
        global points

        if (up_cost_mult <= points):
            points = points - up_cost_mult
            pt_multiplier += 1
            up_cost_mult *= 8
            info_print(points)
            u3.configure(text=f"mult: {up_cost_mult}")
        
    def upg_power():
        global up_cost_power
        global pt_power
        global points

        if (up_cost_power <= points):
            points = points - up_cost_power
            pt_power += 1
            up_cost_power = up_cost_power*80
            info_print(points)
            u4.configure(text=f"power: {up_cost_power}")
    def upg_math():
        global up_cost_math
        global math_upg_num
        global points

        if (up_cost_math <= points):
            points = points - up_cost_math
            math_upg_num += 1
            up_cost_math = up_cost_math+100
            info_print(points)
            u5.configure(text=f"math: {up_cost_math}")

    # interact with
    g1 = ctk.CTkButton(root, text=":3", command= click1 , font=("Ariel", 20), height=150, width=150)  # actual buttons that do above commands
    g1.grid(row=2, column=0, padx=10,pady=10)
    
    math1 = ctk.CTkLabel(root, text = f"{num_one} + {num_two} =", font=("Ariel", 20))
    math1.grid(row=4, column=0)
    entry = ctk.CTkEntry(root, placeholder_text="?")
    entry.grid(row=4, column=1)
    math_solve = ctk.CTkButton(root, text="->", command= add, font=("Ariel", 20), width=150)  # actual buttons that do above commands
    math_solve.grid(row=4, column=2, padx=10)


    # upgrades
    uLabel = ctk.CTkLabel(root, text = "upgrades:", font=("Ariel", 20))
    uLabel.grid(row=0, column=3)
    u2 = ctk.CTkButton(root, text= f"button: {up_cost_pt}", command= upg_button , font=("Ariel", 20), width=150)  # actual buttons that do above commands
    u2.grid(row=2, column=3, padx=10,pady=10)
    u3 = ctk.CTkButton(root, text= f"mult: {up_cost_mult}", command= upg_mult , font=("Ariel", 20), width=150)  # actual buttons that do above commands
    u3.grid(row=3, column=3, padx=10,pady=10)
    u4 = ctk.CTkButton(root, text= f"power: {up_cost_power}", command= upg_power , font=("Ariel", 20), width=150)  # actual buttons that do above commands
    u4.grid(row=4, column=3, padx=10,pady=10)
    u5 = ctk.CTkButton(root, text= f"math: {up_cost_math}", command= upg_math , font=("Ariel", 20), width=150)  # actual buttons that do above commands
    u5.grid(row=5, column=3, padx=10,pady=10)

    

# https://stackoverflow.com/questions/75426884/how-to-use-image-as-button-in-customtkinter

# start
def start():
    buttons()
    root.mainloop()

# if __name__ == "__main__":
#     start()