#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration and styling for Facebook Tool
"""

import os
import sys
import platform
import subprocess
from pathlib import Path
from typing import Callable

class Platform:
    def __init__(self):
        self.is_windows = platform.system() == "Windows"
        self.is_linux = platform.system() == "Linux"
        self.is_termux = "termux" in os.environ.get("PREFIX", "")
        self.is_android = self.is_termux

class Config:
    def __init__(self):
        self.platform = Platform()
        self.r = "\033[91m"  # Red
        self.g = "\033[92m"  # Green
        self.y = "\033[93m"  # Yellow
        self.b = "\033[94m"  # Blue
        self.p = "\033[95m"  # Purple
        self.c = "\033[96m"  # Cyan
        self.w = "\033[97m"  # White
        self.o = "\033[98m"  # Orange
        self.z = "\033[0m"   # Reset
        self.style_box = self.c + "╔═" + self.w
        
        if self.platform.is_windows:
            os.system('color')
            self.r, self.g, self.y = '[91m', '[92m', '[93m'
        
        self.output_dir = Path("output") if not self.platform.is_termux else Path("/sdcard/Download")
        self.data_dir = Path(".data")
        
    def initialize(self):
        """Initialize directories and files."""
        self.ensure_output_dir()
        self.data_dir.mkdir(exist_ok=True)
    
    def ensure_output_dir(self) -> Path:
        """Ensure output directory exists."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        return self.output_dir
    
    def get_output_path(self, filename: str) -> Path:
        """Get full output path."""
        return self.output_dir / filename
    
    def generate_filename(self, prefix: str = "ids") -> Path:
        """Generate timestamped filename."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return self.get_output_path(f"{prefix}_{timestamp}.txt")
    
    def clear_screen(self):
        """Clear terminal screen."""
        os.system('cls' if self.platform.is_windows else 'clear')
    
    def linex(self, count: int = 1):
        """Print separator line."""
        print(self.style_box + "═" * 50 + self.z)
    
    def box(self, char: str) -> str:
        """Create box character."""
        return f"{self.c}╔═{char}═{self.z}"
    
    def animate(self, text: str, delay: float = 0.05):
        """Typewriter animation."""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def open_social(self, platform: str):
        """Open social media links."""
        urls = {
            "tg": "https://t.me/SHAJON404",
            "wp": "https://whatsapp.com/channel/...",
            "fb": "https://facebook.com/...",
            "git": "https://github.com/SHAJON-404"
        }
        if platform in urls and not self.platform.is_termux:
            subprocess.run(["start", urls[platform]] if self.platform.is_windows 
                          else ["xdg-open", urls[platform]], shell=True)
    
    def check_storage_permission(self) -> bool:
        """Check Termux storage permission."""
        if self.platform.is_termux:
            result = subprocess.run(["termux-setup-storage"], 
                                  capture_output=True, text=True)
            return "/sdcard" in os.listdir("/")
        return True
    
    def setup_signal_handlers(self, handler: Callable):
        """Setup Ctrl+C handler."""
        import signal
        signal.signal(signal.SIGINT, lambda s, f: handler())
    
    def random_color(self) -> str:
        """Get random color."""
        import random
        colors = [self.g, self.y, self.b, self.p, self.c]
        return random.choice(colors)

import time