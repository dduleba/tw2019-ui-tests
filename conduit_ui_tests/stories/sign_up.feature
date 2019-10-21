@component_conduit
@feature_signup
Feature: Sign Up

  In order to create Conduit account
  User needs to submit Sign up form


  @test_signup_01
  @auto
  Scenario: User Sign up
    When User opens conduit page
    And User navigate to Sign up page
    And User fills the Sign up page
    And User submit the Sign up page
    Then User should be logged in conduit page

  @test_signup_02
  @auto
  Scenario: User Sign up with special characters
    When User opens conduit page
    And User navigate to Sign up page
    And User enter username "Brzęczyszczykiewicz"
    And User enter password "hasło"
    And User enter email "grzegorz@brzeczyszczykiewicz.test"
    And User submit the Sign up page
    Then User should be logged in conduit page
