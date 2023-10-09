'''
This is the main file of the website to check if a student is pass or fail based on their marks.
'''
from tkinter import Tk, Label, Entry, Button
class StudentResultChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Checker")
        self.math_label = Label(root, text="Math Marks:")
        self.math_label.pack()
        self.math_entry = Entry(root)
        self.math_entry.pack()
        self.science_label = Label(root, text="Science Marks:")
        self.science_label.pack()
        self.science_entry = Entry(root)
        self.science_entry.pack()
        self.english_label = Label(root, text="English Marks:")
        self.english_label.pack()
        self.english_entry = Entry(root)
        self.english_entry.pack()
        self.check_button = Button(root, text="Check Result", command=self.check_result)
        self.check_button.pack()
        self.result_label = Label(root, text="")
        self.result_label.pack()
    def check_result(self):
        math_marks = int(self.math_entry.get())
        science_marks = int(self.science_entry.get())
        english_marks = int(self.english_entry.get())
        total_marks = math_marks + science_marks + english_marks
        if math_marks >= 35 and science_marks >= 35 and english_marks >= 35 and total_marks >= 105:
            self.result_label.config(text="Pass")
        else:
            self.result_label.config(text="Fail")
root = Tk()
app = StudentResultChecker(root)
root.mainloop()