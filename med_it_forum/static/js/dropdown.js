const dropdown = document.querySelector('.dropdown');
const dropdownToggle = dropdown.querySelector('button');
const dropdownMenu = dropdown.querySelector('.dropdown-menu');

dropdownToggle.addEventListener('click', function() {
  dropdownMenu.classList.toggle('show');
  dropdownToggle.setAttribute('aria-expanded', dropdownMenu.classList.contains('show'));
});

document.addEventListener('click', function(event) {
  if (!dropdown.contains(event.target)) {
    dropdownMenu.classList.remove('show');
    dropdownToggle.setAttribute('aria-expanded', 'false');
  }
});