#!/usr/bin/env python3
"""Render the complete, buildless reader. Run with Python 3; no dependencies."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
E = html.escape
CHAPTERS = [
    ('origins', 'Как всё началось', 'Очень древние вампиры. Очень долгая подготовка.', 'От первого впечатления до первого фильма. Дружба, неудачная вечеринка и девять лет вполне спокойной работы.'),
    ('housemates', 'Соседи навечно', 'Четверо. Один дом. Никакого покоя.', 'У каждого — своя вампирская родословная. И свои представления о совместной жизни.'),
    ('people', 'Свои люди', 'Сценарий спрятали. Друзей позвали.', 'В кадре — режиссёры, IT-специалист и воспитательница. А за камерой тоже происходит комедия.'),
    ('craft', 'Магия съёмок', 'Большое кино из подручного бессмертия.', 'Стены после «Хоббита», полёты без потолка и шутки, которые пришлось вырезать.'),
    ('sound', 'Музыка и голоса', 'На слух — уже свои.', 'Песни из разных миров, русское название и Виаго, который снова достался режиссёру.'),
    ('afterlife', 'Жизнь после фильма', 'Снять — полдела. Надо ещё встретить зрителя.', 'Краудфандинг, бессмертный светлый эль и два сериала для тех, кому одного дома мало.'),
]
ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg>'

def figure(m, story_id, index=0):
    positions = {9:'32% 35%',12:'61% 40%',10:'50% 30%',11:'50% 30%'}
    pos = positions.get(story_id,'50% 50%')
    return f'''<figure class="story-photo"><img src="{E(m['src'])}" alt="{E(m['alt'])}" loading="lazy" decoding="async" style="object-position:{pos}"><figcaption>{E(m['caption'])}</figcaption></figure>'''

def article(s):
    n=s['id'];slug=s['slug'];media=s['media']
    photos=''.join(figure(m,n,i) for i,m in enumerate(media))
    if n==5:
        photos='<div class="timeline" aria-label="Этапы создания фильма"><div><strong>2005</strong><span>Короткометражка</span></div><div><strong>2012</strong><span>Съёмки полного метра</span></div><div><strong>2014</strong><span>Премьера на Sundance</span></div></div>'
    if n==20:
        photos='<div class="edit-stats"><div><strong>100<span>+</span></strong><p>часов материала</p></div><div><strong>≈14</strong><p>месяцев монтажа</p></div><div><strong>86</strong><p>минут фильма</p></div></div>'
    if n==23:
        photos='<div class="record-art" role="img" aria-label="Иллюстрация виниловой пластинки You’re Dead, Norma Tanega, 1966"><div class="record"><div class="record-label"><span>NORMA TANEGA</span><strong>YOU’RE<br>DEAD</strong><span>1966</span></div></div><span class="record-note">Для вампиров — свежий релиз.</span></div>'
    if n==24:
        photos='<div class="plan-nine" role="img" aria-label="Plan 9 и Дэвид Лонг — композиторы Misty Mountains"><span>PLAN</span><strong>9</strong><small>MISTY MOUNTAINS<br>С ДЭВИДОМ ЛОНГОМ</small></div>'
    if n==25:
        photos='<div class="lastochka-art"><span>В ФИНАЛЬНЫХ ТИТРАХ</span><strong>«ЛАСТОЧКА»</strong><b>ЛЕНИНГРАД</b><span>Оригинальный фильм · 2014</span></div>'
    if n==28:
        photos='<div class="receipt"><span>KICKSTARTER / 2015</span><strong>$446 666</strong><b>7 204 УЧАСТНИКА</b><hr><span>НА ПРОКАТ ГОТОВОГО ФИЛЬМА В США</span></div>'
    source_links=''.join(f'<li><a href="{E(x["url"])}" target="_blank" rel="noreferrer">{E(x["title"])} <span aria-hidden="true">↗</span></a></li>' for x in s['sources'])
    paras=''.join(f'<p>{E(p)}</p>' for p in s['paragraphs'])
    classes=['story',f'story--{n:02d}']
    if n in [2,5,8,13,18,19,20,23,28,30]:classes.append('story--wide')
    if len(media)>1:classes.append('story--multi')
    if n in [9,10,11,12]:classes.append('story--person')
    mediahtml=f'<div class="story-media media-count-{len(media)}">{photos}</div>' if photos else ''
    return f'''<article class="{' '.join(classes)}" id="{E(slug)}" data-story data-chapter="{s['chapter']}">
      {mediahtml}
      <div class="story-body"><div class="story-meta"><span>{n:02d} / {E(s['kicker'])}</span><a class="permalink" href="#{E(slug)}" aria-label="Ссылка на историю: {E(s['title'])}">#</a></div>
      <h3>{E(s['title'])}</h3><div class="story-copy">{paras}</div>
      <details class="sources"><summary>Источники <span aria-hidden="true">↗</span></summary><ul>{source_links}</ul></details>
      </div></article>'''

def build():
    stories=json.loads((ROOT/'content/stories.json').read_text())['stories']
    intro=stories[0]
    toc='';sections='';nav=''
    for i,(cid,title,headline,description) in enumerate(CHAPTERS,1):
        ss=[s for s in stories if s['chapter']==cid]
        count_label='ИСТОРИИ' if 2 <= len(ss) <= 4 else 'ИСТОРИЙ'
        nav+=f'<a href="#{cid}" data-chapter-link="{cid}"><span>{i:02d}</span> {E(title)}</a>'
        links=''.join(f'<a href="#{s["slug"]}"><span>{s["id"]:02d}</span>{E(s["title"])}</a>' for s in ss)
        toc+=f'<div class="toc-group"><h3><a href="#{cid}">{i:02d} / {E(title)}</a></h3>{links}</div>'
        sections+=f'''<section class="chapter chapter--{cid}" id="{cid}" data-chapter-section>
          <div class="chapter-inner"><header class="chapter-heading"><div class="chapter-label"><span>ГЛАВА {i:02d}</span><span>{len(ss):02d} {count_label}</span></div><h2>{E(headline)}</h2><p>{E(description)}</p></header>
          <div class="stories-grid">{''.join(article(s) for s in ss)}</div></div></section>'''
    introparas=''.join(f'<p>{E(p)}</p>' for p in intro['paragraphs'])
    introsources=''.join(f'<li><a href="{E(x["url"])}" target="_blank" rel="noreferrer">{E(x["title"])} ↗</a></li>' for x in intro['sources'])
    page=f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Вечность. С соседями. — 30 историй о «Реальных упырях»</title>
<meta name="description" content="Как снимали «Реальных упырей»: 30 коротких историй о Тайке Вайтити, Джемейне Клементе, вампирском быте, музыке и дубляже. Без сюжетных развязок.">
<meta name="theme-color" content="#101a15"><meta property="og:type" content="website"><meta property="og:locale" content="ru_RU">
<meta property="og:title" content="Вечность. С соседями."><meta property="og:description" content="30 коротких историй о «Реальных упырях». Без сюжетных развязок.">
<meta property="og:image" content="https://deman4ik.github.io/whatwedoitheshadows/assets/images/title-trio.webp">
<meta property="og:url" content="https://deman4ik.github.io/whatwedoitheshadows/">
<link rel="canonical" href="https://deman4ik.github.io/whatwedoitheshadows/">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="assets/fonts/Oswald-Variable.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="styles.css"><script src="app.js" defer></script></head>
<body><a class="skip-link" href="#stories">К историям</a>
<header class="masthead"><a class="wordmark" href="#top">РЕАЛЬНЫЕ УПЫРИ<span>КИНОИСТОРИИ</span></a><span class="masthead-note">НОВАЯ ЗЕЛАНДИЯ · 2014</span><a class="toc-link" href="#contents">Все темы <span aria-hidden="true">↗</span></a></header>
<main id="top">
<section class="hero" aria-labelledby="hero-title"><div class="hero-inner"><div class="hero-kicker"><span class="live-dot"></span> ДОКУМЕНТАЛЬНО. ПОЧТИ.</div>
<h1 id="hero-title">ВЕЧНОСТЬ.<span>С СОСЕДЯМИ.</span></h1>
<div class="hero-layout"><div class="hero-intro"><p>Бессмертие выдали.<br>Отдельную квартиру — нет.</p><span class="hero-description">Как снимали «Реальных упырей» —<br>от первых клыков до последней шутки.</span><a class="read-link" href="#stories">Читать истории <span aria-hidden="true">↓</span></a><div class="hero-metrics"><span><b>30</b> коротких историй</span><span>Без сюжетных<br>развязок</span></div></div><figure class="hero-photo"><img src="assets/images/title-trio.webp" alt="Виаго, Дикон и Владислав в общем доме" fetchpriority="high" width="1200" height="900"><figcaption>Бессмертные. Соседи. Очень разные люди.</figcaption><span class="photo-stamp" aria-hidden="true">86 МИНУТ<br>ИХ ПРОБЛЕМ</span></figure></div>
</div><div class="hero-bottom"><span>WHAT WE DO IN THE SHADOWS</span><span>ТАЙКА ВАЙТИТИ + ДЖЕМЕЙН КЛЕМЕНТ</span></div></section>
<section class="prologue wrap" id="eternal-roommates" data-story data-chapter="intro"><div class="prologue-label">01 / ЗНАКОМСТВО С ФИЛЬМОМ</div><div class="prologue-copy"><h2 class="visually-hidden">Вечность. С соседями.</h2>{introparas}<details class="sources"><summary>Источники <span aria-hidden="true">↗</span></summary><ul>{introsources}</ul></details></div></section>
<div id="stories" class="reading-start"></div>
<div class="reading-bar"><div class="reading-bar-inner"><nav class="chapter-nav" aria-label="Главы">{nav}</nav><form class="search" role="search"><label class="visually-hidden" for="story-search">Поиск по историям</label>{ICON}<input id="story-search" type="search" placeholder="Найти историю" autocomplete="off"><button class="search-clear" type="button" aria-label="Очистить поиск" hidden>×</button></form></div><div class="reading-progress" aria-hidden="true"></div></div>
<div class="search-feedback" hidden><p role="status" aria-live="polite"></p><button type="button" data-reset-search>Показать все истории</button></div>
<div id="search-intro-slot"></div>
<details class="contents wrap" id="contents"><summary><span>Выберите свою историю</span><span class="contents-count">ОГЛАВЛЕНИЕ · 30 ИСТОРИЙ</span><span class="contents-plus" aria-hidden="true">+</span></summary><nav class="toc-grid" aria-label="Все истории"><div class="toc-intro"><a href="#eternal-roommates"><span>01</span> Вечность. С соседями.</a></div>{toc}</nav></details>
<div class="chapters">{sections}</div>
<div class="empty-search wrap" hidden><span aria-hidden="true">∅</span><h2>В этой комнате никого.</h2><p>Такой истории не нашлось. Попробуйте «Стю», «музыка» или «сценарий».</p><button type="button" data-reset-search>Вернуть все истории</button></div>
<section class="closing"><div class="wrap"><p>ПОРА ЗАНЯТЬ МЕСТО НА ДИВАНЕ.</p><h2>Вечная жизнь.<br>Знакомые проблемы.</h2><a href="#top">Вернуться к началу <span aria-hidden="true">↑</span></a></div></section>
</main><footer class="site-footer wrap"><p>«Реальные упыри» · What We Do in the Shadows · 2014<br><span>Киноистории по материалам презентации. Источники — под каждой историей.</span></p><a href="https://github.com/deman4ik/whatwedoitheshadows" target="_blank" rel="noreferrer">Сайт на GitHub ↗</a></footer>
</body></html>'''
    (ROOT/'index.html').write_text(page)
    print(f'Built index.html: {len(stories)} stories, {len(CHAPTERS)} chapters')

if __name__=='__main__':build()
