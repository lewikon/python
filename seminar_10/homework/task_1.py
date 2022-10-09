from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = 'red'
    
    def running(self):
        print("\033[31m {}" .format(self.__color))
        sleep(7)
        self.__color = 'yellow'
        sleep(3)
        print("\033[33m {}" .format(self.__color))
        self.__color = 'green'
        sleep(7)
        print("\033[32m {}" .format(self.__color))

light =TrafficLight()
light.running()
