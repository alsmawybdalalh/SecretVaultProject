from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import os


# =========================
# شاشة البداية
# =========================
class SplashScreen(Screen):

    def build_ui(self):
        layout = BoxLayout(orientation="vertical", spacing=20, padding=40)

        title = Label(text="SecretVault", font_size="32sp")

        btn = Button(text="دخول", size_hint=(1, 0.3))
        btn.bind(on_press=self.go_next)

        layout.add_widget(title)
        layout.add_widget(btn)

        self.add_widget(layout)

    def go_next(self, instance):
        self.manager.current = "calc"


# =========================
# الآلة الحاسبة
# =========================
class CalculatorScreen(Screen):

    def build_ui(self):
        self.layout = BoxLayout(orientation="vertical")

        self.display = TextInput(
            font_size=40,
            readonly=True,
            halign="right"
        )

        self.layout.add_widget(self.display)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "C","0","=","+"
        ]

        grid = BoxLayout()

        for b in buttons:
            btn = Button(text=b)
            btn.bind(on_press=self.press)
            grid.add_widget(btn)

        self.layout.add_widget(grid)
        self.add_widget(self.layout)

    def press(self, instance):
        t = instance.text

        if t == "C":
            self.display.text = ""

        elif t == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "0"
        else:
            self.display.text += t

        if self.display.text == "7007":
            self.manager.current = "vault"


# =========================
# الخزنة (بسيطة)
# =========================
class VaultScreen(Screen):

    def build_ui(self):
        layout = BoxLayout()

        label = Label(text="الخزنة السرية 🔒")

        layout.add_widget(label)
        self.add_widget(layout)


# =========================
# التطبيق
# =========================
class SecretVaultApp(App):

    def build(self):

        sm = ScreenManager()

        splash = SplashScreen(name="splash")
        splash.build_ui()

        calc = CalculatorScreen(name="calc")
        calc.build_ui()

        vault = VaultScreen(name="vault")
        vault.build_ui()

        sm.add_widget(splash)
        sm.add_widget(calc)
        sm.add_widget(vault)

        sm.current = "splash"

        return sm


if __name__ == "__main__":
    SecretVaultApp().run()