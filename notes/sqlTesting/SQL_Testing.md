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
  
    Table Name
    Table Description
    For each field of the table, provide name and short description.
    List of tests for verifying each table

You must also provide the following (in SQL_TESTING.md)for each data access method (at least one access method for each table or query required to get the data to display):

    Name
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
