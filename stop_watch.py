import PySimpleGUI as sg

sg.theme('black')
layout = [
    [sg.VPush()],
    [sg.Text('Time')],
    [sg.Button('Start'), sg.Button('Lap')],
    [sg.VPush()]
]

window = sg.Window('Stopwatch',
                   layout,
                   size = (300,300),
                   element_justification= 'center'
                   )

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()