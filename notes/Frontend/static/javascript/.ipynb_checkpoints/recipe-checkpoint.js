/* edited 4/12/2024 Hallee Ray */
document.addEventListener('DOMContentLoaded', function() {

    var favebutton = document.getElementById('fave');
    var fclicked = document.getElementById('faveclicked');
    var isYellow = false;
    
    favebutton.addEventListener("onmouseover", function() {
        favebutton.style.backgroundColor = "darkgray";
        favebutton.style.color = "white";
    }); 
                                
    favebutton.addEventListener("click", function() {
        if (isYellow) {
            fclicked.textContent = "Removed recipe from favorites.";
            favebutton.style.backgroundColor = 'white';
            favebutton.style.color = 'black';
            isYellow = false;
        }
        else {
            fclicked.textContent = "Added recipe to favorites!";
            favebutton.style.backgroundColor = "darkgray";
            favebutton.style.color = "yellow";
            isYellow = true;
        }
        
        //hide the text after 2 seconds
        setTimeout(function() {
        fclicked.textContent = "";
        }, 3000);
        
    });
    
    var cartbutton = document.getElementById('cart');
    var cclicked = document.getElementById('cartclicked');
    var isClicked = false;
    cartbutton.addEventListener("click", function() {
        if (isClicked) {
            cclicked.textContent = "Removed ingredients from shopping cart";
            cartbutton.style.backgroundColor = 'white';
            cartbutton.style.color = 'black';
            isClicked = false;
        }
        else {
            cclicked.textContent = "Added ingredients to shopping cart!";
            cartbutton.style.backgroundColor = 'darkgrey';
            cartbutton.style.color = 'white';
            isClicked = true;
        }
        
        //hide the text after 2 seconds
        setTimeout(function() {
        cclicked.textContent = "";
        }, 2000);
    });
    
});
                            


    