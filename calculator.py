import PySimpleGUI as sg

sg.theme('BlueMono')
sg.set_options(font = 'Franklin 20', button_element_size= (6,3))
button_size = (6,3)
layout = [
    [sg.Text('output')],
    [sg.Button('E'), sg.Button('C')],
    [sg.Button(7, size = button_size),sg.Button(8, size = button_size),sg.Button(9, size = button_size),sg.Button('/', size = button_size)],
    [sg.Button(4, size = button_size),sg.Button(5, size = button_size),sg.Button(6, size = button_size),sg.Button('*', size = button_size)],
    [sg.Button(1, size = button_size),sg.Button(2, size = button_size),sg.Button(3, size = button_size),sg.Button('-', size = button_size)],
    [sg.Button(0, size = button_size),sg.Button('.', size = button_size),sg.Button('+', size = button_size)]
]
sg.theme('dark')
window = sg.Window('Calculator', layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()