document.addEventListener('DOMContentLoaded', function() {
    
    //check if the input is a url
    function isValidUrl(url) {
        // Regular expression to match a URL
        var urlPattern = /^(http|https):\/\/[\w\-]+(\.[\w\-]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?$/;
    
        // Test if the URL matches the pattern
        return urlPattern.test(url);
    }

    var fetchurl = document.getElementById('fetch_button');
    fetchurl.addEventListener("click", function() {
        // Get the value from the input field
        var userInput = document.getElementById("recipeUrl").value;

        // Check if input is not empty
        if (userInput.trim() !== "" && isValidUrl(userInput)) {
            
            fetch('/process_url', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: userInput })
        })
        .then(response => {
            if (response.ok) {
                // Handle successful response
                return response.json();
            } else {
                // Handle error response
                throw new Error('Network response was not ok');
            }
        })
        .then(data => {
            // Handle data returned from Flask app
            console.log(data);
        })
        .catch(error => {
            // Handle fetch errors
            console.error('Error:', error);
        });
            console.log("User input:", userInput);

            // Here you can call a function or perform any other action with the user input
        } else {
            // Handle case where input is empty
            console.log("Please enter a valid URL");
        }
    });

});





// var fetch_button = document.querySelector("#fetchbar button.fetch_button")
// fetch_button.addEventListener("click", fetchRecipe) 


// function fetchRecipe() {
//     const urlInput = document.getElementById('recipeUrl').value;

//     if (urlInput === '') {
//         document.getElementById('result').innerText = 'Please enter a URL.';
//         return;
//     }

//     // Make a fetch request to a Flask endpoint with the URL as data
//     fetch('/fetch-recipe', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ url: urlInput }) // Send the URL to the server
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             document.getElementById('result').innerText = 'Recipe fetched successfully!';
//             // Additional logic to handle the fetched data can be added here
//         } else {
//             document.getElementById('result').innerText = 'Error fetching recipe.';
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         document.getElementById('result').innerText = 'An error occurred.';
//     });
// }