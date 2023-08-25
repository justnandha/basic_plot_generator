from tkinter import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math

class Plots():
    def __init__(self):
        self.filepath =None
        self.data =None
        self.xdata = None
        self.ydata =None
        self.smarker = None
        self.mcolor = None
        self.line = None
        self.scat = None
        self.hollow = None
        #----
        self.error = None
        self.e_data = None
        self.xlabel = None
        self.ylabel = None
        self.title = None
        self.legend = None
        self.dpi = None
        #--

        self.output =None

    def csv_data(self,filepath):
        df = pd.read_csv(filepath)
        self.data = df.values
    


    def openfile(self):
        i= True
        o=0

        

        while i:
            self.filepath = filedialog.askopenfilename()
            if self.filepath[-3:] == 'csv':
                self.csv_data(self.filepath)
                i = False
                print(self.filepath)
                if o!=0:
                    label.destroy()
            
            else:
                label = Label(root,text = 'choose a CSV file', font= ('Arial',10))
                label.pack()
                label.place(x=400 , y =50)
                o+=1
            if o == 2:
                label.destroy()
                o=1

        

    def plot(self):
        xlabel = self.xlabel
        ylabel = self.ylabel
        
        fs = 20

        self.fig = plt.figure(figsize = (6,5))
        xdata = int(self.xdata)
        ydata = int(self.ydata)

        x=self.data[:,xdata]
        y=self.data[:,ydata]

        if self.scat == 1 and self.hollow ==1:

            plt.scatter(x=x,y=y,facecolor = 'white', edgecolor = self.mcolor,marker= self.smarker,s=65,label = self.legend,zorder = 10,clip_on = False, linewidth = 1)
        
        elif self.scat ==1:
        
            plt.scatter(x=x,y=y,facecolor =  self.mcolor,marker= self.smarker,s=65,label = self.legend,zorder = 10,clip_on = False, linewidth = 1)
        
        if self.line == 1:
            
            plt.plot(x,y,label = self.legend,zorder = 10,clip_on = False, linewidth = 1)

        if self.error == 1:
            z = int(self.e_data)
            errordata = self.data[:,z]
            plt.errorbar(x=x,y=y,yerr = errordata,capsize = 2,fmt = 'none',ecolor= self.mcolor)

        

        ax = plt.gca()  

        for axis in ['bottom','left','top','right']:
            ax.spines[axis].set_linewidth(1.5)
            ax.spines[axis].set_color('0.2')

        plt.xlim(min(x), max(x))
        plt.ylim(min(y), max(y)+(max(y)*0.2))

        plt.xlabel(xlabel,fontname = 'Arial',fontsize = fs)
        plt.ylabel(ylabel,fontname = 'Arial',fontsize = fs)

        plt.xticks(size = 14, color = '0.2',fontname = 'Arial',fontsize = fs - 8)
        plt.yticks(size = 14, color = '0.2',fontname = 'Arial',fontsize = fs - 8)


        plt.legend(frameon = False,fontsize = fs - 4)
        

        plt.show()

        

    def save_file(self):

        self.plot()
   
        folder_selected = filedialog.askdirectory()
        dpi =int(self.dpi)
        out =str(self.output)
    
        if folder_selected:
            file_path = f"{folder_selected}/"+ out +".png"
            self.fig.savefig(file_path,dpi =dpi)
 


#####################################################################################
        

root = Tk()
root.minsize(height = 400,width = 600)
root.title("Plots")

def labels(root = root,text = "label",x=0,y=0,fs =13,color = "black"):
    label = Label(root,text = text,font = ('Arial',fs),foreground=color)
    label.pack()
    label.place(x=x,y=y)

p = Plots()

def tab1():
    
    def tab2():
        for item in of.winfo_children():
            item.destroy()
        sf = (root)

        label2 = Label(sf,text = 'secnd')
        label2.pack()

        def errorbr():
            if error.get() ==1:
                errordata.config(state=NORMAL)
                errentry.config(state= NORMAL)
            else:
                errordata.config(state=DISABLED)
                errentry.config(state= DISABLED)

        errordata = Label(sf,text = "Error bar column :",font = ('Arial',13),state =DISABLED)
        errordata.pack()
        errordata.place(x=200,y=80)

        errentry = Entry(sf,width = 18,bg = 'gray',state = DISABLED)
        errentry.pack()
        errentry.place(x= 350,y=80)
    

        error = IntVar()
        errorcb = Checkbutton(sf,variable = error,text = 'Error bar',font = ('Arial',13),command=errorbr)
        errorcb.pack()
        errorcb.place(x= 50,y=80)

        xlabel = labels(sf,text ='X label :',x=50,y=150)

        xentry = Entry(sf,width = 18,bg = 'gray')
        xentry.pack()
        xentry.place(x= 150,y=150)

       
        ylabel = labels(sf,text ="Y label :",x =300,y=150)

        yentry = Entry(sf,width = 18,bg = 'gray')
        yentry.pack()
        yentry.place(x= 400,y=150)

        title = labels(sf,text = "Title :",x=50,y = 200)

        tentry = Entry(sf,width = 18,bg = 'gray')
        tentry.pack()
        tentry.place(x= 150,y=200)

        legend = labels(sf,text ="Legend :",x=300,y=200)

        legentry = Entry(sf,width = 18,bg = 'gray')
        legentry.pack()
        legentry.place(x= 400,y=200)

        dpi = labels(sf,text = "DPi :",x=50,y=250)

        output = labels(sf,text = "Output :",x=300,y=250)
        outentry = Entry(sf,width = 18,bg = 'gray')
        outentry.pack()
        outentry.place(x= 400,y=250)

        var3 = IntVar()
        checkt = Checkbutton(sf,text = '300',variable=var3,font = ('Arial',13))
        checkt.pack()
        checkt.place(x=100,y=250)

        var6 =IntVar()
        checks = Checkbutton(sf,text = '600',variable=var6,font = ('Arial',13))
        checks.pack()
        checks.place(x=170,y=250)

        def plotbr():
        
            if error.get() == 1:
                p.error= error.get()
                p.e_data = errentry.get()
            p.xlabel = xentry.get()
            p.ylabel = yentry.get()
            p.title = tentry.get()
            p.legend = legentry.get()

        def plotshow():

            plotbr()

            p.plot()
                

        def save():

            plotbr()

            
            if var3.get() == var6.get() :
                label = labels(sf,text = 'Select any one DPI',x=200,y=280,fs=11,color='Red')
            if outentry.get():
                label = labels(sf,text = 'Output filename',x=200,y=280,fs=11,color='Red')

            else :
                if var3.get() == 1:
                    p.dpi = 300
                if var6.get() == 1:
                    p.dpi = 600
                p.output = outentry.get()
            
            p.save_file()

        def back():
            
            for item in sf.winfo_children():
                item.destroy()
            tab1()

        plotb = Button(sf,text = 'PLOT',font = ("Arial", 13),command = plotshow )
        plotb.pack()
        plotb.place(x= 250, y = 320)  

        button2 = Button(sf,text = 'BACK',font = ("Arial", 13),command =back )
        button2.pack()
        button2.place(x = 100,y = 320)

        btn = Button(sf, text="Save Plot",font = ("Arial", 13), command=save)
        btn.pack()
        btn.place(x=400,y=320)


    of = (root)
    
 
    label1 = labels(of,text = "Open a CSV file",x=130,y=50)

    open = Button(of,text ='Open',command = p.openfile,font = ('Arial',10))
    open.pack(padx=40)
    open.place(x= 300,y=50)


    label2 = labels(of,text = "Enter the column name for datapoints",x=120,y=100,fs=15)

    xdata = labels(of,text = "X Data :",x=50,y=150)

    xentry = Entry(of,width = 18,bg = 'gray')
    xentry.pack()
    xentry.place(x= 150,y=150)

    ydata = labels(of,text = "Y-Data :",x=300,y=150)

    yentry = Entry(of,width = 18,bg = 'gray')
    yentry.pack()
    yentry.place(x= 400,y=150)


    varp= IntVar()
    checkp = Checkbutton(of,variable = varp,text = 'For line plot',font = ('Arial',13))
    checkp.pack()
    checkp.place(x=120,y=200)

    
    def updat():
        if vars.get() == 1:
            checkms.config(state = NORMAL)
            marker.config(state = NORMAL)
            color.config(state = NORMAL)
        else:
            checkms.config(state = DISABLED)
            marker.config(state = DISABLED)
            color.config(state = DISABLED)


    vars= IntVar()
    checks = Checkbutton(of,variable = vars,text = 'For Scatter plot',font = ('Arial',13),command = updat)
    checks.pack()
    checks.place(x=300,y=200)


    varms = IntVar()
    checkms = Checkbutton(of,variable = varms,text = "For Hollow marker ", font = ('Arial',13),state= DISABLED)
    checkms.pack()
    checkms.place(x=50,y = 300)

    markerlab = labels(of,text = "Marker shape :",x=30,y=250)


    marker = Entry(of,width =18,bg = 'gray',state = DISABLED)
    marker.pack()
    marker.place(x= 150,y=250)

    colorlab = labels(of,text = "Color :",x=300,y=250)

    color = Entry(of,width =18,bg = 'gray',state = DISABLED)
    color.pack()
    color.place(x= 400,y=250)

   
    def get_value():
        p.xdata = xentry.get()
        p.ydata = yentry.get()
        p.line = varp.get()
        p.scat = vars.get()
        if p.line != p.scat:
            if p.scat == 1:
                p.smarker = marker.get()
                p.mcolor = color.get()
                p.hollow = varms.get()
            tab2()

        else:
            
            label= labels(of,text ="Select any one plot",x=350,y=300,color = "Red")


    button1 = Button(of,text = 'Next',font = ("Arial", 13),command =get_value)
    button1.pack()
    button1.place(x=350,y=320)

tab1()

root.mainloop()