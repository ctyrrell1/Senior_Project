#object oriented GUI with Tkinter

from Tkinter import *
from tkFileDialog import *
from sample_lin_reg2 import *
from m_lin_reg import *
from kmeans2_usingfile import *


class Application(Frame):
    """ A GUI app for ML. """
    def __init__(self, master):
        """ Initialize the Frame"""
        Frame.__init__(self,master)
        self.filename = 0
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create buttons.  """
        '''
        self.browsetext = Text(self, width = 20, height = 1, wrap = WORD)
        self.browsetext.grid(row = 1, column = 0, columnspan = 2, sticky = W)
        self.browse = Button(self, command = self.getfile, text = "Select File").grid(row = 1)
        '''

        self.welcomelabel = Label(self, text = "WELCOME TO THE MACHINE LEARNING TOOL!", font = "bold").grid(row = 1)
        self.emptyspace = Label(self, text = "").grid(row = 2)
        self.emptyspace = Label(self, text = "").grid(row = 3)
        
        self.algotitle = Label(self, text = "Input 1, 2, or 3 Here:").grid(row =4, sticky = W)
        self.algoEntry = Entry(self)
        self.algoEntry.grid(row = 4)
        #self.algoLabel = Label(self, text = "Input: 1, 2, or 3")
        self.algoLabeldesc = Label(self, text = "1 = Simple Linear Regression\t 2 = Multi Linear Regression \t 3 = K-Means Clustering")
        #self.algoLabel.grid(row = 3, column = 0, sticky = W)
        self.algoLabeldesc.grid(row = 5, column = 0, sticky = W)

        self.emptyspace = Label(self, text = "").grid(row = 6)
        self.emptyspace2 = Label(self, text = "").grid(row = 7)

        self.entry1labal = Label(self, text = "Enter Values for Prediction:").grid(row = 8, sticky = W)
        self.entry1 = Entry(self)
        self.entry1.grid(row = 8)
        self.help1 = Label(self, text = "Format for Simple Linear Regression: 'x' from 0-36").grid(row = 9, sticky = W)
        self.help2 = Label(self, text = "Format for Multi Linear Regression: 'x1' from 0-4, 'x2' from 0-800, 'x3' from 0-800, 'x4' from 0-4").grid(row = 10, sticky = W)
        self.help3 = Label(self, text = "Format for K-Means Clustering: 'x' from 0-36, 'y' from 0-4").grid(row = 11, sticky = W)

        self.emptyspace2 = Label(self, text = "").grid(row = 12)
        self.emptyspace2 = Label(self, text = "").grid(row = 13)

        self.button3labal = Label(self, text = "Predict the Values By Pressing the Button Below)").grid(row = 14, sticky = W)
        self.button3 = Button(self, text = "Predict", command = self.show_prediction)
        self.button3.grid(row = 15, sticky = W)

        self.text1 = Text(self, width = 35, height = 2, wrap = WORD)
        self.text1.grid(row = 16, column = 0, columnspan = 2, sticky = W)

        self.emptyspace2 = Label(self, text = "").grid(row = 17)
        self.emptyspace2 = Label(self, text = "").grid(row = 18)

        self.plotdatalabel = Label(self, text = "Click the Button below to see a plot of the data!").grid(row = 19)
        self.button2 = Button(self, text = "Plot Data", command = self.plot_data)
        self.button2.grid(row = 20)


    def show_prediction(self):
        """ Shows the prediction of the number entered in the field """
        if(self.algoEntry.get() == '1'):
            prediction = predict_linreg(self.entry1.get())
            self.text1.delete(0.0, END)
            self.text1.insert(0.0, prediction)
        if(self.algoEntry.get() == '2'):
            teststring = self.entry1.get()
            testarray = teststring.split(', ')
            prediction = predict_multireg(float(testarray[0]), float(testarray[1]), float(testarray[2]), float(testarray[3]))
            self.text1.delete(0.0, END)
            self.text1.insert(0.0, prediction)
        if(self.algoEntry.get() == '3'):
            teststring = self.entry1.get()
            testarray = teststring.split(', ')
            prediction = predict_cluster(float(testarray[0]), float(testarray[1]))
            self.text1.delete(0.0, END)
            self.text1.insert(0.0, prediction)

    def plot_data(self):
        if(self.algoEntry.get() == '1'):
            plot_linreg()
        elif(self.algoEntry.get() == '2'):
            plot_multireg()
        elif(self.algoEntry.get() == '3'):
            plot_cluster()
'''
    def getfile(self):
        self.filename = askopenfile('r')
        self.browsetext.delete(0.0, END)
        self.browsetext.insert(0.0, inspect.getfile(inspect.currentframe()))
'''
        


root = Tk()
root.title("ML Tool")
root.geometry("525x450")

app = Application(root)

root.mainloop()
