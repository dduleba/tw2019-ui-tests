Feature:  User account create

  In order to create user account
  User needs to Sign Up on page

  @auto
  Scenario: Successful user Sign Up
    Given open url "${cfg.conduit.url}/register" in a web browser
    And page title should be "Conduit"
    When User input text "${generate.test_user}" in "Username" field
    And User input text "test_password" in "password" field
    And User input text "${generate.test_user}@test.pl" in "email" field
    And User submit "Sign up" form
    Then User should see link "Your Feed" on page
    And User should see link "Settings" on page
    And User should see link "New Post" on page
