import pyautogui
import time
from random import randint

screen_width, screen_height = pyautogui.size()
print(f"Screen size: {screen_width} x {screen_height}")  # needs to be 1440x1080 native & 1360x768 in wizard101 (fullscreen borderless)

def buy_button_active():
    x, y = (354, 834)
    r, g, b = pyautogui.screenshot().getpixel((x, y))
    
    # Check if it's glowing yellow
    if r > 200 and g > 200 and b < 120:
        return True
    return False

def buyAllItemsOnPage():
    list_region = (460, 240, 660, 540)
    screenshot = pyautogui.screenshot(region=list_region)

    pixels = screenshot.load()
    width, height = screenshot.size
    item_positions = []

    # focus on the main area on the screen where the items show up on the catalog
    for y in range(90, height - 10, 2):
        yellow_count = 0

        # Focus on center of names
        for x in range(100, width - 100, 4):
            r, g, b = pixels[x, y]
            if r > 200 and g > 180 and b < 80:  # Yellow text
                yellow_count += 1

        # Good threshold
        if yellow_count > 18:
            # Good spacing between items
            if not any(abs(existing_y - y) < 38 for existing_y in item_positions):
                item_positions.append(y)

                # LIMIT TO MAX 9 ITEMS AS THERE IS ONLY 9 SLOTS IN THE BAZAAR
                if len(item_positions) >= 9:
                    break

    # nothing showed up in items for sale list so return and refresh page
    if not buy_button_active():
        return 0

    clickedCount = 0
    for i, rel_y in enumerate(item_positions):
        screen_x = 460 + (width // 2) + 20
        screen_y = 240 + item_positions[0]
        print(f"Clicking item #{i+1} at ({screen_x}, {screen_y})")
        if clickedCount > 0:
            time.sleep(0.25)
        pyautogui.click(screen_x + randint(-5, 5), screen_y + randint(-3, 3))
        clickedCount += 1

        # Now its time to buy the item
        buyButton = (354, 834)
        try:
            pyautogui.click(buyButton[0] + randint(-5, 5), buyButton[1] + randint(-3, 3))
            pyautogui.click(buyButton[0] + randint(-5, 5), buyButton[1] + randint(-3, 3))
            time.sleep(0.1)
            try:
                already_sold = pyautogui.locateOnScreen('sold.png', confidence=0.6, grayscale=True)
                if already_sold:
                    alreadySoldButton = (934, 636)
                    pyautogui.click(alreadySoldButton[0] + randint(-5, 5), alreadySoldButton[1] + randint(-3, 3))
                    pyautogui.click(alreadySoldButton[0] + randint(-5, 5), alreadySoldButton[1] + randint(-3, 3))
                    print(f"Failed To Purchase item (Already Purchased)")
                    return 2 # somebody else got the item so we need to return and refresh page
            except:
                already_sold = None
            
            confirmBuyButton = (721, 640)
            time.sleep(0.3)
            pyautogui.click(confirmBuyButton)
            pyautogui.click(confirmBuyButton)
            print(f"Purchased item")
            time.sleep(0.5)
        except:
            print(f"Failed To Purchase item")
            return 2

            
#time.sleep(5) # if you have only 1 monitor uncomment this so that you have time to tab into the game
while True:
    wallHangingsCategory = (465, 232)
    pyautogui.click(wallHangingsCategory[0] + randint(-10, 10), wallHangingsCategory[1] + randint(-5, 5))
    time.sleep(0.1)
    status = buyAllItemsOnPage()
    if status == 0:
        continue
    elif status == 2:
        continue