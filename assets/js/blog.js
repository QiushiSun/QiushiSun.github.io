(function () {
  'use strict';

  var STORAGE_KEY = 'qs-blog-lang';

  function getStoredLang() {
    try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
  }

  function storeLang(lang) {
    try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) { /* ignore */ }
  }

  function detectDefaultLang() {
    var stored = getStoredLang();
    if (stored === 'en' || stored === 'zh') return stored;
    var nav = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
    return nav.indexOf('zh') === 0 ? 'zh' : 'en';
  }

  function activate(post, lang) {
    post.setAttribute('data-show-lang', lang);
    var btns = post.querySelectorAll('.blog-lang-btn');
    for (var i = 0; i < btns.length; i++) {
      var btn = btns[i];
      if (btn.getAttribute('data-lang-target') === lang) {
        btn.classList.add('is-active');
      } else {
        btn.classList.remove('is-active');
      }
    }
  }

  function init() {
    var posts = document.querySelectorAll('.blog-post[data-lang="bilingual"]');
    if (!posts.length) return;

    for (var i = 0; i < posts.length; i++) {
      (function (post) {
        var lang = detectDefaultLang();
        activate(post, lang);

        var btns = post.querySelectorAll('.blog-lang-btn');
        for (var j = 0; j < btns.length; j++) {
          btns[j].addEventListener('click', function (e) {
            var target = e.currentTarget.getAttribute('data-lang-target');
            if (target !== 'en' && target !== 'zh') return;
            activate(post, target);
            storeLang(target);
          });
        }
      })(posts[i]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
