/* Progressive enhancement: all stories and navigation work without JavaScript. */
(() => {
  const input = document.querySelector('#story-search');
  const form = document.querySelector('.search');
  const clear = document.querySelector('.search-clear');
  const feedback = document.querySelector('.search-feedback');
  const status = feedback.querySelector('[role="status"]');
  const empty = document.querySelector('.empty-search');
  const stories = [...document.querySelectorAll('[data-story]')];
  const sections = [...document.querySelectorAll('[data-chapter-section]')];
  const links = [...document.querySelectorAll('[data-chapter-link]')];
  const progress = document.querySelector('.reading-progress');
  const intro = document.querySelector('.prologue');
  const introOrigin = document.createComment('Intro position when not searching');
  intro.after(introOrigin);
  const introResults = document.querySelector('#search-intro-slot');
  const normalize = value => value.toLocaleLowerCase('ru').replaceAll('ё', 'е').trim();
  const words = value => normalize(value).split(/[^\p{L}\p{N}]+/u).filter(Boolean);
  const searchable = new Map(stories.map(story => [story, words(story.innerText)]));

  function search(scrollToResults = false) {
    const query = normalize(input.value);
    const terms = words(query);
    let matches = 0;
    stories.forEach(story => {
      const match = terms.every(term => searchable.get(story).some(word => word.startsWith(term)));
      story.hidden = !match;
      if (match) matches++;
    });
    sections.forEach(section => {
      section.hidden = ![...section.querySelectorAll('[data-story]')].some(story => !story.hidden);
    });
    document.body.classList.toggle('searching', Boolean(query));
    if (query) introResults.append(intro);
    else introOrigin.before(intro);
    feedback.hidden = !query;
    clear.hidden = !query;
    empty.hidden = !query || matches > 0;
    status.textContent = query ? `Найдено историй: ${matches} из ${stories.length}` : '';
    if (scrollToResults && query) feedback.scrollIntoView({ block: 'start', behavior: 'instant' });
    updatePosition();
  }

  function resetSearch(focus = true) {
    input.value = '';
    search();
    if (focus) input.focus({ preventScroll: true });
  }

  form.addEventListener('submit', event => { event.preventDefault(); search(true); });
  input.addEventListener('input', () => search(true));
  input.addEventListener('keydown', event => {
    if (event.key === 'Escape') resetSearch();
  });
  clear.addEventListener('click', () => resetSearch());
  document.querySelectorAll('[data-reset-search]').forEach(button => button.addEventListener('click', () => resetSearch()));

  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', () => {
      if (input.value) resetSearch(false);
      if (link.getAttribute('href') === '#contents') document.querySelector('#contents').open = true;
    });
  });

  function revealHash() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); }
    catch { return; }
    if (id === 'contents') document.querySelector('#contents').open = true;
    const target = document.getElementById(id);
    if (target?.hidden || target?.closest('[hidden]')) {
      resetSearch(false);
      target.scrollIntoView();
    }
  }
  window.addEventListener('hashchange', revealHash);
  revealHash();

  let scheduled = false;
  function updatePosition() {
    const navHeight = document.querySelector('.reading-bar').offsetHeight;
    document.documentElement.style.setProperty('--nav-height', `${navHeight}px`);
    let active = null;
    sections.filter(section => !section.hidden).forEach(section => {
      if (section.getBoundingClientRect().top <= navHeight + 90) active = section.id;
    });
    links.forEach(link => {
      if (link.dataset.chapterLink === active) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
    const max = document.documentElement.scrollHeight - innerHeight;
    progress.style.width = `${max > 0 ? Math.min(100, scrollY / max * 100) : 0}%`;
    scheduled = false;
  }
  window.addEventListener('scroll', () => {
    if (!scheduled) { scheduled = true; requestAnimationFrame(updatePosition); }
  }, { passive: true });
  window.addEventListener('resize', updatePosition);
  updatePosition();
})();
