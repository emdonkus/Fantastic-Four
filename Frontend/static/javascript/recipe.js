/* edited 4/12/2024 Hallee Ray 
edited 4/16/2024 Hallee Ray*/

document.addEventListener('DOMContentLoaded', function() {

    var favebutton = document.getElementById('fave');
    var isfave = false; //need to get favorite status from DB -> should we change to button to read add/remove from favorites based on DB bool?                        
    favebutton.addEventListener("click", function() {
        if (isfave) {
            favebutton.style.backgroundColor = 'white';
            isfave = false;
        }
        else {
            favebutton.style.backgroundColor = "#f2dea7";
            isfave = true;
        }
        
    });
    
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
                            


    