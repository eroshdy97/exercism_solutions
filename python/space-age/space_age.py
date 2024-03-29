class SpaceAge:
    Earth = 31557600 # seconds
    Mercury = 0.2408467
    Venus = 0.61519726
    Mars = 1.8808158
    Jupiter = 11.862615
    Saturn = 29.447498
    Uranus = 84.016846
    Neptune = 164.79132

    
    def __init__(self, seconds):
        self.seconds = seconds


    def on_earth(self):
        return round(self.seconds / self.Earth, 2)

    def on_mercury(self):
        return round(self.seconds / self.Earth / self.Mercury, 2)

    def on_venus(self):
        return round(self.seconds / self.Earth / self.Venus, 2)

    def on_mars(self):
        return round(self.seconds / self.Earth / self.Mars, 2)

    def on_jupiter(self):
        return round(self.seconds / self.Earth / self.Jupiter, 2)

    def on_saturn(self):
        return round(self.seconds / self.Earth / self.Saturn, 2)

    def on_uranus(self):
        return round(self.seconds / self.Earth / self.Uranus, 2)

    def on_neptune(self):
        return round(self.seconds / self.Earth / self.Neptune, 2)

    