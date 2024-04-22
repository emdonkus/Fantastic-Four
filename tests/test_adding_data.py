import unittest
import psycopg2
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from adding_data import insert_recipe, insert_instructions, insert_ingredients

class TestRecipeFunctions(unittest.TestCase):

    def setUp(self):
        # Set up a connection to the test database
        self.conn = psycopg2.connect('postgres://fantastic_four_user:DtcLO5teJIArKgIREMDgxPqJDjwM06gj@dpg-cogoo4u3e1ms73e6r6ig-a.oregon-postgres.render.com/fantastic_four')
        self.create_tables()

    def tearDown(self):
        # Close the connection and clean up the test database
        self.conn.close()

    def create_tables(self):
        # Create necessary tables in the test database
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipe (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                favorite BOOLEAN NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS instructions (
                id SERIAL PRIMARY KEY,
                recipeID INT NOT NULL,
                StepNumber INT NOT NULL,
                Description TEXT NOT NULL,
                FOREIGN KEY (recipeID) REFERENCES recipe(id)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (
                id SERIAL PRIMARY KEY,
                recipeID INT NOT NULL,
                food VARCHAR(255) NOT NULL,
                FOREIGN KEY (recipeID) REFERENCES recipe(id)
            );
        """)
        self.conn.commit()
        cursor.close()

    def test_1_insert_recipe(self):
        # Test inserting a recipe into the database
        recipe_name = "Test Recipe"
        insert_recipe(self.conn, recipe_name)

        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM recipe WHERE title = %s;", (recipe_name,))
        count = cursor.fetchone()[0]
        cursor.close()
        
        self.assertEqual(count, 1)

    def test_insert_instructions(self):
        # Test inserting instructions into the database
        recipe_name = "Test Recipe"
 
        insert_instructions(self.conn, "tests/test_instructions.txt", recipe_name)

        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM instructions WHERE recipeID IN (SELECT id FROM recipe WHERE title = %s);", (recipe_name,))
        count = cursor.fetchone()[0]
        cursor.close()
        
        self.assertEqual(count, 2)

    def test_insert_ingredients(self):
        # Test inserting ingredients into the database
        recipe_name = "Test Recipe"

        insert_ingredients(self.conn, "tests/test_ingredients.txt", recipe_name)

        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM ingredients WHERE recipeID IN (SELECT id FROM recipe WHERE title = %s);", (recipe_name,))
        count = cursor.fetchone()[0]
        cursor.close()
        
        self.assertEqual(count, 3)

if __name__ == '__main__':
    unittest.main()

