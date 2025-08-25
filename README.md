# wizard101-bazaar-bot
In late 2024, Wizard101 introduced a major [Bazaar revamp](https://www.wizard101.com/game/updatenotes/selenopolis#bazaarrevamp) that completely removed the purchase delay, making buying and selling instant, They also added a search bar so players can quickly find specific items. This bot was created to take advantage of those changes by targeting specific items with the search bar making it super easy to catch rare or valuable items before they disappear from the Bazaar. This bot uses image recognition and pixel based color detection to detect items that appear for sale on the market to quickly purchase them before they can be sold.

# Setup

First you need to install the packages that this project requires. You can install them using pip by doing the following after downloading the repo:

```
pip install -r requirements.txt
```

Due to my laziness for the bot to properly work your native resolution on your computer needs to be 1440x1080 & 1360x768 on Fullscreen Borderless in Wizard101. To achieve this I reccomend you either use [Nvidia Control Panel](https://www.nvidia.com/en-us/software/nvidia-app/) Or [CRU](https://www.monitortests.com/forum/Thread-Custom-Resolution-Utility-CRU) Both Programs will let you make a custom resolution. Once you get the option to make a custom resolution set it to 1440x1080 then do the following: 

- Right click desktop click "Display settings"
- If you have 2 monitors select "Monitor 1"
- Under "Scale and layout" change the size of text, apps and other items to 100%
- Scroll down to "Display Resolution" then select 1440x1080 (The Custom Resolution we made above)
- Click Yes then save and exit

From here everything should be good with your native resolution and all you need to do now is go into Wizard101 and change your resolution to 1360x768 Fullscreen Borderless. 

Additionally If you don’t want to change your native resolution, you can still use the bot by scaling the coordinates to your resolution. The coordinates hard coded on the bot are based on **1440x1080 / 1360x768**, so you can adjust them proportionally for your own screen resolution with a little bit of math. I provided an example below that you could use if you decided you wanted to take this approach. 

```python
import pyautogui

# Original coordinate on 1440x1080
wallHangingsCategory = (465, 232)

# desired screen res you want to be on for ex 1920x1080
current_res = (1920, 1080)

# Scale function
wallHangingsCategory_scaled = (
    int(wallHangingsCategory[0] * current_res[0] / 1440),
    int(wallHangingsCategory[1] * current_res[1] / 1080)
)

print(wallHangingsCategory_scaled)  # Output: (620, 232)
```

# How To Use

Out of the box the bot will only search for items located in the **Wall Hangings Category** of the Bazaar. To Change this you will need to make a new python file and add the following code so that you can move your mouse to the category that you wish to snipe items from and get the x and y cords for that button. This bot works for every category in the bazaar, Treasure Cards, Jewels, Gear, Housing, Reagents etc.

```python
import pyautogui
import time

time.sleep(5)  # Gives you 5 seconds to move you mouse to the category button you want it to click

x, y = pyautogui.position()
print(f"Mouse is at: ({x}, {y})")
```

Once you get your x and y of the bazaar category you want to snipe from all you need to do is go to the bottom of controller.py and replace your x and y. You will notice that the bot takes the cordinates provided and randomly clicks around that area, This is to prevent Wizard101's anti bot from picking up the script, Make sure that when you get the cordinates of a category you want to snipe you put your mouse in the middle of the button so that the script doesnt missclick.


```python
while True:
    wallHangingsCategory = (x, y) # Replace your x and y you got from above here
    pyautogui.click(wallHangingsCategory[0] + randint(-10, 10), wallHangingsCategory[1] + randint(-5, 5))
    time.sleep(0.1)
    status = buyAllItemsOnPage()
    if status == 0:
        continue
    elif status == 2:
        continue
```

Now, simply open the Bazaar, select the category you want to target, type the item into the search bar, then activate the bot. Switch back to Wizard101 and watch as the bot automatically scans and snipes every matching item that appears on screen.

![1](https://github.com/user-attachments/assets/88cfde44-1c06-4388-be94-64299af71985)

Additionally, if you want to take this a step further and scale this up with virtual machines, I highly recommend using [Vultr](https://www.vultr.com/promo/try250). They offer a $250 free credit when you spend just $50, As shown below, the cheapest option with a graphics card starts at only $0.059/hr, which comes out to roughly $40 per month if you run it continuously. This makes it extremely affordable, and you can easily make back the cost by running the bot and selling items back to the community. If you do go this route I highly suggest you join [Gammas](https://gtp.gg/) as its the easiest way to flip anything you snipe.

![image](https://github.com/user-attachments/assets/f1af5b3a-0d38-45cb-8feb-b7f6afb4eac9)


# How It Works

In earlier versions, the bot relied on OCR and full image recognition to find items and correctly position them, which was slow and prone to errors. Now, it takes targeted screenshots of the item area and scans pixels for yellow text, using color thresholds and vertical spacing to detect items without OCR. Once identified, it calculates click positions relative to the screenshot. After a purchase, it assumes remaining items shift up, continuing in the same relative positions, combining color-based detection with fixed coordinates for fast, reliable sniping.

<img width="660" height="550" alt="debug_all_9_items" src="https://github.com/user-attachments/assets/7391969f-70e7-438e-9cf3-f5276fecafbc" />><br>

Due to this being a snipe bot its coded to always assume that if something is purchased that the next item will move up. If you decide you don’t want this logic you can make a small tweak to the code to make it click each item from top to bottom similar to the screenshot above. Go to line 52 on controller.py and make the following change:

```python
for i, rel_y in enumerate(item_positions):
  screen_x = 460 + (width // 2) + 20
  screen_y = 240 + rel_y # this  is the only line that changed
```

# Additional Upgrades
