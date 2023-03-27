const orders = JSON.parse(localStorage.getItem('orders'));
const total = localStorage.getItem('total');

if (orders == null || orders === undefined){
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if (total == null || total === undefined){
    localStorage.setItem('total', 0);
    total = localStorage.getItem('orders');
}

