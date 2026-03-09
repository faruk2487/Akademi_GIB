from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.login_screen import LoginScreen
from screens.home_screen import HomeScreen
from screens.quiz_screen import QuizScreen

class AkademiApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(QuizScreen(name="quiz"))

        return sm

if __name__ == "__main__":
    AkademiApp().run()
