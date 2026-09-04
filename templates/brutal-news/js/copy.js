/* retemplate — copy.js (docs pages only)
 *
 * <div class="snippet"><button class="copy-btn" type="button">Copy</button><pre><code>…</code></pre></div>
 * copies the <code>'s text. A button may instead name its source with
 * data-copy="#some-id".
 */
(function () {
  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('.copy-btn') : null;
    if (!b) return;
    var source = b.dataset.copy ? document.querySelector(b.dataset.copy) : b.parentElement.querySelector('code, pre');
    if (!source) return;
    var text = source.textContent.replace(/\n$/, '');
    var done = function () {
      var old = b.textContent;
      b.textContent = 'Copied';
      setTimeout(function () { b.textContent = old; }, 1200);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, done);
    } else {
      var range = document.createRange();
      range.selectNodeContents(source);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      try { document.execCommand('copy'); } catch (err) { /* nothing more to try */ }
      done();
    }
  });
})();
