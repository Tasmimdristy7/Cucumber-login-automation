Feature: Login to e-commerce platform

  Scenario: Valid login credentials
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should see the dashboard page

  Scenario: Invalid login credentials
    Given I am on the login page
    When I enter invalid credentials
    And I click the login button
    Then I should see an error message
