let billName = document.querySelector('#ord-name')
let size = document.querySelector('#ord-size')
let price = document.querySelector('#ord-price')
let totalBill = document.querySelector('#total-bill')
let orderBtn = document.querySelector('#remove-item-order')



function orderListF() {
    let  orders = JSON.parse(localStorage.getItem('orders'));
    let  total = localStorage.getItem('total');
    let cartSize = orders .length;

    billName.innerHTML = '<h3>name</h3>';
    size.innerHTML = '<h3>size</h3>';
    price.innerHTML = '<h3>price</h3>';
   
 

    for (let i = 0; i < cartSize; i++ ){
        orderBtn.innerHTML  += '<div> class="revome-btn onclick="removeItemOrder(' + i + ')">Remove</div>';
        billName.innerHTML += '<h4>'+ orders[i][0] +'</h4>'
        size.innerHTML += '<h4>'+ orders[i][1] +'</h4>'
        price.innerHTML += '<h4>'+ orders[i][2] +'</h4>'


        // pCart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' : ' + orders[i][2] + btn + '</li>';
    }
    totalBill.innerHTML = '<h3>order total</h3>' + total + ' £';
}
orderListF();