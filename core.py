#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core Facebook API functionality
"""

import re
import json
import asyncio
import aiohttp
from typing import List, Optional, Tuple
from pathlib import Path
import requests
from bs4 import BeautifulSoup

class FileUtils:
    def __init__(self, config):
        self.config = config
    
    def shuffle_file_lines(self, filepath: Path) -> bool:
        """Shuffle lines in file."""
        try:
            lines = filepath.read_text(encoding='utf-8').strip().split('\n')
            import random
            random.shuffle(lines)
            filepath.write_text('\n'.join(lines) + '\n', encoding='utf-8')
            return True
        except:
            return False
    
    def divide_file(self, filepath: Path, parts: int, output_dir: Path) -> List[Path]:
        """Divide file into parts."""
        try:
            lines = filepath.read_text(encoding='utf-8').strip().split('\n')
            chunk_size = len(lines) // parts
            result_files = []
            
            for i in range(parts):
                start = i * chunk_size
                end = start + chunk_size if i < parts - 1 else len(lines)
                chunk = lines[start:end]
                
                output_file = output_dir / f"{filepath.stem}_part{i+1}.txt"
                output_file.write_text('\n'.join(chunk) + '\n', encoding='utf-8')
                result_files.append(output_file)
            
            return result_files
        except:
            return []
    
    def remove_emoji_names(self, filepath: Path) -> int:
        """Remove emoji and stylish names."""
        try:
            emoji_pattern = re.compile(
                "["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                "]+", flags=re.UNICODE
            )
            
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            clean_lines = []
            for line in lines:
                clean_line = re.sub(r'[^0-9a-zA-Z\s|]', '', line.strip())
                if clean_line:
                    clean_lines.append(clean_line)
            
            unique_lines = list(dict.fromkeys(clean_lines))
            filepath.write_text('\n'.join(unique_lines) + '\n', encoding='utf-8')
            return len(unique_lines)
        except:
            return 0
    
    def cut_or_delete_lines(self, filepath: Path, start: int, end: int, 
                          cut_file: Optional[Path] = None) -> bool:
        """Cut or delete lines from file."""
        try:
            lines = filepath.read_text(encoding='utf-8').strip().split('\n')
            
            # 1-based indexing
            cut_lines = lines[start-1:end]
            remaining_lines = lines[:start-1] + lines[end:]
            
            # Write remaining lines back
            filepath.write_text('\n'.join(remaining_lines) + '\n', encoding='utf-8')
            
            # Save cut lines if requested
            if cut_file and cut_lines:
                cut_file.write_text('\n'.join(cut_lines) + '\n', encoding='utf-8')
            
            return True
        except:
            return False
    
    def separate_by_prefix(self, filepath: Path, prefixes: List[str], 
                         output_file: Path) -> int:
        """Separate lines by prefix."""
        try:
            lines = filepath.read_text(encoding='utf-8').strip().split('\n')
            matching_lines = []
            
            prefix_pattern = '|'.join(prefixes)
            for line in lines:
                if re.match(f'^{prefix_pattern}', line.strip()):
                    matching_lines.append(line.strip())
            
            if matching_lines:
                output_file.write_text('\n'.join(matching_lines) + '\n', encoding='utf-8')
            
            return len(matching_lines)
        except:
            return 0

class FacebookAPI:
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()
        self.token = ""
        self.cookie = ""
        self.is_logged_in = False
    
    def extract_uid_from_url(self, url: str) -> Optional[str]:
        """Extract UID from Facebook URL."""
        patterns = [
            r'facebook\.com/([0-9]+)',
            r'profile\.php\?id=([0-9]+)',
            r'facebook\.com/profile\.php\?id=([0-9]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url.lower())
            if match:
                return match.group(1)
        return None
    
    def login_with_cookie(self, cookie_str: str) -> Tuple[bool, str]:
        """Login with cookie (SIMULATED)."""
        try:
            # In real scenario, parse cookie and set session
            self.cookie = cookie_str
            self.session.cookies.update({c.split('=')[0]: c.split('=')[1] for c in cookie_str.split(';') if '=' in c})
            
            # Test login
            response = self.session.get("https://www.facebook.com", timeout=10)
            if response.status_code == 200:
                self.is_logged_in = True
                self.token = "simulated_token_" + str(hash(cookie_str))
                return True, "SUCCESS"
            return False, "INVALID COOKIE"
        except:
            return False, "LOGIN FAILED"
    
    def login_with_credentials(self, uid: str, password: str) -> Tuple[bool, str]:
        """Login with credentials (SIMULATED)."""
        # This is for demo - real login needs proper implementation
        self.is_logged_in = True
        self.token = f"demo_token_{uid}"
        return True, "LOGIN SUCCESS"
    
    def validate_login(self) -> Tuple[bool, int]:
        """Validate current login."""
        try:
            response = self.session.get("https://www.facebook.com", timeout=5)
            return response.status_code == 200, 0
        except:
            self.is_logged_in = False
            return False, 0
    
    async def dump_simple(self, uids: List[str], output_file: Path, 
                         progress_callback=None) -> int:
        """Simple friends dump (DEMO VERSION)."""
        count = 0
        all_ids = set()
        
        async with aiohttp.ClientSession() as session:
            for i, uid in enumerate(uids):
                if progress_callback:
                    progress_callback(f"Processing {i+1}/{len(uids)}: {uid}")
                
                # Simulate getting friends (in real: Graph API call)
                friends = self._simulate_friends(uid)
                all_ids.update(friends)
                count += len(friends)
                await asyncio.sleep(0.5)  # Rate limit
        
        # Save to file
        output_file.write_text('\n'.join(sorted(all_ids)) + '\n', encoding='utf-8')
        return len(all_ids)
    
    async def dump_unlimited(self, uids: List[str], output_file: Path, 
                           unsep_file: Optional[Path], sep_prefixes: Optional[List[str]],
                           progress_callback=None) -> Tuple[int, int]:
        """Unlimited dump (friends + followers simulation)."""
        main_count = await self.dump_simple(uids, output_file, progress_callback)
        
        if unsep_file:
            unsep_file.write_text(output_file.read_text(), encoding='utf-8')
            return main_count, main_count
        
        return main_count, 0
    
    def _simulate_friends(self, uid: str) -> List[str]:
        """Simulate friends list for demo."""
        # Demo data - replace with real API call
        base_ids = [f"{int(uid)+i}" for i in range(1, 11)]
        return base_ids[:5]  # Return 5 friends
    
    def logout(self):
        """Logout."""
        self.session.cookies.clear()
        self.token = ""
        self.cookie = ""
        self.is_logged_in = False