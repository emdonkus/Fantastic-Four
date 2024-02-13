Recipe planner/cookbook- As one finds recipes online, need way to compile them effectively. Could try to take the recipe panel, original link
    Gather the recipe from original page
    save it to a databse of recipes
    have a search function
    users have their own table
    can select up next
    provide ratings and comments
        Tables for ingredients
        Tables for steps
    


-------------
Documentation
    -Every story should have a closing commetn with how the task was resolved
    -make sure to commetn code so someone else can know what we are doing
    -Any coding should have a unit test associated



---------------
Recipe websites:
https://www.eatingwell.com/
https://www.skinnytaste.com/
https://www.budgetbytes.com/
https://www.allrecipes.com/
https://www.thekitchn.com/beef-tips-recipe-23578525#post-recipe-561880415

Print function seems to be a reliable source. EatingWell and AllRecipes have it located in the print formID area and it only contains the post.com suffix

Skinnytastes and budgetbytes have the wprm_print method that takes you a pdf file.

theKitchn uses an event I think to create next page. Not sure hwo to deal with that