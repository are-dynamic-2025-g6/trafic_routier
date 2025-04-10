class ParamObject:
    def __init__(self):
        self.maxAcceleration: float = 0.08
        self.maxBraking: float = .5
        self.turnBrakingTickDuration: float = 30
        self.frictionFactor: float = .176 / 1000
        self.standardMaxSpeed: float = 4
        self.respawnCouldownAverage: float = 20
        self.respawnCouldownGap: float = 10
        