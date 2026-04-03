# config.py এর শুরুতে এই class add করুন (line 10 এর পরে):

class Banner:
    def mrbx_logo(self):
        """MRBX Logo - ASCII Art"""
        logo = f"""
{self.c}╔══════════════════════════════════════╗{self.z}
{self.c}║{self.r}    ██╗  ██╗███████╗███╗   ███╗   {self.c}║{self.z}
{self.c}║{self.r}    ██║  ██║██╔════╝████╗ ████║   {self.c}║{self.z}
{self.c}║{self.r}    ███████║█████╗  ██╔████╔██║   {self.c}║{self.z}
{self.c}║{self.r}    ██╔══██║██╔══╝  ██║╚═█╔╝██║   {self.c}║{self.z}
{self.c}║{self.g}    ██║  ██║███████╗██║ ╚═╝ ██║   {self.c}║{self.z}
{self.c}║{self.g}    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝   {self.c}║{self.z}
{self.c}╠══════════════════════════════════════╣{self.z}
{self.c}║{self.p}    🔥 MRBX Facebook Tool 🔥{self.w}     {self.c}║{self.z}
{self.c}║{self.y}    Real UID|Name Dumper{self.w}         {self.c}║{self.z}
{self.c}╚══════════════════════════════════════╝{self.z}
        """
        return logo

# Config class এ add করুন:
class Config:
    def __init__(self):
        # ... আগের codes ...
        self.banner = Banner()
    
    def show_banner(self):
        """Show MRBX logo."""
        self.clear_screen()
        print(self.banner.mrbx_logo())
        self.linex()
        time.sleep(1.5)
