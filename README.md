Project title (must be something representing your project)
    Anti-Mommy Blog CookBook
Team # 4

Team Name: 
  The Fantastic Four

Product Name:
  CutNPasta.com
  
Team members: list the name, git username, and email for each member.
   Evan Donkus,    emdonkus,   evdo5141@colorado.edu
   Lex Bukowski,   lexbuko22,  albu0228@colorado.edu 
   Matt Scott,     gr8tscott,  masc6977@colorado.edu
   Hallee Ray,     halleeray,  hara7620@colorado.edu

Day/Time/TimeZone for the scheduled team weekly meeting (30 minutes via Zoom)
   1730 Monday MT

Vision statement: what would you tell potential customers?
    Ever felt like you have too many pdf recipes on your computer taking up space? Tired of scrolling through someone's entire origin story just to get to your pork shoulder recipe? It's time to CutNPasta that recipe into your own personal recipe database. Plan out your recipes ahead of time and turn it into a shopping list. View just the recipes and remove those annoying backstories when you just want to eat.

Motivation: why are you working on this project?
    Been busy and looking at online recipes and saving off all the pdfs to my local computer area. Annoying to search through all of the saved ones for things I want.
    
Risks to project completion, possibly including:
    1) new language or working environment
    2) no prior experience working with these team members
    3) different formats for different websites on where recipe is presented
    

Mitigation Strategy for above risks
    1) Learning language from class labs and exploration
    2) Work with team and figure out everyone's specialties, Have frequent meetings to share, learn, and discuss progress
    3) Generating templates scripts for specific websites, limit scope to a few websites and potentially expand later

Development method: scrum, kanban, waterfall: with specifics!
    Scrumban with frequent scrum meetings and using a kanban board to track issues.

Trello: 
    https://trello.com/b/yO1r4fG0/class3308


## Overview

This Flask application serves as a personal cookbook, allowing users to manage recipes, mark favorites, and search for recipes by name. The application is hosted on a Render cloud database.

## Initializing Database

To initialize the database, follow these steps:

1. **Ensure Working Directory:** Make sure your working directory is set to Fantastic-Four.
2. **Run Scripts:**
    ```bash
    python clear_db.py
    python init_render_db.py
    python -m unittest tests.test_adding_data
    ```
    These scripts clear any previous test data, initialize the necessary tables, and test adding data to the database.
3. **Testing Completion:**
    After testing, run:
    ```bash
    python clear_db.py
    python init_render_db.py
    ```
    This clears the database of test data and initializes new blank tables.

## Starting Flask Server

To start the Flask server, run the following command in your terminal:
```bash
flask --app Frontend/app.py run
```
This command runs the Flask server on the default port 5000.

## Application Functionality

### Routes

- `/`: Home page where users can paste a URL into the recipe fetcher to add recipe information to the database.
- `/recipes`: Displays a list of recipes added by the user.
- `/recipes/<recipe_title>`: Displays details of the specified recipe.
- `/favorites`: Displays recipes marked as favorites by the user.
- `/search`: Allows users to search for recipes by name.
- `/cart`: Displays a list of ingredients needed to make the recipes marked as favorites.







Usage
/: Paste a URL into the field to add recipe information from the webpage to the personal cookbook (database).
/favorites: Click the favorites button to toggle a recipe as a favorite.