from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from models.user import User
from database import Database

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()
        self.current_user = None
        self.build_ui()
    
    def build_ui(self):
        """UI oluştur"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Başlık
        title = Label(text='[b]Akademi_GIB[/b]\nSınav Hazırlık Uygulaması', 
                     markup=True, size_hint_y=0.3, font_size='24sp')
        layout.add_widget(title)
        
        # Form
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.5)
        
        # Kullanıcı adı
        form_layout.add_widget(Label(text='Kullanıcı Adı:', size_hint_y=None, height=40))
        self.username_input = TextInput(multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.username_input)
        
        # Şifre
        form_layout.add_widget(Label(text='Şifre:', size_hint_y=None, height=40))
        self.password_input = TextInput(password=True, multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.password_input)
        
        layout.add_widget(form_layout)
        
        # Butonlar
        button_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        
        login_btn = Button(text='Giriş Yap')
        login_btn.bind(on_press=self.login)
        button_layout.add_widget(login_btn)
        
        register_btn = Button(text='Kayıt Ol')
        register_btn.bind(on_press=self.register)
        button_layout.add_widget(register_btn)
        
        layout.add_widget(button_layout)
        self.add_widget(layout)
    
    def login(self, instance):
        """Giriş işlemi"""
        username = self.username_input.text
        password = self.password_input.text
        
        if not username or not password:
            self.show_popup('Hata', 'Lütfen tüm alanları doldurun!')
            return
        
        user = self.db.get_user(username)
        if user and User.verify_password(password, user[2]):
            self.current_user = user
            self.manager.current = 'home'
            self.show_popup('Başarılı', f'Hoşgeldiniz {username}!')
        else:
            self.show_popup('Hata', 'Kullanıcı adı veya şifre yanlış!')
    
    def register(self, instance):
        """Kayıt işlemi"""
        username = self.username_input.text
        password = self.password_input.text
        
        if not username or not password:
            self.show_popup('Hata', 'Lütfen tüm alanları doldurun!')
            return
        
        if len(password) < 6:
            self.show_popup('Hata', 'Şifre en az 6 karakter olmalı!')
            return
        
        hashed_password = User.hash_password(password)
        if self.db.add_user(username, hashed_password):
            self.show_popup('Başarılı', 'Kayıt başarılı! Şimdi giriş yapabilirsiniz.')
            self.username_input.text = ''
            self.password_input.text = ''
        else:
            self.show_popup('Hata', 'Bu kullanıcı adı zaten var!')
    
    def show_popup(self, title, message):
        """Popup göster"""
        popup = Popup(title=title, size_hint=(0.9, 0.3))
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text=message))
        close_btn = Button(text='Kapat', size_hint_y=0.3)
        close_btn.bind(on_press=popup.dismiss)
        layout.add_widget(close_btn)
        popup.content = layout
        popup.open()
