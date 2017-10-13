from tkinter import *
from who import *
import os
import time


class ScrollTxtArea:
    
    def __init__(self, root):
        frame = Frame(root)
        frameG = Frame(root)
        for f in (frame,frameG):
            f.grid(row=0, column=0, sticky="news")
        self.gifFrame(frameG,frame)
        raise_frame(frameG)
        self.textPad(frame)
        self.createEntry(frame)
        self.createButton(frame)
        self.createClearButton(frame)
        self.textArea(frame)
        root.bind_class("Text","<Control-a>",self.selectAllTextAreaText)
        
        
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
        self.entry.bind("<Return>", faqEnterPrint)
        self.entry.bind("<Control-a>", self.selectAllText)
        entryBox.pack(side=TOP)
    
    def createButton(self,frame):
        button = Frame(frame)
        self.button = Button(button, text="Print",command=faqPrint)
        self.button.pack(side=LEFT)
        button.pack(side=TOP)
        
    def createClearButton(self,frame):
        clearbutton = Frame(frame)
        self.clrbutton = Button(clearbutton, text="Clear",command=self.clearResults)
        self.clrbutton.pack(side=RIGHT)
        clearbutton.pack(side=TOP)
        
    def getValues(self, clasifier):
        #print("before ques: ",self.textResult.index("end-1c"))
        self.textResult.insert(END,"\nQustion:"+foo.entry.get())
        self.textResult.tag_add("question_txt",self.textResult.index("end-1c linestart"),self.textResult.index("end-1c"))
        self.textResult.tag_config("question_txt",foreground="green")
        for v in clasifier.fSet:
            #print("before ans: ",self.textResult.index("end-1c"))
            self.textResult.insert(END,"\nAnswer:"+v)
            #print("after ans: ",self.textResult.index("end-1c"))
            
    def getAlertValues(self):
        self.textResult.insert(END,"\nWarning: Please enter the question.")

    def clearResults(self):
        self.textResult.delete(1.0,END)
    
    def selectAllText(self,event):
        # select text after 50ms
        root.after(50, self.select_all, event.widget)

    def select_all(self,widget):
        # select text
        widget.select_range(0, 'end')
        # move cursor to the end
        widget.icursor('end')
        
    def selectAllTextAreaText(self, event):
        event.widget.tag_add("sel","1.0","end")
        
    def gifFrame(self, frameG,frame):
        lbl_with_my_gif = AnimatedGif(frameG, 'giphy.gif', 0.0833)  # (tkinter.parent, filename, delay between frames)
        lbl_with_my_gif.pack()  # Packing the label with the animated gif (grid works just as well)
        lbl_with_my_gif.start()  # Shows gif at first frame and we are ready to go
        gButton = Button(frameG, text="Investigate",command=lambda:raise_frame(frame))
        gButton.pack()

class AnimatedGif(Label):
	"""
	Class to show animated GIF file in a label
	Use start() method to begin animation, and set the stop flag to stop it
	"""
	def __init__(self, root, gif_file, delay=0.04):
		"""
		:param root: tk.parent
		:param gif_file: filename (and path) of animated gif
		:param delay: delay between frames in the gif animation (float)
		"""
		Label.__init__(self, root)
		self.root = root
		self.gif_file = gif_file
		self.delay = delay  # Animation delay - try low floats, like 0.04 (depends on the gif in question)
		self.stop = False  # Thread exit request flag

		self._num = 0

	def start(self):
		""" Starts non-threaded version that we need to manually update() """
		self.start_time = time.time()  # Starting timer
		self._animate()

	def stop(self):
		""" This stops the after loop that runs the animation, if we are using the after() approach """
		self.stop = True

	def _animate(self):
		try:
			self.gif = PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
			self.configure(image=self.gif)
			self._num += 1
		except TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
			self._num = 0
		if not self.stop:    # If the stop flag is set, we don't repeat
			self.root.after(int(self.delay*1000), self._animate)

	def start_thread(self):
		""" This starts the thread that runs the animation, if we are using a threaded approach """
		from threading import Thread  # We only import the module if we need it
		self._animation_thread = Thread()
		self._animation_thread = Thread(target=self._animate_thread).start()  # Forks a thread for the animation

	def stop_thread(self):
		""" This stops the thread that runs the animation, if we are using a threaded approach """
		self.stop = True

	def _animate_thread(self):
		""" Updates animation, if it is running as a separate thread """
		while self.stop is False:  # Normally this would block mainloop(), but not here, as this runs in separate thread
			try:
				time.sleep(self.delay)
				self.gif = PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
				self.configure(image=self.gif)
				self._num += 1
			except TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
				self._num = 0      
       
def raise_frame(showFrame):
        showFrame.tkraise()
            

def faqPrint():
    #Providing training data to the classifier.
    scriptpath = os.path.dirname(__file__)
    filename_when = os.path.join(scriptpath,'when.txt')
    filename_where = os.path.join(scriptpath, 'where.txt')
    filename_who = os.path.join(scriptpath, 'who.txt')

    whenText = open(filename_when, 'r')
    whereText = open(filename_where, 'r')
    whoText = open(filename_who, 'r')
    if foo.entry.get() != '':
        c = Classifier(whenText,whereText,whoText,foo.text.get("1.0",END),foo.entry.get(),dict())
        foo.getValues(c)
    else:
        foo.getAlertValues()
    foo.entry.delete(0,END)
    
def faqEnterPrint(event):
    #Providing training data to the classifier.
    scriptpath = os.path.dirname(__file__)
    filename_when = os.path.join(scriptpath,'when.txt')
    filename_where = os.path.join(scriptpath, 'where.txt')
    filename_who = os.path.join(scriptpath, 'who.txt')

    whenText = open(filename_when, 'r')
    whereText = open(filename_where, 'r')
    whoText = open(filename_who, 'r')
    if foo.entry.get() != '':
        c = Classifier(whenText,whereText,whoText,foo.text.get("1.0",END),foo.entry.get(),dict())
        foo.getValues(c)
    else:
        foo.getAlertValues()
    foo.entry.delete(0,END)
    
root = Tk()
root.resizable(width=False, height=False)
foo = ScrollTxtArea(root)
    
    # print(a)
root.title('FAQCreator')
root.mainloop()

