document.addEventListener("DOMContentLoaded", () => {
  const menuBtn = document.getElementById('menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  // Open/close menu
  menuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });

  // Handle theme toggle (desktop + mobile)
  const themeToggles = [document.getElementById('theme-toggle'), document.getElementById('theme-toggle-mobile')];
  const sunIcons = [document.getElementById('sun-icon'), document.getElementById('sun-icon-mobile')];
  const moonIcons = [document.getElementById('moon-icon'), document.getElementById('moon-icon-mobile')];

  function updateIcons(isDark) {
    sunIcons.forEach(icon => icon.classList.toggle('hidden', !isDark));
    moonIcons.forEach(icon => icon.classList.toggle('hidden', isDark));
  }

  // On page load
  const isDark = localStorage.getItem('theme') === 'dark';
  if (isDark) {
    document.documentElement.classList.add('dark');
  }
  updateIcons(isDark);

  // Toggle logic
  themeToggles.forEach(btn => {
    if (btn) {
      btn.addEventListener('click', () => {
        document.documentElement.classList.toggle('dark');
        const nowDark = document.documentElement.classList.contains('dark');
        localStorage.setItem('theme', nowDark ? 'dark' : 'light');
        updateIcons(nowDark);
      });
    }
  });
});
