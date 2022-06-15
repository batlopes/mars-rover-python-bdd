from behave import given, when, then, register_type
import parse
from src.Rover import Rover
from src.Plateau import Plateau


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


register_type(Number=parse_number)


@given("the rover is at position ({initial_x:Number}, {initial_y:Number}) and facing '{direction}'")
def step_impl(context, initial_x: int, initial_y: int, direction: str):
    plateau = Plateau(4, 4)
    context.rover = Rover(initial_x, initial_y, direction, plateau)


@when("the rover moves forward one step")
def step_impl(context):
    context.rover.navigate('M')


@then("the rover is at position ({final_x:Number}, {final_y:Number})")
def step_impl(context, final_x, final_y):
    assert context.rover.position_x == final_x
    assert context.rover.position_y == final_y

