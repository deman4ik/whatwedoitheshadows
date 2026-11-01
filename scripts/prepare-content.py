#!/usr/bin/env python3
"""Prepare the reader's approved copy and existing images. Requires Pillow.

Run from any directory:
  python3 scripts/prepare-content.py --source-dir /path/to/presentation-workspace

Only content/stories.json, assets/images/*.webp and assets/ASSETS.md are written.
No network requests, cropping, compositing, retouching or image upscaling.
"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageOps


def media(name, alt, caption):
    return {"src": "assets/images/" + Path(name).stem + ".webp", "alt": alt, "caption": caption}


MEDIA = {
    1: [media("title-trio.jpg", "Виаго, Дикон и Владислав в доме", "Кадр фильма «Реальные упыри» (2014).")],
    2: [media("sundance.jpg", "Тайка Вайтити и Джемейн Клемент на сцене", "Тайка Вайтити и Джемейн Клемент. Фото Courtney Young, 2014; конкретное событие не установлено.")],
    3: [
        media("heinous-crime-judge-01-24.jpg", "Тайка Вайтити в роли судьи", "Heinous Crime (2004): судья, 01:24."),
        media("heinous-crime-defendant-00-14.jpg", "Тайка Вайтити в роли подсудимого", "Heinous Crime (2004): подсудимый, 00:14."),
        media("heinous-crime-lawyer-03-04.jpg", "Тайка Вайтити в роли адвоката", "Heinous Crime (2004): адвокат, 03:04."),
        media("heinous-crime-jury-member-02-36.jpg", "Тайка Вайтити в роли присяжного", "Heinous Crime (2004): присяжный, 02:36."),
    ],
    4: [media("short-2005-clement-interview-0015.jpg", "Клемент в вампирском образе ранней короткометражки", "Джемейн Клемент в короткометражке Interviews with Some Vampires (2005), 00:15.")],
    5: [media("short-2005-viago-living-room-0530.jpg", "Виаго в гостиной в ранней короткометражке", "Ранняя короткометражка Interviews with Some Vampires (2005), 05:30.")],
    6: [media("party-costumes-film-2014.jpg", "Вайтити и Клемент в вампирских костюмах", "Кадр фильма 2014 года. Иллюстрация костюмов, не фотография той вечеринки.")],
    7: [media("night.jpg", "Трое вампиров на ночной городской улице", "Промокадр фильма «Реальные упыри» (2014), © Unison Films. Источник: KUNC / NPR.")],
    8: [media("dracula_first_edition_1897.jpg", "Жёлтая обложка первого издания романа Дракула", "Первое издание «Дракулы» Брэма Стокера, 1897. British Library / Wikimedia Commons."), media("spinal_tap_1984_poster.jpg", "Постер фильма Это — Spinal Tap", "«Это — Spinal Tap» (1984). Постер из архива IMP Awards.")],
    9: [media("filmstrip-0265.jpg", "Клемент в образе Владислава", "Владислав в «Реальных упырях» (2014). Кадр: Cap-That."), media("dracula_1992_poster.jpg", "Постер Дракулы Фрэнсиса Форда Копполы", "«Дракула» (1992). Постер из архива IMP Awards.")],
    10: [media("viago-toast.jpg", "Тайка Вайтити в роли Виаго", "Тайка Вайтити — Виаго. Фото: Unison Films / Paladin Pictures, публикация KPBS."), media("c3po-luke-1977.jpg", "C-3PO рядом с Люком Скайуокером на Татуине", "C-3PO и Люк в «Звёздных войнах» (1977). Официальная галерея StarWars.com.")],
    11: [media("deacon-couch.png", "Дикон лежит на диване", "Дикон в ранней короткометражке Interviews with Some Vampires (2005). Это кадр фильма, не запись пробного интервью.")],
    12: [media("filmstrip-0190.jpg", "Бен Фрэншем в гриме Петера", "Петер в «Реальных упырях» (2014). Кадр: Cap-That."), media("nosferatu_1922.jpg", "Макс Шрек в образе графа Орлока", "Граф Орлок, «Носферату» (1922). Wikimedia Commons.")],
    13: [media("script-bts-2014.jpg", "Закулисное фото производства Реальных упырей", "Закулисное фото фильма, опубликованное Monster Complex. Люди на снимке в источнике не подписаны.")],
    14: [media("party-house-meeting-2014-0300.jpg", "Вампиры за столом во время домашнего собрания", "Сцена домашнего собрания в фильме (2014). Кадр: Cap-That.")],
    15: [media("cover.jpg", "Четверо главных вампиров на лестнице", "Промофотография героев «Реальных упырей» (2014), © Unison Films.")],
    16: [media("laptop.jpg", "Стю и Виаго рядом с ноутбуком", "Стю Резерфорд и Тайка Вайтити в фильме (2014), © Unison Films.")],
    17: [media("karen-oleary-police-closeup.jpg", "Карен О’Лири в полицейской форме", "Карен О’Лири в «Реальных упырях» (2014). Кадр: Cap-That.")],
    18: [media("set-empty-interior-2014.jpg", "Пустая декорация вампирского дома с лестницей и часами", "Готовая декорация дома. Фото из портфолио Ra Vincent Workshop."), media("corridor-rig-2014-0354.jpg", "Декорация коридора в больших металлических кольцах на колёсах", "Вращающийся коридор. Кадр фильма о съёмках Behind The Shadows, 03:54.")],
    19: [media("set-building-2014-0400.jpg", "Съёмочная группа поднимает стеновую панель в павильоне", "Строительство декорации: Behind The Shadows, 04:01. Закулисный контекст, не пример ретуши лиц.")],
    20: [media("filmstrip-0255.jpg", "Трое вампиров сидят за домашним столом", "Кадр готового фильма (2014), Cap-That. Не удалённый эпизод."), media("filmstrip-0269.jpg", "Дикон во время домашнего разговора", "Кадр готового фильма (2014), Cap-That. Не удалённый эпизод.")],
    21: [media("party-costumes-film-2014.jpg", "Вампиры Виаго и Владислав в своих костюмах", "Кадр фильма (2014). Иллюстрация вампирского гардероба, не удалённая сцена с превращением.")],
    22: [media("peter-on-ship.jpg", "Петер на палубе парусника в старой фотографии", "Петер на палубе: изображение из начальных титров фильма. Кадр: Cap-That."), media("vampires-group.jpg", "Стилизованная старая групповая фотография вампиров", "Ещё одна фотография из начальных титров «Реальных упырей». Кадр: Cap-That.")],
    23: [media("vampires-1967.jpg", "Групповая фотография вампиров с карточками года", "Изображение из начальных титров фильма, где звучит You’re Dead. Кадр: Cap-That.")],
    24: [media("deacon.jpg", "Дикон у контрабаса в доме вампиров", "Дикон в интерьере «Реальных упырей» (2014), © Unison Films. Кадр фильма, не фотография композиторов.")],
    25: [media("title-trio.jpg", "Виаго, Дикон и Владислав в кадре фильма", "«Реальные упыри» (2014). «Ласточка» звучит в финальных титрах этого фильма.")],
    26: [media("title-poster-en.jpg", "Англоязычный прокатный постер What We Do in the Shadows", "Постер новозеландского проката, 2014. Архив IMP Awards."), media("title-poster-ru-2015.jpg", "Российский прокатный постер Реальные упыри", "Российский постер с датой выхода 16.04.2015. Источник: Kinoafisha.")],
    27: [media("voice-vartanov.jpg", "Режиссёр Александр Вартанов", "Александр Вартанов — голос Виаго и режиссёр дубляжа. Фото PhotoXPress, публикация «Афиши Daily»."), media("viago-toast.jpg", "Виаго с поднятой рукой в доме", "Виаго в исполнении Тайки Вайтити. Фото: Unison Films / Paladin Pictures, KPBS.")],
    28: [media("kickstarter-authors-2015-0012.jpg", "Тайка Вайтити и Джемейн Клемент в ролике кампании Kickstarter", "Авторы в видео кампании на американский прокат фильма, 2015; кадр 00:12.")],
    29: [media("tuatara-delicious-neck-2014.jpg", "Бутылка Delicious Neck с Петером на этикетке рядом с бокалом", "Delicious Neck, Tuatara. Фото из обзора buzz and hum от 20 июля 2014 года; не официальный рекламный снимок.")],
    30: [media("wellington-paranormal-poster.jpg", "Полицейские сериала Паранормальный Веллингтон на промопостере", "«Паранормальный Веллингтон»: промоарт второго сезона. Bell Media / New Zealand Documentary Board."), media("shadows-2019-promo.jpg", "Герои американского сериала Чем мы заняты в тени", "«Чем мы заняты в тени»: промокадр шестого сезона, © Disney. Сериал стартовал в 2019 году.")],
}


# Relevant supporting sources selected from approved slide facts/extra and research.
SOURCE_SELECTION = {
    1: [(1, "www.nzfilm.co.nz"), (5, "thedissolve.com")],
    2: [(2, "thedissolve.com")],
    3: [(3, "www.nzonscreen.com"), (3, "gcm.co.nz")],
    4: [(3, "0vYzGu2X68s")],
    5: [(4, "www.nzfilm.co.nz"), (4, "www.sbs.com.au")],
    6: [(5, "wegotthiscovered.com"), (5, "thedissolve.com")],
    7: [(5, "vancouver.citynews.ca")],
    8: [(6, "filmreviews.net.au"), (6, "cfZR8o4TU5I"), (6, "screenanarchy.com")],
    9: [(7, "thedissolve.com")],
    10: [(7, "thedissolve.com"), (7, "www.finaldraft.com")],
    11: [(7, "www.interviewmagazine.com")],
    12: [(7, "www.fangoria.com"), (7, "www.filmlinc.org"), (7, "www.bfi.org.uk")],
    13: [(8, "www.interviewmagazine.com"), (8, "thedissolve.com"), (8, "t=661s")],
    14: [(8, "t=394s")],
    15: [(9, "www.denofgeek.com")],
    16: [(9, "thatshelf.com"), (9, "www.theguardian.com")],
    17: [(9, "www.nzonscreen.com"), (9, "gayexpress.co.nz")],
    18: [(10, "www.sbs.com.au"), (10, "www.filmlinc.org"), (10, "www.youtube.com")],
    19: [(10, "www.fangoria.com")],
    20: [(11, "www.interviewmagazine.com"), (11, "www.nzfilm.co.nz"), (11, "www.bafta.org")],
    21: [(11, "www.dreadcentral.com")],
    22: [(12, "www.comingsoon.net"), (12, "www.shutterstock.com")],
    23: [(13, "music.apple.com/us/song"), (13, "www.mic.com")],
    24: [(13, "www.plan9.co.nz"), (10, "www.sbs.com.au")],
    25: [(13, "www.kommersant.ru"), (13, "music.apple.com/us/song"), (13, "www.plan9.co.nz")],
    26: [(14, "2015/03/19"), (14, "2015/04/17"), (14, "lumiere.su")],
    27: [(15, "who_is/voice/"), (15, "who_is/voice_director"), (15, "cinemaplex.ru")],
    28: [(16, "www.kickstarter.com")],
    29: [(17, "stoppress.co.nz"), (17, "buzzandhum.wordpress.com")],
    30: [(19, "www.nzonscreen.com"), (19, "about.rogers.com")],
}


# Provenance for images not indexed as a table row in the main asset manifest.
EXTRA_PROVENANCE = {
    "c3po-luke-1977": "Официальная галерея C-3PO: https://www.starwars.com/databank/c-3po . Подлинный кадр «Звёздных войн» (1977).",
    "tuatara-delicious-neck-2014": "Фото из обзора buzz and hum, 20.07.2014: https://buzzandhum.wordpress.com/2014/07/20/tuatara-delicious-neck/ . Подлинная бутылка, не официальный промоснимок.",
    "voice-vartanov": "Александр Вартанов, фото PhotoXPress. Публикация: https://daily.afisha.ru/cinema/3647-kak-hardkornoe-russkoe-kino-sovpalo-s-tragediey-s-pskovskimi-shkolnikami/ .",
    "wellington-paranormal-poster": "Официальный промоарт второго сезона, Bell Media / New Zealand Documentary Board: https://www.bellmedia.ca/the-lede/tv/crave/wellington-paranormal/ . Год старта сериала — 2018, это не дата снимка.",
    "shadows-2019-promo": "Официальный промокадр шестого сезона, © Disney: https://prensa.disneylatino.com/imagenes/what-we-do-in-the-shadows . В материалах источника отмечено редакционное использование; 2019 — год старта сериала, не дата кадра.",
}


def chapter(story_id):
    for name, lower, upper in [("intro", 1, 1), ("origins", 2, 8), ("housemates", 9, 12), ("people", 13, 17), ("craft", 18, 22), ("sound", 23, 27), ("afterlife", 28, 30)]:
        if lower <= story_id <= upper:
            return name
    raise ValueError("Unexpected story id: %s" % story_id)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    source = args.source_dir.resolve()
    target = Path(__file__).resolve().parents[1]
    posts = json.loads((source / "output/social-posts-2026-11-02/posts.json").read_text(encoding="utf-8"))
    deck = json.loads((source / "output/shadows-final-2026-10-28/deck-data.json").read_text(encoding="utf-8"))
    slides = {s["n"]: s for s in deck["slides"]}
    originals = source / "output/shadows-final-2026-10-28/deck/assets"
    stories = []
    for post in posts:
        number = post["id"]
        refs = []
        for slide_id, token in SOURCE_SELECTION[number]:
            facts = slides[slide_id].get("facts", []) + slides[slide_id].get("extra", [])
            match = next((f for f in facts if token in f.get("url", "")), None)
            if not match:
                raise ValueError("Missing source %s for story %s" % (token, number))
            refs.append({"title": match.get("source") or match.get("src") or "Источник", "url": match["url"]})
        stories.append({
            "id": number, "slug": post["slug"], "title": post["title"],
            "kicker": post["kicker"], "paragraphs": post["caption"].split("\n\n"),
            "chapter": chapter(number), "media": MEDIA[number], "sources": refs,
        })
    (target / "content").mkdir(exist_ok=True)
    (target / "assets/images").mkdir(parents=True, exist_ok=True)
    (target / "content/stories.json").write_text(json.dumps({"stories": stories}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    needed = {Path(m["src"]).stem for s in stories for m in s["media"]} | {"night", "title-trio"}
    source_files = {p.stem: p for p in originals.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}}
    manifest = (source / "output/asset-manifest.md").read_text(encoding="utf-8")
    notes = [
        "# Изображения сайта", "",
        "Изображения взяты из существующей финальной презентации, из папки `output/shadows-final-2026-10-28/deck/assets`. Новые изображения не скачивались и не генерировались.", "",
        "WebP: quality 82, method 6; ширина не более 1600 px, для общего кадра `night.webp` — до 1920 px. Маленькие оригиналы не увеличены. Сохранены полная композиция, чёрные поля и существующие субтитры; кадрирования, ретуши и изменения лиц нет.", "",
        "Подписи в `content/stories.json` различают кадры фильма, раннюю короткометражку, закулисные фотографии и поздние промоматериалы сериалов. Фотография не выдаётся за документальное доказательство рассказанного эпизода.", "",
        "Кредиты и происхождение ниже перенесены из готовых материалов проекта. Они описывают источник, а не новую лицензию. Подробный исходный реестр: `output/asset-manifest.md`; дополнения: `output/approved-three-stories-research.md` и `deck-data.json`.", "",
        "## Воспроизведение", "",
        "Установите Pillow и выполните из корня сайта:", "", "```sh", "python3 scripts/prepare-content.py --source-dir '/путь/к/папке/презентации'", "```", "",
        "Команда обновляет только `content/stories.json`, перечисленные WebP и этот реестр. Тексты переносятся из `posts.json` без изменения; ссылки выбраны из одобренных фактов по теме каждой истории.", "",
        "## Файлы и происхождение", "",
    ]
    total = 0
    for stem in sorted(needed):
        original = source_files[stem]
        destination = target / "assets/images" / (stem + ".webp")
        with Image.open(original) as image:
            image = ImageOps.exif_transpose(image)
            old_size = image.size
            max_width = 1920 if stem == "night" else 1600
            if image.width > max_width:
                image = image.resize((max_width, round(image.height * max_width / image.width)), Image.Resampling.LANCZOS)
            image = image.convert("RGBA" if image.mode == "RGBA" else "RGB")
            image.save(destination, format="WEBP", quality=82, method=6)
            size = image.size
        file_size = destination.stat().st_size
        total += file_size
        used = [str(s["id"]).zfill(2) for s in stories if any(Path(m["src"]).stem == stem for m in s["media"])]
        notes.extend(["### `%s.webp`" % stem, "", "- Оригинал: `%s`; %s×%s px." % (original.name, *old_size), "- WebP: %s×%s px; %s КБ." % (*size, round(file_size / 1024, 1)), "- Истории: %s." % ", ".join(used)])
        if stem in {"night", "title-trio"}:
            notes.append("- Также общий визуальный материал обложки сайта.")
        provenance = EXTRA_PROVENANCE.get(stem)
        if not provenance:
            rows = [line for line in manifest.splitlines() if line.startswith("|") and ("`" + original.name + "`") in line]
            if rows:
                provenance = rows[0]
        if stem.startswith("heinous-crime-"):
            provenance = "Полный кадр Heinous Crime (2004), 640×360. Источник видео: https://www.youtube.com/watch?v=puy_UyUptqo ; публикация Flicks: https://www.flicks.co.nz/news/top-ten-48hours-winners/ . Роль и таймкод указаны в подписи истории."
        if stem.startswith("short-2005-"):
            provenance = "Кадр Interviews with Some Vampires (2005). Публичная запись: https://www.youtube.com/watch?v=_ess6DdPHaw ; каталог ACMI: https://www.acmi.net.au/works/178--what-we-do-in-the-shadows-interviews-with-some-vampires/ . Из существующего оригинала презентации: ранее убраны только боковые чёрные поля."
        if not provenance:
            raise ValueError("Missing image provenance: " + stem)
        notes.extend(["", provenance, ""])
    (target / "assets/ASSETS.md").write_text("\n".join(notes) + "\n", encoding="utf-8")
    print("Prepared %s stories, %s images, %.2f MiB" % (len(stories), len(needed), total / 1024 / 1024))


if __name__ == "__main__":
    main()
