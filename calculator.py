import tkinter as tk
from tkinter import font

class PyCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("PyCalculator")
        self.root.geometry("300x450")  # Increased height to accommodate equals button
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        # Create custom fonts
        self.display_font = font.Font(family="Arial", size=14)
        self.button_font = font.Font(family="Arial", size=12, weight="bold")
        
        # Initialize calculator state
        self.current_input = ""
        self.result = ""
        self.last_button = ""
        
        # Create display frames
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Configure grid weights
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1, uniform="btn")

    def create_display(self):
        # Expression display (top)
        self.expression_frame = tk.Frame(self.root, bg="#e0e0e0", height=30)
        self.expression_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10, 0))
        self.expression_label = tk.Label(
            self.expression_frame, 
            text="", 
            anchor="e", 
            bg="#e0e0e0", 
            fg="#333333", 
            font=self.display_font
        )
        self.expression_label.pack(fill="both", expand=True, padx=10)
        
        # Result display (bottom)
        self.result_frame = tk.Frame(self.root, bg="#f5f5f5", height=40)
        self.result_frame.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=(0, 10))
        self.result_label = tk.Label(
            self.result_frame, 
            text="0", 
            anchor="e", 
            bg="#f5f5f5", 
            fg="#000000", 
            font=("Arial", 18, "bold")
        )
        self.result_label.pack(fill="both", expand=True, padx=10)

    def create_buttons(self):
        # Button layout configuration
        buttons = [
            ["(", ")", "DEL", "AC"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "^", "+"]
        ]
        
        # Create buttons in a grid
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                # Create button with custom styling
                btn = tk.Button(
                    self.root,
                    text=btn_text,
                    font=self.button_font,
                    bg="#ffffff" if btn_text not in ["AC", "DEL"] else "#ff9999",
                    fg="#333333",
                    relief="flat",
                    overrelief="groove",
                    borderwidth=1,
                    command=lambda t=btn_text: self.on_button_click(t)
                )
                btn.grid(row=row_idx+2, column=col_idx, sticky="nsew", padx=2, pady=2)
                
                # Style the operator buttons
                if btn_text in ["/", "*", "-", "+", "^"]:
                    btn.config(bg="#e6e6e6")
        
        # Create equals button spanning all columns
        equals_btn = tk.Button(
            self.root,
            text="=",
            font=self.button_font,
            bg="#99ccff",
            fg="#000000",
            relief="flat",
            overrelief="groove",
            borderwidth=1,
            command=lambda: self.on_button_click("=")
        )
        equals_btn.grid(row=7, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)

    def on_button_click(self, button_text):
        if button_text == "AC":
            # Clear all
            self.current_input = ""
            self.result = ""
            self.expression_label.config(text="")
            self.result_label.config(text="0")
        elif button_text == "DEL":
            # Delete last character
            self.current_input = self.current_input[:-1]
            self.expression_label.config(text=self.current_input)
            # Update result display with current input if not empty
            if self.current_input:
                self.result_label.config(text=self.current_input)
            else:
                self.result_label.config(text="0")
        elif button_text == "=":
            # Evaluate expression
            if not self.current_input:
                return  # Nothing to evaluate
                
            try:
                # Replace exponentiation operator
                expression = self.current_input.replace("^", "**")
                result = eval(expression)
                # Format the result
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.result = str(result)
                self.result_label.config(text=self.result)
                # Keep the expression in the top display
                self.expression_label.config(text=self.current_input)
                # Set current input to the result for further calculations
                self.current_input = self.result
            except Exception as e:
                self.result_label.config(text="Error")
                self.current_input = ""
        else:
            # Append button text to current input
            self.current_input += button_text
            self.expression_label.config(text=self.current_input)
            # Update result display with current input
            self.result_label.config(text=self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    app = PyCalculator(root)
    root.mainloop()