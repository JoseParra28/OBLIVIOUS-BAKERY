const pCart = document.querySelector('#p-cart');
const pTotal = document.querySelector('#p-total');

// add pie function
function addPie(pie){
    //  pie name info 
    pieId = '#pie-id' + pie;
    let name = document.querySelector(pieId).innerHTML;
    // pie price info + select specific item
    let radio = 'pie-rad' + pie;
    let pric = document.getElementsByName(radio);
    let size, price ;
    if (pric[0].checked){
    price = pric[0].value;
    size = 'M';
    }
    else {
        price = pric[1].value;
        size = 'L'
    }
    
    let  orders = JSON.parse(localStorage.getItem('orders'));
    let  total = localStorage.getItem('total');
    let cartSize = orders .length;
    // add and item in local storage

    orders[cartSize] = [name, size, price];
    localStorage.setItem('orders', JSON.stringify(orders));
   
    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    // updating order 
    const trolley = document.querySelector('#trolley');
    trolley.innerHTML = orders.length;

    pTotal.innerHTML = 'Total ' + total + ' £';
    pCart.innerHTML += '<li>' + name + ' ' + size + ' : ' + price + '</li>';
    
}

function shoppingCart() {
    let  orders = JSON.parse(localStorage.getItem('orders'));
    let  total = localStorage.getItem('total');
    let cartSize = orders .length;
    pCart.innerHTML = ''
    for (let i = 0; i < cartSize; i++ ){
        pCart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' : ' + orders[i][2] + '</li>';
    }
    pTotal.innerHTML = 'Total ' + total + ' £';
}
shoppingCart();
