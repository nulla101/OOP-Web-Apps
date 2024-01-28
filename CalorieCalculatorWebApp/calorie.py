class Calorie:
    """Representation of the optimal amount of calories
    a person needs to take today.
    Calculated with BMR:
    10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.temperature = float(temperature)

    def calculate(self):
        calories = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * self.temperature

        return calories
