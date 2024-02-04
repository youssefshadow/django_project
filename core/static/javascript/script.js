document.getElementById('burger-menu').addEventListener('click', function () {
    document.getElementById('burger-menu-content').classList.toggle('hidden');
});

document.getElementById('close-burger-menu').addEventListener('click', function () {
    document.getElementById('burger-menu-content').classList.add('hidden');
});
console.log('hi world');