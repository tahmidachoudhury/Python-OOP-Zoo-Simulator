from src.main import *
import random
# using unitest to provide predictable squence of values
from unittest.mock import patch


def test_format_zoo_status():
    zoo = Zoo()
    zoo.show_status()
    pass
    # completed this test by printing to terminal


def test_zoo_animals_after_time_pass():
    zoo = Zoo()

    monkeys = zoo.animals["Monkey"]
    # the pass time should bring the health down of the monkey
    zoo.pass_time()
    assert monkeys[0].health < 100


def test_zoo_animals_after_being_fed():
    zoo = Zoo()

    monkeys = zoo.animals["Monkey"]
    # the pass time should bring the health down of the monkey
    zoo.pass_time()
    zoo.pass_time()

    assert monkeys[0].health < 95
    # the feed animals should bring the health back up in random percentages
    zoo.feed_animals()
    zoo.feed_animals()
    zoo.feed_animals()

    assert monkeys[0].health > 95


def test_zoo_animals_die_after_not_being_fed():
    zoo = Zoo()

    giraffes = zoo.animals["Giraffe"]
    # seven hours should be enough - please rerun pytest
    zoo.pass_time()
    print(giraffes[0].health)
    zoo.pass_time()
    print(giraffes[0].health)
    zoo.pass_time()
    print(giraffes[0].health)
    zoo.pass_time()
    print(giraffes[0].health)
    zoo.pass_time()
    print(giraffes[0].health)
    zoo.pass_time()
    print(giraffes[0].health)
    zoo.pass_time()
    print(giraffes[0].health)

    assert not giraffes[0].alive
