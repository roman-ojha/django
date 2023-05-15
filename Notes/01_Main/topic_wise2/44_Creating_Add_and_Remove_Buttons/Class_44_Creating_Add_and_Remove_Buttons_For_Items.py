"""

    => here we will add feature in 'index.html' which is if we will click on "Add To Cart" Button then it needs to change to increment and decrement item button 
            => function updateCart(cart) {
                for (var item in cart) {
                    document.getElementById('div' + item).innerHTML = "<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
                }
                localStorage.setItem('cart', JSON.stringify(cart));
                document.getElementById('cart').innerHTML = Object.keys(cart).length;
            }
            // If plus or minus button is clicked, change the cart as well as the display value
            $('.divpr').on("click", "button.minus", function() {
                a = this.id.slice(7, );
                // getting id of product 
                cart['pr' + a] = cart['pr' + a] - 1;
                // decrementing the product after clicking plus button
                cart['pr' + a] = Math.max(0, cart['pr' + a]);
                document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
                updateCart(cart);
                
            });
            $('.divpr').on("click", "button.plus", function() {
                a = this.id.slice(6, );
                cart['pr' + a] = cart['pr' + a] + 1;
                // incrementing the product after clicking plus button
                document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
                updateCart(cart);
            });
"""
