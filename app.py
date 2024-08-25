import requests
import pyodbc 
from jproperties import Properties 



from tkinter import *
import tkinter as tk
import datetime
import subprocess 
import json


def prueba ():
    print ("prueba")

window=Tk()

window.title("Conexcion")
window.geometry('550x200')


def sendPost():
    url = "https://dev.gestion-miralejos.com.ar/api/prueba"

    data = []
    data.append({'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'})
    data.append({'sender': 'KAKAKA', 'receiver': 'TATATA', 'message': 'TIITITITI!'})
    headers = {'authorization' : 'pwEFfELCjeuJlXNJbUQuM0GWvuh9JOBizh3EfRlRGSkrneYo9Dw9MRuCNzXpvTL9I9euEGA1xfe'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    var2.set(r.content)

def run(i):
    hora_actual = datetime.datetime.now()
    var1.set(hora_actual.strftime("%Y-%m-%d %H:%M:%S"))
    #configs = Properties()
    #with open('example.properties', 'rb') as read_prop: 
    #    configs.load(read_prop)
    #prop_view = configs.items()
    #data = {}
    #for item in prop_view:
    #    data[item[0]] = item[1].data
    str = 'DRIVER={SQL Server};SERVER=192.168.0.220;Integrated_Security=false;DATABASE=prodmiralejos;UID=miralejosUser;PWD=mira123'
    
    try:
        cnxn = pyodbc.connect(str)
        cursor = cnxn.cursor()
        cursor.execute('SELECT 1+1, 1+2, 1+3')
    except pyodbc.Error as ex:
         var1.set('No se pudo realizar la conexcion')
         

    sendPost()

    listbox.insert(i, hora_actual.strftime("%Y-%m-%d %H:%M:%S"))
    #for row in cursor:
        
     #   i = i + 1
        #print('row = %r' % (row,))

def countdown(i): 
        i = i + 1 
        run(i)
        window.after(30000, countdown, i)

var1 = StringVar()
var2 = StringVar()

#btn = Button(window, text="Click Me", bg="black", fg="white",command=run)
#btn.grid(column=0, row=0)
label = tk.Label( window, textvariable=var1, padx=10 )
label.grid(column=0, row=0)

label2 = tk.Label( window, textvariable=var2, padx=10 )
label2.grid(column=0, row=1)

listbox = tk.Listbox()
listbox.grid(column=0, row=2)
var1.set("")
var2.set("")
countdown(1)

window.mainloop()




  









#response = requests.get("https://jsonplaceholder.typicode.com/posts/10")

#print(response.content)