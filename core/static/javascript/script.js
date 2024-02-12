console.log('Le fichier JavaScript est chargé!');
 
let mobileMenuButton = document.getElementById('mobile-menu-button');
let mobileMenu = document.getElementById('mobile-menu');

mobileMenuButton.addEventListener('click', function () {
    mobileMenu.classList.toggle('hidden');
    mobileMenuButton.classList.toggle('menu-closed');
});


