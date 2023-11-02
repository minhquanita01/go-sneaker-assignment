document.addEventListener('DOMContentLoaded', function () 
{
    var addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    
    addToCartButtons.forEach((button) =>
    {
        button.addEventListener('click', function() 
        {
            var shoeId = this.getAttribute('data-shoe-id');

            this.style.display = 'none';
            this.nextElementSibling.style.display = 'flex';
            
            fetch('/go_shoes/add_to_cart/', 
            {
                method: 'POST',
                body: JSON.stringify({ 'shoe_id': shoeId }),
                headers: 
                {
                    'Content-Type': 'application/json',
                }
            })
            .then((response) => response.json())
            .then((data) => 
                {
                    addHTMLCodeIntoBlock(".cart.column-body", data.html);
                    updateToTalCostDisplay(data.total_cost);
                }
            );
        });
    });
});

function addHTMLCodeIntoBlock(selector, html)
{
    document.querySelector(selector).innerHTML += html;
}

function updateToTalCostDisplay(total_cost) 
{
    document.querySelector(".cart .total-cost").textContent = `$${total_cost.toFixed(2)}`;
}

//Increase item quantity
document.addEventListener('DOMContentLoaded', function () 
{
    document.body.addEventListener("click", (event) =>
    {
        var button = event.target.closest(".item-inc-quantity")
        if (button)
        {
            var shoeId = button.parentElement.parentElement.getAttribute("data-shoe-id");

            fetch('/go_shoes/inc_quantity/', 
            {
                method: 'POST',
                body: JSON.stringify({ 'shoe_id': shoeId }),
                headers: 
                {
                    'Content-Type': 'application/json',
                }
            })
            .then((response) => response.json())
            .then((data) => 
                {
                    updateToTalCostDisplay(data.total_cost);
                    button.previousElementSibling.textContent = data.item_quantity;
                }
            );
        }
    });
});

// Remove from cart
document.addEventListener('DOMContentLoaded', function () 
{
    document.body.addEventListener('click', (event) =>
    {
        var button = event.target.closest('.cart-item-remove');
        if (button) {
            var shoeId = button.parentElement.getAttribute("data-shoe-id");

            fetch('/go_shoes/remove_cart_item/', 
            {
                method: 'POST',
                body: JSON.stringify({ 'shoe_id': shoeId }),
                headers: 
                {
                    'Content-Type': 'application/json',
                }
            })
            .then((response) => response.json())
            .then((data) => 
                {
                    updateToTalCostDisplay(data.total_cost);
                }
            );
            var cartItemContainer = button.closest('.cart-item-container');
            if (cartItemContainer) 
            {
                cartItemContainer.remove();
            }

            var addedCheckIcon = document.querySelector(`.added-to-cart-container[data-shoe-id="${shoeId}"]`);
            addedCheckIcon.style.display = "none";
            addedCheckIcon.previousElementSibling.style.display = "block";
        }
    });
});