// edited 4/12/2024 Hallee Ray 
// edited 4/16/2024 Hallee Ray
// JavaScript file to support recipe.html, home.html 

document.addEventListener('DOMContentLoaded', function() {
    var faveButton = document.getElementById('fave');
    var isFave = false; // Assume default state; you can get this from backend if needed
    
    faveButton.addEventListener("click", function() {
        var recipeId = document.getElementById("title").innerText.replace(" ", "_"); // Assuming the ID is derived from the title
        
        // Toggle the button's appearance based on its current state
        if (isFave) {
            faveButton.style.backgroundColor = 'white';
            faveButton.innerText = 'Add to Favorites';
            isFave = false;
        } else {
            faveButton.style.backgroundColor = "#f2dea7";
            faveButton.innerText = 'Remove from Favorites';
            isFave = true;
        }

        // Send a POST request to toggle the favorite status on the backend
        // fetch('/favorites', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/x-www-form-urlencoded',
        //     },
        //     body: `recipe_id=${encodeURIComponent(recipeId)}`,
        // })
        // .then(response => {
        //     console.log("isFave: ", isFave)
        //     if (!response.ok) {
        //         throw new Error('Failed to toggle favorite status');
        //     }
        //     return response.text(); // Read the response if needed
        // })
        // .catch(error => {
        //     console.error('Error:', error);
        //     alert('An error occurred while toggling favorite status');
        // });
       fetch('/process_url', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `recipe_id=${encodeURIComponent(isFave)}`,  // Data to send
})
.then(response => {
    if (!response.ok) {
        throw new Error('Request failed');
    }
    return response.text();
})
.then(result => {
    console.log('Success:', result);
})
.catch(error => {
    console.error('Error:', error);
});
    });
    

//     var favebutton = document.getElementById('fave');
//     var isfave = false; //need to get favorite status from DB -> should we change to button to read add/remove from favorites based on DB bool?                        
//     favebutton.addEventListener("click", function() {
//         if (isfave) {
//             favebutton.style.backgroundColor = 'white';
//             isfave = false;
//         }
//         else {
//             favebutton.style.backgroundColor = "#f2dea7";
//             isfave = true;
            
//         }
        
//     });
    
    var cartbutton = document.getElementById('cart');
    var isincart = false;
    cartbutton.addEventListener("click", function() {
        if (isincart) {
            cartbutton.style.backgroundColor = 'white';
            isincart = false;
//             Remove from shopping cart
        }
        else {
            cartbutton.style.backgroundColor = '#f2dea7';
            isincart = true;
//             Add to shopping cart
        }
    });
 
    
    
});
                            


    