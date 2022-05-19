import PySimpleGUI as sg

def create_theme(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 14', button_element_size= (6,3))
    button_size = (6,3)
    layout = [
        [sg.Text(
            '',
            font = 'Franklin 26',
            justification= 'right',
            expand_x= True,
            pad = (10,20),
            right_click_menu= theme_menu,
            key = '-TEXT-'
        )
        ],
        #[sg.Push(), sg.Text('output', font = 'Franklin 26')],
        [sg.Button('Enter',expand_x= True), sg.Button('Clear',expand_x= True)],
        [sg.Button(7, size = button_size),sg.Button(8, size = button_size),sg.Button(9, size = button_size),sg.Button('/', size = button_size)],
        [sg.Button(4, size = button_size),sg.Button(5, size = button_size),sg.Button(6, size = button_size),sg.Button('*', size = button_size)],
        [sg.Button(1, size = button_size),sg.Button(2, size = button_size),sg.Button(3, size = button_size),sg.Button('-', size = button_size)],
        [sg.Button(0,expand_x= True),sg.Button('.', size = button_size),sg.Button('+', size = button_size)]
    ]

    return sg.Window('Calculator',layout)

theme_menu = ['menu',['Black','BlueMono','DarkGreen6', 'random']]
window = create_theme('Dark')

cur_display = []
full_op = []
while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_theme(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        cur_display.append(event)
        num_str = ''.join(cur_display)
        window['-TEXT-'].update(num_str)

    if event in ['+','-','/','*']:
        full_op.append(''.join(cur_display))
        cur_display = []
        full_op.append(event)
        window['-TEXT-'].update('')

    if event == 'Clear':
        cur_display = []
        full_op = []
        window['-TEXT-'].update(' ')

    if event == 'Enter':
        full_op.append(''.join(cur_display))
        result = eval(''.join(full_op))
        window['-TEXT-'].update(result)
        full_op = []


window.close()