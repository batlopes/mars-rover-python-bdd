Feature: move the rover

  Scenario Outline: move forward the rover
    Given the rover is at position (<initial x>, <initial y>) and facing '<direction>'
    When the rover moves forward one step
    Then the rover is at position (<final x>, <final y>)

  Examples:
    | initial x | initial y | direction | final x | final y |
    | 2         | 2         | N         | 2       | 3       |
    | 2         | 2         | E         | 3       | 2       |
    | 2         | 2         | S         | 2       | 1       |
    | 2         | 2         | W         | 1       | 2       |
    | 0         | 0         | S         | 0       | 0       |
