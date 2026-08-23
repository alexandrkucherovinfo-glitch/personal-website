(function () {
  'use strict';

  // ---------- Footer year ----------
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ---------- Language toggle (EN / RU) ----------
  // Initial language is set synchronously in <head> based on navigator.language,
  // to avoid a flash of the wrong language. This just wires up the toggle buttons
  // and keeps them in sync with the current html[data-lang] value. No persistence
  // (localStorage) is used on purpose — add it yourself if you want the choice to
  // survive a page reload once this is live on your own domain.
  var langBtns = document.querySelectorAll('.lang-btn');
  function setLang(lang) {
    document.documentElement.setAttribute('data-lang', lang);
    document.documentElement.setAttribute('lang', lang);
    langBtns.forEach(function (btn) {
      var isActive = btn.getAttribute('data-set-lang') === lang;
      btn.classList.toggle('is-active', isActive);
      btn.setAttribute('aria-pressed', String(isActive));
    });
  }
  langBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      setLang(btn.getAttribute('data-set-lang'));
    });
  });
  setLang(document.documentElement.getAttribute('data-lang') === 'ru' ? 'ru' : 'en');

  // ---------- Sticky header shadow ----------
  var header = document.getElementById('site-header');
  var onScroll = function () {
    if (window.scrollY > 8) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ---------- Mobile nav toggle ----------
  var navToggle = document.getElementById('navToggle');
  var primaryNav = document.getElementById('primary-nav');

  function closeNav() {
    navToggle.setAttribute('aria-expanded', 'false');
    primaryNav.classList.remove('is-open');
  }

  navToggle.addEventListener('click', function () {
    var isOpen = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!isOpen));
    primaryNav.classList.toggle('is-open', !isOpen);
  });

  primaryNav.addEventListener('click', function (event) {
    if (event.target.tagName === 'A') closeNav();
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') closeNav();
  });

  // ---------- Scroll reveal ----------
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // ---------- Service card -> contact form prefill ----------
  var serviceSelect = document.getElementById('service');
  document.querySelectorAll('.service-link[data-service]').forEach(function (link) {
    link.addEventListener('click', function () {
      var value = link.getAttribute('data-service');
      if (serviceSelect && value) {
        serviceSelect.value = value;
      }
    });
  });

  // ---------- Contact form validation + submission ----------
  var form = document.getElementById('contactForm');
  var statusEl = document.getElementById('formStatus');

  function setFieldError(fieldId, message) {
    var field = document.getElementById(fieldId);
    var errorEl = document.getElementById(fieldId + '-error');
    var row = field.closest('.form-row');
    if (message) {
      row.classList.add('has-error');
      if (errorEl) errorEl.textContent = message;
    } else {
      row.classList.remove('has-error');
      if (errorEl) errorEl.textContent = '';
    }
  }

  function isValidEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  function validateForm(data) {
    var valid = true;

    if (!data.name.trim()) {
      setFieldError('name', 'Please enter your name.');
      valid = false;
    } else {
      setFieldError('name', '');
    }

    if (!data.email.trim()) {
      setFieldError('email', 'Please enter your email.');
      valid = false;
    } else if (!isValidEmail(data.email)) {
      setFieldError('email', 'Please enter a valid email address.');
      valid = false;
    } else {
      setFieldError('email', '');
    }

    if (!data.message.trim()) {
      setFieldError('message', 'Please add a short message.');
      valid = false;
    } else {
      setFieldError('message', '');
    }

    return valid;
  }

  if (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      var data = {
        name: form.name.value,
        company: form.company.value,
        email: form.email.value,
        service: form.service.value,
        budget: form.budget.value,
        message: form.message.value
      };

      if (!validateForm(data)) {
        statusEl.textContent = 'Please check the highlighted fields and try again.';
        statusEl.className = 'form-status is-error';
        return;
      }

      // -----------------------------------------------------------------
      // NOTE: This is a front-end-only placeholder. No data is sent yet.
      // Connect a real submission handler here, for example:
      //
      //   Formspree:  fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      //   EmailJS:    emailjs.sendForm('SERVICE_ID', 'TEMPLATE_ID', form)
      //   Custom API: fetch('/api/contact', { method: 'POST', body: JSON.stringify(data), headers: {'Content-Type':'application/json'} })
      //
      // Then handle the response/error to update formStatus below instead
      // of the simulated success message.
      // -----------------------------------------------------------------
      statusEl.textContent = 'Thank you, ' + data.name.split(' ')[0] + '. Your message has been prepared — connect a form service (see comments in script.js) to deliver it.';
      statusEl.className = 'form-status is-success';
      form.reset();
    });
  }
})();
