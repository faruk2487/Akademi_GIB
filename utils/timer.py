from kivy.clock import Clock

class Timer:
    def __init__(self, duration, on_tick=None, on_complete=None):
        self.duration = duration
        self.remaining_time = duration
        self.on_tick = on_tick
        self.on_complete = on_complete
        self.is_running = False
        self.event = None
    
    def start(self):
        """Zamanlayıcıyı başlat"""
        if not self.is_running:
            self.is_running = True
            self.event = Clock.schedule_interval(self._tick, 1)
    
    def _tick(self, dt):
        """Her saniye çağrılır"""
        self.remaining_time -= 1
        
        if self.on_tick:
            self.on_tick(self.remaining_time)
        
        if self.remaining_time <= 0:
            self.stop()
            if self.on_complete:
                self.on_complete()
    
    def stop(self):
        """Zamanlayıcıyı durdur"""
        if self.is_running:
            self.is_running = False
            if self.event:
                self.event.cancel()
    
    def reset(self):
        """Zamanlayıcıyı sıfırla"""
        self.stop()
        self.remaining_time = self.duration
    
    def get_time_string(self):
        """Zamanı MM:SS formatında getir"""
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        return f"{minutes:02d}:{seconds:02d}"
