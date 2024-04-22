function fetchRecipe() {
    const urlInput = document.getElementById('recipeUrl').value;

    if (urlInput === '') {
        document.getElementById('result').innerText = 'Please enter a URL.';
        return;
    }

    // Make a fetch request to a Flask endpoint with the URL as data
    fetch('/fetch-recipe', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: urlInput }) // Send the URL to the server
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('result').innerText = 'Recipe fetched successfully!';
            // Additional logic to handle the fetched data can be added here
        } else {
            document.getElementById('result').innerText = 'Error fetching recipe.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'An error occurred.';
    });
}