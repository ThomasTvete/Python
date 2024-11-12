import tkinter as tk
import random

class DecisionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hvalg")

        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=1)

        self.choices = []
        
        self.label = tk.Label(root, text="Skriv inn dine valg, separer de med komma:")
        self.label.grid(row=0, column=1)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.grid(row=1, column=1)
        
        self.start_button = tk.Button(root, text="Start", command=self.do_the_shuffle)
        self.start_button.grid(row=2, column=1)
        
        self.choice_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.choice_label.grid(row=3, column=1)
        
        self.fuck_button = tk.Button(root, text="FUCK", command=self.remove_choice)
        self.fuck_button.grid(row=4, column=0)
        self.fuck_button.grid_remove()
        
        self.yay_button = tk.Button(root, text="YAY", command=lambda: self.confirm_choice(True)) # forskjeller på lambda og =>?
        self.yay_button.grid(row=4, column=2, columnspan=2)
        self.yay_button.grid_remove()
        
        self.root.bind("<Button-1>", self.select_choice)
        
    def do_the_shuffle(self):
        self.choices = self.entry.get().split(',')
        self.shuffle_choices()
        
    def shuffle_choices(self):
        if self.choices:
            random_choice = random.choice(self.choices)
            self.choice_label.config(text=random_choice)
            self.shuffle_timer = self.root.after(100, self.shuffle_choices)
        
    def select_choice(self, event): # trenger å ta med et event argument pga slik binding funker(?), bruk det til å sjekke man klikker rett sted kanskje?
        clicked_spot = event.widget

        if clicked_spot == self.choice_label and self.choice_label.cget("text"):
            self.root.after_cancel(self.shuffle_timer)
            self.fuck_button.grid()
            self.yay_button.grid()
        
    def remove_choice(self):
        selected_choice = self.choice_label.cget("text")
        if selected_choice in self.choices:
            self.choices.remove(selected_choice) # muligens et problem, sjekk senere
        if len(self.choices) > 1:
            self.fuck_button.grid_remove()
            self.yay_button.grid_remove()
            self.shuffle_choices()
        else:
            self.confirm_choice(False)
        
    def confirm_choice(self,yay_choice):
        if yay_choice:
            selected_choice = self.choice_label.cget("text")
        elif not yay_choice:
            selected_choice = self.choices[0]
        self.choice_label.config(text=f"Du valgte {selected_choice}! Gratulerer?")
        self.fuck_button.grid_remove()
        self.yay_button.grid_remove()
        self.root.after(5000, self.root.quit)
        

root = tk.Tk()
app = DecisionApp(root)
root.mainloop()