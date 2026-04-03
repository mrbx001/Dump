#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 COMPLETE WORKING FACEBOOK TOOL - TERMUX READY 🚀
Fixed for Termux - SHAJON-404 Style
"""

import sys
import time
import asyncio
import os
from pathlib import Path
from typing import List, Optional

# Import local modules
import config
from core import FacebookAPI, FileUtils

class App:
    def __init__(self) -> None:
        """Initialize application."""
        self._config = config.Config()
        self._api = FacebookAPI(self._config)
        self._file_utils = FileUtils(self._config)
    
    @property
    def config(self) -> config.Config:
        return self._config
    
    @property
    def api(self) -> FacebookAPI:
        return self._api
    
    @property
    def is_logged_in(self) -> bool:
        return self._api.is_logged_in
    
    def _get_input(self, prompt: str) -> str:
        return input(f'{self.config.style_box} {prompt}: {self.config.g}').strip()
    
    def _get_int_input(self, prompt: str, default: int = 1) -> int:
        try:
            return int(self._get_input(prompt))
        except:
            print(f"{self.config.r}[DEFAULT: {default}]")
            return default
    
    def _get_yes_no(self, prompt: str) -> bool:
        resp = self._get_input(f"{prompt} [y/n]").lower()
        return resp in ['y', 'yes', '1']
    
    def _get_uid_list(self) -> List[str]:
        print(f"{self.config.style_box} PASTE UID LIST (ENTER খালি দিন)")
        uids = []
        while True:
            try:
                line = input().strip()
                if not line:
                    break
                uid = line.split('|')[0].strip()
                if uid.isdigit():
                    uids.append(uid)
            except:
                break
        return uids
    
    async def _do_simple_dump(self):
        """Simple dump demo."""
        self.config.clear_screen()
        print(f"{self.config.style_box} 🔥 SIMPLE DUMP STARTED 🔥")
        
        if not self.api.is_logged_in:
            print(f"{self.config.r}LOGIN FIRST!")
            input("Press Enter...")
            return
        
        filename = self._get_input("Output filename")
        output_file = self.config.generate_filename(filename or "friends")
        
        uids = self._get_uid_list()
        if not uids:
            print("No UIDs!")
            return
        
        print(f"Processing {len(uids)} UIDs...")
        count = await self.api.dump_simple(uids, output_file)
        
        print(f"\n✅ DUMP COMPLETE!")
        print(f"📁 File: {self.config.g}{output_file}")
        print(f"👥 IDs: {self.config.g}{count}")
        input("\nPress Enter...")
    
    def _menu_file_utils(self):
        """File utility menu."""
        while True:
            self.config.clear_screen()
            print(f"{self.config.style_box} 📁 FILE UTILITIES")
            print("1. 🎲 File Mixer")
            print("2. ✂️  File Divider") 
            print("3. 🧹 Remove Duplicates")
            print("4. 😎 Remove Emojis")
            print("0. ⬅️  Back")
            
            choice = self._get_input("Choose").strip()
            
            if choice == "1":
                filepath = self._get_input("File path")
                if self._file_utils.shuffle_file_lines(Path(filepath)):
                    print("✅ File shuffled!")
            elif choice == "2":
                filepath = self._get_input("File path")
                parts = self._get_int_input("Parts")
                files = self._file_utils.divide_file(Path(filepath), parts, self.config.output_dir)
                print(f"✅ {len(files)} parts created!")
            elif choice == "3":
                filepath = self._get_input("File path")
                count = self._file_utils.remove_emoji_names(Path(filepath))
                print(f"✅ {count} clean lines!")
            elif choice == "0":
                break
            
            input("Press Enter...")
    
    def _do_cookie_login(self):
        """Cookie login."""
        self.config.clear_screen()
        print(f"{self.config.style_box} 🍪 COOKIE LOGIN")
        print("Paste sb= cookie from browser")
        
        cookie = self._get_input("Cookie")
        success, msg = self.api.login_with_cookie(cookie)
        
        if success:
            print(f"{self.config.g}✅ LOGIN SUCCESS!")
            print(f"Token: {self.api.token[:30]}...")
            time.sleep(2)
            return True
        else:
            print(f"{self.config.r}❌ {msg}")
            time.sleep(2)
            return False
    
    def _main_menu(self):
        """Main menu loop."""
        while True:
            self.config.clear_screen()
            print(f"{self.config.style_box} 🔥 FACEBOOK DUMP TOOL 🔥")
            print(f"Status: {'🟢 LOGGED IN' if self.is_logged_in else '🔴 LOGIN NEEDED'}")
            print("\n1️⃣  Login Cookie")
            print("2️⃣  💎 SIMPLE DUMP")
            print("3️⃣  📁 File Tools") 
            print("4️⃣  🔗 URL to UID")
            print("0️⃣  ❌ Exit")
            
            choice = self._get_input("Choose").strip()
            
            if choice == "1":
                self._do_cookie_login()
            elif choice == "2" and self.is_logged_in:
                asyncio.run(self._do_simple_dump())
            elif choice == "3":
                self._menu_file_utils()
            elif choice == "4":
                url = self._get_input("Facebook URL")
                uid = self.api.extract_uid_from_url(url)
                print(f"UID: {self.config.g}{uid or 'Not found'}")
                input()
            elif choice == "0":
                print("👋 Bye!")
                sys.exit(0)
            else:
                print("Invalid!")
                time.sleep(1)
    
    def run(self) -> None:
        """Main run method - FIXED!"""
        try:
            self.config.initialize()
            print("🚀 Tool Started!")
            self._main_menu()
        except KeyboardInterrupt:
            print("\n👋 Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"❌ Error: {e}")

# 🔥 MAIN ENTRY POINT
def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
