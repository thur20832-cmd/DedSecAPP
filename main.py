from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

# Configuração da Janela (Preto total)
Window.clearcolor = (0, 0, 0, 1)

class DedSecInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10)

        # 1. Cabeçalho Estilizado
        self.header = Label(
            text="[ DEDSEC // OS_V1.0 ]",
            font_size='24sp',
            color=(0, 1, 0, 1),
            size_hint_y=0.1,
            bold=True
        )
        self.add_widget(self.header)

        # 2. Grade de Botões (O "Jogo")
        # 2 colunas, botões organizados como na imagem que imaginamos
        self.menu_grid = GridLayout(cols=2, spacing=15, size_hint_y=0.6)
        
        # Lista de botões do DedSec
        self.buttons_data = [
            "NETHACK", "MAPS", 
            "MESSAGES", "PROFILE", 
            "BOTNET", "OBJECTIVES"
        ]

        for name in self.buttons_data:
            btn = Button(
                text=name,
                background_normal='', # Remove a imagem padrão cinza
                background_color=(0, 0.1, 0, 1), # Fundo verde escuro
                color=(0, 1, 0, 1), # Texto verde neon
                bold=True,
                border=(2, 2, 2, 2)
            )
            # Ao clicar, chama a função de ação
            btn.bind(on_release=self.on_button_click)
            self.menu_grid.add_widget(btn)

        self.add_widget(self.menu_grid)

        # 3. Console de Log (Feedback do jogo)
        self.console = Label(
            text="> SYSTEM ONLINE\n> WAITING FOR INPUT...",
            font_size='14sp',
            color=(0, 0.7, 0, 1),
            size_hint_y=0.3,
            halign='left',
            valign='top',
            text_size=(Window.width - 30, None)
        )
        self.add_widget(self.console)

    def on_button_click(self, instance):
        action = instance.text
        self.console.text = f"> INITIALIZING {action}...\n> BYPASSING SECURITY..."
        
        # Simula uma resposta após 1 segundo
        Clock.schedule_once(lambda dt: self.finish_action(action), 1)

    def finish_action(self, action):
        responses = {
            "NETHACK": "> SCANNING LOCAL NETWORK... \n> VULNERABILITIES DETECTED.",
            "MAPS": "> GPS ACTIVE. TRACKING SAN FRANCISCO NODES.",
            "MESSAGES": "> ENCRYPTED CHANNEL OPEN.",
            "PROFILE": "> USER: MARCUS // REPUTATION: UNKNOWN.",
            "BOTNET": "> BOTNET RESOURCES: 100% AVAILABLE.",
            "OBJECTIVES": "> MAIN TASK: BREACH CTOS 2.0."
        }
        self.console.text = responses.get(action, "> COMMAND EXECUTED.")

class DedSecApp(App):
    def build(self):
        return DedSecInterface()

if __name__ == "__main__":
    DedSecApp().run()
    
