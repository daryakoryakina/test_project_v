# Created by win10 at 28.05.2019
Feature: quantity of active vacancies when choosing a country of Canada and french language


  Scenario Outline: choice a country of <country>

    When I open Home Page
    Then I click on the country field
    Then I choosing a country <country>
     And I see the <country> on the country's field

    Examples:
    |country      |
    |Canada       |

   Scenario Outline: choice a <language>

    When I click to the language field
    Then I click to language <language> checkbox
     And I see the <language> on the language's field

    Examples:
    |language     |
    |french       |

   Scenario: quantity of active vacancies

     When When I click to the language field
     And I click to apply button
     Then I check count of vacancies card in the vacancies block
     And I print quantity of active vacancies