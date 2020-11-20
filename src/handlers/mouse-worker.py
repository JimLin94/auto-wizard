import autopy
import os

# https://github.com/autopilot-rs/autopy

def find_image_example():
    target = os.path.open('../img/avator.png')
    avator = autopy.bitmap.Bitmap.open(target)

    pos = haystack.find_bitmap(avator)
    if pos:
        print("Found avator at: %s" % str(pos))

find_image_example()