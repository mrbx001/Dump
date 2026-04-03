# main.py এর run() method এ:
def run(self) -> None:
    """Main run with MRBX logo."""
    try:
        self.config.initialize()
        self.config.show_banner()  # 🔥 MRBX LOGO এখানে!
        print(f"{self.config.g}🚀 MRBX Tool Ready!")
        print(f"{self.config.y}📱 Termux: {self.config.platform.is_termux}")
        self._main_menu()
    except KeyboardInterrupt:
        print(f"\n{self.config.r}👋 MRBX: Bye!")
        sys.exit(0)

# _main_menu update:
def _main_menu(self):
    """MRBX Main Menu."""
    while True:
        self.config.clear_screen()
        self.config.banner.mrbx_logo()  # Logo প্রতিবার!
        
        status = f"{'🟢 LOGGED IN' if self.is_logged_in else '🔴 LOGIN NEEDED'}"
        print(f"{self.config.style_box} Status: {self.config.p}{status}")
        self.config.linex()
        
        print(f"{self.config.box('1')} 🔥 {self.config.g}REAL FRIENDS DUMP")
        print(f"{self.config.box('2')} 💎 {self.config.y}HYBRID DUMP (Fast)")
        print(f"{self.config.box('3')} 📁 {self.config.c}FILE TOOLS")
        print(f"{self.config.box('4')} 🔗 {self.config.b}URL→UID")
        print(f"{self.config.box('5')} 🍪 {self.config.p}COOKIE LOGIN")
        print(f"{self.config.box('0')} ❌ {self.config.r}EXIT MRBX")
        
        self.config.linex()
        choice = self._get_input("MRBX> ").strip()
        
        # Menu logic...
