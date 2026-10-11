/* Inkwell Books — apply.js: client-side checks + double-submit guard */
(function () {
  const form = document.getElementById('applyForm');
  if (!form) return;
  const btn = document.getElementById('applySubmit');
  const file = form.querySelector('input[type=file]');
  const MAX = 5 * 1024 * 1024;
  const OK = ['pdf', 'doc', 'docx'];

  function showError(input, msg) {
    const wrap = input.closest('.ap-field');
    wrap.classList.add('has-error');
    let p = wrap.querySelector('.ap-err.js');
    if (!p) { p = document.createElement('p'); p.className = 'ap-err js'; wrap.appendChild(p); }
    p.textContent = msg;
  }
  function clearError(input) {
    const wrap = input.closest('.ap-field');
    wrap.classList.remove('has-error');
    const p = wrap.querySelector('.ap-err.js');
    if (p) p.remove();
  }

  file && file.addEventListener('change', () => {
    clearError(file);
    const f = file.files[0];
    if (!f) return;
    const ext = f.name.split('.').pop().toLowerCase();
    if (!OK.includes(ext)) { showError(file, 'Please upload a PDF, DOC or DOCX file.'); file.value = ''; }
    else if (f.size > MAX) { showError(file, 'File is too large — max 5 MB.'); file.value = ''; }
  });

  form.addEventListener('submit', (e) => {
    let firstBad = null;
    form.querySelectorAll('[required]').forEach((el) => {
      clearError(el);
      if (!el.value.trim()) {
        showError(el, 'This field is required.');
        firstBad = firstBad || el;
      } else if (el.type === 'email' && !el.checkValidity()) {
        showError(el, 'Enter a valid email address.');
        firstBad = firstBad || el;
      }
    });
    if (firstBad) { e.preventDefault(); firstBad.focus(); return; }
    btn.disabled = true;
    btn.textContent = 'Submitting…';
  });
})();
