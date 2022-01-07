from MakeBlosum import *
from Tkinter import *

window = Tk()
window.title("BLOSSUM APPLICATION")
window.geometry('600x350')
window.configure(background='palegreen')

lbl=Label(window,text
          ="BLOSUM APPLICATION",fg="navy",bg="palegreen",font=("Times New Roman", 30))
lbl.pack()

lbl1=Label(window,text="By Nur Aina, Jeanny, Sophia\n\n",fg="navy",bg="palegreen",font=("Arial", 10))
lbl1.pack()

lbl2=Label(window,text="What is Blosum?",fg="navy", bg="palegreen", font=("Arial Bold", 15))
lbl2.pack()

lbl3=Label(window,text="BLOSUM (BLOcks SUbstitution Matrix) matrix is a substitution matrix used\n" 
            "for sequence alignment of proteins. BLOSUM matrices are used to score alignments\n"
            "between evolutionarily divergent protein sequences. They are based on local alignments.\n\n",fg="navy",bg="palegreen",font=("Arial", 10))
lbl3.pack()

lbl4=Label(window,text="This application will perform BLOSUM on the desired csv file.\n"
           "Once you have click the button below, you will need to enter the file you wish to calculate.\n\n",fg="navy", bg="palegreen", font=("Arial", 10))
lbl4.pack()

lbl5=Label(window,text="To start BLOSUM application, please click the button below.",fg="navy", bg="palegreen", font=("Arial", 10))
lbl5.pack()

def clicked():
    window.destroy()
    MakeBlosum().main()
       
btn = Button(window, text="START",command=clicked)
btn.pack()

window.mainloop()

