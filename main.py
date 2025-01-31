import tkinter as tk
from tkinter import messagebox
import time
import os
import re

BGCOLOR='#222'
MODES=["NORMAL","COUNTDOWN"]
current_mode="NORMAL"
CAPTION='simpleTimer'
command_buffer=""
in_command_mode=False
caption_mode=True

# Timer app
class TimerApp:
    def __init__(self, root):
        self.root = root
        self.remaining_seconds = 300
        self.set_seconds=300

        self.running = False

        # GUI setup
        self.label = tk.Label(root, text=self.format_time(), font=("Helvetica", 52,'bold'),bg=BGCOLOR)
        self.label.pack(pady=20)

        #self.root.bind("<space>", self.toggle_timer)
        self.root.bind("<KeyPress>",self.on_key_press)
        self.update_label()


    def get_color(self):
        if self.remaining_seconds>self.set_seconds*3/10:
            return '#44bfff'
        elif self.remaining_seconds > self.set_seconds/10:
            return '#ffa500'
        else:
            return '#ff4500'
    def format_time(self):
        hours, remainder = divmod(self.remaining_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def update_label(self):
        self.label.config(text=self.format_time(),fg=self.get_color())
        self.root.after(1000, self.update_label)

    def toggle_timer(self, event=None):
        if self.running:
            self.stop_timer()
        else:
            self.start_timer()

    def start_timer(self):
        self.running = True
        self.run_timer()

    def run_timer(self):
        global current_mode
        self.label.config(fg=self.get_color())
        if self.running and self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.root.after(1000, self.run_timer)
        elif self.remaining_seconds == 0:
            self.running = False
            current_mode="NORMAL"


    def stop_timer(self):
        self.running = False

    def update_caption(self):
        if caption_mode:
            if in_command_mode:
                root.title(CAPTION+" :"+command_buffer)
            else:
                root.title(CAPTION)
        else:
            root.title('')

    def is_valid_time(self,input_str):
        return bool(re.fullmatch(r'(\d+h)?(\d+m)?(\d+s)?',input_str))

    def parse_time(self,input_str):
        match=re.findall(r'(\d+)([hms])',input_str)
        total_seconds=0
        if match:
            for value,unit in match:
                if unit=='h':
                    total_seconds+=int(value)*3600
                elif unit=='m':
                    total_seconds+=int(value)*60
                elif unit=='s':
                    total_seconds+=int(value)
        if total_seconds>359999:
            total_seconds=359999
        return total_seconds


    def on_key_press(self,event):
        global command_buffer, in_command_mode
        if event.keysym=="colon":
            command_buffer=""
            in_command_mode=True
        elif in_command_mode:
            if event.keysym=="Return":
                self.process_command(command_buffer)
                in_command_mode=False
            elif event.keysym=="Escape":
                in_command_mode=False
            elif event.keysym=="BackSpace":
                if len(command_buffer)>0:
                    command_buffer=command_buffer[:-1]
                else:
                    in_command_mode=False
            else:
                command_buffer+=event.char

        self.update_caption()

    def process_command(self,cmd):
        global current_mode,remaining_seconds,caption_mode
        if cmd.startswith("set ") and current_mode=="NORMAL":
            time_str=cmd[4:].strip()
            if self.is_valid_time(time_str):
                parsed_time=self.parse_time(time_str)
                self.remaining_seconds=parsed_time
                self.set_seconds=parsed_time
            else:
                self.flash_display()
            self.update_label()
            current_mode="NORMAL"
        elif cmd=="start" and current_mode=="NORMAL" and not self.running:
            self.start_timer()
            current_mode="COUNTDOWN"
        elif cmd=="stop" and current_mode=="COUNTDOWN":
            self.stop_timer()
            current_mode="NORMAL"

        elif cmd=="reset" and current_mode in ["NORMAL","COUNTDOWN"]:
            self.stop_timer()
            self.remaining_seconds=self.set_seconds
            self.update_label()
            current_mode="NORMAL"
        elif cmd=="nocaption":
            caption_mode=False
            self.update_caption()
        elif cmd=="caption":
            caption_mode=True
            self.update_caption()
        elif cmd=="exit":
            root.quit()
        else:
            self.flash_display()
    def flash_display(self):
        original_bg=root.cget("bg")
        root.config(bg="#fff")
        self.label.config(bg="#fff")
        colors=['#fff','#eee','#ddd','#ccc','#bbb','#aaa','#999','#888','#777','#666','#555']
        for i,color in enumerate(colors):
            root.after(i*10+40,lambda c=color:root.config(bg=c))
            root.after(i*10+40,lambda c=color:self.label.config(bg=c))

        root.after(len(colors)*10+40,lambda:root.config(bg=original_bg))
        root.after(len(colors)*10+40,lambda:self.label.config(bg=original_bg))

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x100')
    root.config(bg=BGCOLOR)
    root.title(CAPTION)
    root.resizable(False,False)
    app = TimerApp(root)
    root.attributes('-topmost',True)
    root.mainloop()
