from pydirectinput import *
import pyautogui
from time import sleep

# SCALE TO FIT MUST BE TURNED OFF ON VIGILIX screenshot search funtion only works if the text is that size.

# 05/10/2022 end notes. Date Entry is slow
PROMO_NUMBER = "5192"
PROMOTION_DESCRIPTION = "BC Sugar 4.98 lmt 3"
START_DATE = "06/08/2022"
END_DATE = "06/14/2022"
PRICE = "4.98"
LIMIT_NO = "3"
REPORTING_DEPARTMENT = str(1)
UPC = [
    7003834448,
    1346234623,
    2462456345,
    1235135131,
    1351351351,
]


# Enters UPCs from a list into the last section
def UPC_filler():
    sleep(.5)  # gives the program time to see
    plu_info = pyautogui.locateOnScreen("plu_button.png", confidence=.7)
    plu_button = pyautogui.center(plu_info)
    for x in UPC:
        pyautogui.click(plu_button)
        pyautogui.click(plu_button)
        pyautogui.typewrite(str(x))
        press("tab")
        press("enter")


def coupon_engine():
    click(904, 750)
    # Open New Promotion ctrl+
    keyDown("ctrl")
    keyDown("n")
    keyUp("ctrl")
    keyUp("n")

    # fill out General info
    pyautogui.write(PROMO_NUMBER)
    press("tab")
    pyautogui.write(PROMOTION_DESCRIPTION)

    # Enter Date / Very slow atm
    press("tab")
    press("right", 10)
    press("backspace", 15)
    pyautogui.write(START_DATE)
    press("tab", 2)
    press("right", 10)
    press("backspace", 15)
    pyautogui.write(END_DATE)

    # Uses screenshot witchcraft to click the button
    detailed_information = pyautogui.locateOnScreen("Detailed_info_button.png", confidence=.8)
    detail_button = pyautogui.center(detailed_information)
    pyautogui.click(detail_button)

    # Detailed infromation entry
    press("tab", 9)
    press("down")
    press("tab")
    press("backspace", 2)
    write(LIMIT_NO)
    press("tab", 2)
    write(REPORTING_DEPARTMENT)

    # Use skynet's bullshitery to click on conditions/rewards
    conditions_rewards = pyautogui.locateOnScreen("conditions_img.png", confidence=.8)
    condition_button = pyautogui.center(conditions_rewards)
    pyautogui.click(condition_button)

    # Bullshit reverse Tab loop god forgrive me (It's 22 forward Tabs To get to add rewards)
    for x in range(3):
        keyDown("shift")
        keyDown("tab")
        keyUp("shift")
        keyUp("tab")
    press("enter")
    press("tab")

    # Get to sell AT, Slow but doesn't require anything fancy
    for x in range(22):
        keyDown("down")
        keyUp("up")
    press("tab")
    press("enter")

    # General info
    pyautogui.write(PRICE)
    press("tab", 6)
    press("left")
    press("tab", 3)
    pyautogui.write(REPORTING_DEPARTMENT)

    # Item_level_selector
    item_select_info = pyautogui.locateOnScreen("item_level.png", confidence=.8)
    item_level_button = pyautogui.center(item_select_info)
    pyautogui.click(item_level_button)


coupon_engine()
UPC_filler()
