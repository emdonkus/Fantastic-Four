'''
Author: Lex Bukowski
Date: April 21, 2024
Usage: These are support functions that will populate the Render database with the information extracted from the wget extraction
algorithm that are stored in text files. Each function reads a .txt file that is created by the extraciton algorithm and adds the
information to the database. The usage statements are:

    insert_recipe(database_connection,recipe_name)
    insert_instructions(database_connection,instructions_file,recipe_name)
    insert_ingredients(database_connection,ingredients_file,recipe_name)

'''


import psycopg2

# Function to create a database connection
def connect_to_db():
    try:
        conn = psycopg2.connect('postgres://fantastic_four_user:DtcLO5teJIArKgIREMDgxPqJDjwM06gj@dpg-cogoo4u3e1ms73e6r6ig-a.oregon-postgres.render.com/fantastic_four')
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

# Function to read Recipe name from the extraction text file and insert into the database
def insert_recipe(connection, recipe_name):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO recipe (title, favorite) VALUES (%s, %s);"
        cursor.execute(insert_query, (recipe_name, False))
        connection.commit()
        cursor.close()
    except psycopg2.Error as e:
        print("Error inserting recipe:", e)


# Function to read instructions from the extraction text file and insert into the database
def insert_instructions(conn, file_name, recipe_name):
    try:
        cursor = conn.cursor()

        # Find the recipeID for the given recipe name
        find_recipe_query = "SELECT id FROM recipe WHERE title = %s;"
        cursor.execute(find_recipe_query, (recipe_name,))
        recipe_id = cursor.fetchone()[0]

        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                instruction = line.strip()
                insert_query = "INSERT INTO instructions (recipeID, StepNumber, Description) VALUES (%s, %s, %s);"
                cursor.execute(insert_query, (recipe_id, line_number, instruction,))
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        print("Error inserting instructions:", e)


# Function to read ingredients from the extraction text file and insert into the database
def insert_ingredients(conn, file_name, recipe_name):
    try:
        cursor = conn.cursor()
        
        # Find the recipeID for the given recipe name
        find_recipe_query = "SELECT id FROM recipe WHERE title = %s;"
        cursor.execute(find_recipe_query, (recipe_name,))
        recipe_id = cursor.fetchone()[0]
        #Add error handling for not finding the foreign key
        
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                ingredient = line.strip()
                insert_query = "INSERT INTO ingredients (recipeID, food) VALUES (%s, %s);"
                cursor.execute(insert_query, (recipe_id, ingredient))
        
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        print("Error inserting ingredients:", e)

# Function to Get Recipe Name
def check_recipe_exist(conn, recipe):
    try:
        cursor = conn.cursor()
        select_query = "SELECT EXISTS(SELECT 1 FROM recipe WHERE title = %s);"
        cursor.execute(select_query, (recipe,))
        recipe_exists = cursor.fetchone()[0]
        cursor.close()
        if recipe_exists:
            print("Recipe exists")
        else:
            print("Doesn't exist")
        return recipe_exists
    except psycopg2.Error as e:
        print("Error checking recipe existence:", e)
        return False

def main():
    conn = connect_to_db()
    if conn is not None:
        # insert_recipe(conn,"Chicken_Florentine")
        # # insert_ingredients(conn, "../Recipes/skinnytaste/Chicken_Florentine/Chicken_Florentine_ingredients.txt","Chicken_Florentine")
        # # insert_instructions(conn,"../Recipes/skinnytaste/Chicken_Florentine/Chicken_Florentine_instructions.txt","Chicken_Florentine")
        # check_recipe_exist(conn, "Chicken_Florentine")
        # check_recipe_exist(conn,"adsfasfs")
        conn.close()
        print("Database conn closed.")

if __name__ == "__main__":
    main()
