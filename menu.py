import pynput as pn
import keyboard as kb
import os

scene = 'menu'
scene_selector = '0'
button_1, button_2 = 'z', 'x'
button_1_pos = (1000,500)
button_2_pos = (500,200)
button_1_pressed, button_2_pressed = False, False

mouse = pn.mouse.Controller()

def menu():
    global scene
    os.system('cls||clear')
    while scene == 'menu':
        print('welcome, what you want to do?')
        print(f'your hotkeys and positions: \nkey1: {button_1}, key2: {button_2} \npreset1: {button_1_pos}, preset2: {button_2_pos}')
        print('1. start program')
        print('2. set hotkeys')
        print('3. set preset positions')
        print('q. for exit')
        scene_selector = input()

        if scene_selector == '1':
            scene = 'start'
            start()
        if scene_selector == '2':
            scene = 'sethotkey'
            set_hot_keys()

        if scene_selector == '3':
            scene = 'setpresets'
            set_presets_pos()

        if scene_selector == 'q':
            scene = 'none'
            break

def start():
    global scene
    global button_1, button_2
    global button_1_pressed, button_2_pressed
    global button_1_pos, button_2_pos
    print('esc for exit')
    while scene == 'start':
        if kb.is_pressed(button_1) and not button_1_pressed:
            button_1_pressed = True
            move_mouse(button_1_pos)
            click_mouse()
            print(f'{button_1} pressed')
        if not kb.is_pressed(button_1) and button_1_pressed:
            button_1_pressed = False

        if kb.is_pressed(button_2) and not button_2_pressed:
            button_2_pressed = True
            move_mouse(button_2_pos)
            click_mouse()
            print(f'{button_2} pressed')
        if not kb.is_pressed(button_2) and button_2_pressed:
            button_2_pressed = False
        
        if kb.is_pressed('esc'):
            scene = 'menu'
            menu()

def set_hot_keys():
    global scene
    global button_1, button_2
    print('press key for set to button 1')
    while True:
        button_1 = kb.read_key(True)
        if button_1 != 'enter':
            break
    # kb.wait(button_1, suppress=False)
    print(f"saved: - Button 1: {button_1}")
    print('press key for set to button 2')
    while True:
        button_2 = kb.read_key(True)
        if button_2 != button_1:
            break

    os.system("cls||clear")
    print(f"saved:\n - Button 1: {button_1}\n - Button 2: {button_2}")

    print('esc for exit')
    while True:
        if kb.is_pressed('esc'):
            scene = 'menu'
            menu()
            break

def set_presets_pos():
    global scene
    global button_1_pos, button_2_pos
    global mouse
    print('set the mouse on the preset, then press 1')
    while True:
        if kb.is_pressed('1'):
            button_1_pos = mouse.position
            break
    print(f"saved: - Button 1: {button_1_pos}")
    print('set the mouse on the preset, then press 2')
    while True:
        if kb.is_pressed('2'):
            button_2_pos = mouse.position
            break

    os.system("cls||clear")
    print(f"saved:\n - Button 1: {button_1_pos}\n - Button 2: {button_2_pos}")
    print('esc for exit')
    while True:
        if kb.is_pressed('esc'):
            scene = 'menu'
            menu()
            break


def move_mouse(preset):
    global mouse, button_1_pressed
    mouse.position = preset

def click_mouse():
    mouse.press(pn.mouse.Button.left)
    mouse.release(pn.mouse.Button.left)

menu()