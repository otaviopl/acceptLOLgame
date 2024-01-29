import pyautogui
import time 
def click_accept_button():
    accept_button_location = None
    print('Looking for a button')
    while accept_button_location is None:
        accept_button_location= pyautogui.locateOnScreen('accept.png',confidence=0.7)
        time.sleep(1)
    print('Sucess!')
    accept_button_center = pyautogui.center(accept_button_location)
    pyautogui.click(accept_button_center)
    time.sleep(5)
    exit()

click_accept_button