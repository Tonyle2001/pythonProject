import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['km to mile', 'kg to pound', 'sec to min'], key = '-UNIT-'),
        sg.Button('Convert', key = '-CONVERT-')
     ],
    [sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)


def switch(case):
    if case == 'km to mile':
        output = round(float(input_val) * 0.6214, 2)
        output_string = f'{input_val} km are {output} miles.'

    elif case == 'kg to pound':
        output = round(float(input_val) * 2.20462, 2)
        output_string = f'{input_val} kg are {output} pounds.'

    elif case == 'sec to min':
        output = round(float(input_val) / 60, 2)
        output_string = f'{input_val} sec are {output} min.'

    window['-OUTPUT-'].update(output_string)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_val = values['-INPUT-']
        if input_val.isnumeric():
            switch(values['-UNIT-'])

        else:
            window['-OUTPUT-'].update('PLEASE ENTER A NUMBER!')




window.close()


