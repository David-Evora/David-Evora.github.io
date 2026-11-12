/* Idioma, tema e cópia de contatos. Menu, foco, rolagem e movimento vêm do kit (assets/system.js e motion). */
(function () {
  "use strict";
  var d = document, root = d.documentElement;
  function $(s, c) { return (c || d).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }
  function save(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  function lang() { return root.getAttribute("data-lang") === "en" ? "en" : "pt"; }
  var T = { pt: { copied: "Copiado para a área de transferência" }, en: { copied: "Copied to the clipboard" } };
  var docTitle = d.title;

  function setLang(l, persist) {
    root.setAttribute("data-lang", l);
    root.lang = l === "en" ? "en" : "pt-BR";
    if (persist) save("de-lang", l);
    $$("[data-aria-en]").forEach(function (el) {
      if (!el.hasAttribute("data-aria-pt")) el.setAttribute("data-aria-pt", el.getAttribute("aria-label") || "");
      el.setAttribute("aria-label", l === "en" ? el.getAttribute("data-aria-en") : el.getAttribute("data-aria-pt"));
    });
    $$("[data-alt-en]").forEach(function (im) {
      if (!im.hasAttribute("data-alt-pt")) im.setAttribute("data-alt-pt", im.getAttribute("alt") || "");
      im.setAttribute("alt", l === "en" ? im.getAttribute("data-alt-en") : im.getAttribute("data-alt-pt"));
    });
    $$("meta[data-en]").forEach(function (m) {
      if (!m.hasAttribute("data-pt")) m.setAttribute("data-pt", m.getAttribute("content") || "");
      m.setAttribute("content", l === "en" ? m.getAttribute("data-en") : m.getAttribute("data-pt"));
    });
    d.title = l === "en" ? "David Évora · Software Engineering · Data · AI" : docTitle;
  }
  setLang(lang(), false);
  $("#lang-btn").addEventListener("click", function () { setLang(lang() === "en" ? "pt" : "en", true); });

  var mq = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : { matches: false };
  function theme() { return root.getAttribute("data-theme") || (mq.matches ? "dark" : "light"); }
  function themeColor() {
    var m = $('meta[name="theme-color"]');
    if (m) m.setAttribute("content", theme() === "dark" ? "#0d0e10" : "#eef0f3");
  }
  themeColor();
  $("#theme-btn").addEventListener("click", function () {
    var n = theme() === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", n);
    save("de-theme", n);
    themeColor();
  });
  if (mq.addEventListener) mq.addEventListener("change", themeColor);

  var live = $("#live");
  $$("[data-copy]").forEach(function (b) {
    b.addEventListener("click", function () {
      var txt = b.getAttribute("data-copy");
      function ok() {
        b.classList.add("is-copied");
        live.textContent = ""; window.setTimeout(function () { live.textContent = T[lang()].copied; }, 30);
        window.setTimeout(function () { b.classList.remove("is-copied"); }, 2000);
      }
      function fallback() {
        // shortcut: execCommand("copy") is deprecated; kept as the fallback where clipboard.writeText is refused
        var a = b.parentNode.querySelector("a");
        var r = d.createRange(); r.selectNodeContents(a);
        var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
        try { if (d.execCommand("copy")) ok(); } catch (e) {}
      }
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(txt).then(ok, fallback);
      else fallback();
    });
  });

  // seção atual na barra (aria-current="location")
  var links = $$('.nav__link[href^="#"]');
  if ("IntersectionObserver" in window && links.length) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var id = e.target.id === "infofrota-fluxo" || e.target.id === "validacao" || e.target.id === "cmapss" || e.target.id === "sgtcc" ? "infofrota" : e.target.id === "contato" ? "contato" : e.target.id;
        links.forEach(function (l) {
          if (l.getAttribute("href") === "#" + id) l.setAttribute("aria-current", "location"); else l.removeAttribute("aria-current");
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    $$("main > section[id], footer[id]").forEach(function (s) { io.observe(s); });
  }
})();
