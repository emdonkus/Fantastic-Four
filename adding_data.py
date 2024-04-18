import psycopg2

# Function to create a database connection
def connect_to_db():
    try:
        conn = psycopg2.connect('postgres://fantastic_four_user:DtcLO5teJIArKgIREMDgxPqJDjwM06gj@dpg-cogoo4u3e1ms73e6r6ig-a.oregon-postgres.render.com/fantastic_four')
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

# Function to read Recipe name from the file and insert into the database
def insert_recipe(connection, recipe_name):
    try:
        cursor = connection.cursor()
        insert_query = "INSERT INTO recipe (title, favorite) VALUES (%s, %s);"
        cursor.execute(insert_query, (recipe_name, False))
        connection.commit()
        cursor.close()
        print(f"Inserted recipe: {recipe_name}")
    except psycopg2.Error as e:
        print("Error inserting recipe:", e)


# Function to read instructions from the file and insert into the database
def insert_instructions(conn, file_name):
    try:
        cursor = conn.cursor()
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                instruction = line.strip()
                insert_query = "INSERT INTO instructions (instruction) VALUES (%s);"
                cursor.execute(insert_query, (instruction,))
                print(f"Inserted instruction {line_number}: {instruction}")
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        print("Error inserting instructions:", e)


# Function to read ingredients from the file and insert into the database
def insert_ingredients(conn, file_name, recipe_name):
    try:
        cursor = conn.cursor()
        
        # Find the recipeID for the given recipe name
        find_recipe_query = "SELECT id FROM recipe WHERE title = %s;"
        cursor.execute(find_recipe_query, (recipe_name,))
        recipe_id = cursor.fetchone()[0]
        
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                ingredient = line.strip()
                insert_query = "INSERT INTO ingredients (recipeID, food) VALUES (%s, %s);"
                cursor.execute(insert_query, (recipe_id, ingredient))
                print(f"Inserted ingredient {line_number}: {ingredient}")
        
        conn.commit()
        cursor.close()
    except psycopg2.Error as e:
        print("Error inserting ingredients:", e)

def main():
    conn = connect_to_db()
    if conn is not None:
        insert_recipe(conn,"Perfect Pot Roast")
        insert_ingredients(conn, "Perfect_Pot_Roast_ingredients-checkpoint.txt","Perfect Pot Roast")
        conn.close()
        print("Database conn closed.")

if __name__ == "__main__":
    main()
