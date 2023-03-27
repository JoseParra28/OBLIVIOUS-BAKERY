const pCart = document.querySelector('#p-cart');
const pTotal = document.querySelector('#p-total');

// add pie function
function addPie(pie){
    // get a pie 
    pCart.innerHTML += '<li>' + pie + '</li>';
}
