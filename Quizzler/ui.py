from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.iconbitmap("images/questionmark1.ico")
        self.window.config(padx=20, pady=20, bg="black")

        self.canvas = Canvas(width=500, height=354, bg="black", highlightthickness=0)

        self.background_img = PhotoImage(file="images/bg22.png")
        self.green_img = PhotoImage(file="images/bg_greenn.png")
        self.red_img = PhotoImage(file="images/bg_red.png")

        self.background = self.canvas.create_image(250, 177, image=self.background_img)
        self.questions = self.canvas.create_text(250, 177, width=350, text="Question", fill="white",
                                                 font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)

        self.score_label = Label(text="Score: 0", fg="white", bg="black", font=("Arial", 15, "bold"))
        self.score_label.grid(column=1, row=0)

        right_image = PhotoImage(file="images/checkmark22.png")
        self.right_button = Button(image=right_image, highlightthickness=0, bg="black", command=self.right_pressed)
        self.right_button.grid(column=0, row=3)

        wrong_image = PhotoImage(file="images/checkmark111.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, bg="black", command=self.wrong_pressed)
        self.wrong_button.grid(column=1, row=3)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.background, image=self.background_img)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.questions, text=f"You've reached the end of the quiz. "
                                                        f"Your final score is: {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def wrong_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.score(is_right)

    def right_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.score(is_right)

    def score(self, is_right):
        if is_right:
            self.canvas.itemconfig(self.background, image=self.green_img)
        else:
            self.canvas.itemconfig(self.background, image=self.red_img)
        self.window.after(1000, self.get_next_question)
