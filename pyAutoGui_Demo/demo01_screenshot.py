import pyautogui

image1 = pyautogui.screenshot(imageFilename="screenshot.png")

region = (0, 100, 300, 400)
image2 = pyautogui.screenshot(region=region, imageFilename="screenshot2.png")

