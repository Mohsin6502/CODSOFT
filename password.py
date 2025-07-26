import tkinter as tk
from tkinter import ttk
import random
import string
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Generate Password")
        self.root.geometry("450x350")
        self.root.configure(bg='#f0f4f8')
        
        # Character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation
        
        # GUI Elements
        self.create_gui()
        
    def create_gui(self):
        # Title
        title = tk.Label(self.root, text="Generate Password", font=('Arial', 16, 'bold'), bg='#f0f4f8', fg='#2c3e50')
        title.pack(pady=10)
        
        # Generated Password
        frame_pass = tk.Frame(self.root, bg='#f0f4f8')
        frame_pass.pack(pady=10)
        tk.Label(frame_pass, text="Generated Password:", font=('Arial', 10), bg='#f0f4f8', fg='#34495e').pack(side=tk.LEFT)
        self.pass_var = tk.StringVar()
        entry = tk.Entry(frame_pass, textvariable=self.pass_var, width=20, font=('Arial', 10), bg='#ffffff', fg='#2c3e50', relief='flat', bd=2)
        entry.pack(side=tk.LEFT, padx=5)
        
        # Make the generate button small but visible
        tk.Button(
            frame_pass,
            text="↻ Generate",
            font=('Arial', 9, 'bold'),
            bg='#f39c12',  # bright orange
            fg='#ffffff',
            activebackground='#e67e22',
            activeforeground='#ffffff',
            relief='raised',
            bd=2,
            padx=4,
            pady=1,
            width=8,  # small width
            height=1,
            command=self.generate_password
        ).pack(side=tk.LEFT, padx=8)
        
        # Password Strength
        frame_strength = tk.Frame(self.root, bg='#f0f4f8')
        frame_strength.pack(pady=5)
        tk.Label(frame_strength, text="Password Strength:", font=('Arial', 10), bg='#f0f4f8', fg='#34495e').pack(side=tk.LEFT)
        self.strength_var = tk.StringVar(value="Weak")
        self.strength_label = tk.Label(frame_strength, textvariable=self.strength_var, font=('Arial', 10, 'bold'), bg='#f0f4f8', fg='#e74c3c')
        self.strength_label.pack(side=tk.LEFT, padx=10)
        strength_bar = ttk.Progressbar(frame_strength, variable=self.strength_var, maximum=100, length=200, style='custom.Horizontal.TProgressbar')
        strength_bar.pack(side=tk.LEFT, padx=5)
        
        # Style for progress bar
        style = ttk.Style()
        style.configure('custom.Horizontal.TProgressbar', background='#27ae60', troughcolor='#ecf0f1')
        
        # Password Length
        frame_length = tk.Frame(self.root, bg='#f0f4f8')
        frame_length.pack(pady=5)
        tk.Label(frame_length, text="Password Length:", font=('Arial', 10), bg='#f0f4f8', fg='#34495e').pack(side=tk.LEFT)
        self.length_var = tk.IntVar(value=6)
        tk.Spinbox(frame_length, from_=4, to_=32, textvariable=self.length_var, width=5, font=('Arial', 10), bg='#ffffff', fg='#2c3e50', relief='flat').pack(side=tk.LEFT)
        
        # Characters to include
        tk.Label(self.root, text="Characters to include", font=('Arial', 10), bg='#f0f4f8', fg='#34495e').pack(pady=5)
        frame_checks = tk.Frame(self.root, bg='#f0f4f8')
        frame_checks.pack()
        self.use_uppercase = tk.BooleanVar(value=True)
        self.use_lowercase = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        
        tk.Checkbutton(frame_checks, text="Upper Case Letters", variable=self.use_uppercase, font=('Arial', 10), bg='#f0f4f8', fg='#34495e', activebackground='#f0f4f8', selectcolor='#f0f4f8').pack(anchor=tk.W)
        tk.Checkbutton(frame_checks, text="Lower Case Letters", variable=self.use_lowercase, font=('Arial', 10), bg='#f0f4f8', fg='#34495e', activebackground='#f0f4f8', selectcolor='#f0f4f8').pack(anchor=tk.W)
        tk.Checkbutton(frame_checks, text="Numbers (0-9)", variable=self.use_digits, font=('Arial', 10), bg='#f0f4f8', fg='#34495e', activebackground='#f0f4f8', selectcolor='#f0f4f8').pack(anchor=tk.W)
        tk.Checkbutton(frame_checks, text="Symbols (! @ # $ %)", variable=self.use_symbols, font=('Arial', 10), bg='#f0f4f8', fg='#34495e', activebackground='#f0f4f8', selectcolor='#f0f4f8').pack(anchor=tk.W)
        
        # Buttons
        frame_buttons = tk.Frame(self.root, bg='#f0f4f8')
        frame_buttons.pack(pady=20)
        tk.Button(frame_buttons, text="Cancel", font=('Arial', 10), bg='#e74c3c', fg='#ffffff', relief='flat', command=self.root.quit).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_buttons, text="Accept Password", font=('Arial', 10), bg='#2ecc71', fg='#ffffff', relief='flat', command=self.accept_password).pack(side=tk.RIGHT, padx=5)
        tk.Button(frame_buttons, text="?", font=('Arial', 10, 'bold'), bg='#3498db', fg='#ffffff', relief='flat', command=self.show_help).pack(side=tk.RIGHT, padx=5)
        
    def generate_password(self):
        length = self.length_var.get()
        chars = ""
        if self.use_uppercase.get(): chars += self.uppercase
        if self.use_lowercase.get(): chars += self.lowercase
        if self.use_digits.get(): chars += self.digits
        if self.use_symbols.get(): chars += self.symbols
        if not chars:
            self.pass_var.set("Select at least one character type!")
            self.strength_var.set("Weak")
            self.strength_label.config(fg="#e74c3c")
            return
        password = ''.join(random.choice(chars) for _ in range(length))
        self.pass_var.set(password)
        # Strength assessment
        strength_score = min(100, (len(chars) + length) * 5)
        if strength_score > 70:
            self.strength_var.set("Strong")
            self.strength_label.config(fg="#27ae60")  # green
        elif strength_score > 40:
            self.strength_var.set("Medium")
            self.strength_label.config(fg="#f39c12")  # orange
        else:
            self.strength_var.set("Weak")
            self.strength_label.config(fg="#e74c3c")  # red
            
    def accept_password(self):
        password = self.pass_var.get()
        if password and "Select" not in password:
            messagebox.showinfo("Success", f"Password '{password}' accepted!")
            
    def show_help(self):
        messagebox.showinfo("Help", "Generate a strong password by selecting character types and length.")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()