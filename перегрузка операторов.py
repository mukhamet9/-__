class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eg__ (self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


Build1 = Building(9, 'кирпичный')
Build2 = Building(10, 'панельный')
print(Build1 == Build2)