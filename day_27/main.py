import tkinter

window = tkinter.Tk()
window.title("Introduction to Tkinter")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a label", font=("Roboto", 18))
label.pack()








window.mainloop()