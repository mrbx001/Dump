#!/usr/bin/env python3
import sys, time, asyncio
from pathlib import Path
import config
from core import FacebookAPI, FileUtils

class App:
    def __init__(self):
        self.config = config.Config()
        self.api = FacebookAPI(self.config)
        self.utils = FileUtils()
    
    def _get_input(self, prompt):
        return input(f"{self.config.mc}{prompt}{self.config.z} ").strip()
    
    def _get_uid_list(self):
        print("UIDs paste (Enter):")
        uids = []
        while True:
            try:
                line = input().strip()
                if not line: break
                uids.append(line.split('|')[0])
            except: break
        return uids
    
    async def _dump(self):
        self.config.show_banner()
        filename = self._get_input("Filename [mrbx_ids]")
        output = self.config.generate_filename(filename or "mrbx_ids")
        
        uids = self._get_uid_list()
        if not uids: return
        
        print("Dumping...")
        count = await self.api.dump_simple(uids, output)
        
        print(f"\n{self.config.mg}✅ MRBX Dump Complete!")
        print(f"📁 {output}")
        print(f"👥 {count} IDs")
        input()
    
    def run(self):
        while True:
            self.config.show_banner()
            print(f"{self.config.box('1')} {self.config.mr}MRBX DUMP")
            print(f"{self.config.box('2')} {self.config.mg}FILE MIX")
            print(f"{self.config.box('0')} {self.config.mr}EXIT")
            
            choice = self._get_input("MRBX> ").strip()
            
            if choice == '1':
                asyncio.run(self._dump())
            elif choice == '2':
                path = Path(self._get_input("File"))
                if self.utils.shuffle_file_lines(path):
                    print("✅ Mixed!")
                input()
            elif choice == '0':
                print("👋 MRBX Bye!")
                break
    
    def box(self, char):
        return f"{self.config.mc}╔═{char}═"

App().run()
