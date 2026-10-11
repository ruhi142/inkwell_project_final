/* ==========================================================================
   INKWELL BOOKS — chatbot.js
   Controls the floating widget shared across every page (included from base.html).
   Icon-only by default; click toggles the panel open/closed.

   Book suggestions now come from the REAL catalog (catalog_data.py) through
   the /category/chat-data/ endpoint. Whatever category the user types, the bot
   shows that category's highest-rated books.
   ========================================================================== */

(function () {
  const widget = document.getElementById('chatWidget');
  if (!widget) return;

  const fab = document.getElementById('chatFab');
  const closeBtn = document.getElementById('chatPanelClose');
  const body = document.getElementById('chatPanelBody');
  const form = document.getElementById('chatPanelForm');
  const input = document.getElementById('chatPanelInput');

  function openChat() {
    widget.classList.add('is-open');
    input && input.focus();
  }
  function closeChat() {
    widget.classList.remove('is-open');
  }
  function toggleChat() {
    widget.classList.contains('is-open') ? closeChat() : openChat();
  }

  fab.addEventListener('click', toggleChat);
  closeBtn && closeBtn.addEventListener('click', (e) => { e.stopPropagation(); closeChat(); });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeChat();
  });

  // --------------------------------------------------------------------
  // Catalog data (loaded once from Django: every category + every book)
  // --------------------------------------------------------------------
  let BOOKS = [];
  let CATS = [];
  fetch('/category/chat-data/')
    .then(r => r.json())
    .then(d => { BOOKS = d.books; CATS = d.cats; })
    .catch(() => {});

  // Words that carry no category meaning
  const STOP = new Set(['the','and','for','you','can','are','any','some','good','best','great',
    'book','books','suggest','recommend','show','find','looking','want','read','reading','need',
    'please','under','below','within','with','about','give','something','novel','novels','like',
    'help','have','what','which','new','top','popular','cheap','less','than','rupees','price',
    'contact','support','human','agent','complain','team']);

  // User word -> word used in your category names (add more any time)
  const SYNONYMS = { kids:'children', kid:'children', child:'children', poem:'poetry', poems:'poetry',
    comic:'graphic', comics:'graphic', manga:'graphic', scifi:'sci', detective:'mystery',
    whodunit:'mystery', motivational:'self', money:'finance', stocks:'finance',
    startup:'entrepreneurship', startups:'entrepreneurship' };

  // Compare words by their first 5 letters, so romantic/romance, history/historical match
  function keysOf(text) {
    return (text.toLowerCase().match(/[a-z]{3,}/g) || [])
      .filter(w => !STOP.has(w))
      .map(w => SYNONYMS[w] || w)
      .map(w => (w.length >= 5 ? w.slice(0, 5) : w));
  }

  function findPool(keys) {
    if (!keys.length) return null;
    let best = 0, hits = [];
    CATS.forEach(c => {
      const ck = keysOf(c.title);
      const score = keys.filter(k => ck.includes(k)).length;
      if (score > best) { best = score; hits = [c]; }
      else if (score === best && score > 0) hits.push(c);
    });
    if (best > 0) {
      const slugs = new Set(hits.map(c => c.slug));
      return {
        label: hits.map(c => c.title).join(' / '),
        books: BOOKS.filter(b => slugs.has(b.slug) || slugs.has(b.parent)),
      };
    }
    // No category matched: try book titles / author names
    const textKeys = b => keysOf(b.title + ' ' + b.author);
    let byText = BOOKS.filter(b => keys.every(k => textKeys(b).includes(k)));   // all words match (e.g. full author name)
    if (!byText.length) byText = BOOKS.filter(b => keys.some(k => textKeys(b).includes(k)));
    return byText.length ? { label: 'your search', books: byText } : null;
  }

  const BOOK_URL = (id) => `/category/book/${id}/`;

  function escapeHtml(str) {
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }

  function addMessage(content, who, isHtml) {
    const div = document.createElement('div');
    div.className = 'chat-msg ' + who;
    if (isHtml) {
      div.innerHTML = content;
    } else {
      div.textContent = content;
    }
    body.appendChild(div);
    body.scrollTop = body.scrollHeight;
    return div;
  }

  function showTyping() {
    const div = addMessage('<span class="chat-typing"><span></span><span></span><span></span></span>', 'bot', true);
    div.classList.add('is-typing');
    return div;
  }

  function bookListHtml(books, intro) {
    const items = books.slice(0, 4).map(b => (
      `<a class="chat-book" href="${BOOK_URL(b.id)}">` +
        `<span class="chat-book-title">${escapeHtml(b.title)}</span>` +
        `<span class="chat-book-meta">${escapeHtml(b.author)} · ₹${b.price} · ★ ${b.rating}</span>` +
      `</a>`
    )).join('');
    return `<div class="chat-books-intro">${escapeHtml(intro)}</div><div class="chat-books">${items}</div>`;
  }

  function extractBudget(text) {
    const m = text.match(/(?:under|below|less than|within)\s*₹?\s*(\d{2,5})|₹\s*(\d{2,5})|(\d{2,5})\s*(?:rs|rupees|₹)/i);
    if (!m) return null;
    return parseInt(m[1] || m[2] || m[3], 10);
  }

  // Core intent → reply logic, keyword-driven against what the user typed.
  function getReply(rawText) {
    const text = rawText.toLowerCase().trim();

    // Greetings
    if (/^(hi|hello|hey|yo|good (morning|afternoon|evening))\b/.test(text)) {
      return { html: false, text: "Hi there! 👋 Tell me a genre (like romance, thriller, self-help or academic) or a budget, and I'll pull up a few top-rated titles for you." };
    }

    // Thanks / bye
    if (/thank|thanks|thank you/.test(text)) {
      return { html: false, text: "You're welcome! Happy reading 📚 — let me know if you'd like more suggestions." };
    }
    if (/\b(bye|goodbye|see you)\b/.test(text)) {
      return { html: false, text: "Take care! Come back anytime you're looking for your next read. 👋" };
    }

    // Order tracking / delivery status
    if (/\border|track(ing)?|delivery|dispatch|shipp?ing|where.?s my/.test(text)) {
      return {
        html: true,
        text: `You can check your order status on the <a href="/orders/track/">Track Order</a> page, or see everything you've bought under <a href="/orders/my-orders/">My Orders</a>. Our helpline is <a href="tel:+911234567890">+91 12345 67890</a> if you need a hand.`,
      };
    }

    // Offers / discounts / coupon codes
    if (/discount|offer|coupon|code|deal/.test(text)) {
      return {
        html: true,
        text: `Here are our live offers: <strong>READ25</strong> for flat 25% off Fiction, an extra 10% off on prepaid orders, free delivery above ₹499, and buy-2-get-1-free on Academic books. Check the full <a href="/category/sale/">Sale shelf</a> for up to 70% off.`,
      };
    }

    // Book suggestions (checked before the generic help intent below)
    if (!BOOKS.length) {
      return { html: false, text: "Give me a second, I'm still loading the shelves. Please try again." };
    }

    const budget = extractBudget(text);
    const keys = keysOf(text);
    const found = findPool(keys);   // null when nothing in the catalog matches

    const isHelp = /\bhelp\b|contact|human|agent|support|complain/.test(text);
    const wantsSuggestion = /suggest|recommend|\bbooks?\b|\bread\b|looking for|show me|find me/.test(text)
      || found !== null || budget !== null || (keys.length > 0 && !isHelp);

    if (wantsSuggestion) {
      // They named something, but it isn't in our collection: say so, don't show random books
      if (!found && keys.length && budget === null) {
        const names = CATS.filter(c => !c.parent).map(c => c.title).join(', ');
        return { html: false, text: `I couldn't find that in our collection yet. Try one of: ${names}.` };
      }

      let pool = found ? found.books.slice() : BOOKS.slice();
      if (budget !== null) pool = pool.filter(b => b.price <= budget);
      pool.sort((a, b) => b.rating - a.rating || Math.random() - 0.5);  // best rated first

      if (pool.length === 0) {
        return { html: false, text: "I couldn't find a match for that, so try a different category or a higher budget." };
      }
      const intro = found
        ? `Top-rated picks from ${found.label}${budget !== null ? ' under ₹' + budget : ''}:`
        : budget !== null ? `Top-rated titles under ₹${budget}:` : "Our top-rated titles:";
      return { html: true, text: bookListHtml(pool, intro) };
    }

    // Help / human / contact (checked after suggestions so "self help" etc.
    // above still resolve to book picks)
    if (isHelp) {
      return {
        html: true,
        text: `I can help you find a book, check an order, or point you to an offer. For anything else, our team is reachable on the <a href="/contact/">Contact page</a> or at <a href="tel:+911234567890">+91 12345 67890</a>.`,
      };
    }

    // Fallback
    return {
      html: true,
      text: `I didn't quite catch that. Try asking things like <em>"suggest a romantic book"</em>, <em>"books under ₹300"</em>, or <em>"where's my order?"</em> — or browse a <a href="/category/fiction/">category</a> above.`,
    };
  }

  // Quick-suggestion chips inside the welcome message
  body && body.addEventListener('click', (e) => {
    const chip = e.target.closest('[data-suggest]');
    if (chip) {
      handleUserMessage(chip.getAttribute('data-suggest'));
      return;
    }
  });

  function handleUserMessage(text) {
    if (!text.trim()) return;
    addMessage(text, 'user');
    input.value = '';

    const typingEl = showTyping();

    setTimeout(() => {
      const reply = getReply(text);
      typingEl.remove();
      addMessage(reply.text, 'bot', !!reply.html);
    }, 450);
  }

  form && form.addEventListener('submit', (e) => {
    e.preventDefault();
    handleUserMessage(input.value);
  });
})();