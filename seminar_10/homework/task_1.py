from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color__ = 'red'
    
    def running(self):
        print("\033[31m {}" .format(self.__color__))
        sleep(7)
        self.__color__ = 'yellow'
        sleep(3)
        print("\033[33m {}" .format(self.__color__))
        self.__color__ = 'green'
        sleep(7)
        print("\033[32m {}" .format(self.__color__))
light =TrafficLight()
light.running()
