class ParamObject:
    def __init__(self):
        self.maxAcceleration: float = 0.08
        self.maxBraking: float = .5
        self.checkIntersectionDistFactor: float = 10
        self.checkPassingDuration: int = 15
        self.stopDistFactor: float = 5
        self.frictionFactor: float = .176 / 1000
        self.standardMaxSpeed: float = 4
        self.respawnCouldownAverage: float = 1
        self.respawnCouldownGap: float = 0
        self.keepSameDirection: int = -1
        