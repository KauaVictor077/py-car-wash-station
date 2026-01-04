# app/main.py (edit at ref 8ac477ed0e8eb8f8945b5ead27fbbff18acc02cc)

class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, comfort_power: int, clean_power: int, average_rating: float, count_of_ratings: int):
        # store parameters expected by tests
        self.comfort_power = comfort_power
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        """Serve list of Car instances. Call wash_single_car for each car and return total income."""
        total = 0.0
        for car in cars:
            total += self.wash_single_car(car)
        return total

    def wash_single_car(self, car: Car) -> float:
        """
        Update car.clean_mark if it is less than station's clean_power.
        Return price charged for washing this car (0 if not washed).
        Note: calculate_washing_price should NOT modify car.clean_mark; use it only to compute price.
        """
        price = self.calculate_washing_price(car)
        if car.clean_mark < self.clean_power:
            # perform wash: set car.clean_mark to station's clean_power
            car.clean_mark = self.clean_power
        return price

    def calculate_washing_price(self, car: Car) -> float:
        """
        Compute the price for washing the car without mutating car.clean_mark.
        Implementation details (pricing formula) must match specs/tests.
        If car.clean_mark >= clean_power -> price 0.0
        """
        if car.clean_mark >= self.clean_power:
            return 0.0
        # Placeholder pricing formula: price per unit = self.average_rating * SOME_FACTOR
        # You should replace the formula below with the project's required pricing logic.
        units = self.clean_power - car.clean_mark
        price_per_unit = self.average_rating * 0.6666666667  # example to be adjusted
        return round(units * price_per_unit, 2)

    def rate_service(self, mark: int) -> None:
        """Update average_rating and count_of_ratings when a new mark arrives."""
        total = self.average_rating * self.count_of_ratings
        total += mark
        self.count_of_ratings += 1
        self.average_rating = round(total / self.count_of_ratings, 1)
