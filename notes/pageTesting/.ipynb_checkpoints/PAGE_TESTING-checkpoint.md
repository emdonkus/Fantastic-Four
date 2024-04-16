Home Page
----------------------
Page Description: This page will be the home page for CutNPasta where the user can navigate to the subpages. It displays information such as up to 4 recipes favorited by the user, a snapshot of the recipe plan for the week with the recipe titles, and a snapshot of the current items in the shopping cart. Clicking on these objects redirect the user to the page corresponding to the snapshot. Additionally, the home page includes a search bar that allows users to search the recipe database for a recipe with a given name, and buttons that redirect the user to the favorites page, recents page, and shopping cart page.
<figure width=100%>
    <img src="images_design/homepage.png" alt="CutNPasta Home"ALIGN="center" />
</figure>

-----------------------
Parameters needed for the page: <br>
Page Title<br>
Containers for Weekly snapshot, favorites, shopping cart<br>
ingredients in shopping cart<br>
buttons for favorites, recents, shopping cart, weekly snapshot<br>
href links to redirect the user to the corresponding page<br>
input forms for user to use search bar<br>

----------------------
Data needed to render the page:<br>
Weekly snapshot:<br>
    Recipe name<br>
    Day of week selection <br>
Favorites:<br>
    Recipe name<br>
    Selection of favorite or not (Boolean)<br>
    image<br>
    ingredients<br>
Shopping cart:<br>
    Ingredients<br>
    Quantity of ingredient<br>
    
-----------------------
Link destinations for the page: <br>
Route for page: /<br>
Link destinations include \<a href> links to the shopping cart page, weekly plan page, favorites page, recents page, and recipe page specified by an input in the search bar. Utilize flask routes for the webpages: /favorites, /recents, /recipe, /index, /cart, /plan, /<br>

    
------------------------
List of tests for verifying the rendering of the page<br>
    The search bar appears in the top right and takes in user input<br>
    Entering user input into the search bar redirects the user to the corresponding recipe page<br>
    Clicking on a container or button for weekly snapshot directs the user to the weekly plan page<br>
    Clicking on a container or button for favorites directs the user to the favorites page<br>
    Clicking on a container or button for for recents directs the user to the recents page<br>
    Clicking on a container or button for for shopping cart directs the user to the shopping cart page<br>
    Ingredients in the shopping cart are displayed with the correct quantity for all recipes added to the shopping cart<br>
    Check for 404 page not found errors<br>
    Test flask routes for home page<br>
    
    
    
Shopping Cart
----------------------
Page Description: This page displays all of the ingredients currently in the shopping cart. When the user adds recipes to the shopping cart, like ingredients are aggregated and the total quantity of each ingredient is displayed. There are buttons for the user to add or remove from the quantity of each ingredient. There is a list of the recipe names that were added to the shopping cart. The user can deselect a recipe to remove all of the associated ingredients from the shopping cart. If there are redundant ingredients, only the quantity required for the removed recipe are removed from the shopping cart.
<figure width=100%>
    <img src="images_design/shopping_cart.png" alt="CutNPasta Shopping Cart"ALIGN="center" />
</figure>
-----------------------

Parameters needed for the page:<br>
Page Title<br>
URL Route<br>
Quantity of each ingredient<br>
Ingredient name<br>
Recipe names<br>
buttons to add or remove ingredient/recipe from shopping cart<br>

----------------------

Data needed to render the page:<bR>
    Recipe name<br>
    Ingredients<br>
    Ingredient quantity<br>
-----------------------

Link destinations for the page:<br>
Route for page: /cart<br>
Links are used to redirect the user to the recipe page of a recipe when the name of the recipe is clicked on.

------------------------
List of tests for verifying the rendering of the page:<br>
Recipe names include links to the recipe page of the recipe on click<br>
Clicking add or remove from quantity adds or removes the quantity of the ingredient by 1<br>
clicking remove a recipe name removes only the quantity of each ingredient needed for the recipe from the shopping cart<br>
If an ingredient is needed in multiple recipes, the ingredient name only appears once in shopping cart with the quantity of the ingredient for all the recipes displayed<br>


Favorites
----------------------
Page Description (include a mockup or hand drawn image of the page): <br>
Displays the recipes, recipe image, and ingredients for recipes that have been marked as favorite by the user.
<figure width=100%>
    <img src="images_design/favorites.png" alt="CutNPasta Favorites"ALIGN="center" />
</figure>
-----------------------
Parameters needed for the page:<br>
    Page Title<br>
    URL Route<br>
    Recipe Name<br>
    Favorite selection (Boolean)<br>
    href redirect link to recipe page<br>
    button to remove favorite<br>
    
----------------------

Data needed to render the page:<br>
    Recipe name<br>
    Ingredients<br>
    Ingredient quantity<br>
    
-----------------------

Link destinations for the page:<br>
    Route: /favorites<br>
    href to recipe pages<br>
    
------------------------

List of tests for verifying the rendering of the page:<br>
Ensure the image appears on the right side of the recipe name, ingredients and instructions<br>
Ingredients displayed as a quantitative list with the correct quantity of each ingredient for the recipes<br>
Clicking the remove from favorites button removes the recipe name and ingredients from the display<br>
Clicking on the recipe name loads the correct page for the specific recipe<br>
    




Recents
----------------------
Page Description (include a mockup or hand drawn image of the page):<br>
Displays recipe name, recipe image, and ingredients for recipes' whose pages were recently visited by the user.
<figure width=100%>
    <img src="images_design/recents.png" alt="CutNPasta Recents"ALIGN="center" />
</figure>
-----------------------
Parameters needed for the page: <br>
    Page Title<br>
    URL Route<br>
    Recipe Name<br>
    href redirect link to recipe page<br>
    button to add to favorites<br>
----------------------
Data needed to render the page: <br>
    Recipe name<br>
    Recipe Image<br>
    Ingredients<br>
    Ingredient quantity<br>
    Time the recipe page was accessed<br>
-----------------------
Link destinations for the page: <br>
    Route: /recents<br>
    href to recipe pages<br>
------------------------
List of tests for verifying the rendering of the page: <br>
Ensure the image appears on the right side of the recipe name and ingredients<br>
Ingredients displayed as a quantitative list with the correct quantity of each ingredient for the recipes<br>
Clicking the add to favorites button adds the recipe to the favorites table of the DB<br>
Clicking on the recipe name loads the correct page for the specific recipe<br>
Only recipe pages that were recently visited appear on the list<br>




Recipe Display
----------------------
Page Description (include a mockup or hand drawn image of the page):<br>
Displays recipe name, recipe image, ingredients, and instructions for the recipe. Buttons allow users to add the recipe to favorites, shopping cart, and/or weekly plan. When the button for weekly plan is clicked, a pop up menu allows the user to select the day of week and meal (breakfast, lunch, or dinner) to add the recipe to.
<figure width=100%>
    <img src="images_design/recipe_display.png" alt="CutNPasta Recipe Display"ALIGN="center" />
</figure>
-----------------------
Parameters needed for the page: <br>
Page Title<br>
URL Route<br>
Recipe Name<br>
Recipe Image<br>
Quantity of each ingredient<br>
Ingredient names<br>
buttons to add or remove ingredient/recipe from shopping cart, favorites, weekly plan<br>
----------------------
Data needed to render the page:<br>
    Recipe Name<br>
    Recipe Image<br>
    Ingredients<br>
    Ingredient quantity<br>
    Instructions<br>
-----------------------
Link destinations for the page: <br>
    Route: /$recipe_name<br>
    href links to all other pages<br>
------------------------
List of tests for verifying the rendering of the page: <br>
    Ensure the image appears on the right side of the recipe name and ingredients<br>
    Ingredients displayed as a quantitative list with the correct quantity of each ingredient for the recipe<br>
    Clicking the add to favorites button adds the recipe to the favorites table of the DB<br>
    Clicking the add to shopping cart button adds the ingredients to the shopping cart<br>
    Clicking on a container or button for weekly snapshot brings up options for the user to add the recipe to a weekday, and meal (breakfast/lunch/dinner)<br>
    Ensure no visual overlap for any of the containers<br>
    Check for 404 page not found errors<br>


Weekly Plan
----------------------
Page Description (include a mockup or hand drawn image of the page):<br>
The weekly plan displays a weekly calendar with the recipe selection for each day and meal (breakfast, lunch, and dinner). A button can be clicked to add all ingredients from the recipe to the shopping cart.
<figure width=100%>
    <img src="images_design/weeklyplan.png" alt="CutNPasta Weekly Plan"ALIGN="center" />
</figure>
-----------------------
Parameters needed for the page: <br>
    Weekday display<br>
    Meal Selection<br>
    Recipe Names<br>
----------------------
Data needed to render the page: <br>
    Recipe Names<br>
    Recipe Images<br>
    Ingredents list<br>
    Ingredients Quantity<br>
    Instructions list<br>
    Selection for day of week and meal<br>
    
-----------------------
Link destinations for the page:<br>
    Route: /plan<br>
    href links to recipe pages<br>
------------------------
List of tests for verifying the rendering of the page: <br>
    Images are not blocking other containers on page<br>
    Recipe names presented with ingredients for the associated recipe<br>
    Ingredients are not aggregated, instead are presented by only the quantity and ingredient for each recipe<br>
    Meal selection is specific to each day<br>
    Recipes can be selected for multiple days/meals<br>
    Clicking add to shopping cart button adds the ingredients to the shopping cart<br>
    Clicking recipe name redirects the user to the recipe page<br>
    Check for 404 page not found errors<br>
    






