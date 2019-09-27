@component_conduit
@feature_article
Feature: Article

  In order to create article
  Signed in user needs to submit create article form

  Background: User preparation
    Given created User
    And conduit page is opened

  @test_article_01
  @auto
  Scenario: User create article
    Given User is signed in
    When User navigate to create article page
    And User fills the new article form
    And User sumbit the new article form
    Then User should see the new article on page

  @test_article_02
  @manual
  Scenario: New article should be visible globally by not signed in user


    #  --> Validate article visible by not logged user - piszemy z nimi całość REST easy / UI e2e test - acceptance
