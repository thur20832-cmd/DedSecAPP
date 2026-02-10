from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import random

# Definindo a cor de fundo preta
Window.clearcolor = (0, 0, 0, 1)

class DedSecApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15)
        
        # Logo Estilizado
        self.logo = Label(
            text="[DED SEC]", 
            font_size='50sp',
            color=(0, 1, 0, 1), # Verde Neon
            markup=True,
            bold=True
        )
        self.add_widget(self.logo)

        # Status do Sistema
        self.status = Label(
            text="STATUS: ENCRYPTED",
            font_size='18sp',
            color=(0.5, 0.5, 0.5, 1) # Cinza
        )
        self.add_widget(self.status)

        # Botão de Interação
        self.btn = Button(
            text="INITIALIZE SCAN",
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 0, 1),
            color=(1, 1, 1, 1),
            font_name='Roboto' # No Android ele pega a fonte padrão
        )
        self.btn.bind(on_press=self.start_scan)
        self.add_widget(self.btn)

        # Console de Logs (Onde a mágica acontece)
        self.console = Label(
            text="> Waiting for command...",
            font_size='14sp',
            color=(0, 0.8, 0, 1),
            halign='left',
            valign='top',
            text_size=(Window.width - 40, None)
        )
        self.add_widget(self.console)

    def start_scan(self, instance):
        self.console.text = "> Bypassing firewall...\n> Accessing ctOS node..."
        self.status.text = "STATUS: BREACHING..."
        self.status.color = (1, 0, 0, 1) # Muda pra vermelho
        # Faz um efeito de log subindo
        Clock.schedule_once(self.update_log, 1)

    def update_log(self, dt):
        ips = [f"192.168.0.{random.randint(1, 255)}" for _ in range(3)]
        self.console.text += f"\n> Targets found: {', '.join(ips)}\n> Decrypting data..."
        self.status.text = "STATUS: DATA EXTRACTED"
        self.status.color = (0, 1, 1, 1) # Ciano

class MainApp(App):
    def build(self):
        return DedSecApp()

if __name__ == "__main__":
    MainApp().run()
    
