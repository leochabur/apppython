import requests
import pyodbc 
from jproperties import Properties 



from tkinter import *
import tkinter as tk
import datetime



def prueba ():
    print ("prueba")

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')


def run():
    hora_actual = datetime.datetime.now()
    var1.set(hora_actual.strftime("%Y-%m-%d %H:%M:%S"))
    configs = Properties() 
    with open('example.properties', 'rb') as read_prop: 
        configs.load(read_prop) 
    prop_view = configs.items() 
    data = {}
    for item in prop_view: 
        data[item[0]] = item[1].data
    str = 'DRIVER={SQL Server};SERVER='+data['host']+';Integrated_Security=false;DATABASE='+data['db']+';PORT='+data['port']+';UID='+data['user']+';PWD='+data['pwd']
    cnxn = pyodbc.connect(str)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM ChequesP chP INNER JOIN CheqPConci chPC ON chPC.cpcchp_ID = chP.chp_ID LEFT JOIN Proveed P ON P.pro_Cod = chP.chppro_Cod')
    i = 0
    for row in cursor:
        listbox.insert(i, row[2])
        i = i + 1
        #print('row = %r' % (row,))

def countdown():  
        run()
        window.after(6000, countdown)  

var1 = StringVar()

#btn = Button(window, text="Click Me", bg="black", fg="white",command=run)
#btn.grid(column=0, row=0)
label = tk.Label( window, textvariable=var1, padx=10 )
label.grid(column=0, row=0)
listbox = tk.Listbox()
listbox.grid(column=0, row=1)
var1.set("")
countdown()

window.mainloop()




  









#response = requests.get("https://jsonplaceholder.typicode.com/posts/10")

#print(response.content)