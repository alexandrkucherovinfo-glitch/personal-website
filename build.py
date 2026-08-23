# -*- coding: utf-8 -*-
"""Generates index.html from content.py for Alexander Kucherov's bilingual site."""
import html as _html
from content import (ICONS, NAV, EXPERTISE, SERVICES, PRODUCT_GROUPS, NUMBERS,
                      METHOD_STEPS, TIMELINE, CASE_STUDIES, AUDIENCE)


def e(s):
    return _html.escape(s, quote=False)


def bi(en, ru, tag="span"):
    """Bilingual inline span pair."""
    return f'<{tag} data-lang="en">{e(en)}</{tag}><{tag} data-lang="ru">{e(ru)}</{tag}>'


def icon(name, css_class="icon"):
    return f'<svg class="{css_class}" aria-hidden="true"><use href="#icon-{name}"></use></svg>'


# ---------------------------------------------------------------- sprite ---
def build_sprite():
    symbols = []
    for name, inner in ICONS.items():
        symbols.append(f'<symbol id="icon-{name}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                        f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{inner}</symbol>')
    return '<svg class="icon-sprite" aria-hidden="true">' + ''.join(symbols) + '</svg>'


# ------------------------------------------------------------------ nav ---
def build_nav():
    items = []
    for anchor, en, ru in NAV:
        items.append(f'<li><a href="#{anchor}">{bi(en, ru)}</a></li>')
    items.append(f'<li><a href="#contact" class="nav-cta">{bi("Contact", "Контакты")}</a></li>')
    return ''.join(items)


# ------------------------------------------------------------- expertise ---
def build_expertise():
    cards = []
    for icn, ten, tru, den, dru in EXPERTISE:
        cards.append(f'''<article class="expertise-card reveal">
            <div class="card-icon">{icon(icn)}</div>
            <h3>{bi(ten, tru)}</h3>
            <p>{bi(den, dru)}</p>
          </article>''')
    return ''.join(cards)


def build_about_facts():
    items = []
    for _icn, ten, tru, _d1, _d2 in EXPERTISE:
        items.append(f'<li>{bi(ten, tru)}</li>')
    return ''.join(items)


# -------------------------------------------------------------- services ---
def build_services():
    cards = []
    for icn, ten, tru, foren, foru, items, data_service, wide in SERVICES:
        li = ''.join(f'<li>{bi(a, b)}</li>' for a, b in items)
        wide_cls = ' service-card-wide' if wide else ''
        list_cls = ' service-list-inline' if wide else ''
        cards.append(f'''<article class="service-card{wide_cls} reveal">
            <div class="card-icon">{icon(icn)}</div>
            <h3>{bi(ten, tru)}</h3>
            <p class="service-for">{bi(foren, foru)}</p>
            <ul class="{list_cls.strip()}">{li}</ul>
            <a href="#contact" class="service-link" data-service="{e(data_service)}">{bi("Discuss this service →", "Обсудить эту услугу →")}</a>
          </article>''')
    return ''.join(cards)


# -------------------------------------------------------------- products ---
def build_products():
    groups = []
    for gen, gru, items in PRODUCT_GROUPS:
        cards = []
        for icn, ten, tru, den, dru, tagen, tagru in items:
            cards.append(f'''<article class="product-card reveal">
              <div class="card-icon card-icon-sm">{icon(icn)}</div>
              <p class="product-tag">{bi(tagen, tagru)}</p>
              <h4>{bi(ten, tru)}</h4>
              <p>{bi(den, dru)}</p>
              <a href="#contact" class="product-link" data-service="{e(ten)}">{bi("Ask about this →", "Спросить об этом →")}</a>
            </article>''')
        groups.append(f'''<div class="products-group">
            <h3 class="products-group-title">{bi(gen, gru)}</h3>
            <div class="card-grid card-grid-products">{''.join(cards)}</div>
          </div>''')
    return ''.join(groups)


# --------------------------------------------------------------- numbers ---
def build_numbers():
    cards = []
    for icn, ven, vru, len_, lru in NUMBERS:
        cards.append(f'''<div class="number-card reveal">
            <div class="card-icon card-icon-sm">{icon(icn)}</div>
            <p class="number-value">{bi(ven, vru)}</p>
            <p class="number-label">{bi(len_, lru)}</p>
          </div>''')
    return ''.join(cards)


# ------------------------------------------------------------- method ------
def build_method():
    steps = []
    for i, (ten, tru, den, dru) in enumerate(METHOD_STEPS, start=1):
        steps.append(f'''<li class="method-step reveal">
            <span class="method-index">{i:02d}</span>
            <h3>{bi(ten, tru)}</h3>
            <p>{bi(den, dru)}</p>
          </li>''')
    return ''.join(steps)


# ----------------------------------------------------------- timeline ------
def build_timeline():
    items = []
    for dates_en, dates_ru, company, ten, tru, den, dru, ien, iru, condensed in TIMELINE:
        cls = ' timeline-item-condensed' if condensed else ''
        impact = f'<p class="timeline-impact">{bi(ien, iru)}</p>' if ien else ''
        items.append(f'''<article class="timeline-item{cls} reveal">
            <div class="timeline-meta">
              <p class="timeline-dates">{bi(dates_en, dates_ru)}</p>
              <p class="timeline-company">{e(company)}</p>
            </div>
            <div class="timeline-content">
              <h3>{bi(ten, tru)}</h3>
              <p>{bi(den, dru)}</p>
              {impact}
            </div>
          </article>''')
    return ''.join(items)


# --------------------------------------------------------- case studies ---
def build_case_studies():
    cards = []
    for tagen, tagru, ten, tru, chen, chru, apen, apru, reen, reru in CASE_STUDIES:
        cards.append(f'''<article class="case-card reveal">
            <p class="case-tag">{bi(tagen, tagru)}</p>
            <h3>{bi(ten, tru)}</h3>
            <p><strong>{bi("Challenge.", "Задача.")}</strong> {bi(chen, chru)}</p>
            <p><strong>{bi("Approach.", "Подход.")}</strong> {bi(apen, apru)}</p>
            <p><strong>{bi("Result.", "Результат.")}</strong> {bi(reen, reru)}</p>
          </article>''')
    return ''.join(cards)


# --------------------------------------------------------------- audience --
def build_audience():
    items = []
    for en, ru in AUDIENCE:
        items.append(f'<li class="reveal">{bi(en, ru)}</li>')
    return ''.join(items)


TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script>
    (function () {{
      try {{
        var nav = (navigator.language || navigator.userLanguage || 'en').toLowerCase();
        var lang = nav.indexOf('ru') === 0 ? 'ru' : 'en';
        document.documentElement.setAttribute('data-lang', lang);
        document.documentElement.setAttribute('lang', lang);
      }} catch (e) {{}}
    }})();
  </script>

  <title>Alexander Kucherov | Business Transformation Consultant &amp; AI-Powered Services</title>
  <meta name="description" content="20+ years turning business chaos into working systems. Consulting, done-for-you services and ready-made playbooks for businesses and individuals.">
  <meta name="keywords" content="Project Manager, Digital Transformation Consultant, Business Transformation, Operations Consultant, AI Automation for Business, CRM Implementation, Business Process Optimisation, Program Management, Change Management, Business Consultant, Career Coaching, International Job Search">
  <meta name="author" content="Alexander Kucherov">
  <meta name="robots" content="index, follow">

  <meta property="og:type" content="website">
  <meta property="og:title" content="Alexander Kucherov | Business Transformation Consultant &amp; AI-Powered Services">
  <meta property="og:description" content="20+ years turning business chaos into working systems. Consulting, done-for-you services and ready-made playbooks for businesses and individuals.">
  <meta property="og:image" content="assets/images/og-image.png">
  <meta property="og:url" content="https://alexandrkucherovinfo-glitch.github.io/personal-website/">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Alexander Kucherov | Business Transformation Consultant &amp; AI-Powered Services">
  <meta name="twitter:description" content="20+ years turning business chaos into working systems. Consulting, done-for-you services and ready-made playbooks.">
  <meta name="twitter:image" content="assets/images/og-image.png">

  <link rel="icon" type="image/svg+xml" href="assets/images/favicon.svg">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css">
</head>
<body>

  {sprite}

  <a class="skip-link" href="#main-content">{skip_link}</a>

  <header class="site-header" id="site-header">
    <div class="container header-inner">
      <a href="#home" class="brand">Alexander Kucherov</a>

      <div class="header-right">
        <div class="lang-switch" role="group" aria-label="Language / Язык">
          <button type="button" class="lang-btn" data-set-lang="en">EN</button>
          <button type="button" class="lang-btn" data-set-lang="ru">RU</button>
        </div>

        <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="primary-nav">
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
          <span class="nav-toggle-bar"></span>
          <span class="visually-hidden">Toggle navigation menu</span>
        </button>

        <nav class="primary-nav" id="primary-nav" aria-label="Primary">
          <ul>
            {nav}
          </ul>
        </nav>
      </div>
    </div>
  </header>

  <main id="main-content">

    <!-- ============ HERO ============ -->
    <section class="hero" id="home">
      <div class="container hero-inner">
        <div class="hero-copy reveal">
          <p class="eyebrow">Alexander Kucherov</p>
          <h1>{hero_h1}</h1>
          <p class="hero-subhead">{hero_subhead}</p>
          <p class="hero-statement">{hero_statement}</p>
          <div class="hero-actions">
            <a href="#contact" class="btn btn-primary">{hero_btn1}</a>
            <a href="#products" class="btn btn-ghost">{hero_btn2}</a>
          </div>
          <p class="hero-contact">
            <a href="mailto:alexandr.kucherov.info@gmail.com">alexandr.kucherov.info@gmail.com</a>
            <span aria-hidden="true">&middot;</span>
            <a href="https://linkedin.com/in/alexandr-kucherov-b542a823" target="_blank" rel="noopener">LinkedIn</a>
          </p>
        </div>

        <div class="hero-portrait reveal">
          <img src="assets/images/portrait-placeholder.svg" alt="Portrait of Alexander Kucherov" width="480" height="576" loading="eager">
          <p class="hero-badge">{hero_badge}</p>
        </div>
      </div>
    </section>

    <!-- ============ ABOUT ============ -->
    <section class="section" id="about">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{about_eyebrow}</p>
          <h2>{about_h2}</h2>
        </div>

        <div class="about-grid">
          <div class="about-copy reveal">
            <p>{about_p1}</p>
            <p>{about_p2}</p>
            <p>{about_p3}</p>
          </div>

          <ul class="about-facts reveal" aria-label="Core competencies">
            {about_facts}
          </ul>
        </div>
      </div>
    </section>

    <!-- ============ KEY NUMBERS ============ -->
    <section class="section section-alt" id="numbers" aria-label="Key achievements">
      <div class="container">
        <div class="numbers-grid">
          {numbers}
        </div>
        <p class="numbers-footnote reveal">{numbers_footnote}</p>
      </div>
    </section>

    <!-- ============ EXPERTISE ============ -->
    <section class="section" id="expertise">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{expertise_eyebrow}</p>
          <h2>{expertise_h2}</h2>
          <p class="section-lede">{expertise_lede}</p>
        </div>

        <div class="card-grid card-grid-3">
          {expertise}
        </div>
      </div>
    </section>

    <!-- ============ SERVICES ============ -->
    <section class="section section-alt" id="services">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{services_eyebrow}</p>
          <h2>{services_h2}</h2>
          <p class="section-lede">{services_lede}</p>
        </div>

        <div class="card-grid card-grid-2 services-grid">
          {services}
        </div>
      </div>
    </section>

    <!-- ============ PRODUCTS ============ -->
    <section class="section" id="products">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{products_eyebrow}</p>
          <h2>{products_h2}</h2>
          <p class="section-lede">{products_lede}</p>
        </div>

        {products}

        <p class="products-note reveal">{products_note}</p>
      </div>
    </section>

    <!-- ============ HOW I WORK ============ -->
    <section class="section section-alt" id="how-i-work">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{method_eyebrow}</p>
          <h2>{method_h2}</h2>
        </div>

        <ol class="method-steps">
          {method}
        </ol>
      </div>
    </section>

    <!-- ============ EXPERIENCE ============ -->
    <section class="section" id="experience">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{experience_eyebrow}</p>
          <h2>{experience_h2}</h2>
        </div>

        <div class="timeline">
          {timeline}
        </div>
      </div>
    </section>

    <!-- ============ CASE STUDIES ============ -->
    <section class="section section-alt" id="case-studies">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{cases_eyebrow}</p>
          <h2>{cases_h2}</h2>
        </div>

        <div class="card-grid card-grid-3">
          {case_studies}
        </div>
      </div>
    </section>

    <!-- ============ WHO I WORK WITH ============ -->
    <section class="section" id="who-i-work-with">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{audience_eyebrow}</p>
          <h2>{audience_h2}</h2>
        </div>

        <ul class="audience-grid">
          {audience}
        </ul>
      </div>
    </section>

    <!-- ============ CONTACT ============ -->
    <section class="section section-alt" id="contact">
      <div class="container contact-grid">
        <div class="contact-intro reveal">
          <p class="eyebrow">{contact_eyebrow}</p>
          <h2>{contact_h2}</h2>
          <p>{contact_p}</p>
          <p class="contact-direct">
            <a href="mailto:alexandr.kucherov.info@gmail.com">alexandr.kucherov.info@gmail.com</a><br>
            <a href="https://linkedin.com/in/alexandr-kucherov-b542a823" target="_blank" rel="noopener">linkedin.com/in/alexandr-kucherov-b542a823</a>
          </p>
        </div>

        <form class="contact-form reveal" id="contactForm" novalidate>
          <div class="form-row">
            <label for="name">{label_name} <span aria-hidden="true">*</span></label>
            <input type="text" id="name" name="name" autocomplete="name" required>
            <span class="form-error" id="name-error"></span>
          </div>

          <div class="form-row">
            <label for="company">{label_company}</label>
            <input type="text" id="company" name="company" autocomplete="organization">
          </div>

          <div class="form-row">
            <label for="email">{label_email} <span aria-hidden="true">*</span></label>
            <input type="email" id="email" name="email" autocomplete="email" required>
            <span class="form-error" id="email-error"></span>
          </div>

          <div class="form-row">
            <label for="service">{label_service}</label>
            <select id="service" name="service">
              <option value="" data-en="{opt_select_en}" data-ru="{opt_select_ru}">{opt_select_en}</option>
              {service_options}
            </select>
          </div>

          <div class="form-row form-row-full">
            <label for="message">{label_message} <span aria-hidden="true">*</span></label>
            <textarea id="message" name="message" rows="5" required></textarea>
            <span class="form-error" id="message-error"></span>
          </div>

          <div class="form-row form-row-full">
            <button type="submit" class="btn btn-primary btn-full">{btn_submit}</button>
            <p class="form-status" id="formStatus" role="status" aria-live="polite"></p>
          </div>
        </form>
      </div>
    </section>

  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <p>&copy; <span id="year"></span> Alexander Kucherov. {footer_rights}</p>
      <p class="footer-links">
        <a href="mailto:alexandr.kucherov.info@gmail.com">{footer_email}</a>
        <span aria-hidden="true">&middot;</span>
        <a href="https://linkedin.com/in/alexandr-kucherov-b542a823" target="_blank" rel="noopener">LinkedIn</a>
      </p>
    </div>
  </footer>

  <script src="js/script.js"></script>
</body>
</html>
'''


def build_service_options():
    opts = []
    for _icn, ten, tru, *_rest, data_service, _wide in SERVICES:
        opts.append(f'<option value="{e(data_service)}" data-en="{e(ten)}" data-ru="{e(tru)}">{e(ten)}</option>')
    for gen, gru, items in PRODUCT_GROUPS:
        for _icn, ten, tru, *_rest in items:
            opts.append(f'<option value="{e(ten)}" data-en="{e(ten)}" data-ru="{e(tru)}">{e(ten)}</option>')
    opts.append('<option value="Other" data-en="Other (please specify in message)" '
                 'data-ru="Другое (уточните в сообщении)">Other (please specify in message)</option>')
    return ''.join(opts)


def main():
    out = TEMPLATE.format(
        sprite=build_sprite(),
        skip_link=bi("Skip to main content", "Перейти к основному содержанию"),
        nav=build_nav(),
        hero_h1=bi(
            "20+ years turning business chaos into working systems — now available as consulting, "
            "done-for-you services, and ready-made playbooks.",
            "20+ лет опыта превращать хаос в бизнесе в работающую систему — теперь доступно как консалтинг, "
            "услуги под ключ и готовые методики.", tag="span"),
        hero_subhead=bi(
            "Project Management • Digital Transformation • Operations • AI-Powered Services",
            "Управление проектами • Цифровая трансформация • Операции • Услуги с AI"),
        hero_statement=bi(
            "For more than 20 years I have helped multinational companies and high-growth businesses across "
            "Automotive, Banking, Insurance and Telecommunications turn strategy into working operating systems. "
            "Today that same experience also powers a set of fixed-scope services and digital products — "
            "for businesses, and for people navigating their own big moves.",
            "Более 20 лет я помогаю международным компаниям и быстрорастущим бизнесам в автомобильной, банковской, "
            "страховой и телеком-отраслях превращать стратегию в работающие операционные системы. Сегодня тот же "
            "опыт упакован в услуги с понятным результатом и готовые продукты — для бизнеса и для людей, "
            "которые сами проходят через большие перемены."),
        hero_btn1=bi("Work With Me", "Работать со мной"),
        hero_btn2=bi("Explore Products", "Готовые продукты"),
        hero_badge=bi(
            "Open to remote & relocation · Cyprus · USA · Turkey · Georgia · Uzbekistan",
            "Открыт к удалёнке и переезду · Кипр · США · Турция · Грузия · Узбекистан"),
        about_eyebrow=bi("About", "Обо мне"),
        about_h2=bi("Business, technology and operations — working as one system",
                    "Бизнес, технологии и операции — как единая система"),
        about_p1=bi(
            "Alexander is a senior project and business transformation leader with more than 20 years of experience "
            "across multinational companies and high-growth businesses in Automotive, Banking, Insurance and "
            "Telecommunications. He has built teams and operations from scratch, launched digital platforms, and led "
            "nationwide network expansion programmes for international brands.",
            "Александр — руководитель с более чем 20-летним опытом в управлении проектами и трансформации "
            "бизнеса, работавший в международных компаниях и быстрорастущих проектах в автомобильной, банковской, "
            "страховой и телеком-отраслях. Он строил команды и операционные процессы с нуля, запускал цифровые "
            "платформы и руководил программами национального масштаба для международных брендов."),
        about_p2=bi(
            "His work sits at the intersection of business, technology and people. Rather than managing projects "
            "in isolation, Alexander designs the operating systems around them — defining requirements, "
            "coordinating software engineers and vendors, implementing CRM/ERP platforms, and putting KPI and "
            "governance structures in place so that results are repeatable, not accidental.",
            "Его работа находится на стыке бизнеса, технологий и людей. Вместо того чтобы управлять проектами "
            "изолированно, Александр выстраивает операционную систему вокруг них — формулирует требования, "
            "координирует разработчиков и подрядчиков, внедряет CRM/ERP-платформы и выстраивает систему KPI и "
            "управления, чтобы результат был закономерным, а не случайным."),
        about_p3=bi(
            "He works fluently with cross-functional teams — sales, marketing, operations and technology "
            "— and is equally comfortable setting strategy with executive stakeholders and writing the "
            "business requirements that development teams build against. The sections below turn that same "
            "experience into services you can hire directly, and products you can use on your own.",
            "Он свободно работает с кросс-функциональными командами — продажами, маркетингом, операциями и "
            "технологиями — и одинаково уверенно чувствует себя, формируя стратегию с топ-менеджментом и "
            "составляя бизнес-требования, по которым работают команды разработки. Ниже этот же опыт превращён в "
            "услуги, которые можно заказать напрямую, и продукты, которыми можно воспользоваться самостоятельно."),
        about_facts=build_about_facts(),
        numbers=build_numbers(),
        numbers_footnote=bi("Experience spans Automotive, Banking, Insurance and Telecommunications.",
                             "Опыт охватывает автомобильную отрасль, банкинг, страхование и телеком."),
        expertise_eyebrow=bi("Expertise", "Экспертиза"),
        expertise_h2=bi("Where strategy meets execution", "Там, где стратегия встречается с реализацией"),
        expertise_lede=bi("Twelve areas of practice, each tied to a business outcome rather than a buzzword.",
                           "Двенадцать направлений практики, каждое привязано к результату для бизнеса, а не к модному термину."),
        expertise=build_expertise(),
        services_eyebrow=bi("Services", "Услуги"),
        services_h2=bi("How I can help your business", "Как я могу помочь вашему бизнесу"),
        services_lede=bi("Advisory, delivery and training built around the same competencies used to run the programmes above.",
                          "Консалтинг, реализация и обучение — на основе тех же компетенций, что и в описанных выше программах."),
        services=build_services(),
        products_eyebrow=bi("Products & Done-For-You Services", "Продукты и услуги под ключ"),
        products_h2=bi("Fixed-scope help you can buy directly", "Готовая помощь, которую можно купить напрямую"),
        products_lede=bi(
            "Not open-ended consulting — packaged outcomes with a clear scope, format and turnaround, "
            "built from the same 20+ years of experience above.",
            "Не открытый консалтинг, а упакованные результаты с понятным объёмом, форматом и сроками — на основе "
            "того же 20-летнего опыта, что описан выше."),
        products=build_products(),
        products_note=bi(
            "Don't see exactly what you need? Message me — most of these can be scoped down to a single "
            "session or up to an ongoing engagement.",
            "Не нашли то, что нужно? Напишите мне — почти любой из этих продуктов можно сузить до одной сессии "
            "или расширить до постоянного сотрудничества."),
        method_eyebrow=bi("Methodology", "Методология"),
        method_h2=bi("How I work", "Как я работаю"),
        method=build_method(),
        experience_eyebrow=bi("Experience", "Опыт"),
        experience_h2=bi("Career highlights", "Ключевые этапы карьеры"),
        timeline=build_timeline(),
        cases_eyebrow=bi("Selected Case Studies", "Избранные кейсы"),
        cases_h2=bi("Transformation in practice", "Трансформация на практике"),
        case_studies=build_case_studies(),
        audience_eyebrow=bi("Who I Work With", "С кем я работаю"),
        audience_h2=bi("Built for leaders driving change", "Для тех, кто ведёт изменения"),
        audience=build_audience(),
        contact_eyebrow=bi("Contact", "Контакты"),
        contact_h2=bi("Let's discuss your project", "Обсудим ваш проект"),
        contact_p=bi(
            "Tell me a little about your business and what you're trying to solve. I respond personally to every "
            "enquiry, usually within one to two business days.",
            "Расскажите немного о вашем бизнесе или задаче. Я отвечаю лично на каждое обращение, обычно в течение "
            "одного-двух рабочих дней."),
        label_name=bi("Name", "Имя"),
        label_company=bi("Company", "Компания"),
        label_email=bi("Email", "Email"),
        label_service=bi("What do you need help with?", "С чем нужна помощь?"),
        opt_select_en="Select an option…",
        opt_select_ru="Выберите вариант…",
        service_options=build_service_options(),
        label_message=bi("Message", "Сообщение"),
        btn_submit=bi("Discuss Your Project", "Обсудить проект"),
        footer_rights=bi("All rights reserved.", "Все права защищены."),
        footer_email=bi("Email", "Email"),
    )
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(out)
    print("Wrote index.html:", len(out), "bytes")


if __name__ == '__main__':
    main()
