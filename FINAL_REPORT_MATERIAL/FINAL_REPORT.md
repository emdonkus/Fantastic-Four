

<h1>
    Project Title: Anti-Mommy Blog CookBook
</h1>
<h3>
    Team:
</h3>
<p>
    <ul>
        <li> Matthew Scott </li>
        <li> Lex Bukowski </li>
        <li> Hallee Ray </li>
        <li> Evan Donkus </li>
    </ul>
</p>
<h2>
    Links
</h2>
<p>
    <ul>
        <li><a href="https://trello.com/b/yO1r4fG0/class3308">Project tracker </a></li>
        <li><a href="https://github.com/emdonkus/Fantastic-Four">Github</a></li>
        <li><a href="https://fantastic-four.onrender.com">Cut'n'Pasta Website</a></li>
    </ul>
</p>
<h2>
    Completed Tasks
</h2>
    <p>
        <ul>
            <li>Accepts links from a subset of recipe blogs, using wordpress module</li>
            <li>Retireves recipe name, ingredients and instructions</li>
            <li>Adds data from text files to database</li>
            <li>Database populates /recipes route with all of the recipes in the database </li>
            <li>Databse populates /recipes/"recipe_name" dynamic route with recipe name, ingredients, and instructions</li>
            <li> /favorites route populates with recipes marked as favorites in database </li>
        </ul>
    </p>
<h2>
    In-Work Tasks
</h2>
    <p>
        <ul>
            <li>Front end favorites button does not toggle favorite boolean on the backend (disconnect between frontend patch request and backend patch handling) </li>
            <li>Fetch recipe button does not call script to web scrape the url and add the information to the database </li>
            <li>Unit tests for front end data population from the database</li>
            <li>Unit tests for patch and post requests from frontend user input</li>
        </ul>
    </p>

<h2>
    Future Work
</h2>
<p>
    <ul>
        <li>Shopping cart additions and functionality to combine repeated ingredients</li>
        <li>Accept links for websites that don't use Wordpress Recipe Module</li>
        <li>Provide better unit testing for DataParser class</li>
        <li>Provide better unit testing for front end page population</li>
        <li>Implement keyword search of the database</li>
        <li>Simplify navigation to a nav.html to reduce duplicates between html files</li>
        <li>Organize code</li>
    </ul>
</p>
<h2>
    Bugs and Issues
</h2>
<p>
    <ul>
        <li>Certain parts of recipe extraction do not properly break up ingredients and instructions. This resutls from deployed html having oddball syntax</li>
        <li> DataParser's parsing syntax needs to be improved to handle more conditions</li>
        <li> As more recipes are added, more files are added to recipes before being added to the database. Reduce or remov ethe need for additioanl files to be created</li>
        <li>Missing unit testing</li>
    </ul>
</p>
<h2>
    Website Demonstration
</h2>
<a href="https://drive.google.com/file/d/15ICaVa3tmzHCdUTTqjd2n2iVksS-n84A">
    Google Drive Link. Video was too large for github.
</a>

<h2>
Reflection
</h>
    <h3>
        Functionality
    </h3>
        <p>
            Overall, the application is a button connectivity away from being the product we were hoping to build. The fetch recipe button does not connect to the python and bash scripts that fetch, parse, and add the data to the databse. The bash script can be called from the terminal with a URL as an argument and has the desired functionality. The recipes, favorites, and recipes/"recipe_name" dynamic route all work well with the intended functionality and live data from the database. The shopping cart feature is built well on the front end, but is not built on the backend due to the recurring trouble we had linking user input on the front end to backend flask method calls.
        </p>
    <h3>
        Integration
    </h3>
        <p>
            The main struggles near the end of this project had to do with getting our front end functionality to integrate with the back end functionality. The pieces were built separately and the team did not agree on the "handoff" point between the front end and the back end before building the features. This led to confusion on how they would connect and the expectation of each persons work.
        </p>    
    <h3>
        Testing
    </h3>
        <p>
            Unit testing was a shortcoming of our project. Unit tests were built for initial database connection function and the functions for adding data to each table. Unit testing the shell web scrapping script proved to be challenging due to the fact that it was written in bash, not python. Unit tests should also have been written for the flask route functions that were populating information from the database, however more time was spent troubleshooting the http method calls, and the results could visually be seen to be correct, so testing those functions was pushed to the backburner while trying to build more funcitonality. That mindset seems to be the downfall of many coding projects at every level and should be avoided.
        </p>
    <h3>
        Backend Tools
    </h3>
        <p>
            The backend tools used were PostgreSQL, the python module psycopg2, and Render Cloud Hosting. Postgres is a very industry standard relational database tool and worked well for our project. The only downside was while using the psycopg2 module, SQL statements are written in strings, which can be hard to debug and are much harder to visualize in VSCode. There is likely a better way to write large database operations in python, however for our project needs, these tools were sufficient.
        </p>
    <h3>
        Documentation
    </h3>
        <p>
            No documentation programs or automation was used in this project. A README was written which does fully explain to a new user how to initiate and run the flask application, however this was built at the end of the project. There are many documentaiton tools that would have helped create the documentaiton features were built instead of waiting until the end of the project.
        </p>
    <h3>
        Configuraiton Management
    </h3>
        <p>
            As we were working, our source code became messy. Sometimes we would edit the same piece of code at the same time. Often this resulted in merge conflicts that we had to resolve through reading each others code. When the code we were editing was well documented and the git commits were clear, this was an easy solution. When it was poorly commented or unclear, merging became a pain. A few times, we had to have a meeting to make sure we could resolve the issue while getting the right changes in the code. This issue was more prevalent due to the lack of feature branches we created, and especially as project deadlines approached, more pushing to main was occuring. The editing and pushing to the main branch is not a good coding practice, and sorting through the merge issues, in the long run, probably took more time than if branches were created and merged properly.
        </p>
    <h3>
        Code Editors
    </h3>
        <p>
            We used VSCode and JupyterHub as code editors to complete this project. Using multiple IDE's proved to be tricky, as spinning up the built flask server required different functions on JupyterHub than it did while using VSCode. JupyterHub was very useful for giving the team a standard linux platform to code off of, but it is very basic when compared to code visualization and customization compared to VSCode.
        </p>
    <h3>
        Task Tracking
    </h3>
        <p>
            We used trello for task tracking. It took a lot of upfront to set it up for tasking and lacked good features for relating it to versions of code or any code changes. This tool, as all task managmenet/project tracking tools, takes a concentrated effort from users to maintian and update. For our small project, tasking was sorted out effectively at our meetings and we were able to make sure everyone was involved. For larger projects, a task tracking tool like this is necessary but I think that more often than not large orgs also have dedicated people to managing tools and encouraging (enforcing) use. This tool did lack a lot of good features for story pointing, designating relationship between tasks such as blocking tasks. 
        </p>

Make sure that your repository has the following files committed to remote repository:

    FINAL_REPORT.md
    Project presentation files from Presentation Milestone
    Video of demo
    Source code
    Test cases
    Source documentation, and auto-doc files
    Link to Public Deployment Site (Heroku or similar)
