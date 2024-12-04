#! python3

# Cookie clicker auto clicker

import pyautogui, os, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')


def findImage(imagePath):
    try:
        return pyautogui.locateCenterOnScreen(imagePath, confidence=0.9)
    except Exception:
        return None

cookCoords = findImage('Images\\BigCookie.png')
assert cookCoords is not None, 'Finner ikke noen jævla cookie!!!'
upgrCoords = (2273, 206)
cursBuild = (2271, 318)
buildCoords = []

diffBuilds = 5
lastBuild = (2271, 318)
clicks = 0

buildDirectory = 'Images\\Buildings'
buildImgPaths = []



for image in os.scandir(buildDirectory):
    if image.is_file():
        buildImgPaths.append(image.path)    

logging.info('Fant alle bildene håper jeg')

for i in range(diffBuilds):
    buildCoords.append(lastBuild)
    x, y = lastBuild
    lastBuild = (x, y + 50)
    
try:
    while True:
        clicks += 1
        pyautogui.click(cookCoords)
        if clicks % 100 == 0:
            pyautogui.click(upgrCoords)
            pyautogui.moveRel(0, 300)
            for building in reversed(buildImgPaths):
                coords = findImage(building)
                #buildClicks = 0
                if coords is None:
                    logging.warning(f'Fant ikke bildet for {os.path.basename(building)}')
                    continue
                pyautogui.click(coords)
                #buildClicks += 1
            clicks = 0
except KeyboardInterrupt:
    logging.info('Avslutter programmet fordi du ble lei')
