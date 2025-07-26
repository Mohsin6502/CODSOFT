import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors ✊🖐✌️")
        self.root.geometry("480x400")
        self.root.configure(bg='#232946')  # Modern dark blue
        self.anonymous_score = 0
        self.pc_score = 0
        self.pc_choice = ""
        self.create_gui()

    def create_gui(self):
        # Title
        tk.Label(self.root, text="Rock Paper Scissors", font=('Segoe UI', 22, 'bold'), bg='#121629', fg='#eebbc3', pady=10).pack(fill='x')

        # Player Labels
        frame_players = tk.Frame(self.root, bg='#232946')
        frame_players.pack(pady=10, fill='x')
        tk.Label(frame_players, text="Player 1 : Anonymous", font=('Segoe UI', 12, 'bold'), bg='#232946', fg='#eebbc3').pack(side=tk.LEFT, padx=30)
        tk.Label(frame_players, text="Player 2 : Computer", font=('Segoe UI', 12, 'bold'), bg='#232946', fg='#eebbc3').pack(side=tk.RIGHT, padx=30)

        # Buttons Frame
        frame_buttons = tk.Frame(self.root, bg='#232946')
        frame_buttons.pack(pady=18)
        # Modern buttons with emojis
        tk.Button(frame_buttons, text="✊ Rock", font=('Segoe UI', 12, 'bold'), bg='#eebbc3', fg='#232946', activebackground='#b8c1ec', activeforeground='#232946', relief='raised', bd=2, width=10, command=lambda: self.play('rock')).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_buttons, text="🖐 Paper", font=('Segoe UI', 12, 'bold'), bg='#b8c1ec', fg='#232946', activebackground='#eebbc3', activeforeground='#232946', relief='raised', bd=2, width=10, command=lambda: self.play('paper')).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_buttons, text="✌️ Scissor", font=('Segoe UI', 12, 'bold'), bg='#eebbc3', fg='#232946', activebackground='#b8c1ec', activeforeground='#232946', relief='raised', bd=2, width=10, command=lambda: self.play('scissor')).pack(side=tk.LEFT, padx=10)

        # Computer Choice Display
        self.pc_opted = tk.Label(self.root, text="PC Opted: ", font=('Segoe UI', 13, 'bold'), bg='#232946', fg='#b8c1ec')
        self.pc_opted.pack(pady=8)

        # Scores
        score_frame = tk.Frame(self.root, bg='#232946')
        score_frame.pack(pady=5)
        self.score_anon = tk.Label(score_frame, text="Anonymous Score: 0", font=('Segoe UI', 12, 'bold'), bg='#232946', fg='#eebbc3', relief='groove', bd=2, width=20)
        self.score_anon.pack(side=tk.LEFT, padx=10)
        self.score_pc = tk.Label(score_frame, text="PC Score: 0", font=('Segoe UI', 12, 'bold'), bg='#232946', fg='#eebbc3', relief='groove', bd=2, width=20)
        self.score_pc.pack(side=tk.RIGHT, padx=10)

        # Result
        self.result = tk.Label(self.root, text="", font=('Segoe UI', 14, 'bold'), bg='#232946', fg='#f6c90e')
        self.result.pack(pady=10)

        # Close Game Button
        tk.Button(self.root, text="Close Game", font=('Segoe UI', 11, 'bold'), bg='#f6c90e', fg='#232946', activebackground='#eebbc3', activeforeground='#232946', relief='raised', bd=2, padx=10, pady=2, command=self.root.quit).pack(pady=15)

    def play(self, user_choice):
        choices = ['rock', 'paper', 'scissor']
        computer_choice = random.choice(choices)
        self.pc_choice = computer_choice
        if user_choice == computer_choice:
            result = "It's a tie!"
            color = '#b8c1ec'
        elif (user_choice == 'rock' and computer_choice == 'scissor') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissor' and computer_choice == 'paper'):
            result = "Anonymous Won! 🎉"
            color = '#27ae60'
            self.anonymous_score += 1
        else:
            result = "PC Won! 💻"
            color = '#e74c3c'
            self.pc_score += 1
        self.score_anon.config(text=f"Anonymous Score: {self.anonymous_score}")
        self.pc_opted.config(text=f"PC Opted: {computer_choice.capitalize()}")
        self.score_pc.config(text=f"PC Score: {self.pc_score}")
        self.result.config(text=result, fg=color)
        
def main():
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()