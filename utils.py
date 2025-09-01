import random #NIKHIL SAINI BOTS
import time #NIKHIL SAINI BOTS
import math #NIKHIL SAINI BOTS
import os #NIKHIL SAINI BOTS
from vars import CREDIT #NIKHIL SAINI BOTS
from pyrogram.errors import FloodWait #NIKHIL SAINI BOTS
from datetime import datetime,timedelta #NIKHIL SAINI BOTS

class Timer: #NIKHIL SAINI BOTS
    def __init__(self, time_between=5): #NIKHIL SAINI BOTS
        self.start_time = time.time() #NIKHIL SAINI BOTS
        self.time_between = time_between #NIKHIL SAINI BOTS

    def can_send(self): #NIKHIL SAINI BOTS
        if time.time() > (self.start_time + self.time_between): #NIKHIL SAINI BOTS
            self.start_time = time.time() #NIKHIL SAINI BOTS
            return True #NIKHIL SAINI BOTS
        return False #NIKHIL SAINI BOTS

#lets do calculations #NIKHIL SAINI BOTS
def hrb(value, digits= 2, delim= "", postfix=""): #NIKHIL SAINI BOTS
    """Return a human-readable file size. #NIKHIL SAINI BOTS
    """ #NIKHIL SAINI BOTS
    if value is None: #NIKHIL SAINI BOTS
        return None #NIKHIL SAINI BOTS
    chosen_unit = "B" #NIKHIL SAINI BOTS
    for unit in ("KB", "MB", "GB", "TB"): #NIKHIL SAINI BOTS
        if value > 1000: #NIKHIL SAINI BOTS
            value /= 1024 #NIKHIL SAINI BOTS
            chosen_unit = unit #NIKHIL SAINI BOTS
        else: #NIKHIL SAINI BOTS
            break #NIKHIL SAINI BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #NIKHIL SAINI BOTS

def hrt(seconds, precision = 0): #NIKHIL SAINI BOTS
    """Return a human-readable time delta as a string. #NIKHIL SAINI BOTS
    """ #NIKHIL SAINI BOTS
    pieces = [] #NIKHIL SAINI BOTS
    value = timedelta(seconds=seconds) #NIKHIL SAINI BOTS

    if value.days: #NIKHIL SAINI BOTS
        pieces.append(f"{value.days}day") #NIKHIL SAINI BOTS

    seconds = value.seconds #NIKHIL SAINI BOTS

    if seconds >= 3600: #NIKHIL SAINI BOTS
        hours = int(seconds / 3600) #NIKHIL SAINI BOTS
        pieces.append(f"{hours}hr") #NIKHIL SAINI BOTS
        seconds -= hours * 3600 #NIKHIL SAINI BOTS

    if seconds >= 60: #NIKHIL SAINI BOTS
        minutes = int(seconds / 60) #NIKHIL SAINI BOTS
        pieces.append(f"{minutes}min") #NIKHIL SAINI BOTS
        seconds -= minutes * 60 #NIKHIL SAINI BOTS

    if seconds > 0 or not pieces: #NIKHIL SAINI BOTS
        pieces.append(f"{seconds}sec") #NIKHIL SAINI BOTS

    if not precision: #NIKHIL SAINI BOTS
        return "".join(pieces) #NIKHIL SAINI BOTS

    return "".join(pieces[:precision]) #NIKHIL SAINI BOTS

timer = Timer() #NIKHIL SAINI BOTS

async def progress_bar(current, total, reply, start): #NIKHIL SAINI BOTS
    if timer.can_send(): #NIKHIL SAINI BOTS
        now = time.time() #NIKHIL SAINI BOTS
        diff = now - start #NIKHIL SAINI BOTS
        if diff < 1: #NIKHIL SAINI BOTS
            return #NIKHIL SAINI BOTS
        else: #NIKHIL SAINI BOTS
            perc = f"{current * 100 / total:.1f}%" #NIKHIL SAINI BOTS
            elapsed_time = round(diff) #NIKHIL SAINI BOTS
            speed = current / elapsed_time #NIKHIL SAINI BOTS
            remaining_bytes = total - current #NIKHIL SAINI BOTS
            if speed > 0: #NIKHIL SAINI BOTS
                eta_seconds = remaining_bytes / speed #NIKHIL SAINI BOTS
                eta = hrt(eta_seconds, precision=1) #NIKHIL SAINI BOTS
            else: #NIKHIL SAINI BOTS
                eta = "-" #NIKHIL SAINI BOTS
            sp = str(hrb(speed)) + "/s" #NIKHIL SAINI BOTS
            tot = hrb(total) #NIKHIL SAINI BOTS
            cur = hrb(current) #NIKHIL SAINI BOTS
            bar_length = 10 #NIKHIL SAINI BOTS
            completed_length = int(current * bar_length / total) #NIKHIL SAINI BOTS
            remaining_length = bar_length - completed_length #NIKHIL SAINI BOTS

            symbol_pairs = [ #NIKHIL SAINI BOTS
                #("🟢", "⚪"), #NIKHIL SAINI BOTS
                #("⚫", "⚪"), #NIKHIL SAINI BOTS
                #("🔵", "⚪"), #NIKHIL SAINI BOTS
                #("🔴", "⚪"), #NIKHIL SAINI BOTS
                #("🔘", "⚪"), #NIKHIL SAINI BOTS
                ("🟩", "⬜") #NIKHIL SAINI BOTS
            ] #NIKHIL SAINI BOTS
            chosen_pair = random.choice(symbol_pairs) #NIKHIL SAINI BOTS
            completed_symbol, remaining_symbol = chosen_pair #NIKHIL SAINI BOTS

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #NIKHIL SAINI BOTS

            try: #NIKHIL SAINI BOTS
                #await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎🦋✨═══─╯`') 
                await reply.edit(f'<blockquote>`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`</blockquote>') 
            except FloodWait as e: #NIKHIL SAINI BOTS
                time.sleep(e.x) #NIKHIL SAINI BOTS 



import math
import subprocess

def split_file_ffmpeg(filepath, chunk_size=2*1024*1024*1024):
    """ Split large video file (>2GB) into parts using ffmpeg """
    try:
        # Get video duration using ffprobe
        cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", filepath
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        duration = float(result.stdout.strip())

        # Calculate number of parts based on file size
        total_size = os.path.getsize(filepath)
        num_parts = math.ceil(total_size / chunk_size)
        part_duration = duration / num_parts

        base, ext = os.path.splitext(filepath)
        output_files = []
        for i in range(num_parts):
            start_time = i * part_duration
            out_file = f"{base}_part{i+1}{ext}"
            cmd = [
                "ffmpeg", "-y", "-i", filepath, "-ss", str(start_time),
                "-t", str(part_duration), "-c", "copy", out_file
            ]
            subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output_files.append(out_file)

        return output_files
    except Exception as e:
        print(f"Split error: {e}")
        return [filepath]
