let billName = document.querySelector('#ord-name')
let size = document.querySelector('#ord-size')
let price = document.querySelector('#ord-price')
let totalBill = document.querySelector('#total-bill')
let rm = document.querySelector('#rm')

function shoppingCartTotal() {
    let  orders = JSON.parse(localStorage.getItem('orders'));
    let  total = localStorage.getItem('total');
    let cartSize = orders .length;

    billName.innerHTML = '<h3>name</h3>';
    size.innerHTML = '<h3>size</h3>';
    price.innerHTML = '<h3>price</h3>';
    rm.innerHTML = '<h3>Remove</h3>';
    

    for (let i = 0; i < cartSize; i++ ){
        rm.innerHTML += '<h4><button class="btn-danger" onclick="removeItem(' + i + ')">X</button></h4>';
        billName.innerHTML += '<h4>' + orders[i][0] + '</h4>';
        size.innerHTML += '<h4>' + orders[i][1] + '</h4>';
        price.innerHTML += '<h4>' + orders[i][2] + '</h4>';
    }
    totalBill.innerHTML = 'Total ' + total + ' £';
}
shoppingCartTotal();

function removeItem(n){
    let  orders = JSON.parse(localStorage.getItem('orders'));
    let  total = localStorage.getItem('total');

    total = Number(total) - Number(orders[n][2]);
    orders.splice(n,1);

     // updating order 
     const trolley = document.querySelector('#trolley');
     trolley.innerHTML = orders.length;

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);

    shoppingCartTotal();
}

let note = document.querySelector('#message')


 function order(){
    let msg = note.value;
    let orders = localStorage.getItem('orders')


    let url = 'food/shopping-cart';
    let orderData = {};
    orderData['orders'] = orders;
    orderData['note'] = msg;
    $.ajax({
        urls:url,
        type: "POST",
        data: orderData,
        success: function(data){
            window.location.replace('/susscess.html');
            console.log("The data was sent")
        }
    })

 }