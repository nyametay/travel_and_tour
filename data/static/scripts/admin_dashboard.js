// Mobile menu toggle
const menuToggle = document.getElementById('menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');
menuToggle.addEventListener('click', () => {
mobileMenu.classList.toggle('hidden');
});

// Theme toggle logic
const themeButtons = [document.getElementById('theme-toggle'), document.getElementById('theme-toggle-mobile')];
const sunIcons = [document.getElementById('sun-icon'), document.getElementById('sun-icon-mobile')];
const moonIcons = [document.getElementById('moon-icon'), document.getElementById('moon-icon-mobile')];

function updateThemeIcons(isDark) {
sunIcons.forEach(icon => icon.classList.toggle('hidden', !isDark));
moonIcons.forEach(icon => icon.classList.toggle('hidden', isDark));
}

function setTheme(dark) {
document.documentElement.classList.toggle('dark', dark);
localStorage.setItem('theme', dark ? 'dark' : 'light');
updateThemeIcons(dark);
}

// Initialize theme
const isDark = localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches);
setTheme(isDark);

themeButtons.forEach(button => {
if (button) {
  button.addEventListener('click', () => setTheme(!document.documentElement.classList.contains('dark')));
}
});

// ===== Edit Modal =====
const editModal = document.getElementById('editModal');
const editForm = document.getElementById('editForm');
const cancelEdit = document.getElementById('cancelEdit');

document.querySelectorAll('.edit-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    editModal.classList.remove('hidden');
    editModal.classList.add('flex');

    document.getElementById('edit-id').value = btn.dataset.id;
    document.getElementById('edit-name').value = btn.dataset.name;
    document.getElementById('edit-description').value = btn.dataset.description;

    // Show image preview
    const preview = document.getElementById('edit-preview');
    preview.src = btn.dataset.image || '';
    preview.style.display = btn.dataset.image ? 'block' : 'none';

    editForm.action = `/admin/edit_destination/${btn.dataset.id}`;
  });
});

cancelEdit.addEventListener('click', () => {
  editModal.classList.add('hidden');
  editModal.classList.remove('flex');
});
