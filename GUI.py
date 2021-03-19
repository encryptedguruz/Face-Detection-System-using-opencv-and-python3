import tkinter as tk 
from tkinter import ttk 
import os
  
# Creating tkinter window 
window = tk.Tk() 
window.title('Combobox') 
window.geometry('500x250') 
  
a = None
    
def getSelectedDept(event):
    
    global a
    a = deptchoosen.get()
    
    temp_path = os.path.join('F:/data analysis notebooks/opencv/user/',a)
    
    student_list = os.listdir(temp_path)
    
    studentchoosen['values'] = student_list
  
    

    
    
    
# label 
ttk.Label(window, text = "Select the Department :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
# Combobox creation 
n = tk.StringVar() 
deptchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
  
dept_list = os.listdir('F:/data analysis notebooks/opencv/user')
    
# Adding combobox drop down list 
deptchoosen['values'] = dept_list
  
deptchoosen.grid(column = 1, row = 5) 
deptchoosen.current(1) 

deptchoosen.bind("<<ComboboxSelected>>", getSelectedDept)

ttk.Label(window, text = "Select the Student :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 10, padx = 10, pady = 25) 

n = tk.StringVar() 
studentchoosen = ttk.Combobox(window, width = 27, textvariable = n) 
studentchoosen.grid(column = 1, row = 10) 
studentchoosen.current() 


window.mainloop()