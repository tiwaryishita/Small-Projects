from tkinter import *
from textblob import TextBlob

def check_spelling():
    a=TextBlob(spell_check.get())
    spell=Label(window,text="The correct spelling is :",font=("Arial",30,"bold"),bg="white")
    spell.pack()
    correct_text=Label(window,text=str(a.correct()),font=("Arial",45,"bold"),bg="white")
    correct_text.pack()

window=Tk()
window.title("My Spelling Checker")
window.geometry("800x600")
window.config(background="white")

text_heading=Label(window,text="Spelling Checker",font=("Arial",50,"bold"),bg="white",fg="black")
text_heading.pack()

text_check=Label(window,text="Enter the spelling",font=("Arial",35,"bold"),bg="black",fg="white")
text_check.pack()

spell_check=Entry(window,font=("Arial",45,"bold"),width=500,bg="white")
spell_check.pack()

Check_button=Button(window,text="Check!!",font=("Arial",30,"bold"),fg="white",bg="red",command=check_spelling)
Check_button.pack()

window.mainloop()
