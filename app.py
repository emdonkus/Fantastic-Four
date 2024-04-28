# import prefix

from flask import Flask, url_for
from flask import send_file
from flask import render_template, request
import os
from Frontend import prefix
from Frontend import adding_data
import psycopg2
import subprocess

from flask import Flask, url_for

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
#prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
# @app.route('/prefix_url')  
# def prefix_url():
#     return 'The URL for this page is {}'.format(url_for('prefix_url'))

# @app.route('/prefix_image')  
# def prefix_image():
#     image_path = url_for('static',filename='recipe/Perfect_Pot_Roast/image.jpeg')
#     title_path = url_for('static',filename='recipe/Perfect_Pot_Roast/title.txt')
#     # image_path = url_for('static', filename="image.jpeg")
#     print("image_path2: ", image_path)
#     print("title_path2: ", title_path)
#     page = f'<img src="{image_path}" alt="Recipe Image">'
#     title = f'<h1>Recipe: { title_path }</h1>'
#     return title #page


#. venv/bin/activate
# export FLASK_DEBUG=true
# flask --app app.py run

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
# prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
# @app.route('/prefix_url')  
# def prefix_url():
#     return 'The URL for this page is {}'.format(url_for('prefix_url'))

################
@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        #Call genRecipes.sh<URL form form>

        return

    #lst = ''' 
    #    <h1>Home Index</h1>
    #    <ul>
    #        <li>{}</li>
    #        <li>{}</li>
    #        <li>{}</li>
    #        <li>{}</li>
    #    </ul>
    #    '''.format(url_for('home'),url_for('search'),url_for('favorites'),url_for('about'),url_for('recipe'))
    #return lst
    # Rendering the template with the data
    return render_template('home.html')

@app.route('/hello')
def hello():
    welcome = '''
        <h1>Hello new vistor!</h1>
        This is the welcome page for CutNPasta!
        '''
    return welcome

@app.route('/about')
def about():
    # lst = ''' 
    #     <ul>
    #         <li>Team 4</li>
    #         <li>CUid: masc6977</li>
    #         <li>Github: gr8tscott</li>
    #     </ul>
    #     '''
    lst = 'The about page'
    return lst


####Static
@app.route('/search') ###may need to be made dynamic
def search():
    # hardcoded for Perfect Pot Roast
    recipe_id = 'Perfect_Pot_Roast'
    image_path = url_for('static', filename=f'recipe/{recipe_id}/image.jpeg')
    title_path = f'static/recipe/{recipe_id}/title.txt'
    
    with open(title_path, 'r') as f:
        title = f.read().strip()
        
    return render_template('search.html',image_path=image_path, 
                           title=title,)


@app.route('/favorites', methods=['POST', 'GET'])
def favorites():
    recipe_id = 'Perfect_Pot_Roast'
    
    # if request.method == 'POST':
    #     # Extract recipe ID from the POST request
    #     recipe_id = request.form['recipe_id']

    #     # Toggle the favorite boolean in the database for the specified recipe ID
    #     conn = adding_data.connect_to_db()

    #     try:
    #         cursor = conn.cursor()
    #         update_query = "UPDATE recipe SET favorite = NOT favorite WHERE id = %s;"
    #         cursor.execute(update_query, (recipe_id,))
    #         conn.commit()
    #         cursor.close()
    #     except psycopg2.Error as e:
    #         print("Error toggling favorite:", e)
    #         return "Error toggling favorite"


    if request.method == 'GET':
        conn = adding_data.connect_to_db()

        try:
            cursor = conn.cursor()
            select_query = "SELECT title FROM recipe WHERE favorite = %s;"
            cursor.execute(select_query, (True,))
            favorite_recipes = [row[0] for row in cursor.fetchall()]
            cursor.close()

        except psycopg2.Error as e:
            print("Error fetching favorite recipes:", e)
            return []

        # Getting file paths for different components of the recipe
        #image_path = url_for('static', filename=f'recipe/{recipe_id}/image.jpeg')
        image_path = 'Recipes/skinnytaste/Almond_Cake/Almond_Cake_image.jpg'
        title_path = f'Frontend/static/recipe/{recipe_id}/title.txt'

        # Print the file paths for debugging
        print("Image Path:", image_path)
        print("Title Path:", title_path)
        print(favorite_recipes)

        # Reading content from the files
        with open(title_path, 'r') as f:
            title = f.read().strip()

        # Rendering the template with the data
        #return favorite_recipes
        return render_template('favorites.html', 
                                image_path=image_path, 
                            recipes=favorite_recipes)
    

@app.route('/cart')
def cart():
    ## Get request for shopping cart table
    ## title and ingredients
    thisdict = {'Perfect Pot Roast': ['1. 4 pounds boneless chuck roast, excess fat trimmedKosher salt and freshly ground black pepper, to taste','2. 2 tablespoons canola oil', '3. 1 medium sweet onion, cut into 1-inch wedges','4. 2 tablespoons tomato paste','5. 4 cloves garlic, minced','6. 1 cup dry red wine*','7. 1 cup beef stock'],
           '2Perfect Pot Roast2': ['1. 4 pounds boneless chuck roast, excess fat trimmedKosher salt and freshly ground black pepper, to taste','2. 2 tablespoons canola oil', '3. 1 medium sweet onion, cut into 1-inch wedges','4. 2 tablespoons tomato paste','5. 4 cloves garlic, minced','6. 1 cup dry red wine*','7. 1 cup beef stock']}
    filename = 'static/cart.html'
    # return send_file(filename)
    return render_template('cart.html', recipes=thisdict)


@app.route('/recipes',methods = ['GET'])
def get_recipes():
    # dummy image
    recipe_id = 'Perfect_Pot_Roast'
    image_path = url_for('static', filename=f'recipe/{recipe_id}/image.jpeg')
    
    if request.method == 'GET':
        conn = adding_data.connect_to_db()

        try:
            cursor = conn.cursor()
            select_query = "SELECT title FROM recipe;"
            cursor.execute(select_query)
            recipes = [row[0] for row in cursor.fetchall()]
            cursor.close()

        except psycopg2.Error as e:
            print("Error fetching recipes:", e)
            return []

    return render_template('allrecipes.html', recipes=recipes, image=image_path)



####Dynamic
@app.route('/recipes/<recipe_title>', methods=['POST', 'GET'])
def recipes(recipe_title):
        
    if request.method == 'POST':
        # Extract recipe ID from the POST request
        recipe_id = request.form['recipe_id']

        # Toggle the favorite boolean in the database for the specified recipe ID
        conn = adding_data.connect_to_db()

        try:
            cursor = conn.cursor()
            update_query = "UPDATE recipe SET favorite = NOT favorite WHERE id = %s;"
            cursor.execute(update_query, (recipe_id,))
            conn.commit()
            cursor.close()
            return

        except psycopg2.Error as e:
            print("Error toggling favorite:", e)
            return "Error toggling favorite"
        

    if request.method == 'GET':
        conn = adding_data.connect_to_db()
        try:
            cursor = conn.cursor()
            title_query = "SELECT title FROM recipe WHERE title = %s;"
            cursor.execute(title_query, (recipe_title,))
            title = cursor.fetchone()[0]
            print(title)

            find_recipe_query = "SELECT id FROM recipe WHERE title = %s;"
            cursor.execute(find_recipe_query, (recipe_title,))
            recipe_id = cursor.fetchone()[0]
            print(recipe_id)

            ingredients_query = "SELECT food FROM ingredients WHERE recipeID = %s;"
            cursor.execute(ingredients_query, (recipe_id,))
            ingredients = cursor.fetchall()

            instructions_query = "SELECT description FROM instructions WHERE recipeID = %s;"
            cursor.execute(instructions_query, (recipe_id,))
            instructions = cursor.fetchall()

            cursor.close()
            conn.close()

            # Concatenate ingredients into a single string
            ingredients_str = '\n'.join([ingredient[0] for ingredient in ingredients])

            # Concatenate instructions into a single string
            instructions_str = '\n'.join([instruction[0] for instruction in instructions])

            image_path = url_for('static', filename=f'recipe/{title}/image.jpeg')

        except psycopg2.Error as e:
            return print("Error fetching recipe:", e)


            # Rendering the template with the data
    return render_template('recipe.html', 
                            image_path=image_path, 
                            title=title, 
                            ingredients=ingredients, 
                            instructions=instructions)

#testing route for Perfect Pot Roast Recipe Page
# @app.route('/recipe')
# def recipe():

#     recipe_id = 'Perfect_Pot_Roast'
#     # Getting file paths for different components of the recipe
#     image_path = url_for('static', filename=f'recipe/{recipe_id}/image.jpeg')
#     title_path = f'static/recipe/{recipe_id}/title.txt'
#     ingredients_path = f'static/recipe/{recipe_id}/ingredients.txt'
#     instructions_path = f'static/recipe/{recipe_id}/instructions.txt'
    
#     # Print the file paths for debugging
#     print("Image Path:", image_path)
#     print("Title Path:", title_path)
#     print("Ingredients Path:", ingredients_path)
#     print("Instructions Path:", instructions_path)
    
#     # Reading content from the files
#     with open(title_path, 'r') as f:
#         title = f.read().strip()

#     with open(ingredients_path, 'r') as f:
#         ingredients = f.read().strip()

#     with open(instructions_path, 'r') as f:
#         instructions = f.read().strip()
        
#         # Rendering the template with the data
#     return render_template('recipe.html', 
#                             image_path=image_path, 
#                             title=title, 
#                             ingredients=ingredients, 
#                             instructions=instructions)

##New Recipe URL
from flask import jsonify
import subprocess

# run the scripts to extract the recipe name, image, ingredients, and instructions from the RUL
@app.route('/fetch-recipe')
def fetch_recipe():
    # return render_template('fetchRecipe.html')
    data = request.json
    url = data.get('url')

    if not url:
        return jsonify(success=False, message="No URL provided"), 400
    
    # Trigger script.sh with the provided URL
    try:
        subprocess.run(['./extract_scripts/retrieveURL.sh', url], check=True)
        return jsonify(success=True)
    except subprocess.CalledProcessError:
        return jsonify(success=False, message="Error during scraping")
    

@app.route('/process_url', methods=['GET', 'POST'])
def process_url():
    # Retrieve URL from JSON data sent in the request body
    if(request.method == 'POST'):
        recipe_id = request.form.get('recipe_id', default=False)  # This should match the key in the POST data
    # answer = get_post(recipe_id)
    # Do something with recipe_id
    return "Success", 200
#     data = request.get_json()
#     user_url = data.get('url')

#     # Process the URL (e.g., fetch data from the URL)
#     # Here, you can add your logic to process the URL and return any data
#     # For now, just return a simple response
#     return jsonify({'message': 'URL received', 'url': user_url})
    
# @app.post('/post_recipe')
# def post_recipe():
#     if(request.method == 'POST'):
#         print("post")
#         name = request.form['username']
#         print("URL: ", name)
#         return "Success", 200
#     else:
#         return "NOPE NOPE NOPE"
    
###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    # with app.test_request_context():
        # print(url_for('index'))
        # print(url_for('about'))
        # print(url_for('login'))
        # print(url_for('login', next='/'))
        # print(url_for('profile', username='masc6977'))
    app.run(host='0.0.0.0', port=3308)