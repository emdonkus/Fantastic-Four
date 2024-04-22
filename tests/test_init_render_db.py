'''
Author: Lex Bukowski
Date: April 22, 2024
Usage: Tests the creation of the recipe, ingredients, and instructions table in the Render database
'''


import unittest
import psycopg2

class TestTableCreation(unittest.TestCase):

    def setUp(self):
        # Set up a connection to the database
        self.conn = psycopg2.connect('postgres://fantastic_four_user:DtcLO5teJIArKgIREMDgxPqJDjwM06gj@dpg-cogoo4u3e1ms73e6r6ig-a.oregon-postgres.render.com/fantastic_four')
        self.cur = self.conn.cursor()

    def tearDown(self):
        # Close the database connection
        self.cur.close()
        self.conn.close()

    def test_table_creation(self):
        # Check if recipe, ingredients, and instructions table exists

        self.cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'recipe')")
        recipe_table_exists = self.cur.fetchone()[0]
        self.assertTrue(recipe_table_exists)

        self.cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'ingredients')")
        ingredients_table_exists = self.cur.fetchone()[0]
        self.assertTrue(ingredients_table_exists)

        self.cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'instructions')")
        instructions_table_exists = self.cur.fetchone()[0]
        self.assertTrue(instructions_table_exists)

    # def test_ingredients_table_creation(self):
    #     # Check if ingredients table exists
    #     self.cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'ingredients')")
    #     ingredients_table_exists = self.cur.fetchone()[0]
    #     self.assertTrue(ingredients_table_exists)

    # def test_instructions_table_creation(self):
    #     # Check if instructions table exists
    #     self.cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'instructions')")
    #     instructions_table_exists = self.cur.fetchone()[0]
    #     self.assertTrue(instructions_table_exists)

if __name__ == '__main__':
    unittest.main()
