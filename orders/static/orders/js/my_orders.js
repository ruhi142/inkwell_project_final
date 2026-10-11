(function () {
  document.querySelectorAll('.ord-invoice-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const original = btn.textContent;
      btn.textContent = 'Preparing…';
      setTimeout(() => { btn.textContent = original; }, 900);
    });
  });

  // ---- star ratings ----
  function getCookie(name) {
    const m = document.cookie.match('(?:^|; )' + name + '=([^;]*)');
    return m ? decodeURIComponent(m[1]) : '';
  }

  function paint(group, value) {
    group.querySelectorAll('.ord-star').forEach((star) => {
      star.classList.toggle('is-on', Number(star.dataset.value) <= value);
    });
  }

  document.querySelectorAll('.ord-stars').forEach((group) => {
    let current = Number(group.dataset.rating) || 0;
    paint(group, current);

    group.querySelectorAll('.ord-star').forEach((star) => {
      star.addEventListener('mouseenter', () => paint(group, Number(star.dataset.value)));
      star.addEventListener('click', () => {
        const value = Number(star.dataset.value);
        const previous = current;
        current = value;
        paint(group, current);
        fetch(group.dataset.url, {
          method: 'POST',
          headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: 'rating=' + value,
          credentials: 'same-origin',
        })
          .then((r) => { if (!r.ok) throw new Error(); })
          .catch(() => { current = previous; paint(group, current); });
      });
    });
    group.addEventListener('mouseleave', () => paint(group, current));
  });
})();