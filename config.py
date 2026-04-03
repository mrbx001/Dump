#!/usr/bin/env python3
import os, sys, time
from pathlib import Path
from datetime import datetime

class Config:
    def __init__(self):
        self.mc = "\033[96m"
        self.mr = "\033[91m"
        self.mg = "\033[92m"
        self.mp = "\033[95m"
        self.z = "\033[0m"
        self.output_dir = Path("/sdcard/Download")
    
    def show_banner(self):
        os.system('clear')
        print(f"""
{self.mc}╔══════════════════════════════════════╗
{self.mc}║{self.mr}    ██╗  ██╗███████╗███╗   ███╗   {self.mc}║
{self.mc}║{self.mr}    ██║  ██║██╔════╝████╗ ████║   {self.mc}║
{self.mc}║{self.mr}    ███████║█████╗  ██╔████╔██║   {self.mc}║
{self.mc}║{self.mr}    ██╔══██║██╔══╝  ██║╚═█╔╝██║   {self.mc}║
{self.mc}║{self.mg}    ██║  ██║███████╗██║ ╚═╝ ██║   {self.mc}║
{self.mc}║{self.mg}    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝   {self.mc}║
{self.mc}╠══════════════════════════════════════╣
{self.mc}║{self.mp}    🔥 MRBX Facebook Tool 🔥     {self.mc}║
{self.mc}╚══════════════════════════════════════╝{self.z}
        """)
        print(f"{self.mc}═{'═' * 48}{self.z}")
    
    def generate_filename(self, prefix="mrbx"):
        ts = datetime.now().strftime("%d%m%Y_%H%M")
        return self.output_dir / f"MRBX_{prefix}_{ts}.txt"
    
    def clear_screen(self):
        os.system('clear')
    
    def linex(self):
        print(f"{self.mc}═{'═' * 48}{self.z}")
