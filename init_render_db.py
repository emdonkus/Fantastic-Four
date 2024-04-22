'''
Author: Lex Bukowski
Date: 4/21/2024
Usage: This file connects to the Render hosted database and creates the three tables "recipe", "ingredients", and "instructions" that store
the recipes, ingredients, and instructions that were extraced using the extraction algorithm. These database tables are then used to
populate the application.
'''


import os
import psycopg2

conn = psycopg2.connect('postgres://fantastic_four_user:DtcLO5teJIArKgIREMDgxPqJDjwM06gj@dpg-cogoo4u3e1ms73e6r6ig-a.oregon-postgres.render.com/fantastic_four')

cur = conn.cursor()


# Create recipe table
cur.execute('CREATE TABLE IF NOT EXISTS recipe ( id serial PRIMARY KEY,'
                                                'title varchar(150) NOT NULL,'
                                                'favorite boolean NOT NULL);'
                                                # Image somehow
                                                )

# Create ingredients table
cur.execute('CREATE TABLE IF NOT EXISTS ingredients (id serial PRIMARY KEY,'
                                        'recipeID INT NOT NULL,'
                                       'food varchar(150) NOT NULL,'
                                       'FOREIGN KEY (recipeID) REFERENCES recipe(id)'
                                       ');'
            )

# Create instructions table
cur.execute('CREATE TABLE IF NOT EXISTS instructions ('
            'id serial PRIMARY KEY,'
            'recipeID INT NOT NULL,'
            'StepNumber INT NOT NULL,'
            'Description VARCHAR(500) NOT NULL,'
            'FOREIGN KEY (recipeID) REFERENCES recipe(id)'
            ');'
            )


# # Add sample data to the recipe table
# cur.execute('''INSERT INTO recipe (title, favorite)
#             VALUES
#             ('Perfect_Pot_Roast', True),
#             ('Chicken Noodle Soup', False);            
#             ''')

# # Add sample data to the ingredients table
# cur.execute(
#     '''
#         INSERT INTO ingredients (id, recipeID, food)
#         VALUES
#         (1, 1, 'chicken'),
#         (2, 1, 'waffles');

# '''
# )

# # Add sample data to the instructions table
# cur.execute(
#     '''
#     INSERT INTO instructions (id, recipeID, StepNumber, Description)
#     VALUES
#     (1, 1, 1, 'Fry the chicken'),
#     (2, 1, 2, 'Make some waffles');

# '''
# )



conn.commit()
cur.close()
conn.close()