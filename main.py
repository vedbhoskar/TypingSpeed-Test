import tkinter as tk
import random
import time

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Test App")
        self.root.geometry("400x200")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Hello, how are you?",
            "Python is a popular programming language.",
            "Change your thoughts and you change your world.",
            "The future belongs to those who believe in the beauty of their dreams.",
            "Don't watch the clock; do what it does. Keep going.",
            "Strive not to be a success, but rather to be of value.",
            "The only way to do great work is to love what you do.",
            "The secret of getting ahead is getting started.",
            "Your time is limited, don't waste it living someone else's life."
        ]
        self.current_sentence = ""

        self.timer_running = False
        self.start_time = 0

        self.create_widgets()

    def create_widgets(self):
        self.lbl_instruction = tk.Label(self.root, text="Type the following sentence:")
        self.lbl_instruction.pack(pady=10)

        self.lbl_sentence = tk.Label(self.root, text=self.generate_sentence())
        self.lbl_sentence.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.btn_submit = tk.Button(self.root, text="Submit", command=self.check_input)
        self.btn_submit.pack()

        self.lbl_result = tk.Label(self.root, text="")
        self.lbl_result.pack(pady=10)

        self.btn_again = tk.Button(self.root, text="Try Again", command=self.try_again, state=tk.DISABLED)
        self.btn_again.pack()

    def generate_sentence(self):
        self.current_sentence = random.choice(self.sentences)
        return self.current_sentence

    def check_input(self):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True

        input_text = self.entry.get()
        if input_text == self.current_sentence:
            self.timer_running = False
            elapsed_time = time.time() - self.start_time
            self.lbl_result.config(text=f"Speed: {self.calculate_speed(elapsed_time)} wpm")
            self.btn_again.config(state=tk.NORMAL)
        else:
            self.lbl_result.config(text="Incorrect input. Try again.")

    def calculate_speed(self, elapsed_time):
        words = self.current_sentence.split()
        word_count = len(words)
        
        if elapsed_time != 0:
            words_per_minute = (word_count / elapsed_time) * 60
            return round(words_per_minute)
        else:
            return 0

    def try_again(self):
        self.entry.delete(0, tk.END)
        self.lbl_sentence.config(text=self.generate_sentence())
        self.lbl_result.config(text="")
        self.btn_again.config(state=tk.DISABLED)

root = tk.Tk()
app = SpeedTestApp(root)
root.mainloop()
