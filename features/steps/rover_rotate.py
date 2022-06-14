from behave import *
from src.Rover import Rover
from src.Plateau import Plateau


@given("a Rover instance with direction 'N'")
def step_impl(context):
    plateau = Plateau(5, 5)
    context.rover = Rover(1, 1, 'N', plateau)


@when("receive a 'R' navigate instruction")
def step_impl(context):
    context.rover.navigate('R')


@then("Rover direction attribute is equal to 'E'")
def step_impl(context):
    assert context.rover.direction == 'E'
