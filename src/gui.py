from tkinter import Tk, Label, Button, Radiobutton, StringVar, messagebox
import mcq_reader

class MCQApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Multiple Choice Quiz")
        self.mcqs = mcq_reader.read_mcqs("src/assets/input.txt")
        self.current_question_index = 0
        self.score = 0

        # Question Label
        self.question_label = Label(master, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Options
        self.selected_option = StringVar()
        self.option_buttons = []
        for i in range(4):
            button = Radiobutton(master, text="", variable=self.selected_option, value=f"Option {i}", font=("Arial", 12), wraplength=400)
            button.pack(anchor="w", padx=20, pady=5)
            self.option_buttons.append(button)

        # Feedback Label
        self.feedback_label = Label(master, text="", font=("Arial", 12), fg="green")
        self.feedback_label.pack(pady=10)

        # Next Button
        self.next_button = Button(master, text="Next", command=self.next_question, state="disabled", font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.mcqs):
            mcq = self.mcqs[self.current_question_index]
            self.question_label.config(text=mcq['question'])
            self.selected_option.set(None)  # Reset selected option
            for i, option in enumerate(mcq['options']):
                self.option_buttons[i].config(text=option, value=option[0])  # Set value to A, B, C, or D
            self.feedback_label.config(text="")  # Clear feedback
            self.next_button.config(state="disabled")  # Disable "Next" button until an answer is selected
        else:
            self.show_score()

    def check_answer(self):
        mcq = self.mcqs[self.current_question_index]
        selected_answer = self.selected_option.get()
        if selected_answer == mcq['answer']:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer is: {mcq['answer']}", fg="red")
        self.next_button.config(state="normal")  # Enable "Next" button

    def next_question(self):
        self.current_question_index += 1
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Finished", f"You scored {self.score}/{len(self.mcqs)}.")
        self.master.quit()

def main():
    root = Tk()
    app = MCQApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()