"""
    => here we are showing cart item that user had added:
        -> $('#popcart').popover();
            updatePopover(cart);
            function updatePopover(cart)
            {
                console.log('We are inside updatePopover');
                var popStr = "";
                popStr = popStr + "<h5> Cart for your items in my shopping cart </h5><div class='mx-2 my-2'>";
                var i = 1;
                for (var item in cart){
                    popStr = popStr + "<b>" + i + "</b>. ";
                    popStr = popStr + document.getElementById('name' + item).innerHTML.slice(0, 19) + "... Qty: " + cart[item] + '<br>';
                    i = i+1;
                }
                popStr = popStr + "</div>" 
                console.log(popStr);
                document.getElementById('popcart').setAttribute('data-content', popStr);
                $('#popcart').popover('show');
            }
"""
