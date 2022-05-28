import PySimpleGUI as sg

smileys = [
    'happy',[':)','xD',':D','<3'],
    'sad',[':(','T_T'],
    'other',[':3']
]
smileys_events = smileys[1] + smileys[3] + smileys[5]
menu_layout = [
    ['File',['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', smileys],
]

sg.theme('Dark')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key = '-DOCNAME-')],
    [sg.Multiline(no_scrollbar= True, size = (40,30), key = '-TEXTBOX-')]
]

window = sg.Window('Text_Editor', layout)

while True:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Word Count':
        full_text = value['-TEXTBOX-']
        clean_text = full_text.replace('\n', ' ').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        if full_text == '':
            word_count = 0
            sg.popup(f'words: {word_count}\ncharacters: {char_count}')
        else:
            sg.popup(f'words: {word_count}\ncharacters: {char_count}')

    if event in smileys_events:
        current_text = value['-TEXTBOX-']
        new_text = current_text + ' ' + event
        window['-TEXTBOX-'].update(new_text)

window.close()
