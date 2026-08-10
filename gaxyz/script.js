const menu = document.querySelector('.menu');
const links = document.querySelector('.nav-links');
menu?.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') === 'true';
  menu.setAttribute('aria-expanded', String(!open));
  links?.classList.toggle('open', !open);
});
links?.addEventListener('click', () => {
  menu?.setAttribute('aria-expanded', 'false');
  links.classList.remove('open');
});
