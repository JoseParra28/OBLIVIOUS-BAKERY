const navToggler = document.querySelector('.nav-toggler');
const navMenu = document.querySelector('.site-navbar ul');
const navLinks = document.querySelectorAll('.site-navbar a');


allEventListners();


function allEventListners() {
  navToggler.addEventListener('click', togglerClick);
  navLinks.forEach( elem => elem.addEventListener('click', navLinkClick));
}


function togglerClick() {
  navToggler.classList.toggle('toggler-open');
  navMenu.classList.toggle('open');
}


function navLinkClick() {
  if(navMenu.classList.contains('open')) {
    navToggler.click();
  }
}

let orders = JSON.parse(localStorage.getItem('orders'));
let total = localStorage.getItem('total');

if (orders == null || orders === Number){
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if (total == null || total === Number){
    localStorage.setItem('total');
    total = localStorage.getItem('orders');
}

let trolley = document.querySelector('#trolley');
trolley.innerHTML = orders.length;
