import config  # এটা থাকবে
from core import FacebookAPI, FileUtils
def _main_menu(self):
    while True:
        self.config.clear_screen()
        self.config.banner.mrbx_logo(self.config)  # 🔥 এই line যোগ
        print(f"{self.config.mc}MRBX Status: {'🟢 ON' if self.is_logged_in else '🔴 OFF'}{self.config.z}")
        
        print(f"{self.config.box('1')} {self.config.mr}REAL DUMP")
        print(f"{self.config.box('2')} {self.config.mg}HYBRID DUMP")
        # ... rest same

def run(self) -> None:
    try:
        self.config.initialize()
        self.config.show_banner()  # 🔥 এই line যোগ করুন
        self._main_menu()
    except:
        pass
