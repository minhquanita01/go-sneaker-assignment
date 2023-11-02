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

document.addEventListener('DOMContentLoaded', function() 
{
    var incQuantityButtons = document.querySelectorAll('.item-inc-quantity');
    incQuantityButtons.forEach(function(button) 
    {
        button.addEventListener('click', function() 
        {
            var itemQuantity = this.previousElementSibling.textContent;
            var itemPrice = this.parentElement.parentElement.previousElementSibling.textContent.slice(1);

            fetch('/go_shoes/inc-quantity/', 
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