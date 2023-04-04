const hours = 24;
const now = new Date().GetTime();
const stepTime = localStorage.getItem('stepTime');

if (stepTime == null){
    localStorage.getItem('StepTime', now);
}
else {
    if (now - stepTime > hours*60*60*1000){
        localStorage.clear();
        localStorage.setItem('stepTime', now);
    }
}

let orders = JSON.parse(localStorage.getItem('orders'));
let total = localStorage.getItem('total');

if (orders == null || orders === undefined){
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if (total == null || total === undefined){
    localStorage.setItem('total', 0);
    total = localStorage.getItem('orders');
}

let trolley = document.querySelector('#trolley');
trolley.innerHTML = orders.length;




