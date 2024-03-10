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
    Selection of favorite or not \~this sounds weird??? How do I say this??~<br>
    image<br>
    ingredients<br>
Shopping cart:<br>
    Ingredients<br>
    Quantity of ingredient<br>
    
-----------------------
Link destinations for the page: <br>
Link destinations include \<a href> links to the shopping cart page, weekly plan page, favorites page, recents page, and recipe page specified by an input in the search bar.
    
------------------------
List of tests for verifying the rendering of the page<br>
    The search bar appears in the top right and takes in user input<br>
    Entering user input into the search bar redirects the user to the corresponding recipe page<br>
    Clicking on a container or button for weekly snapshot directs the user to the weekly plan page<br>
    Clicking on a container or button for favorites directs the user to the favorites page<br>
    Clicking on a container or button for for recents directs the user to the recents page<br>
    Clicking on a container or button for for shopping cart directs the user to the shopping cart page<br>
    Ingredients in the shopping cart are displayed with the correct quantity for all recipes added to the shopping cart<br>
    
    
 
