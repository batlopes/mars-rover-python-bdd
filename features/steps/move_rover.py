from behave import given, when, then
from src.Rover import Rover
from src.Plateau import Plateau


@given("the rover is at position (2, 2) and facing 'N'")
def step_impl(context):
    plateau = Plateau(4, 4)
    context.rover = Rover(2, 2, 'N', plateau)


@given("the rover is at position (2, 2) and facing 'E'")
def step_impl(context):
    plateau = Plateau(4, 4)
    context.rover = Rover(2, 2, 'E', plateau)


@given("the rover is at position (2, 2) and facing 'S'")
def step_impl(context):
    plateau = Plateau(4, 4)
    context.rover = Rover(2, 2, 'S', plateau)


@given("the rover is at position (0, 0) and facing 'S'")
def step_impl(context):
    plateau = Plateau(4, 4)
    context.rover = Rover(0, 0, 'S', plateau)


@given("the rover is at position (2, 2) and facing 'W'")
def step_impl(context):
    plateau = Plateau(4, 4)
    context.rover = Rover(2, 2, 'W', plateau)


@when("the rover moves forward one step")
def step_impl(context):
    context.rover.navigate('M')


@then("the rover is at position (2, 3)")
def step_impl(context):
    assert context.rover.position_x == 2
    assert context.rover.position_y == 3


@then("the rover is at position (3, 2)")
def step_impl(context):
    assert context.rover.position_x == 3
    assert context.rover.position_y == 2


@then("the rover is at position (2, 1)")
def step_impl(context):
    assert context.rover.position_x == 2
    assert context.rover.position_y == 1


@then("the rover is at position (1, 2)")
def step_impl(context):
    assert context.rover.position_x == 1
    assert context.rover.position_y == 2


@then("the rover is at position (0, 0)")
def step_impl(context):
    assert context.rover.position_x == 0
    assert context.rover.position_y == 0
