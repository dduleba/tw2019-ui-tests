@component_conduit
@feature_sign_in
Feature: Conduit Sign in

  In order to Sign in
  User needs to submit Sign in form with correct data


  @test_signin_01
  @auto
  Scenario: User sign in with valid credentials
    Given created User
    And User opens conduit page
    When User navigate to Sign in page
    And User fill Sign in form with correct data
    And User submit Sign in form
    Then User should be logged in conduit page


  @test_signin_02
  @manual
  Scenario: User try to sign in with wrong credentials
