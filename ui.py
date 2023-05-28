from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=('Comic Sans MS',20,'italic','underline','bold'))
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="cyan")
        # self.question_text = self.canvas.create_text(text="Some Question Text",fill=THEME_COLOR)
        self.question_text = self.canvas.create_text(150,125,text="Some Question Text", fill='dark orange',font=('Roboto',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true_img = PhotoImage(file='images/true.png')
        self.true_btn = Button(image=self.true_img)
        self.true_btn.grid(row=2,column=0)

        self.false_img = PhotoImage(file='images/false.png')
        self.false_btn = Button(image=self.false_img)
        self.false_btn.grid(row=2,column=1)


        self.window.mainloop()