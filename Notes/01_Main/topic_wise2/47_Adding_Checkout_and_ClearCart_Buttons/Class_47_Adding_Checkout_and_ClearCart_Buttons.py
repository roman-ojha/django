"""
    => here in 'index.html' we had added script which will add button in cart which are 'Checkout' and 'Chear Cart ' button 
            -> function updatePopover(cart) {
                    console.log('We are inside updatePopover');
                    var popStr = "";
                    popStr = popStr + "<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
                    var i = 1;
                    for (var item in cart) {
                        popStr = popStr + "<b>" + i + "</b>. ";
                        popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0, 19) + "... Qty: " + cart[item] + '<br>';
                        i = i + 1;
                    }
                    popStr = popStr + "</div> <a href='/shop/checkout'><button class='btn btn-primary' id ='checkout'>Checkout</button></a> <button class='btn btn-primary' onclick='clearCart()' id ='clearCart'>Clear Cart</button>     "
                    console.log(popStr);
                    document.getElementById('popcart').setAttribute('data-content', popStr);
                    $('#popcart').popover('show');
                }
                function clearCart() {
                    cart = JSON.parse(localStorage.getItem('cart'));
                    for (var item in cart) {
                        document.getElementById('div' + item).innerHTML = '<button id="' + item + '" class="btn btn-primary cart">Add To Cart</button>'
                    }
                    localStorage.clear();
                    cart = {};
                    updateCart(cart);
                }
                $('.divpr').on("click", "button.minus", function() {
                    a = this.id.slice(7, );
                    cart['pr' + a] = cart['pr' + a] - 1;
                    cart['pr' + a] = Math.max(0, cart['pr' + a]);
                    document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
                    updateCart(cart);
                });
                $('.divpr').on("click", "button.plus", function() {
                    a = this.id.slice(6, );
                    cart['pr' + a] = cart['pr' + a] + 1;
                    document.getElementById('valpr' + a).innerHTML = cart['pr' + a];
                    updateCart(cart);
                });
"""
