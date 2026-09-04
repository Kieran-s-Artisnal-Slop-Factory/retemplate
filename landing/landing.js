/* The landing page's search and filters. Search matches the title; tags AND
 * together; both AND with each other. Nothing here touches the templates. */
(function () {
  var search = document.getElementById('search');
  var empty = document.getElementById('empty');
  var count = document.getElementById('count');
  var chips = Array.prototype.slice.call(document.querySelectorAll('.chip[data-tag]'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('.template-card'));

  function activeTags() {
    return chips.filter(function (c) { return c.getAttribute('aria-pressed') === 'true'; })
                .map(function (c) { return c.dataset.tag; });
  }

  function update() {
    var q = search.value.trim().toLowerCase();
    var tags = activeTags();
    var shown = 0;
    cards.forEach(function (card) {
      var title = (card.dataset.title || '').toLowerCase();
      var has = (card.dataset.tags || '').split(/\s+/);
      var ok = (!q || title.indexOf(q) !== -1) &&
               tags.every(function (t) { return has.indexOf(t) !== -1; });
      card.hidden = !ok;
      if (ok) shown++;
    });
    empty.hidden = shown > 0;
    count.textContent = shown + ' of ' + cards.length;
  }

  function clear() {
    search.value = '';
    chips.forEach(function (c) { c.setAttribute('aria-pressed', 'false'); });
    update();
  }

  search.addEventListener('input', update);
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') === 'true' ? 'false' : 'true');
      update();
    });
  });
  document.getElementById('clear').addEventListener('click', clear);
  document.getElementById('clear-2').addEventListener('click', clear);
  update();
})();
