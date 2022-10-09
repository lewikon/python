class Road:
    def __init__(self):
        self.a = 25
    
    def weight(self, _lengh:int, _width:int, _thickness:int):
        return _lengh * _width * _thickness * self.a

road = Road()
print ('{} кг или {} тонн'.format(road.weight(20,5000,5),road.weight(20,5000,5)/1000))

