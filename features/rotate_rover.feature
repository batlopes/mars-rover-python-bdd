Feature: rotate the rover

  Scenario Outline: rotate to right
    Given a Rover instance with direction '<initial direction>'
    When receive a 'R' navigate instruction
    Then Rover direction attribute is equal to '<final direction>'

  Examples:
    | initial direction | final direction |
    | N                 | E               |
    | E                 | S               |
    | S                 | W               |
    | W                 | N               |


  Scenario Outline: rotate to left
    Given a Rover instance with direction '<initial direction>'
    When receive a 'L' navigate instruction
    Then Rover direction attribute is equal to '<final direction>'

  Examples:
    | initial direction | final direction |
    | N                 | W               |
    | E                 | N               |
    | S                 | E               |
    | W                 | S               |
