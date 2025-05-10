import pynput as pn
import keyboard as kb
import os
from Button import *
import time
from setup import *

class App:
    def __init__(self):
        self.running = True
        self.mouse = pn.mouse.Controller()

        self.button1 = Button()
        self.button2 = Button()

        self.scene = 'menu'
        self.scene_selector = '0'

        self.settings = load_settings()

        if self.settings:
            self.set_user_settings()

    def set_user_settings(self):
        self.button1.key = self.settings["button_keys"][0]["button1_key"]
        self.button2.key = self.settings["button_keys"][0]["button2_key"]

        self.button1.pos = tuple(self.settings["positions"][0]["button1_pos"])
        self.button2.pos = tuple(self.settings["positions"][0]["button2_pos"])

    def move_mouse(self, preset):
        self.mouse.position = preset

    def click_mouse(self):
        self.mouse.press(pn.mouse.Button.left)
        self.mouse.release(pn.mouse.Button.left)

    def get_single_key(self):
        while True:
            event = kb.read_event()
            if event.event_type == kb.KEY_DOWN:
                return event.name
             

    def menu(self):
        while self.running:
            os.system('cls||clear')
            show_name()
            # print('welcome, what you want to do?')
            print(f'Hotkeys: key1: {self.button1.key}, key2: {self.button2.key}\nPositions: preset1: {self.button1.pos}, preset2: {self.button2.pos}')
            print('''1. 𝖘𝖙𝖆𝖗𝖙 𝖕𝖗𝖔𝖌𝖗𝖆𝖒''')
            print('''2. 𝖘𝖊𝖙 𝖇𝖎𝖓𝖉𝖎𝖓𝖌''')
            print('''3. 𝖘𝖊𝖙 𝖕𝖗𝖊𝖘𝖊𝖙 𝖕𝖔𝖘𝖎𝖙𝖎𝖔𝖓𝖘''')
            print('''q. 𝖊𝖝𝖎𝖙''')
            self.scene_selector = self.get_single_key()
            time.sleep(0.15) 

            if self.scene_selector == '1':
                # self.scene = 'start'
                self.start()
                
            if self.scene_selector == '2':
                # self.scene = 'sethotkey'
                self.set_hot_keys()

            if self.scene_selector == '3':
                # self.scene = 'setpresets'
                self.set_presets_pos()

            if self.scene_selector == 'q':
                save_settings(self.button1.key, self.button2.key, self.button1.pos, self.button2.pos)
                self.running = False
                # self.scene = 'none'

    def start(self):
        print('esc for exit')
        while True:
            if kb.is_pressed(self.button1.key) and not self.button1.is_pressed:
                self.button1.is_pressed = True
                self.move_mouse(self.button1.pos)
                self.click_mouse()
                print(f'{self.button1.key} pressed')

            if not kb.is_pressed(self.button1.key) and self.button1.is_pressed:
                self.button1.is_pressed = False

            if kb.is_pressed(self.button2.key) and not self.button2.is_pressed:
                self.button2.is_pressed = True
                self.move_mouse(self.button2.pos)
                self.click_mouse()
                print(f'{self.button2.key} pressed')

            if not kb.is_pressed(self.button2.key) and self.button2.is_pressed:
                self.button2.is_pressed = False
            
            if kb.is_pressed('esc'):
                # self.scene = 'menu'
                break
        self.menu()

    def set_hot_keys(self):
        print('press key for set to button 1')
        while True:
            self.button1.set_key(kb.read_key(True))
            if self.button1.key != 'enter':
                break
        # kb.wait(self.button1.key, suppress=False)
        print(f"saved: - Button 1: {self.button1.key}")
        print('press key for set to button 2')
        while True:
            self.button2.set_key(kb.read_key(True))
            if self.button2.key != self.button1.key:
                break

        os.system("cls||clear")
        print(f"saved:\n - Button 1: {self.button1.key}\n - Button 2: {self.button2.key}")

        print('esc for exit')
        while True:
            if kb.is_pressed('esc'):
                # self.scene = 'menu'
                break
        self.menu()

    def set_presets_pos(self):
        print('set the mouse on the preset, then press 1')
        while True:
            if kb.is_pressed('1'):
                self.button1.set_pos(self.mouse.position)
                break
        print(f"saved: - Button 1: {self.button1.pos}")
        print('set the mouse on the preset, then press 2')
        while True:
            if kb.is_pressed('2'):
                self.button2.set_pos(self.mouse.position)
                break

        os.system("cls||clear")
        print(f"saved:\n - Button 1: {self.button1.pos}\n - Button 2: {self.button2.pos}")
        print('esc for exit')
        while True:
            if kb.is_pressed('esc'):
                # self.scene = 'menu'
                break
        self.menu()