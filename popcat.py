import pyautogui, time, sys, random

def auto_click(delay):
    pyautogui.click()
    pyautogui.click()
    time.sleep(delay)
    pyautogui.click()
    pyautogui.click()
    
if __name__ == '__main__':    
    running = True
    counter = 0
    multiplier = random.random()
    interval = 0.2
    while running:
        counter += 1
        if counter >= 50:
            counter = 0   
            multiplier = random.random()
        auto_click(interval * multiplier)