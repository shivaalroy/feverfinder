from tools import Tool
import pico

def getData():
  t = Tool("feverfinder","Shivaal")
  return t.getTemperature()