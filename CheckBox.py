from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string('''

<Exe6>
    BoxLayout:
        orientation: 'vertical'

        Label:
            size_hint_y:.50
            text:'Selecciona el tiempo verbal correcto de la oración dada.\\nSolo tendrás una oportunidad'
            markup: True
            font_size:'25sp'
        Label:
            size_hint_y:.20
            text:'[color=ff9900]It can get very cold in this house.[/color]'
            markup: True
            font_size:'30sp'
        GridLayout:

            cols: 2
            padding: 30
            row_force_default:True
            row_default_height:35
            CheckBox:
                id: B1

                size_hint_x: None
                width: 50
                height: 20
                group:'A'
                active: False
            Label:
                id: L1
                text: "  Presente"
                size_hint_x: None
                width: 100
                markup: True
            CheckBox:
                id: B2

                size_hint_x: None
                width: 50
                height: 20
                group:'A'
                active:False
            Label:
                id: L2
                text: "Pasado"
                size_hint_x: None
                width: 100
            CheckBox:
                id: B3

                size_hint_x: None
                width: 50
                height: 20
                group:'A'

            Label:
                id: L3
                text: "Futuro"
                size_hint_x: None
                width: 100



            CheckBox:
                id: B4

                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L4
                text: "                   Presente Perfecto"
                size_hint_x: None
                width: 100
        Label:
            size_hint_y:.9

            FloatLayout:


                Button:
                    id: btn1
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.8}
                    text: 'Check'
                    background_color: [.7,.7,1,1]
                    on_press: if B1.active == True: message.text = '[color=009900]Excelente![/color]'
                    on_press: if B1.active == False: message.text = '[color=ff3333]Lo siento! , Presione Next[/color]'
                    on_release: if B1.active == True: btn1.state = 'down'
                    on_release: if B1.active == True: btn2.disabled = False
                    on_release: if B1.active == False: btn2.disabled = False
                    on_release: if B1.active == False: btn1.state = 'down'
                    on_release: if B1.active == True: L1.text='[color=009900]  Presente[/color]'
                    on_release: if B1.active == False: L1.text='[color=009900]Presente[/color]'
                    on_release: if B1.active == False: B1.disabled,B2.disabled,B3.disabled = 'off'
                    on_release: if B1.active == False: B4.disabled = 'off'
                    on_release: if B1.active == True: B2.disabled,B3.disabled,B4.disabled = 'off'
                Button:
                    id: btn2
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.2}
                    text: 'Next'
                    background_color: [.7,.7,1,1]
                    on_release: root.manager.current = root.manager.next()
                    disabled: True

                Label:
                    id: message
                    text: ''
                    pos_hint:{'center_x': 4, 'y': 1.55}
                    font_size: '28sp'
                    markup: True



<Exe7>
    BoxLayout:
        orientation: 'vertical'

        Label:
            size_hint_y:.50
            text:'Selecciona el tiempo verbal correcto de la oración dada:'
            markup: True
            font_size:'25sp'
        Label:
            size_hint_y:.20
            text:'[color=ff9900]He had been driving for hours before he arrived.[/color]'
            markup: True
            font_size:'30sp'
        GridLayout:
            cols: 2
            padding: 30
            row_force_default:True
            row_default_height:35
            CheckBox:
                id: B1
                text: "Button 1"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L1
                text: "                    Presente Progresivo"
                size_hint_x: None
                width: 100
            CheckBox:
                id: B2
                text: "Button 3"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L2
                text: "             Pasado perfecto"
                size_hint_x: None
                width: 100
            CheckBox:
                id: B3
                text: "Button 5"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
                active: False
            Label:
                id: L3
                text: "                                 Pasado Perfecto Progresivo"
                size_hint_x: None
                width: 100
                markup: True
            CheckBox:
                id: B4
                text: "Button 5"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L4
                text: "                 Presente Perfecto"
                size_hint_x: None
                width: 100
        Label:
            size_hint_y:.9

            FloatLayout:
                Button:
                    id: btn1
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.8}
                    text: 'Check'
                    background_color: [.7,.7,1,1]
                    on_press: if B3.active == True: message.text = '[color=009900]Excelente![/color]'
                    on_press: if B3.active== False: message.text = '[color=ff3333]Lo siento! , Presione Next[/color]'

                    on_release: if B3.active == True: btn1.state = 'down'
                    on_release: if B3.active == True: btn2.disabled = False
                    on_release: if B3.active == False: btn2.disabled = False
                    on_release: if B3.active == False: btn1.state = 'down'
                    on_release: if B3.active == True: L3.text='[color=009900]                                 Pasado Perfecto Progresivo[/color]'
                    on_release: if B3.active == False: L3.text='[color=009900]                                 Pasado Perfecto Progresivo[/color]'
                    on_release: if B3.active == False: B1.disabled,B2.disabled,B3.disabled = 'off'
                    on_release: if B3.active == False: B4.disabled = 'off'
                    on_release: if B3.active == True: B1.disabled,B2.disabled,B4.disabled = 'off'
                Button:
                    id: btn2
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.2}
                    text: 'Next'
                    background_color: [.7,.7,1,1]
                    on_release: root.manager.current = root.manager.next()
                    disabled: True

                Label:
                    id: message
                    text: ''
                    pos_hint:{'x': 4, 'y': 1.55}
                    font_size: '28sp'
                    markup: True
<Exe8>

    BoxLayout:
        orientation: 'vertical'

        Label:
            size_hint_y:.50
            text:'Selecciona el tiempo verbal correcto de la oración dada:'
            markup: True
            font_size:'25sp'
        Label:
            size_hint_y:.20
            text:'[color=ff9900]The engine functioned perfectly during the test flight.[/color]'
            markup: True
            font_size:'30sp'
        GridLayout:
            cols: 2
            padding: 30
            row_force_default:True
            row_default_height:35
            CheckBox:
                id: B1

                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L1
                text: "                    Pasado Progresivo"
                size_hint_x: None
                width: 100
            CheckBox:
                id: B2

                size_hint_x: None
                width: 50
                height: 20
                group:'A'
                active: False
            Label:
                id: L2
                text: "             Pasado simple"
                size_hint_x: None
                width: 100
                markup: True
            CheckBox:
                id: B3

                size_hint_x: None
                width: 50
                height: 20
                group:'A'

            Label:
                id: L3
                text: "                                 Pasado Perfecto Progresivo"
                size_hint_x: None
                width: 100
                markup: True
            CheckBox:
                id: B4

                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L4
                text: "                 Presente Perfecto"
                size_hint_x: None
                width: 100
        Label:
            size_hint_y:.9

            FloatLayout:
                Button:
                    id: btn1
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.8}
                    text: 'Check'
                    background_color: [.7,.7,1,1]
                    on_press: if B2.active == True: message.text = '[color=009900]Excelente![/color]'
                    on_press: if B2.active== False: message.text = '[color=ff3333]Lo siento! , Presione Next[/color]'

                    on_release: if B2.active == True: btn1.state = 'down'
                    on_release: if B2.active == True: btn2.disabled = False
                    on_release: if B2.active == False: btn2.disabled = False
                    on_release: if B2.active == False: btn1.state = 'down'
                    on_release: if B2.active == True: L2.text='[color=009900]             Pasado simple[/color]'
                    on_release: if B2.active == False: L2.text='[color=009900]             Pasado simple[/color]'
                    on_release: if B2.active == False: B1.disabled,B3.disabled,B4.disabled = 'off'
                    on_release: if B2.active == False: B2.disabled = 'off'
                    on_release: if B2.active == True: B1.disabled,B3.disabled,B4.disabled = 'off'
                Button:
                    id: btn2
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.2}
                    text: 'Next'
                    background_color: [.7,.7,1,1]
                    on_release: root.manager.current = root.manager.next()
                    disabled: True

                Label:
                    id: message
                    text: ''
                    pos_hint:{'x': 4, 'y': 1.55}
                    font_size: '28sp'
                    markup: True

<Exe9>
    BoxLayout:
        orientation: 'vertical'

        Label:
            size_hint_y:.50
            text:'Selecciona el tiempo verbal correcto de la oración dada:'
            markup: True
            font_size:'25sp'
        Label:
            size_hint_y:.20
            text:'[color=ff9900]Some new aeronautical technicians are working\\nin La Carlota.[/color]'
            markup: True
            font_size:'30sp'
        GridLayout:
            cols: 2
            padding: 30
            row_force_default:True
            row_default_height:35
            CheckBox:
                id: B1
                text: "Button 1"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
                active: False
            Label:
                id: L1
                text: "                    Presente Progresivo"
                size_hint_x: None
                width: 100
                markup: True
            CheckBox:
                id: B2
                text: "Button 3"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'

            Label:
                id: L2
                text: "             Presente simple"
                size_hint_x: None
                width: 100

            CheckBox:
                id: B3
                text: "Button 5"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'

            Label:
                id: L3
                text: "                                 Presente Perfecto Progresivo"
                size_hint_x: None
                width: 100
                markup: True
            CheckBox:
                id: B4
                text: "Button 5"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L4
                text: "                Presente Perfecto"
                size_hint_x: None
                width: 100
        Label:
            size_hint_y:.9

            FloatLayout:
                Button:
                    id: btn1
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.8}
                    text: 'Check'
                    background_color: [.7,.7,1,1]
                    on_press: if B1.active == True: message.text = '[color=009900]Excelente![/color]'
                    on_press: if B1.active== False: message.text = '[color=ff3333]Lo siento! , Presione Next[/color]'

                    on_release: if B1.active == True: btn1.state = 'down'
                    on_release: if B1.active == True: btn2.disabled = False
                    on_release: if B1.active == False: btn2.disabled = False
                    on_release: if B1.active == False: btn1.state = 'down'
                    on_release: if B1.active == True: L1.text='[color=009900]                    Presente Progresivo[/color]'
                    on_release: if B1.active == False: L1.text='[color=009900]                    Presente Progresivo[/color]'
                    on_release: if B1.active == False: B2.disabled,B3.disabled,B4.disabled = 'off'
                    on_release: if B1.active == False: B1.disabled = 'off'
                    on_release: if B1.active == True: B2.disabled,B3.disabled,B4.disabled = 'off'
                Button:
                    id: btn2
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.2}
                    text: 'Next'
                    background_color: [.7,.7,1,1]
                    on_release: root.manager.current = root.manager.next()
                    disabled: True

                Label:
                    id: message
                    text: ''
                    pos_hint:{'x': 4, 'y': 1.55}
                    font_size: '28sp'
                    markup: True

<Exe10>
    BoxLayout:
        orientation: 'vertical'

        Label:
            size_hint_y:.50
            text:'Selecciona el tiempo verbal correcto de la oración dada:'
            markup: True
            font_size:'25sp'
        Label:
            size_hint_y:.20
            text:'[color=ff9900]Janet will be talking, and Emily will be listening to\\nevery word.[/color]'
            markup: True
            font_size:'30sp'
        GridLayout:
            cols: 2
            padding: 30
            row_force_default:True
            row_default_height:35
            CheckBox:
                id: B1
                text: "Button 1"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L1
                text: "                                  Futuro Perfecto Progresivo"
                size_hint_x: None
                width: 100

            CheckBox:
                id: B2
                text: "Button 3"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L2
                text: "                Futuro perfecto"
                size_hint_x: None
                width: 100
            CheckBox:
                id: B3
                text: "Button 5"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
                active: False
            Label:
                id: L3
                text: "                  Futuro Progresivo"
                size_hint_x: None
                width: 100
                markup: True
            CheckBox:
                id: B4
                text: "Button 5"
                size_hint_x: None
                width: 50
                height: 20
                group:'A'
            Label:
                id: L4
                text: "Futuro"
                size_hint_x: None
                width: 100
        Label:
            size_hint_y:.9

            FloatLayout:
                Button:
                    id: btn1
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.8}
                    text: 'Check'
                    background_color: [.7,.7,1,1]
                    on_press: if B3.active == True: message.text = '[color=009900]Excelente![/color]'
                    on_press: if B3.active== False: message.text = '[color=ff3333]Lo siento! , Presione Next[/color]'

                    on_release: if B3.active == True: btn1.state = 'down'
                    on_release: if B3.active == True: btn2.disabled = False
                    on_release: if B3.active == False: btn2.disabled = False
                    on_release: if B3.active == False: btn1.state = 'down'
                    on_release: if B3.active == True: L3.text='[color=009900]                  Futuro Progresivo[/color]'
                    on_release: if B3.active == False: L3.text='[color=009900]                  Futuro Progresivo[/color]'
                    on_release: if B3.active == False: B1.disabled,B2.disabled,B3.disabled = 'off'
                    on_release: if B3.active == False: B4.disabled = 'off'
                    on_release: if B3.active == True: B1.disabled,B2.disabled,B4.disabled = 'off'
                Button:
                    id: btn2
                    size_hint: .7, .42
                    pos_hint:{'x': 1.6, 'y': 1.2}
                    text: 'Next'
                    background_color: [.7,.7,1,1]
                    on_release: root.manager.current = root.manager.next()
                    disabled: True

                Label:
                    id: message
                    text: ''
                    pos_hint:{'x': 4, 'y': 1.55}
                    font_size: '28sp'
                    markup: True

<Exe11>

    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
        Button:
            text: "[color=ff9900]Resultado de los ejercicios[/color]"
            font_size:'25dp'
            size_hint: 1, None
            markup: True
        GridLayout:
            cols: 2
            Label:
                text: "[color=009900]Total de respuestas correctas[/color]"
                font_size:'25dp'
                markup: True

            Button:
                text: "07"
                size_hint_x: None
                width: 100
            Label:
                text: "[color=ff3333]Total de respuestas incorrectas[/color]"
                font_size:'25dp'
                markup: True
            Button:
                text: "03"
                size_hint_x: None
                width: 100
            Label:
                text: "[color=3333ff]Puntuación total[/color]"
                font_size:'25dp'
                markup: True

            Button:
                text: "7/10"
                size_hint_x: None
                width: 100
        Button:
            text: "Retornar a inicio"
            font_size:'25dp'
            size_hint: 1, None



''')


# declara las pantallas


class Exe6(Screen):
    pass


class Exe7(Screen):
    pass


class Exe8(Screen):
    pass


class Exe9(Screen):
    pass


class Exe10(Screen):
    pass


class Exe11(Screen):
    pass

# Crea el screenmanager


sm = ScreenManager()

sm.add_widget(Exe6(name='Exe6'))


sm.add_widget(Exe7(name='Exe7'))


sm.add_widget(Exe8(name='Exe8'))


sm.add_widget(Exe9(name='Exe9'))


sm.add_widget(Exe10(name='Exe10'))


sm.add_widget(Exe11(name='Exe11'))







class InglesIApp(App):
    def build(self):
        Window.clearcolor = 0, 0, 0.1, 0.8
        return sm




if __name__ == '__main__':
    InglesIApp().run()
