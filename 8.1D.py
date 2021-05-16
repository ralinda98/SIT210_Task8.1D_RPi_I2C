import smbus
import time

# Constants for brightness levels
TOO_DARK = 10
DARK = 40
MEDIUM = 100
BRIGHT = 500

# Master Device I2C Address
DEVICE = 0x23
# Measure at 1lx resolution for 120ms
ONE_TIME_H_RES_MODE = 0x20

bus = smbus.SMBus(1)

def convertToDecimal(data):
  # Converts 2 bytes of data into a decimal number.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight():
  # Read data from I2C interface
  data = bus.read_i2c_block_data(DEVICE, ONE_TIME_H_RES_MODE)
  return convertToDecimal(data)

def printBrightness(lightData):
  if lightData <= TOO_DARK:
    brightness = "Too Dark : "
  elif lightData <= DARK:
    brightness = "Dark : "
  elif lightData <= MEDIUM:
    brightness = "Medium : "
  elif lightData <= BRIGHT:
    brightness = "Bright : "
  else:
    brightness = "Too Bright : "
  return brightness

def main():

  while True:
    lightLevel=readLight()
    print("Light Level : " + printBrightness(lightLevel) + format(lightLevel,'.2f') + " lx")
    time.sleep(0.5)

if __name__=="__main__":
   main()