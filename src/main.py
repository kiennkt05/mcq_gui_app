import os
import tkinter as tk
from tkinter import messagebox
from mcq_reader import read_mcqs

class MCQApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Multiple Choice Quiz")
        self.mcqs = []
        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(master, text="", wraplength=400)
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()
        self.option_buttons = []

        for i in range(4):
            btn = tk.Radiobutton(master, text="", variable=self.options_var, value="", command=self.check_answer)
            btn.pack(anchor='w')
            self.option_buttons.append(btn)

        self.feedback_label = tk.Label(master, text="", wraplength=400)
        self.feedback_label.pack(pady=10)

        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        # Replace the dropdown menu with an entry field and a button
        self.question_selector_label = tk.Label(master, text="Enter Question Number:")
        self.question_selector_label.pack(pady=5)

        self.question_selector_entry = tk.Entry(master)
        self.question_selector_entry.pack(pady=5)

        self.question_selector_button = tk.Button(master, text="Go", command=self.select_question_by_number)
        self.question_selector_button.pack(pady=5)

        mcq_file_path = os.path.join(os.path.dirname(__file__), "assets", "input.txt")
        self.load_mcqs(mcq_file_path)
        self.display_question()

    def load_mcqs(self, file_path):
        if os.path.exists(file_path):
            self.mcqs = read_mcqs(file_path)
            for i, mcq in enumerate(self.mcqs):
                print(f"Question {i + 1}: {mcq['question']}")
        else:
            messagebox.showerror("Error", f"{file_path} not found.")
            self.master.quit()

    def select_question(self, question_label):
        # Extract the question index from the label (e.g., "Question 1" -> index 0)
        question_index = int(question_label.split()[-1]) - 1
        self.current_question_index = question_index
        self.display_question()

    def select_question_by_number(self):
        try:
            # Get the question number from the entry field
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
            if mcq['question']:
                self.question_label.config(text=mcq['question'])
            else:
                self.question_label.config(text="Question not available.")
            for i, option in enumerate(mcq['options']):
                self.option_buttons[i].config(text=option, value=option[0])  # Set value to A, B, C, or D
            self.options_var.set(None)  # Reset selected option
            self.feedback_label.config(text="")  # Clear feedback
            self.next_button.config(state=tk.DISABLED)  # Disable the "Next" button until the correct answer is selected
        else:
            self.end_quiz()

    def check_answer(self):
        selected_answer = self.options_var.get()
        correct_answer = self.mcqs[self.current_question_index]['answer']
        if selected_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
            self.next_button.config(state=tk.NORMAL)  # Enable the "Next" button
        else:
            self.feedback_label.config(text="Incorrect! Try again.", fg="red")

    def next_question(self):
        print(f"Moving to question {self.current_question_index + 2}")  # Debugging
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