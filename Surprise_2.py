import tkinter as tk
from tkinter import messagebox
import random

# Define more surprises
new_quotes = [
    "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "What we think, we become. - Buddha",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "Be yourself; everyone else is already taken. - Oscar Wilde",
]

scientific_facts = [
    "The human brain has about 86 billion neurons.",
    "Water can boil and freeze at the same time, under the right conditions (the triple point).",
    "There are more stars in the universe than grains of sand on Earth.",
    "The speed of sound is faster in water than in air.",
    "The largest known volcano in the solar system is on Mars (Olympus Mons).",
]

inspirational_facts = [
    "The word 'impossible' itself says 'I'm possible'.",
    "Failure is the stepping stone to success.",
    "You are braver than you believe, stronger than you seem, and smarter than you think.",
    "Dream big and dare to fail.",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
]

# Combine the surprises
new_surprises = new_quotes + scientific_facts + inspirational_facts

# Function to show a random surprise
def new_surprise_me():
    surprise = random.choice(new_surprises)
    messagebox.showinfo("Your Surprise!", surprise)

# Create a new application window
app = tk.Tk()
app.title("Surprise Me!")
app.geometry("450x450")
app.configure(bg="#34495e")

# Add a fancy header label
header_label = tk.Label(app, text="Ready for another surprise?", 
                        font=("Comic Sans MS", 18, "bold"), 
                        bg="#34495e", fg="#ecf0f1")
header_label.pack(pady=60)

# Add a fun surprise button
new_button = tk.Button(app, 
                        text="Surprise Me Again!", 
                        font=("Verdana", 14, "bold"), 
                        bg="#e74c3c", 
                        fg="white", 
                        activebackground="#c0392b", 
                        activeforeground="white", 
                        relief="groove", 
                        bd=8,
                        command=new_surprise_me)
new_button.pack(pady=30)

# Add a footer label
footer_label = tk.Label(app, text="Enjoy the wonders of knowledge!", 
                         font=("Arial", 12, "italic"), 
                         bg="#34495e", fg="#bdc3c7")
footer_label.pack(pady=20)

# Run the application
app.mainloop()
