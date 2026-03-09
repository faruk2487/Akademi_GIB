from kivy.uix.screen import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from database import Database

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()
        self.current_user = None
        self.build_ui()
    
    def build_ui(self):
        """Ana ekran UI oluştur"""
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Hoşgeldiniz mesajı
        self.welcome_label = Label(text='Hoşgeldiniz!', size_hint_y=0.2, font_size='24sp')
        layout.add_widget(self.welcome_label)
        
        # İstatistikler
        stats_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.3)
        
        self.total_exams_label = Label(text='Toplam Sınavlar\n0', size_hint_y=None, height=80)
        stats_layout.add_widget(self.total_exams_label)
        
        self.avg_score_label = Label(text='Ortalama Puan\n0', size_hint_y=None, height=80)
        stats_layout.add_widget(self.avg_score_label)
        
        layout.add_widget(stats_layout)
        
        # Butonlar
        button_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.4)
        
        start_exam_btn = Button(text='Sınava Başla', size_hint_y=None, height=60)
        start_exam_btn.bind(on_press=self.start_exam)
        button_layout.add_widget(start_exam_btn)
        
        view_results_btn = Button(text='Sonuçları Göster', size_hint_y=None, height=60)
        view_results_btn.bind(on_press=self.view_results)
        button_layout.add_widget(view_results_btn)
        
        logout_btn = Button(text='Çıkış Yap', size_hint_y=None, height=60)
        logout_btn.bind(on_press=self.logout)
        button_layout.add_widget(logout_btn)
        
        layout.add_widget(button_layout)
        self.add_widget(layout)
    
    def on_enter(self):
        """Ekrana girildiğinde çağrılır"""
        if hasattr(self, 'manager') and hasattr(self.manager, 'current_user'):
            self.current_user = self.manager.current_user
            self.welcome_label.text = f'Hoşgeldiniz, {self.current_user[1]}!'
            self.load_statistics()
    
    def load_statistics(self):
        """İstatistikleri yükle"""
        if self.current_user:
            results = self.db.get_user_results(self.current_user[0])
            
            self.total_exams_label.text = f'Toplam Sınavlar\n{len(results)}'
            
            if results:
                avg_score = sum([r[2] for r in results]) / len(results)
                self.avg_score_label.text = f'Ortalama Puan\n{int(avg_score)}'
            else:
                self.avg_score_label.text = 'Ortalama Puan\n0'
    
    def start_exam(self, instance):
        """Sınava başla"""
        if self.manager:
            self.manager.current = 'exam'
    
    def view_results(self, instance):
        """Sonuçları göster"""
        if self.current_user:
            results = self.db.get_user_results(self.current_user[0])
            
            if not results:
                self.show_popup('Bilgi', 'Henüz sınav sonucu yok!')
                return
            
            message = 'Son 5 Sınav Sonucu:\n\n'
            for i, result in enumerate(results[:5], 1):
                message += f'{i}. Puan: {result[2]}/{result[3]} - Başarı: {int(result[2]/result[3]*100)}%\n'
            
            self.show_popup('Sınav Sonuçları', message)
    
    def logout(self, instance):
        """Çıkış yap"""
        self.manager.current = 'login'
        self.current_user = None
    
    def show_popup(self, title, message):
        """Popup göster"""
        popup = Popup(title=title, size_hint=(0.9, 0.5))
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(Label(text=message))
        close_btn = Button(text='Kapat', size_hint_y=0.2)
        close_btn.bind(on_press=popup.dismiss)
        layout.add_widget(close_btn)
        popup.content = layout
        popup.open()
