from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="DEDSEC - NETHACK AUTH", font_size=30, color=(0, 1, 0, 1)))
        self.key_input = TextInput(hint_text="Chave de Operativo", password=True, multiline=False)
        layout.add_widget(self.key_input)
        btn_entrar = Button(text="AUTENTICAR", background_color=(0, 0.7, 0, 1))
        btn_entrar.bind(on_press=self.verificar_chave)
        layout.add_widget(btn_entrar)
        self.add_widget(layout)

    def verificar_chave(self, instance):
        if self.key_input.text == "DEDSEC_MASTER_2024":
            self.manager.current = 'nethack_main'
        else:
            self.key_input.hint_text = "ACESSO NEGADO"
            self.key_input.text = ""

class NetHackMain(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()
        self.layout.add_widget(Label(text="[ CAMERA FEED ATIVO ]", color=(0, 0.5, 0, 1)))
        with self.layout.canvas.after:
            Color(0, 1, 0, 0.1)
            self.rect = Rectangle(size=(2000, 2000))
        self.btn_hack = Button(text="SEGURE PARA ACESSAR", size_hint=(0.8, 0.15),
                              pos_hint={'center_x': 0.5, 'y': 0.05}, background_color=(0, 0.3, 0, 1))
        self.btn_hack.bind(on_press=self.iniciar_contagem)
        self.btn_hack.bind(on_release=self.parar_contagem)
        self.layout.add_widget(self.btn_hack)
        self.tempo = 0
        self.add_widget(self.layout)

    def iniciar_contagem(self, instance):
        self.tempo = 0
        Clock.schedule_interval(self.contar, 0.1)

    def parar_contagem(self, instance):
        Clock.unschedule(self.contar)
        if self.tempo < 2.0:
            self.btn_hack.text = "CANCELADO (SEGURE 2s)"
            self.btn_hack.background_color = (0, 0.3, 0, 1)

    def contar(self, dt):
        self.tempo += dt
        progresso = int((self.tempo / 2.0) * 100)
        self.btn_hack.text = f"ACESSANDO... {progresso}%"
        if self.tempo >= 2.0:
            self.btn_hack.text = "!!! SISTEMA DOMINADO !!!"
            self.btn_hack.background_color = (1, 0, 0, 1)
            return False

class NetHackApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(NetHackMain(name='nethack_main'))
        return sm

if __name__ == '__main__':
    NetHackApp().run()

