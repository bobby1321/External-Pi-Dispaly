import time
import string
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import threading
import os
import signal

lastUpdate = time.time()
run = True

def endMyLife():
        while(True):
                if (time.time() - lastUpdate) > 10:
                        disp.clear()
                        disp.display()
                        os.kill(os.getpid(), signal.SIGUSR1)



# Raspberry Pi pin configuration:
RST = 8
# Note the following are only used with SPI:
DC = 9
SPI_PORT = 0
SPI_DEVICE = 1

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT,$

# Initialize library.
disp.begin()

NewThread = threading.Thread(target=endMyLife)
NewThread.start()


while run:
        lastUpdate = time.time()
        if raw_input() == 'Stop':
                run = False
                disp.clear()
                disp.display()
                break
        cpuTemp = "CPU Temp: " + raw_input() + u"\u00B0"
        cpuSpeed = "CPU Speed:" + raw_input() + " MHz"
        cpuLoad = "CPU Load: " + raw_input() + " %"
        gpuTemp = "GPU Temp: " + raw_input() + u"\u00B0"
        gpuSpeed = "GPU Speed:" + raw_input() + " MHz"
        gpuLoad = "GPU Load: " + raw_input() + " %"
        #print("Howdy")

        # Clear display.
        disp.clear()
        disp.display()

        image = Image.new('1', (128, 64))
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        draw.text((0, 0), cpuTemp,  font=font, fill=255)
        draw.text((0, 8), cpuSpeed, font=font, fill=255)
        draw.text((0, 16), cpuLoad, font=font, fill=255)
        draw.text((0, 24), gpuTemp, font=font, fill=255)
        draw.text((0, 32), gpuSpeed, font=font, fill=255)
        draw.text((0, 40), gpuLoad, font=font, fill=255)

        # Display image.
        disp.image(image)
        disp.display()
