# import prefix

from flask import Flask, url_for
from flask import send_file


# create app to use in this Flask application
app = Flask(__name__)

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
    # Extract the query parameters from the URL
    recipe_id = request.args.get('recipe_id')
    title = request.args.get('title')
    ingredients = request.args.get('ingredients')

    return render_template('recipe.html', recipe_id=recipe_id, title=title, ingredients=ingredients)