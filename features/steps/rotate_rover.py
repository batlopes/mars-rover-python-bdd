from behave import given, when, then
from src.Rover import Rover
from src.Plateau import Plateau


@given("a Rover instance with direction '{direction}'")
def step_impl(context, direction: str):
    plateau = Plateau(5, 5)
    context.rover = Rover(1, 1, direction, plateau)


@when("receive a '{rotate_direction}' navigate instruction")
def step_impl(context, rotate_direction: str):
    context.rover.navigate(rotate_direction)


@then("Rover direction attribute is equal to '{direction}'")
def step_impl(context, direction: str):
    assert context.rover.direction == direction
