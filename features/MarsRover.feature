Feature: rotate the rover

  Scenario: rotate to right
     Given a Rover instance with direction 'N'
      When receive a 'R' navigate instruction
      Then Rover direction attribute is equal to 'E'