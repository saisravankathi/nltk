from tkinter import *
from who import *
import os

class ScrollTxtArea:
    
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.textPad(frame)
        self.createEntry(frame)
        self.createButton(frame)
        self.textArea(frame)
        
    def textPad(self,frame):
        textPad = Frame(frame)
        self.text = Text(textPad, height=8, width=90)
              
        scroll = Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)

        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)
        self.text.get("1.0",END)
        
    def textArea(self,frame):
        textArea = Frame(frame)
        self.textResult = Text(textArea, height=8, width=90)
        scroll = Scrollbar(textArea)
        self.textResult.configure(yscrollcommand=scroll.set)
        self.textResult.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        textArea.pack(side=TOP)
        self.textResult.get("1.0", END)
        
    def createEntry(self,frame):
        entryBox = Frame(frame)
        self.entry = Entry(entryBox)
        self.entry.pack(side=LEFT)
        entryBox.pack(side=TOP)
    
    def createButton(self,frame):
        button = Frame(frame)
        self.button = Button(button, text="Print",command=kathiPrint)
        self.button.pack(side=LEFT)
        button.pack(side=TOP)

    def printValue(self):
        self.textResult.insert(END,"\n"+self.entry.get())
        #Providing training data to the classifier.
    #     scriptpath = os.path.dirname(__file__)
    #     filename_who = os.path.join(scriptpath,'who.txt')
    #     filename_sample = os.path.join(scriptpath, 'sample.txt')
    # 
    #     whoText = open(filename_who, 'r')
    #     sampleText = open(filename_sample, 'r')
    #     classifyer = Classifier()
    #     classifyer.kathi(whoText,sampleText,self.textResult.get("1.0",END))
    #     print (classifyer.finalListOfSentences)
        
    def getValues(self, clasifier):
        self.textResult.insert(END,"\nQustion:"+foo.entry.get())
        print(clasifier.fL)
        #for v in clasifier.fL:
            #self.textResult.insert(END, "\n"+v.key()+": "+v.value())
        

def kathiPrint():
      #Providing training data to the classifier.
    scriptpath = os.path.dirname(__file__)
    filename_when = os.path.join(scriptpath,'when.txt')
    filename_where = os.path.join(scriptpath, 'where.txt')

    whenText = open(filename_when, 'r')
    whereText = open(filename_where, 'r')
    c = Classifier(whenText,whereText,foo.text.get("1.0",END),dict())
    foo.getValues(c)
    
root = Tk()
root.resizable(width=False, height=False)
foo = ScrollTxtArea(root)
    # a = foo.printValue()
    # print(a)
root.title('Text with Scroll')
root.mainloop()

