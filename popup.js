var btnAbrirpopup = document.getElementById('btn-abrir-popup'),
    overlay =document.getElementById('overlay'),
    poup = document.getElementById('popup'),
    btnCerrarpopup = document.getElementById('btn-cerra-popup');

btnAbrirpopup .addEventListener('click', function(){
        overlay.classList.add('active'),
        popup.classList.remove('active');
    });
btnCerrarpopup.addEventListener('click',function(){
    overlay.classList.remove('active');
    popup.classList.remove('active');
});