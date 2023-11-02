document.addEventListener('DOMContentLoaded', function() 
{
    var addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    
    addToCartButtons.forEach(function(button) 
    {
        button.addEventListener('click', function() 
        {
            var shoeId = this.getAttribute('data-shoe-id');

            this.style.display = 'none';
            this.nextElementSibling.style.display = 'flex';
            
            fetch('/go_shoes/add-to-cart/', 
            {
                method: 'POST',
                body: JSON.stringify({ 'shoe_id': shoeId }),
                headers: 
                {
                    'Content-Type': 'application/json',
                }
            })
            .then((response) => response.json())
            .then((data) => updateCartDisplay(data));
        });
    });
});

function updateCartDisplay(data) 
{
    document.querySelector('.cart.column-body').innerHTML += data.html;

    document.querySelector(".cart .total-cost").textContent = `$${data.total_cost}`;
}

document.addEventListener('DOMContentLoaded', function() 
{
    var incQuantityButtons = document.querySelectorAll('.item-inc-quantity');
    incQuantityButtons.forEach(function(button) 
    {
        button.addEventListener('click', function() 
        {
            var itemQuantity;
        });
    });
});