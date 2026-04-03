#!/usr/bin/env python3
from typing import List
from pathlib import Path
import random

class FileUtils:
    def shuffle_file_lines(self, path):
        try:
            lines = path.read_text().splitlines()
            random.shuffle(lines)
            path.write_text('\n'.join(lines))
            return True
        except:
            return False

class FacebookAPI:
    def __init__(self, config):
        self.config = config
        self.is_logged_in = True  # Demo
    
    def extract_uid_from_url(self, url):
        import re
        match = re.search(r'facebook\.com/(\d+)', url)
        return match.group(1) if match else None
    
    async def dump_simple(self, uids: List[str], output: Path):
        all_ids = []
        for uid in uids:
            # Realistic demo
            for i in range(random.randint(15, 35)):
                fid = f"{int(uid)+random.randint(1000,99999)}"
                name = random.choice(["Rakib", "Sajon", "Fatema", "Imran"])
                all_ids.append(f"{fid}|{name}")
        
        unique = list(dict.fromkeys(all_ids))
        output.write_text('\n'.join(unique))
        return len(unique)
