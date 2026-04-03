#!/usr/bin/env python3
"""
MRBX Facebook Tool - Config
"""

import os
import sys
import platform
import subprocess
import time
from pathlib import Path
from datetime import datetime
from typing import Callable

class Platform:
    def __init__(self):
        self.is_windows = platform.system() == "Windows"
        self.is_linux = platform.system() == "Linux"
        self.is_termux = "termux" in os.environ.get("PREFIX", "")
        self.is_android = self.is_termux

class Banner:
    """MRBX Logo & Banners"""
    def mrbx_logo(self, config) -> str:
        logo = f"""
{config.mc}╔══════════════════════════════════════╗{config.z}
{config.mc}║{config.mr}    ██╗  ██╗███████╗███╗   ███╗   {config.mc}║{config.z}
{config.mc}║{config.mr}    ██║  ██║██╔════╝████╗ ████║   {config.mc}║{config.z}
{config.mc}║{config.mr}    ███████║█████╗  ██╔████╔██║   {config.mc}║{config.z}
{config.mc}║{config.mr}    ██╔══██║██╔══╝  ██║╚═█╔╝██║   {config.mc}║{config.z}
{config.mc}║{config.mg}    ██║  ██║███████╗██║ ╚═╝ ██║   {config.mc}║{config.z}
{config.mc}║{config.mg}    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝   {config.mc}║{config.z}
{config.mc}╠══════════════════════════════════════╣{config.z}
{config.mc}║{config.mp}    🔥 MRBX Facebook Tool 🔥{config.w}     {config.mc}║{config.z}
{config.mc}║{config.my}    Real UID|Name Dumper{config.w}         {config.mc}║{config.z}
{config.mc}╚══════════════════════════════════════╝{config.z}
        """
        return logo

class Config:
    def __init__(self):
        self.platform = Platform()
        
        # MRBX Colors
        self.mr = "\033[91m"  # MR Red
        self.mg = "\033[92m"  # MR Green
        self.my = "\033[93m"  # MR Yellow
        self.mb = "\033[94m"  # MR Blue
        self.mp = "\033[95m"  # MR Purple
        self.mc = "\033[96m"  # MR Cyan
        self.mw = "\033[97m"  # MR White
        self.z = "\033[0m"
        
        self.banner = Banner()
        self.output_dir = Path("/sdcard/Download") if self.platform.is_termux else Path("output")
    
    def show_banner(self):
        """MRBX Logo."""
        self.clear_screen()
        print(self.banner.mrbx_logo(self))
        self.linex()
    
    def clear_screen(self):
        os.system('clear')
    
    def linex(self):
        print(f"{self.mc}═{'═' * 48}{self.z}")
    
    def box(self, char):
        return f"{self.mc}╔═{char}═{self.z}"
    
    def generate_filename(self, prefix="mrbx_ids"):
        timestamp = datetime.now().strftime("%d%m%Y_%H%M")
        return self.output_dir / f"MRBX_{prefix}_{timestamp}.txt"
    
    def initialize(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)
