import pyautogui
import os
import time
from constants.colors import target_colors

"""
Try to implement pyautogui instead of autopy
"""

# AutoPY
# screenshot_path = 'src/img/screenshot.png'
# max_runtime_sec = 60 * 60 * 24

def fishing():
    max_runtime_sec = 60 * 60 * 24

    while (max_runtime_sec > 0):
        time.sleep(1)
        max_runtime_sec = max_runtime_sec - 1

        for color in target_colors:
            print("Color %s" % color)

            pos = pyautogui.pixelMatchesColor(100, 200, tuple(color))

            # AutoPy
            # autopy.bitmap.capture_screen().save(os.path.join(os.getcwd(), screenshot_path))

            # source = autopy.bitmap.Bitmap.open(screenshot_path)
            # result = autopy.bitmap.Bitmap.find_color()

            # print(result)

            # pos = source.find_bitmap(result)
            # if pos:
            #     autopy.mouse.move(pos[0] / scale, pos[1] / scale)

            print("Found avator at: %s" % str(pos))
