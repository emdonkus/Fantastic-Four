TABLE NAME:
Recipe Table: 
  _id: int
      Uniqe id for the recipe
  Favorite: bool
      True or false that the item has been favorited
  Title: string
      The title of the recipe
  Image: jpeg, png, jpg
      An image associated with the specific recipe


Ingredient Table
  recipeID: foreign key
      Represents the id that the ingredient belongs to
  Food: string 
      The ingredient and its quantity as a string ('1 onion')

Instruction Table
  recipeID: foreign key
      Represents the id that the ingredient belongs to
  StepNumber: int
      Represents the order that the instruction should be displayed on the HTML webpage
  Description: string 
      The string description of the specific instruction step the chef should use 

User Table:
  UserID: key
      Unique user id
  Email: string
      User's email used for signin purposes
  Password: string
      Uniqe user password paired with email

  
Descriptions:   
  Recipe: Includes a uniqe _id, whether the recipe is included in the favorites (represented by a boolean), a string for the title, and finally an image that will be stored as pngs or jpegs.
  Ingredient: Includes the recipe id that the ingredient belongs to and a string for the actual ingredient.
  Instruction: Includes the recipe id that the instruction belongs to, the step number for it to be read and displayed on the HTML webpage in the correct order, and the string for that specific recipe step.
  User: Includes the user's unique id and an email string as well as a password.

List of Tests:
    -Test adding values to the table, should add all columns successfully
    -Test adding duplicate recipe, should error on duplicate primary key id
    -Test removing recipe, should remove all columns with that recipe id
    -Test non-null constraints work by attempting to add blank columns
    -Test foreign key constraints by adding values with correct and incorrect foreign keys
    -Test table creation for each table to ensure it exists and was created with correct data types (can be done with a query)

Use case name
    Verify Recipe Table
Description
    Test data extraction and entry for recipe table
Pre-conditions
    User has recipe data
Test steps
    1. Enter recipe into extraction area
Expected result
    Favorites recipe should be added
Actual result
    User's recipe area has a recipe shown
Status (Pass/Fail)
    Fail
Notes
    Front end display of feature has not been created yet. Extraction algorithm is passing tests.
Post-conditions
    Recipe is successfully extracted and added to database. User has recipes in their recipes area


Use case name
    Verify User Login Table
Description
    User login should only work for correct email/password combo
Pre-conditions
    User has an account and valid email/password
Test steps
    1. Enter email into login test area
    2. Verify email exists in table
    3. Enter password for email
    4. Verify password/email combination is valid
    5. Verify that user data matches after login
Expected result
    User should be able to login
Actual result
    User can see their user information and recipes
Status (Pass/Fail)
    Fail
Notes
    Feature has not been created yet
Post-conditions
    User is validated with database and successfully signed into their account.


            Use case name
               Search for Recipe by Name
            Description
                Search the stored recipes by part of the recipe name
            Pre-conditions
                Recipes are stored in the recepie database
            Test steps
                1. Navigate to recipe search bar
                2. Type text string of desired search value
                3. SQL API will return query of all recipes with user input text string somewhere in the recipe name
                4. Show results on webpage
            Expected result
                User should be able to see list of recipes with the input text thread in the name on the webpage
            Actual result
                Query is created, but user value is not being passed in to query and query is not reporting results to webpage
            Status (Pass/Fail)
                Fail
            Notes
                Test is failing becuase feature has not been completed yet
            Post-conditions
                Webpage is updated displaying recipes with user input text in the recipe name
                Webpage navigation is updated to go back and try again or open one of the recipes shown


            Use case name
                Search for Recipe by Ingredient
            Description
                Search the Ingredients table for recipe ID's (foreign key) that contain a specific ingredient
            Pre-conditions
                Recipe table has data in it
                Ingredients table has data in it
                Foreign Key of Indgredients table is functioning correctly with recipe table primary key
            Test steps
                1. Navigate to ingredient search bar
                2. Type desired test string of ingredient to search for
                3. SQL API will return query of all recipe names with a recipe ID that matches the foreign key of any ingredient in the ingredients table that has a name that matches the user input text string
                4. Show results on webpage
            Expected result
                List of recipes that contain the user input ingredient will display on the webpage
            Actual result
                Nothing is displayed on webpage
            Status (Pass/Fail)
                Fail
            Notes
                Test fails as the feature has not been completed yet
            Post-conditions
                List of recipes with the user typed ingredient are displayed on the webpage
                Webpage navigation is updated to go back and try again or open one of the recipes shown

DATA ACCESS METHOD TESTS: (Hallee: ingredients pulling correctly,Hallee: instruction pulling correctly,Evan: Favorites (recipe table),Matt user login should only work for correct email/password combo,Lex: search by text of the recipe table for ingredient (chicken recipe ingredient),Lex: Search ingredients table for recipe with specific ingredient (corn))
    Recipe Tests:
    Test1
    Name: Add data to table
    Description: Tests to make sure the recipe is properly added to the table
    Parameters
    return values
    List of tests for verifying each access method

  
    Table Name
    Table Description
    For each field of the table, provide name and short description.
    List of tests for verifying each table

You must also provide the following (in SQL_TESTING.md)for each data access method (at least one access method for each table or query required to get the data to display):

    Use case name
    Description
    Parameters
    return values
    List of tests for verifying each access method

Here is a format that can be used for describing each test:

            
            Use case name
                Verify login with valid user name and password
            Description
                Test the Google login page
            Pre-conditions
                User has valid user name and password
            Test steps
                1. Navigate to login page
                2. Provide valid user name
                3. Provide valid password
                4. Click login button
            Expected result
                User should be able to login
            Actual result
                User is navigated to dashboard with successful login
            Status (Pass/Fail)
                Pass
            Notes
                N/A
            Post-conditions
                User is validated with database and successfully signed into their account.
                The account session details are logged in database. 
