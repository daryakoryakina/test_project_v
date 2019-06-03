# Created by win10 at 28.05.2019
Feature: quantity of active vacancies when choosing a country and language


  Scenario Outline: choice a country of '<country>'
    When I open Home Page
    Then I click on the country field
    Then I choosing a '<country>'country
    Then I click to the '<language>' field
    Then I click to language '<language>', '<param>' checkbox
    And I see '<country>'
    And I see the '<language>' on the language's field
    And I click to apply button
    Then I check count of vacancies card with '<language>' and '<country>' parameters in the vacancies block
    And I print quantity vacancies
    And I clear filter

    Examples:
    |country                 | language | param   |
    |Australia               | English  | ch-7    |
    |Russian Federation      | Russian  | ch-22   |
    |Canada                  | French   | ch-10   |


   # Scenario Outline: choice a '<language>'

    # Then I click to the '<language>' field
    # Then I click to language '<language>' checkbox
     # And I see the '<language>' on the language's field
     # And I click to apply button

    # Examples:
    # |language     |
    # |English      |
    # |French       |


