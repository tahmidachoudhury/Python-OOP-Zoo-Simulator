class Animal:
    def __init__(self, name, health_threshold, death_threshold):
        self.name = name
        # health will always begin at 100
        self.health = 100.0
        # this is mainly for Elephants where they cannot walk after 70%
        self.health_threshold = health_threshold
        # threshold at which they die
        self.death_threshold = death_threshold
        self.alive = True

    def apply_health_reduction(self, percentage):
        reduction = self.health * (percentage/100)
        self.health -= reduction
        return self.health

    def feed(self, percentage):
        self.health *= (1 + percentage/100)
        # health should be capped at 100
        self.health = min(100, self.health)
        return self.health

    def check_health(self):
        pass
