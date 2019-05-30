# Created by win10 at 28.05.2019
Feature: quantity of active vacancies when choosing a country of Canada and french language


  Scenario Outline: choice a country of '<country>'
    When I open Home Page
    Then I click on the country field
    Then I choosing a '<country>'country
    Then I click to the '<language>' field
    Then I click to language '<language>' checkbox
    And I see '<country>'
    And I see the '<language>' on the language's field
    And I click to apply button

    Examples:
    |country      | language |
    |Australia    | English  |
    |Canada       | French   |

   # Scenario Outline: choice a '<language>'

    # Then I click to the '<language>' field
    # Then I click to language '<language>' checkbox
     # And I see the '<language>' on the language's field
     # And I click to apply button

    # Examples:
    # |language     |
    # |English      |
    # |French       |


   Scenario: quantity of active vacancies

     When I check count of vacancies card in the vacancies block
     Then I print quantity of active vacancies