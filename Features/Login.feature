Feature: Verify login Functionality

@sanity
Scenario: Login with Valid Credentials
          Given user in login page
          When user enters username
          And user enters password
          And user enters Email ID
          And user enter login button
          Then user should be logged in successfully

@sanity @smoke
Scenario: Login with Duplicate Credentials
          Given user in login page
          When user enters duplicate username
          And user enters password
          And user enters Email ID
          And user enter login button
          Then user should be logged in successfully

@abcd
Scenario: Login with Invalid Credentials
          Given user in login page
          When user enters duplicate username
          And user enters password

