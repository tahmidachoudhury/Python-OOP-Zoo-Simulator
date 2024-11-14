import random


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
        self.below_threshold = False

    def apply_health_reduction(self, percentage):
        if self.alive:
            reduction = self.health * (percentage/100)
            self.health -= reduction
            self.check_health()
            return self.health

    def feed(self, percentage):
        if self.alive:
            self.health *= (1 + percentage/100)
            # health should be capped at 100
            self.health = min(100, self.health)
            self.check_health()
            return self.health

    # the return are for the tests
    def check_health(self):
        if self.name == "Elephant" and self.below_threshold:
            self.alive = False
            print(f"{self.name} has died.")
            return f"{self.name} has died."

        elif self.name == "Elephant" and self.health < self.health_threshold:
            self.below_threshold = True
            print(
                f"An {self.name} cannot walk due to poor health. Give the animals some food quickly.")
            return f"An {self.name} cannot walk due to poor health. Give the animals some food quickly."

        elif self.health < self.death_threshold:
            self.alive = False
            print(f"{self.name} has died.")
            return f"{self.name} has died."


class Zoo:
    def __init__(self):
        self.time = 0  # Track time in hours
        self.animals = {
            # the for _ in range just repeats the animal 5 times into the list
            "Monkey": [Animal("Monkey", 30, 30) for _ in range(5)],
            "Giraffe": [Animal("Giraffe", 50, 50) for _ in range(5)],
            "Elephant": [Animal("Elephant", 70, 70) for _ in range(5)],
        }

    def show_status(self):
        status_lines = []
        for animal_type, animal_list in self.animals.items():
            status_lines.append(f"{animal_type}s:")
            for i, animal in enumerate(animal_list, 1):
                status = "Alive" if animal.alive else "Dead"
                status_lines.append(
                    f"  {animal_type} {i}: Health = {animal.health:.2f}%, Status = {status}")
            status_lines.append("")  # blank line between animal groups
        print("\n".join(status_lines).strip())
        print("|---------------------------------------------------------|")

    def feed_animals(self):
        print("Feeding animals...")
        for animal_type, animal_list in self.animals.items():
            feed_percentage = random.uniform(10, 25)
            print(f"{animal_type}s are fed with {feed_percentage:.2f}% increase.")
            for animal in animal_list:
                animal.feed(feed_percentage)
        self.show_status()

    def pass_time(self):
        self.time += 1
        print(f"Time: {self.time} hours have passed.")
        for animal_type, animal_list in self.animals.items():
            for animal in animal_list:
                if animal.alive:
                    health_reduction = random.uniform(0, 20)
                    animal.apply_health_reduction(health_reduction)
        self.show_status()


if __name__ == "__main__":
    zoo = Zoo()

    while True:
        print("\nOptions:")
        print("1. Pass 1 hour")
        print("2. Feed animals")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            zoo.pass_time()
        elif choice == "2":
            zoo.feed_animals()
        elif choice == "3":
            print("Exiting Zoo Simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
