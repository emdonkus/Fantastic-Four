# import prefix

from flask import Flask, url_for
from flask import send_file
from flask import render_template, request
import os
import prefix

from flask import Flask, url_for

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

@app.route('/prefix_image')  
def prefix_image():
    image_path = url_for('static',filename='recipe/Perfect_Pot_Roast/image.jpeg')
    title_path = url_for('static',filename='recipe/Perfect_Pot_Roast/title.txt')
    # image_path = url_for('static', filename="image.jpeg")
    print("image_path2: ", image_path)
    print("title_path2: ", title_path)
    page = f'<img src="{image_path}" alt="Recipe Image">'
    title = f'<h1>Recipe: { title_path }</h1>'
    return title #page


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
def home():
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
    filename = 'static/search.html'
    return send_file(filename)

@app.route('/favorites')
def favorites():
    recipe_id = 'Perfect_Pot_Roast'
    
    # Getting file paths for different components of the recipe
    image_path = url_for('static', filename=f'recipe/{recipe_id}/image.jpeg')
    title_path = f'static/recipe/{recipe_id}/title.txt'

    # Print the file paths for debugging
    print("Image Path:", image_path)
    print("Title Path:", title_path)

    # Reading content from the files
    with open(title_path, 'r') as f:
        title = f.read().strip()

    # Rendering the template with the data
    return render_template('favorites.html', 
                           image_path=image_path, 
                           title=title)

@app.route('/cart')
def cart():
    filename = 'static/cart.html'
    return send_file(filename)

####Dynamic
@app.route('/recipe')
def recipe():
    recipe_id = 'Perfect_Pot_Roast'
    
    # Getting file paths for different components of the recipe
    image_path = url_for('static', filename=f'recipe/{recipe_id}/image.jpeg')
    title_path = f'static/recipe/{recipe_id}/title.txt'
    ingredients_path = f'static/recipe/{recipe_id}/ingredients.txt'
    instructions_path = f'static/recipe/{recipe_id}/instructions.txt'
    
    # Print the file paths for debugging
    print("Image Path:", image_path)
    print("Title Path:", title_path)
    print("Ingredients Path:", ingredients_path)
    print("Instructions Path:", instructions_path)
    
    # Reading content from the files
    with open(title_path, 'r') as f:
        title = f.read().strip()

    with open(ingredients_path, 'r') as f:
        ingredients = f.read().strip()

    with open(instructions_path, 'r') as f:
        instructions = f.read().strip()
    
    # Rendering the template with the data
    return render_template('recipe.html', 
                           image_path=image_path, 
                           title=title, 
                           ingredients=ingredients, 
                           instructions=instructions)

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