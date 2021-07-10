from tkinter import*
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, Canvas, Button, GROOVE
from tkinter.ttk import Frame, Label, Entry
from tkinter import ttk, filedialog, simpledialog
import tkinter.font as tkFont
from tkinter import messagebox
import os
import csv
#import ScriptExecute
import sys
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))


LARGE_FONT = ("Arial", 16)
JMX_File=""
VUser_Load=""
TVID=1
ConfigFile=""

 


class LoadConfig():

    def __init__(self):
        super().__init__()
        self.initUI()   
    def initUI(self):

        def loaddata(self):
            with open(os.path.abspath(ConfigFileName)) as myfile:
                csvread = csv.reader(myfile, delimiter=',')
                for row in csvread:
                    print('load row:', row)
                    self.tv.insert("", 'end', values=row)

        ConfigFileName = filedialog.askopenfilename(initialdir = "/",title = "Select config file", filetypes = ( ("JMeter Config files", "*.config"), ("All files", "*.config") ) )

        global ConfigFile 
        ConfigFile = os.path.abspath(ConfigFileName)
        

        self.tv=ttk.Treeview()
        self.tv['columns']=('Load Generator', 'Script', 'VUser')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Load Generator', anchor=CENTER, width=30)
        self.tv.column('Script', anchor=CENTER, width=220)
        self.tv.column('VUser', anchor=CENTER, width=40)


        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Load Generator', text='Load Generator', anchor=CENTER)
        self.tv.heading('Script', text='Script', anchor=CENTER)
        self.tv.heading('VUser', text='VUser', anchor=CENTER)
        self.tv.place(x=200,y=120,width=1084,height=600)
        
        vsb = Scrollbar(self.tv)
        vsb.pack(side=RIGHT,fill=Y)
        self.tv.configure(yscrollcommand=vsb.set)
        vsb.config(command=self.tv.yview)
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        loaddata(self)


        self.GButton_Run=Button()
        ft = tkFont.Font(family='Times',size=20)
        self.GButton_Run["font"] = ft
        self.GButton_Run["bg"] = "#90ee90"
        self.GButton_Run["justify"] = "center"
        self.GButton_Run["text"] = "Run Test"
        self.GButton_Run["relief"] = "ridge"
        self.GButton_Run["state"] = "normal"
        self.GButton_Run.place(x=200,y=750,width=200,height=90)
        self.GButton_Run["command"] = self.GButton_Run_command



    def GButton_Run_command(self):
        Release=simpledialog.askstring("Release", "Enter Release", initialvalue="")
        print(Release)
        cmd = "python3 ScriptExecute.py  " + ConfigFile +" "+ Release
        print(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        result = out.splitlines()
        for lin in result:
            print(lin)



class NewConfiguration(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

# GUI   Section 
        GLabel_321=Label()
        ft = tkFont.Font(family='Times',size=20)
        GLabel_321["font"] = ft
        GLabel_321["justify"] = "center"
        GLabel_321["text"] = "File Select (JMX)"
        GLabel_321.place(x=170,y=160,width=184,height=30)

        self.GButton_753=Button()
        ft = tkFont.Font(family='Times',size=20)
        self.GButton_753["font"] = ft
        self.GButton_753["justify"] = "center"
        self.GButton_753["text"] = "File Select"
        self.GButton_753["relief"] = "ridge"
        self.GButton_753.place(x=370,y=160,width=138,height=30)
        self.GButton_753["command"] = self.GButton_753_command

        GLabel_333=Label()
        ft = tkFont.Font(family='Times',size=20)
        GLabel_333["font"] = ft
        GLabel_333["justify"] = "center"
        GLabel_333["text"] = ""
        GLabel_333.place(x=570,y=160,width=284,height=30)


        GLabel_322=Label()
        ft = tkFont.Font(family='Times',size=20)
        GLabel_322["font"] = ft
        GLabel_322["justify"] = "center"
        GLabel_322["text"] = "Enter VUser / Threads "
        GLabel_322.place(x=170,y=200,width=184,height=30)

        self.GLineEdit_134=Entry()
        ft = tkFont.Font(family='Times',size=20)
        self.GLineEdit_134["font"] = ft
        self.GLineEdit_134["justify"] = "left"
        self.GLineEdit_134["text"] = "0"
        self.GLineEdit_134.place(x=370,y=200,width=138,height=30)
    
        GLabel_422=Label()
        ft = tkFont.Font(family='Times',size=20)
        GLabel_422["font"] = ft
        GLabel_422["justify"] = "center"
        GLabel_422["text"] = "Select Load-Generator"
        GLabel_422.place(x=170,y=240,width=184,height=30)
        
# list box 

        self.GListBox_626=Listbox()
        ft = tkFont.Font(family='Times',size=20)
        self.GListBox_626["font"] = ft
        self.GListBox_626["justify"] = "left"
        self.GListBox_626.place(x=370,y=240,width=148,height=200)
        self.GListBox_626["listvariable"] = "loadgen"
        self.GListBox_626["selectborderwidth"] = "1"
        self.GListBox_626["selectmode"] = "multiple"
        
        scrollbar = Scrollbar(self.GListBox_626)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.GListBox_626.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.GListBox_626.yview)
        fopen=open('/Users/yningapp/Documents/automation/auto/host.txt', 'r')

        for item in fopen:
            self.GListBox_626.insert(END, item.rstrip())
        fopen.close()
            #GListBox_626.insert(end, item)

# Save the contents to tree         
       
        self.GButton_756=Button()
        ft = tkFont.Font(family='Times',size=20)
        self.GButton_756["font"] = ft
        self.GButton_756["justify"] = "center"
        self.GButton_756["text"] = "Next"
        self.GButton_756["relief"] = "ridge"
        self.GButton_756.place(x=370,y=460,width=138,height=30)
        self.GButton_756["command"] = self.GButton_756_command

# Tree View 
        self.tv=ttk.Treeview()
        self.tv['columns']=('Load Generator', 'Script', 'VUser')
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.column('Load Generator', anchor=CENTER, width=30)
        self.tv.column('Script', anchor=CENTER, width=220)
        self.tv.column('VUser', anchor=CENTER, width=40)

        self.tv.heading('#0', text='', anchor=CENTER)
        self.tv.heading('Load Generator', text='Load Generator', anchor=CENTER)
        self.tv.heading('Script', text='Script', anchor=CENTER)
        self.tv.heading('VUser', text='VUser', anchor=CENTER)
        self.tv.place(x=570,y=240,width=1084,height=600)

        vsb = Scrollbar(self.tv)
        vsb.pack(side=RIGHT,fill=Y)
        self.tv.configure(yscrollcommand=vsb.set)
        vsb.config(command=self.tv.yview)

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

# delete Button 

        self.GButton_758=Button()
        ft = tkFont.Font(family='Times',size=20)
        self.GButton_758["font"] = ft
        self.GButton_758["justify"] = "center"
        self.GButton_758["text"] = "Delete"
        self.GButton_758["relief"] = "ridge"
        self.GButton_758.place(x=840,y=840,width=138,height=30)
        self.GButton_758["command"] = self.GButton_758_command

# save Button on Tree 

        self.GButton_757=Button()
        ft = tkFont.Font(family='Times',size=20)
        self.GButton_757["font"] = ft
        self.GButton_757["justify"] = "center"
        self.GButton_757["text"] = "Save"
        self.GButton_757["relief"] = "ridge"
        self.GButton_757.place(x=640,y=840,width=138,height=30)
        self.GButton_757["command"] = self.GButton_757_command


    
        self.GButton_Run=Button()
        ft = tkFont.Font(family='Times',size=20)
        self.GButton_Run["font"] = ft
        self.GButton_Run["bg"] = "#90ee90"
        self.GButton_Run["justify"] = "center"
        self.GButton_Run["text"] = "Run Test"
        self.GButton_Run["relief"] = "ridge"
        self.GButton_Run["state"] = "disabled"
        self.GButton_Run.place(x=190,y=800,width=200,height=90)
        self.GButton_Run["command"] = self.GButton_Run_command


    def GButton_758_command(self):
        selected_item = self.tv.selection()[0] ## get selected item
        self.tv.delete(selected_item)


#saving the file selection.

    def GButton_756_command(self):
        VLoad = self.GLineEdit_134.get()
        global VUser_Load
        global TVID
        global JMX_File
        VUser_Load = VLoad 
        for i in self.GListBox_626.curselection():
            TVID=TVID+i+1
            self.tv.insert(parent='', index=TVID, iid=TVID, text='', values=(self.GListBox_626.get(i),JMX_File,VUser_Load))

        self.GLineEdit_134.delete(0,END)
        self.GLineEdit_134.insert(0,"")
        self.GLabel_333["text"]=" "
        JMX_File = " "
        VUser_Load =" "


    def GButton_Run_command(self):

        Release=simpledialog.askstring("Release", "Enter Release", initialvalue="")
        print(Release)
        cmd = "python3 ScriptExecute.py  " + ConfigFile +" "+ Release
        print(cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        result = out.splitlines()
        for lin in result:
            print(lin)
            """
            if not lin.startswith('#'):
                print(lin)
            """
        



# File open and JMeter JMX Selection

    def GButton_753_command(self):
        FileName = filedialog.askopenfilename(initialdir = "/",title = "Select file", filetypes = ( ("JMeter files", "*.jmx"), ("All files", "*.*") ) )
        self.GLabel_333=Label()
        ft = tkFont.Font(family='Times',size=20)
        self.GLabel_333["font"] = ft
        self.GLabel_333["justify"] = "center"
        self.GLabel_333["text"] = os.path.basename(FileName)
        self.GLabel_333.place(x=570,y=160,width=600,height=30)
        FileDet = os.path.basename(FileName)
        global JMX_File
        JMX_File = FileDet

# Save JMX Configuration 

    def GButton_757_command(self):


        #fname=filedialog.asksaveasfilename(initialfile = 'JMeterConfig.config',title = "Save file", mode='w',newline=' ',defaultextension=".config")
        fname = filedialog.asksaveasfilename(initialfile = 'JMeterConfig.config', defaultextension=".config",title = "Save file")
        fname = open(fname,'w')
        #print(os.path.abspath(fname.name))
    
        messagebox.showinfo("showinfo", "File Saved")
        csvwriter = csv.writer(fname, delimiter=',')
        for row_id in self.tv.get_children():
            row = self.tv.item(row_id)['values']
            print('save row:', row)
            csvwriter.writerow(row)
        self.GButton_Run["state"] = "normal"
        global ConfigFile 
        ConfigFile = os.path.abspath(fname.name)
        fname.close()
        








        """ 
        with open("JMeterConfig.config", "w", newline='') as myfile:
            csvwriter = csv.writer(myfile, delimiter=',')
            for row_id in self.tv.get_children():
                row = self.tv.item(row_id)['values']
                print('save row:', row)
                csvwriter.writerow(row)
                """
       
    
"""
def TreeList():
           
    tv = ttk.Treeview()
    tv['columns']=('Load Generator', 'Script', 'VUser')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Load Generator', anchor=CENTER, width=80)
    tv.column('Script', anchor=CENTER, width=80)
    tv.column('VUser', anchor=CENTER, width=80)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Load Generator', text='Load Generator', anchor=CENTER)
    tv.heading('Script', text='Script', anchor=CENTER)
    tv.heading('VUser', text='VUser', anchor=CENTER)
    tv.place(x=570,y=240,width=1084,height=600)


    style = ttk.Style()
    style.theme_use("default")
    style.map("Treeview")

    """
   
# Creates action based on selection


    

# Call's the Configuration settings.


class JMeterConfiguration(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.master.geometry('1800x1200')
        self.master.resizable(width=True, height=True)
        self.master.title("JMeterConfiguration")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self)
        frame1.pack(fill=X)

        self.GButton_700=Button()
        ft = tkFont.Font(family='Times',size=20)
        self.GButton_700["font"] = ft
        self.GButton_700["justify"] = "center"
        self.GButton_700["text"] = "Do you Want to Create a New JMeter Configuration"
        self.GButton_700["relief"] = "groove"
        self.GButton_700.place(x=550,y=10,width=500,height=30)
        self.GButton_700["command"] = self.printValue

        #Button(frame1,text="Do you Want to Create a New JMeter Configuration", padx=10, pady=5,relief=GROOVE, command=printValue).pack()
        #Button["state"]="disabled"
        self.master.mainloop()




    def printValue(self):
        pname = messagebox.askyesno('Yes|No', 'Do you Want to Create a New Configuration?')
       
        if pname == True:
            self.GButton_700["state"]="disabled"
            app=NewConfiguration()
        else:
            self.GButton_700["state"]="disabled"
            app=LoadConfig()
     
            

		
def main():
    """
    root = Tk()
   
    root.geometry('1800x1200')

    root.resizable(width=True, height=True)
    root.title("Configuration ")
    """
    
    
    app = JMeterConfiguration()

    #root.mainloop()


if __name__ == "__main__":
    
	main()



