import requests
import pyodbc 
from jproperties import Properties 
from tkinter import *
import tkinter as tk
import datetime
import json


def prueba ():
    print ("prueba")

window=Tk()

window.title("Conexcion")
window.geometry('550x200')


def sendPost(cursor, i):
    hora_actual = datetime.datetime.now()
    url = "https://dev.gestion-miralejos.com.ar/api/prueba"
    data = []
    headers = {'authorization' : 'pwEFfELCjeuJlXNJbUQuM0GWvuh9JOBizh3EfRlRGSkrneYo9Dw9MRuCNzXpvTL9I9euEGA1xfe'}
    rows = cursor.fetchall()
    x = 0
    for row in rows:
         lastId = row[0]
         data.append({'id': row[0], 'fecha': row[3].strftime("%Y-%m-%d_%H:%M:%S"), 'codigo': row[0]})
         x = x + 1
    r = requests.post(url, data=json.dumps(data), headers=headers)
    if r.status_code == 200:
        var2.set("Enviados " + str(x) + " registros exitosamente " + hora_actual.strftime("%Y-%m-%d %H:%M:%S"))
    else :
        var2.set("Error al enviar la respuesta")

def run(i):

    hora_actual = datetime.datetime.now()
    strConn = 'DRIVER={SQL Server};SERVER=192.168.0.37;Integrated_Security=false;DATABASE=SBDARITA;UID=sa;PWD=sa'
    try:
        cnxn = pyodbc.connect(strConn)
        cursor = cnxn.cursor()
        if lastId == 0 :
            sql = "SELECT TOP 10 chp_ID, chp_Importe, chp_NroCheq, chp_FEnt FROM ChequesP WHERE chp_FEnt = '"+ hora_actual.strftime("%Y-%m-%d") +"'"
        else :
            sql = "SELECT TOP 10 chp_ID, chp_Importe, chp_NroCheq, chp_FEnt FROM ChequesP WHERE chp_ID > " + str(lastId)
        cursor.execute(sql)
        var1.set('Estado: Conectado a la BD Local')
        sendPost(cursor, i)
    except pyodbc.Error as ex:
         var1.set(sql)
         
def countdown(i): 
        i = i + 1 
        run(i)
        window.after(30000, countdown, i)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
lastId = IntVar()

label = tk.Label( window, textvariable=var1, padx=10 )
label.grid(column=0, row=0)

label2 = tk.Label( window, textvariable=var2, padx=10 )
label2.grid(column=0, row=1)

label3 = tk.Label( window, textvariable=var3, padx=10 )
label3.grid(column=0, row=2)

var1.set("")
var2.set("")
var3.set("")
lastId = 0
countdown(1)

window.mainloop()