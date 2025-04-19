import os
import tkinter as tk
from tkinter import messagebox
from mcq_reader import read_mcqs

class MCQApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Multiple Choice Quiz")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.mcqs = []
        self.current_question_index = 0
        self.score = 0

        # Main Frame
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack(expand=True)

        # Progress Label
        self.progress_label = tk.Label(self.main_frame, text="Question 1", font=("Arial", 12), fg="blue")
        self.progress_label.pack(pady=5)

        # Question Label
        self.question_label = tk.Label(self.main_frame, text="", wraplength=500, font=("Arial", 14), justify="left")
        self.question_label.pack(pady=20)

        # Options
        self.options_var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.main_frame, text="", variable=self.options_var, value=f"Option {i}",
                                 font=("Arial", 12), wraplength=500, anchor="w", command=self.check_answer)
            btn.pack(anchor="w", pady=5)
            self.option_buttons.append(btn)

        # Feedback Label
        self.feedback_label = tk.Label(self.main_frame, text="", wraplength=500, font=("Arial", 12), fg="green")
        self.feedback_label.pack(pady=10)

        # Navigation Frame
        self.nav_frame = tk.Frame(self.main_frame)
        self.nav_frame.pack(pady=20)

        # Next Button
        self.next_button = tk.Button(self.nav_frame, text="Skip", command=self.next_question, font=("Arial", 12),
                                     bg="#4CAF50", fg="white", padx=10, pady=0)
        self.next_button.pack(side="left", padx=10)

        # Question Selector Entry and Button
        self.question_selector_entry = tk.Entry(self.nav_frame, font=("Arial", 12), width=5)
        self.question_selector_entry.pack(side="left", padx=10)

        self.question_selector_button = tk.Button(self.nav_frame, text="Go", command=self.select_question_by_number,
                                                  font=("Arial", 12), bg="#2196F3", fg="white", padx=10, pady=0)
        self.question_selector_button.pack(side="left", padx=10)

        # Load MCQs and Display the First Question
        mcq_file_path = os.path.join(os.path.dirname(__file__), "assets", "input.txt")
        self.load_mcqs(mcq_file_path)
        self.display_question()

    def load_mcqs(self, file_path):
        if os.path.exists(file_path):
            self.mcqs = read_mcqs(file_path)
        else:
            messagebox.showerror("Error", f"{file_path} not found.")
            self.master.quit()

    def select_question_by_number(self):
        try:
            question_number = int(self.question_selector_entry.get())
            if 1 <= question_number <= len(self.mcqs):
                self.current_question_index = question_number - 1
                self.display_question()
            else:
                self.feedback_label.config(text="Invalid question number. Try again.", fg="red")
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.", fg="red")

    def display_question(self):
        if self.current_question_index < len(self.mcqs):
            mcq = self.mcqs[self.current_question_index]
            self.progress_label.config(text=f"Question {self.current_question_index + 1} of {len(self.mcqs)}")
            self.question_label.config(text=mcq['question'])
            self.options_var.set(None)  # Reset selected option
            for i, option in enumerate(mcq['options']):
                self.option_buttons[i].config(text=option, value=option[0])  # Set value to A, B, C, or D
            self.feedback_label.config(text="")  # Clear feedback
            self.next_button.config(text="Skip")  # Set button text to "Skip"
        else:
            self.end_quiz()

    def check_answer(self):
        selected_answer = self.options_var.get()
        correct_answer = self.mcqs[self.current_question_index]['answer']
        if selected_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", fg="red")
        self.next_button.config(state=tk.NORMAL, text="Next")  # Enable "Next" button

    def next_question(self):
        self.current_question_index += 1
        self.display_question()

    def end_quiz(self):
        retry = messagebox.askyesno("Quiz Finished", f"You scored {self.score}/{len(self.mcqs)}.\nDo you want to retake the quiz?")
        if retry:
            self.current_question_index = 0
            self.score = 0
            self.display_question()
        else:
            self.master.quit()

def main():
    root = tk.Tk()
    app = MCQApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()