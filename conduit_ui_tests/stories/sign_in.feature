@component_conduit
@feature_sign_in
Feature: Conduit Sign in

  In order to Sign in
  User needs to submit Sign in form with correct data


  Background: User preparation
    Given created User with follwoing configuration:
    And Sign in conduit page is opened


  @test_signin_01
  @auto
  Scenario: User sign in with valid credentials
    When User fill Sign in form with correct data
    And User submit Sign in form
    Then User should be logged in conduit page


  @test_signin_02
  @manuals
  Scenario: User try to sigin in with wrong credentials
