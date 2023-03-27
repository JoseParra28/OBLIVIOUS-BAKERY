let billName = document.querySelector('#ord-name')
let size = document.querySelector('#ord-size')
let price = document.querySelector('#ord-price')
let totalBill = document.querySelector('#total-bill')



function orderListF() {
    let  orders = JSON.parse(localStorage.getItem('orders'));
    let  total = localStorage.getItem('total');
    let cartSize = orders .length;

    billName.innerHTML = 'Name';
    size.innerHTML = 'Size';
    price.innerHTML = 'Price';
   
 

    for (let i = 0; i < cartSize; i++ ){
        // btn = '<button class="revome-btn onclick="removeItem(' + i + ')">Remove</button>';
        billName.innerHTML += '<h4>'+ orders[i][0] +'</h4>'
        size.innerHTML += '<h4>'+ orders[i][1] +'</h4>'
        price.innerHTML += '<h4>'+ orders[i][2] +'</h4>'


        // pCart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][1] + ' : ' + orders[i][2] + btn + '</li>';
    }
    totalBill.innerHTML = 'Total ' + total + ' £';
}
orderListF();