from behave import given, when, then
from src.Rover import Rover
from src.Plateau import Plateau


@given("a Rover instance with direction 'N'")
def step_impl(context):
    plateau = Plateau(5, 5)
    context.rover = Rover(1, 1, 'N', plateau)


@given("a Rover instance with direction 'E'")
def step_impl(context):
    plateau = Plateau(5, 5)
    context.rover = Rover(1, 1, 'E', plateau)


@given("a Rover instance with direction 'S'")
def step_impl(context):
    plateau = Plateau(5, 5)
    context.rover = Rover(1, 1, 'S', plateau)


@given("a Rover instance with direction 'w'")
def step_impl(context):
    plateau = Plateau(5, 5)
    context.rover = Rover(1, 1, 'W', plateau)


@when("receive a 'R' navigate instruction")
def step_impl(context):
    context.rover.navigate('R')


@when("receive a 'L' navigate instruction")
def step_impl(context):
    context.rover.navigate('L')


@then("Rover direction attribute is equal to 'N'")
def step_impl(context):
    assert context.rover.direction == 'N'


@then("Rover direction attribute is equal to 'E'")
def step_impl(context):
    assert context.rover.direction == 'E'


@then("Rover direction attribute is equal to 'S'")
def step_impl(context):
    assert context.rover.direction == 'S'


@then("Rover direction attribute is equal to 'W'")
def step_impl(context):
    assert context.rover.direction == 'W'
