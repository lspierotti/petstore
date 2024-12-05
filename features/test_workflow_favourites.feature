Feature: Complete workflow for adding, retrieving, updating, and deleting a pet
  As a user of the Pet Store API
  I want to add, retrieve, update, and delete a pet
  So that I can verify the correct behavior of the API endpoints

  Scenario: Complete workflow for adding, retrieving, updating, and deleting a pet
    # Step 1: Add a new pet
    When the user is authenticated with a valid token and create an new pet
    Then the response status should be 200
    Then the response should include the pet ID in the response

    # Step 2: Retrieve the added pet
    When the user sends a GET request to retrieve the pet by its ID
    Then the response status should be 200
    Then the response should include the category name "Peter Parker"

    # Step 3: Update the pet's details
    When the user sends a request to update the category name to "Spidey"
    Then the response status should be 200

    # Step 4: Delete the pet
    When the user sends a DELETE request to remove the pet by its ID
    Then the response status should be 200
    
