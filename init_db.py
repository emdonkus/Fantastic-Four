import os
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="3308TermProject",
    user="postgres",
    password="")

cur = conn.cursor()

# Create recipe table
cur.execute('DROP TABLE IF EXISTS recipe')
cur.execute('CREATE TABLE recipe (              id serial PRIMARY KEY,'
                                                'title varchar(150) NOT NULL,'
                                                'favorite boolean NOT NULL);'
                                                # Image somehow
                                                )

# Create ingredients table
cur.execute('DROP TABLE IF EXISTS ingredients;')
cur.execute('CREATE TABLE ingredients (id serial PRIMARY KEY,'
                                        'recipeID INT NOT NULL,'
                                       'food varchar(150) NOT NULL,'
                                       'FOREIGN KEY (recipeID) REFERENCES recipe(id)'
                                       ');'
            )

# Create instructions table
cur.execute('DROP TABLE IF EXISTS instructions')
cur.execute('CREATE TABLE instructions ('
            'id serial PRIMARY KEY,'
            'recipeID INT NOT NULL,'
            'StepNumber INT NOT NULL,'
            'Description VARCHAR(255) NOT NULL,'
            'FOREIGN KEY (recipeID) REFERENCES recipe(id)'
            ');'
            )


# Add sample data to the recipe table
cur.execute('''INSERT INTO recipe (id, title, favorite)
            VALUES
            (1,'Chicken and Waffles', True),
            (2,'Chicken Noodle Soup', False);            
            ''')

# Add sample data to the ingredients table
cur.execute(
    '''
        INSERT INTO ingredients (id, recipeID, food)
        VALUES
        (1, 1, 'chicken'),
        (2, 1, 'waffles');

'''
)

# Add sample data to the instructions table
cur.execute(
    '''
    INSERT INTO instructions (id, recipeID, StepNumber, Description)
    VALUES
    (1, 1, 1, 'Fry the chicken'),
    (2, 1, 2, 'Make some waffles');

'''
)



conn.commit()
cur.close()
conn.close()