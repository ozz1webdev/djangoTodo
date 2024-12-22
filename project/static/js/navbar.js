const mobileMenu = document.getElementById('mobile-menu');
const navList = document.querySelector('.overlay');

mobileMenu.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    navList.classList.toggle('active');
});