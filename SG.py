import PySimpleGUI as sg
sg.theme('Green')
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
layout=[[sg.Text('Enter your numbers:')],
        [sg.InputText(key='int1'),sg.Text('+, -- ,X, /'),sg.InputText(key='int2'),sg.Text(key='answer',size=(20,1))],
        [sg.Button("Add"),sg.Button("Subtract"),sg.Button("Multiply"),sg.Button("Divide")]]
window=sg.Window('Calculator').layout(layout)

while True:
    event,values=window.Read()
    if event is None:
        break
    try:
        num1=int(values['int1'])
        num2=int(values['int2'])
    except:
        answer="invalid number"
        window.FindElement('answer').update(answer)
        continue
    if event=="Add":
        answer=add(num1,num2)
    if event=="Subtract":
        answer=subtract(num1,num2)
    if event=="Multiply":
        answer=multiply(num1,num2)
    if event=="Divide":
        answer=divide(num1,num2)
    window.FindElement('answer').update(answer)
