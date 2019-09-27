Feature:  User account create with page objects

  In order to create user account
  User needs to Sign Up on page

  @auto
  Scenario: Successful user Sign Up by with page objects
    Given open url "${cfg.conduit.url}/register" in a web browser
    When User fill out the Sign up form
      | option   | value                               |
      | username | ${generate.test_user}               |
      | email    | ${generate.test_user}@testdomain.pl |
      | password | ${generate.test_user}_password      |
    And User submit Sign up form
    Then User should be logged in
#    And User should be on Home page