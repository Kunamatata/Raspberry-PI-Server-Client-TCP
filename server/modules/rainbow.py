import time

def colorChase(pixels, color, wait):
    for i in range(len(pixels)):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def rainbowCycle(pixels, wait):
    for j in range(255):
        for i in range(len(pixels)):
            pixel_index = (i * 256 // len(pixels)) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)