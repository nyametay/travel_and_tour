 // Theme toggle script
const themeToggle = document.getElementById('theme-toggle');
const sunIcon = document.getElementById('sun-icon');
const moonIcon = document.getElementById('moon-icon');

if (localStorage.getItem('theme') === 'dark') {
  document.documentElement.classList.add('dark');
  sunIcon.classList.remove('hidden');
} else {
  moonIcon.classList.remove('hidden');
}

themeToggle.addEventListener('click', () => {
  document.documentElement.classList.toggle('dark');
  if (document.documentElement.classList.contains('dark')) {
    localStorage.setItem('theme', 'dark');
    sunIcon.classList.remove('hidden');
    moonIcon.classList.add('hidden');
  } else {
    localStorage.setItem('theme', 'light');
    moonIcon.classList.remove('hidden');
    sunIcon.classList.add('hidden');
  }
});