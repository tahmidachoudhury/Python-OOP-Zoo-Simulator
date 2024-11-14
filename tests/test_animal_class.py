from src.main import *


def test_health_reduction_on_animal():
    Monkey = Animal("Monkey", 30, 30)

    monkey_health = Monkey.apply_health_reduction(20)
    assert monkey_health == 80.0

    monkey_health = Monkey.apply_health_reduction(50)
    assert monkey_health == 40.0

    monkey_health = Monkey.apply_health_reduction(80)
    assert monkey_health == 8.0


def test_health_increase_after_food():

    Elephant = Animal("Elephant", 70, 70)
    Elephant.apply_health_reduction(20)
    elephant_health_after_food = Elephant.feed(25)
    assert elephant_health_after_food == 100

    giraffe = Animal("Giraffe", 50, 50)
    giraffe.apply_health_reduction(18)
    giraffe_health_after_food = giraffe.feed(19)
    assert giraffe_health_after_food == 97.58

    monkey = Animal("Monkey", 30, 30)
    monkey.apply_health_reduction(15)
    monkey_health_after_food = monkey.feed(23)
    assert monkey_health_after_food == 100
