/* retemplate copy.js (docs pages only). A .copy-btn copies the <code> or
 * <pre> beside it, or the element named by its data-copy selector. */
(function () {
  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('.copy-btn') : null;
    if (!b) return;
    var source = b.dataset.copy ? document.querySelector(b.dataset.copy) : b.parentElement.querySelector('code, pre');
    if (!source) return;
    var text = source.textContent.replace(/\n$/, '');
    var old = b.textContent;
    var done = function () { b.textContent = 'Copied'; setTimeout(function () { b.textContent = old; }, 1200); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, done);
    } else {
      var range = document.createRange();
      range.selectNodeContents(source);
      var sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range);
      try { document.execCommand('copy'); } catch (err) { /* nothing more to try */ }
      done();
    }
  });
})();
