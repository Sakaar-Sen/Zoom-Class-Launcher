import pyautogui as p
import time

time.sleep(2)
def zoom():
    p.hotkey('win')
    time.sleep(1)
    p.write('Zoom')
    time.sleep(1)
    p.hotkey('enter')
    time.sleep(15)
    p.hotkey('win', 'up')
    p.click(750, 400)
    time.sleep(1)
    p.write('3050672190')
    for i in range(3):
        time.sleep(1)
        p.hotkey('tab')
    p.hotkey('enter')
    time.sleep(1)
    p.hotkey('tab')
    time.sleep(1)
    p.hotkey('enter')
    time.sleep(1)
    p.hotkey('tab')
    time.sleep(1)
    p.hotkey('enter')
    time.sleep(3)
    p.write('100366')
    p.moveTo(750, 400)


def whatsapp():
    time.sleep(2)
    p.hotkey('win')
    time.sleep(0.5)
    p.write('Whatsapp')
    time.sleep(0.5)
    p.hotkey('enter')
    time.sleep(1)


def adobe():
    location = """E:\Pdfs\Chemical kinetics.pdf"""
    p.hotkey('win', 'r')
    time.sleep(0.5)
    p.write(location)
    p.hotkey('enter')
    time.sleep(1)



zoom()



