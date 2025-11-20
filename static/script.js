// Optional: Add "loading..." text when user submits the form
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  const button = form.querySelector('button');
  const input = form.querySelector('input');

  form.addEventListener('submit', () => {
    if (input.value.trim() !== '') {
      button.disabled = true;
      button.textContent = '⏳ Loading...';
    }
  });

  // Optional: Clear error on input change
  input.addEventListener('input', () => {
    const errorMsg = document.querySelector('.error');
    if (errorMsg) {
      errorMsg.style.display = 'none';
    }
  });
});
