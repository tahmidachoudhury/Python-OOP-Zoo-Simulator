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


def test_dead_animal_shouldnt_eat_or_reduce():
    # if animal is dead then nothing should return
    Monkey = Animal("Monkey", 30, 30)
    Monkey.alive = False
    monkey_health = Monkey.apply_health_reduction(20)
    assert monkey_health == None

    Elephant = Animal("Elephant", 70, 70)
    Elephant.alive = False
    elephant_health_after_food = Elephant.feed(25)
    assert elephant_health_after_food == None


def test_animal_dies_when_health_is_under_death_threshold():

    giraffe = Animal("Giraffe", 50, 50)
    giraffe.apply_health_reduction(60)
    giraffe.check_health()
    assert not giraffe.alive

    monkey = Animal("Monkey", 30, 30)
    monkey.apply_health_reduction(60)
    monkey.apply_health_reduction(50)
    result = monkey.check_health()
    assert result == "Monkey has died."


def test_elephant_is_incapacitated_when_health_is_under_health_threshold():

    elephant = Animal("Elephant", 70, 70)
    elephant.apply_health_reduction(40)
    # elephant is at 40% and will be below threshold
    result = elephant.below_threshold
    assert result
    print_statement = elephant.check_health
    # assert print_statement == "An Elephant cannot walk due to poor health. Give the animals some food quickly."
