# import prefix

from flask import Flask, url_for
from flask import send_file
from flask import render_template, request
import os


# create app to use in this Flask application
app = Flask(__name__)

#. venv/bin/activate
#flask --app app.py run

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
# prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
# @app.route('/prefix_url')  
# def prefix_url():
#     return 'The URL for this page is {}'.format(url_for('prefix_url'))

################
@app.route('/')
def index():
    lst = ''' 
        <h1>Home Index</h1>
        <ul>
            <li>{}</li>
            <li>{}</li>
            <li>{}</li>
            <li>{}</li>
        </ul>
        '''.format(url_for('index'),url_for('search'),url_for('favorites'),url_for('about'),url_for('recipe'))
    return lst

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
    filename = 'static/search.html'
    return send_file(filename)

@app.route('/favorites')
def favorites():
    filename = 'static/favorites.html'
    return send_file(filename)

@app.route('/cart')
def cart():
    filename = 'static/cart.html'
    return send_file(filename)

####Dynamic
@app.route('/recipe')
def recipe():
    # # Extract the query parameters from the URL
    # recipe_id = request.args.get('recipe_id')
    # title = request.args.get('title')
    # ingredients = request.args.get('ingredients')
    #/movie?title=Avatar&director=James%20Cameron
    #/recipe?recipe_id=1&title=Bolognese&ingredients=meatsauce
    # Extract the query parameters from the URL
    recipe_id = request.args.get('recipe_id')
        #/recipe?recipe_id=Perfect_Pot_Roast
    # Assuming your recipe text files are stored in the 'recipe' folder
    recipe_folder = os.path.join(app.root_path, f'recipe/{recipe_id}')
    
    # Check if the recipe folder exists
    if not os.path.exists(recipe_folder):
        return "Recipe not found", 404
    
    # Construct the path to the recipe text file based on the recipe_id
    title_file_path = os.path.join(recipe_folder, f'title.txt')
    ingredients_file_path = os.path.join(recipe_folder, f'ingredients.txt')
    instructions_file_path = os.path.join(recipe_folder, f'instructions.txt')
    image_path = os.path.join(recipe_folder, 'image.jpeg')
    
    # Check if the files exist
    if not all(map(os.path.exists, [title_file_path, ingredients_file_path, instructions_file_path, image_path])):
        return "Recipe files not found", 404
    
    # Read the content of each recipe text file
    with open(title_file_path, 'r') as title_file:
        title = title_file.read()
    
    with open(ingredients_file_path, 'r') as ingredients_file:
        ingredients = ingredients_file.read()
    
    with open(instructions_file_path, 'r') as instructions_file:
        instructions = instructions_file.read()
    
    return render_template('recipe.html', recipe_id=recipe_id, title=title, ingredients=ingredients, instructions=instructions, image_path=image_path)

@app.route('/recipe/image.jpeg')
def get_image():
    # Extract the query parameters from the URL
    recipe_id = request.args.get('recipe_id')
    
    # Get the path to the image file
    # image_path = os.path.join(app.root_path, f'recipe/{recipe_id}', 'image.jpeg')
    image_path = os.path.join(app.root_path, 'static', 'image.jpeg')

    # Return the image file
    return send_from_directory(os.path.dirname(image_path), 'image.jpeg')
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