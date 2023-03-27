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

    pCart.innerHTML += '<li>' + name + ' ' + size + ' : ' + price + '</li>';
    
}
