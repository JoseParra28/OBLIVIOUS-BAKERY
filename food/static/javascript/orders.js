const pCart = document.querySelector('#p-cart');
const pTotal = document.querySelector('#p-total');

// add pie function
function addPie(pie){
    // get a pie 
    pieId = '#pie-id' + pie;
    const name = document.querySelector(pieId).innerHTML;
    pCart.innerHTML += '<li>' + name + '</li>';
}
