/* Thomas Moor — Digital Services: header, mobile menu, cookie consent + GA4, contact form. */
(function () {
  "use strict";
  var cfg = window.SITE_CONFIG || {};
  var body = document.body;

  /* ---------------- sticky header: transparent at top, solid once scrolled */
  var header = document.querySelector(".site-header");
  function onScroll() { header.classList.toggle("scrolled", window.scrollY > 10); }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------------- mobile menu */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  function setMenu(open) {
    toggle.setAttribute("aria-expanded", String(open));
    body.classList.toggle("nav-open", open);
  }
  toggle.addEventListener("click", function () { setMenu(toggle.getAttribute("aria-expanded") !== "true"); });
  nav.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && body.classList.contains("nav-open")) { setMenu(false); toggle.focus(); } });
  window.matchMedia("(min-width: 981px)").addEventListener("change", function (m) { if (m.matches) setMenu(false); });

  /* ---------------- cookie consent + Google Analytics (Consent Mode v2, loaded only after "Accept") */
  var KEY = "tm_consent";
  var gaLoaded = false;
  function getConsent() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setConsent(v) { try { localStorage.setItem(KEY, v); } catch (e) { /* storage blocked */ } }
  function gaConfigured() { return cfg.gaId && !/X{4,}/.test(cfg.gaId); }

  function loadGA() {
    if (gaLoaded || !gaConfigured()) return;
    gaLoaded = true;
    gtag("consent", "update", { analytics_storage: "granted" });
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(cfg.gaId);
    document.head.appendChild(s);
    gtag("js", new Date());
    gtag("config", cfg.gaId);
  }

  function clearGACookies() {
    var host = location.hostname.replace(/^www\./, "");
    document.cookie.split(";").forEach(function (c) {
      var name = c.split("=")[0].trim();
      if (name.indexOf("_ga") !== 0) return;
      ["", "; domain=" + host, "; domain=." + host].forEach(function (d) {
        document.cookie = name + "=; Max-Age=0; path=/" + d;
      });
    });
  }

  var banner = document.getElementById("cookie-banner");
  function showBanner() { banner.hidden = false; }
  var consent = getConsent();
  if (consent === "granted") loadGA();
  else if (consent !== "denied") showBanner();

  banner.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-consent]");
    if (!btn) return;
    var value = btn.getAttribute("data-consent");
    setConsent(value);
    banner.hidden = true;
    if (value === "granted") {
      loadGA();
    } else {
      gtag("consent", "update", { analytics_storage: "denied" });
      clearGACookies();
      if (gaLoaded) location.reload(); // fully unload the GA script
    }
  });
  document.querySelectorAll("[data-cookie-settings]").forEach(function (b) {
    b.addEventListener("click", showBanner);
  });

  /* ---------------- contact form (Web3Forms) */
  var form = document.getElementById("contact-form");
  if (form) {
    var status = form.querySelector(".form-status");
    var msgs = JSON.parse(form.getAttribute("data-messages"));
    var submit = form.querySelector("[type=submit]");

    function say(text, kind) {
      status.textContent = text;
      status.className = "form-status" + (kind ? " is-" + kind : "");
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = form.elements.name, email = form.elements.email;
      name.removeAttribute("aria-invalid");
      email.removeAttribute("aria-invalid");

      if (!name.value.trim()) { name.setAttribute("aria-invalid", "true"); say(msgs.required, "error"); name.focus(); return; }
      if (email.value && !email.checkValidity()) { email.setAttribute("aria-invalid", "true"); say(msgs.email, "error"); email.focus(); return; }
      if (!cfg.web3formsKey || cfg.web3formsKey.indexOf("YOUR_") === 0) { say(msgs.notConfigured, "error"); return; }

      form.elements.access_key.value = cfg.web3formsKey;
      submit.disabled = true;
      say(msgs.sending);

      fetch(form.action, { method: "POST", headers: { Accept: "application/json" }, body: new FormData(form) })
        .then(function (res) { return res.json().then(function (data) { return { ok: res.ok, data: data }; }); })
        .then(function (r) {
          if (!r.ok || !r.data.success) throw new Error(r.data.message || "Request failed");
          form.reset();
          say(msgs.success, "success");
          if (gaLoaded) gtag("event", "generate_lead");
        })
        .catch(function () { say(msgs.error, "error"); })
        .then(function () { submit.disabled = false; });
    });
  }
})();
