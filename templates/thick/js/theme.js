/* retemplate — theme.js
 *
 * Loaded synchronously in <head>, before the stylesheets, so the visitor's
 * stored scheme is applied before first paint. Retoken's model exactly:
 * localStorage['retoken-scheme'] is 'light' or 'dark', or absent for
 * "follow the OS". Storage access is wrapped: file:// and private windows
 * may throw, and then the page simply follows the OS.
 *
 * It also mirrors the *effective* scheme to <html data-scheme="light|dark">
 * so CSS can swap things light-dark() cannot (images, ornaments, content).
 */
(function () {
  var KEY = 'retoken-scheme';
  var ORDER = { auto: 'light', light: 'dark', dark: 'auto' };
  var root = document.documentElement;
  var mq = window.matchMedia('(prefers-color-scheme: dark)');
  var choice = 'auto';
  try {
    var v = localStorage.getItem(KEY);
    if (v === 'light' || v === 'dark') choice = v;
  } catch (e) { /* no storage: follow the OS */ }

  function apply(c) {
    choice = c;
    root.style.colorScheme = c === 'auto' ? '' : c;
    root.dataset.scheme = c === 'auto' ? (mq.matches ? 'dark' : 'light') : c;
    var buttons = document.querySelectorAll('.scheme-toggle');
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].dataset.scheme = c;
      buttons[i].setAttribute('aria-label', 'Theme: ' + c);
      buttons[i].title = 'Theme: ' + c + ' (click to change)';
    }
  }

  apply(choice);
  mq.addEventListener('change', function () { if (choice === 'auto') apply('auto'); });
  document.addEventListener('DOMContentLoaded', function () { apply(choice); });
  document.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('.scheme-toggle') : null;
    if (!b) return;
    var next = ORDER[choice] || 'auto';
    try {
      if (next === 'auto') localStorage.removeItem(KEY); else localStorage.setItem(KEY, next);
    } catch (err) { /* keep the choice for this page view only */ }
    apply(next);
  });
})();
