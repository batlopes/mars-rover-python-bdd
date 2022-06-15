Feature: rotate the rover

  Scenario Outline: rotate
    Given a Rover instance with direction '<initial direction>'
    When receive a '<rotate direction>' navigate instruction
    Then Rover direction attribute is equal to '<final direction>'

  Examples:
    | initial direction | rotate direction | final direction |
    | N                 | R                | E               |
    | E                 | R                | S               |
    | S                 | R                | W               |
    | W                 | R                | N               |
    | N                 | L                | W               |
    | E                 | L                | N               |
    | S                 | L                | E               |
    | W                 | L                | S               |