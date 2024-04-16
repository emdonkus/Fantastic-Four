Fantastic Four
Team 4
Evan Donkus, Lex Bukowski, Matthew Scott, Hallee Ray
USAGE : SQL Table design and testing


TABLE NAME:
Recipe Table: 
  _id: int
      Unique id for the recipe (PRIMARY KEY)
  Favorite: bool
      True or false that the item has been favorited (NOT-NULL)
  Title: string
      The title of the recipe (NOT-NULL)
  Image: jpeg, png, jpg
      An image associated with the specific recipe (NO CONTRAINTS)


Ingredient Table
  ID: int 
      Unique ID for the ingredient (PRIMARY KEY)
  recipeID: (foreign key to recipe table)
      Represents the id that the ingredient belongs to (NOT-NULL)
  Food: string 
      The ingredient and its quantity as a string ('1 onion') (NOT-NULL)

Instruction Table
  ID: int 
      Unique ID for the instruction (PRIMARY KEY)
  recipeID: (foreign key to recipe table)
      Represents the id that the ingredient belongs to (NOT-NULL)
  StepNumber: int
      Represents the order that the instruction should be displayed on the HTML webpage (NOT-NULL)
  Description: string 
      The string description of the specific instruction step the chef should use (NOT-NULL)

User Table:
  UserID: key
      Unique user id (PRIMARY KEY)
  Email: string
      User's email used for signin purposes (NOT-NULL)
  Password: string
      Uniqe user password paired with email (NOT-NULL)

 

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
                
                
Use case name
    Verify ingredients
Description
    Test that the ingredients for a recipe are displayed correctly 
Pre-conditions
    The ingredients table associated with a recipe id is populated	
Test steps
    1.Navigate to the recipes page
    2. User clicks desired recipe
    3. Verify that the ingredients shown include the correct quantity and name with no redundancy 
Expected result
    The correct ingredients and quantity should be displayed for the desired recipe
Actual result
    The ingredients and quantity are not displayed on the page
Status (Pass/Fail)
    Fail
Notes
    Feature not yet implemented
Post-conditions
    Recipe ingredients displayed on the page 
    Next button appears to navigate to next recipe

Use case name
    Verify instructions
Description
    Test that the instructions for a recipe are displayed correctly 
Pre-conditions
    The instructions table associated with a recipe id is populated
    Foreign Key of Ingredients table is functioning correctly with recipe table primary key
Test steps
    1. Navigate to the recipes page
    2. User selects desired recipe
    3. Verify that the instructions shown are correct, in the correct order
Expected result
    The correct instructions and order should be displayed for a given recipe
Actual result
    The instructions are not displayed on the page
Status (Pass/Fail)
    Fail
Notes
    Feature not yet implemented
Post-conditions
    Recipe instructions displayed on the page in the correct order
    Next button appears to allow navigation to the next recipe