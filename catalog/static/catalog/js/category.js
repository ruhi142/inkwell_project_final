/* ==========================================================================
   INKWELL BOOKS — category.js
   Sort dropdown reorders the grid; a compact "Show" dropdown (All / New / Pre-Loved)
   filters instantly with no reload; Add to Cart and the wishlist
   heart are wired to the shared InkwellStore (localStorage) engine.
   ========================================================================== */

(function () {
  const grid = document.getElementById('catBookGrid');
  const sortSelect = document.getElementById('catSort');
    const emptyMsg = document.getElementById('catEmptyMsg');
  if (!grid) return;

  const cards = Array.from(grid.children);

  function bookDataFromCard(card) {
    return {
      id: card.dataset.id,
      title: card.dataset.title,
      author: card.dataset.author,
      price: Number(card.dataset.price),
      old_price: Number(card.dataset.oldPrice),
      img: card.dataset.img,
    };
  }

  /* ---------- SORT ---------- */
  if (sortSelect) {
    sortSelect.addEventListener('change', () => {
      const mode = sortSelect.value;
      const sorted = [...cards].sort((a, b) => {
        if (mode === 'price-low') return a.dataset.price - b.dataset.price;
        if (mode === 'price-high') return b.dataset.price - a.dataset.price;
        if (mode === 'discount') return b.dataset.discount - a.dataset.discount;
        return a.dataset.order - b.dataset.order; // "popular" = original order
      });
      sorted.forEach((card) => grid.appendChild(card));
    });
  }

  /* ---------- SHOW: All / New / Pre-Loved ----------
     A small dropdown beside "Sort by". Options with no books on this page
     are removed, and the whole dropdown is hidden when every book on the
     page has the same condition (e.g. the Pre-Loved page itself). */
  const showSelect = document.getElementById('catShow');
  const showWrap = document.getElementById('catShowWrap');
  const countEl = document.getElementById('catResultCount');

  function applyShow() {
    const mode = showSelect ? showSelect.value : 'all';
    let visible = 0;
    cards.forEach((card) => {
      const show = mode === 'all' || card.dataset.condition === mode;
      card.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    if (emptyMsg) emptyMsg.style.display = (visible === 0 && cards.length) ? 'block' : 'none';
    if (countEl) countEl.textContent = visible;
    try {
      history.replaceState(null, '', mode === 'all' ? location.pathname : '?show=' + mode);
    } catch (e) { /* ignore */ }
  }

  if (showSelect) {
    const present = new Set(cards.map(c => c.dataset.condition));
    Array.from(showSelect.options).forEach((opt) => {
      if (opt.value !== 'all' && !present.has(opt.value)) opt.remove();
    });
    if (present.size < 2 && showWrap) showWrap.hidden = true;   // nothing to choose between
    const wanted = new URLSearchParams(location.search).get('show');
    if (wanted && Array.from(showSelect.options).some(o => o.value === wanted)) showSelect.value = wanted;
    showSelect.addEventListener('change', applyShow);
    applyShow();
  }

  /* ---------- ADD TO CART ---------- */
  cards.forEach((card) => {
    const addBtn = card.querySelector('.btn-add-cart');
    addBtn && addBtn.addEventListener('click', () => {
      if (!window.InkwellStore) return;
      InkwellStore.addToCart(bookDataFromCard(card));
      const original = addBtn.textContent;
      addBtn.textContent = 'Added ✓';
      addBtn.classList.add('is-added');
      setTimeout(() => {
        addBtn.textContent = original;
        addBtn.classList.remove('is-added');
      }, 1200);
    });
  });

  /* ---------- WISHLIST HEART ---------- */
  cards.forEach((card) => {
    const wishBtn = card.querySelector('.cat-wishlist-btn');
    if (!wishBtn || !window.InkwellStore) return;

    const item = bookDataFromCard(card);
    if (InkwellStore.isInWishlist(item.id)) {
      wishBtn.classList.add('is-saved');
    }

    wishBtn.addEventListener('click', () => {
      const nowSaved = InkwellStore.toggleWishlist(item);
      wishBtn.classList.toggle('is-saved', nowSaved);
    });
  });
})();
