# Изображения сайта

Изображения взяты из существующей финальной презентации, из папки `output/shadows-final-2026-10-28/deck/assets`. Новые изображения не скачивались и не генерировались.

WebP: quality 82, method 6; ширина не более 1600 px, для общего кадра `night.webp` — до 1920 px. Маленькие оригиналы не увеличены. Сохранены полная композиция, чёрные поля и существующие субтитры; кадрирования, ретуши и изменения лиц нет.

Подписи в `content/stories.json` различают кадры фильма, раннюю короткометражку, закулисные фотографии и поздние промоматериалы сериалов. Фотография не выдаётся за документальное доказательство рассказанного эпизода.

Кредиты и происхождение ниже перенесены из готовых материалов проекта. Они описывают источник, а не новую лицензию. Подробный исходный реестр: `output/asset-manifest.md`; дополнения: `output/approved-three-stories-research.md` и `deck-data.json`.

## Воспроизведение

Установите Pillow и выполните из корня сайта:

```sh
python3 scripts/prepare-content.py --source-dir '/путь/к/папке/презентации'
```

Команда обновляет только `content/stories.json`, перечисленные WebP и этот реестр. Тексты переносятся из `posts.json` без изменения; ссылки выбраны из одобренных фактов по теме каждой истории.

## Файлы и происхождение

### `c3po-luke-1977.webp`

- Оригинал: `c3po-luke-1977.jpg`; 1200×675 px.
- WebP: 1200×675 px; 65.1 КБ.
- Истории: 10.

Официальная галерея C-3PO: https://www.starwars.com/databank/c-3po . Подлинный кадр «Звёздных войн» (1977).

### `corridor-rig-2014-0354.webp`

- Оригинал: `corridor-rig-2014-0354.jpg`; 1680×1050 px.
- WebP: 1600×1000 px; 64.7 КБ.
- Истории: 18.

| A34 | `corridor-rig-2014-0354.jpg` | 1680×1050 | Слайд 11. Чистый кадр браузера на 03:54 из публичного видео Behind The Shadows о съёмках фильма 2014 года: [YouTube](https://www.youtube.com/watch?v=l3B4yXLxSPE&t=234s), контекст и ограничения — [S39](../04_sources_and_assets.md). Видна вращающаяся декорация коридора в металлических кольцах и на колёсах; рядом стоят два человека, действия персонажей нет. Чёрные полосы сохранены; размер — захват браузера, не исходное разрешение видео. Исходный браузерный JPEG оставлен отдельно; файл для презентации перекодирован в JPEG без кадрирования и изменения размера. Права повторного использования не подтверждены. |

### `cover.webp`

- Оригинал: `cover.jpg`; 4928×3280 px.
- WebP: 1600×1065 px; 249.4 КБ.
- Истории: 15.

| `cover.jpg` | A04–A07, исходный групповой портрет на лестнице для CSS-портретов Владислава, Виаго, Дикона и Петера | 4928×3280 | [Kinopoisk image endpoint](https://avatars.mds.yandex.net/get-kinopoisk-image/1773646/980461ea-8066-49a3-8c04-684f3f32b54d/orig); подпись из материалов проекта: кадр фильма, © Unison Films. Источник размещения — не правообладатель, лицензию повторно не проверяли.

### `deacon.webp`

- Оригинал: `deacon.jpg`; 4928×3280 px.
- WebP: 1600×1065 px; 129.3 КБ.
- Истории: 24.

| `deacon.jpg` | A06, отдельный кадр Дикона у контрабаса | 4928×3280 | [Kinopoisk image endpoint](https://avatars.mds.yandex.net/get-kinopoisk-image/1900788/be33b0d2-e31c-4aaa-ad1c-6b382406c55a/orig); подпись из материалов проекта: кадр фильма, © Unison Films. Источник размещения — не правообладатель, лицензию повторно не проверяли.

### `deacon-couch.webp`

- Оригинал: `deacon-couch.png`; 2532×1170 px.
- WebP: 1600×739 px; 33.0 КБ.
- Истории: 11.

| `deacon-couch.png` | A17, Дикон лежит на диване для слайда 8 | 2532×1170 | Кадр ранней короткометражки *Interviews with Some Vampires* (2005), опубликован в [обзоре Stand-Up Comedy Historian](https://www.standupcomedyhistorian.com/post/what-we-do-in-the-shadows-and-its-kiwi-spinoffs); [исходный PNG](https://static.wixstatic.com/media/3ba802_342b2c2305a542c28fac1061368811a6~mv2.png). Оригинал содержит чёрные поля и русские субтитры; в слайде они убираются кадрированием CSS. Сохранять указание на раннюю версию, не подписывать кадром полнометражного фильма 2014 года.

### `dracula_1992_poster.webp`

- Оригинал: `dracula_1992_poster.jpg`; 508×755 px.
- WebP: 508×755 px; 96.2 КБ.
- Истории: 09.

| *Bram Stoker's Dracula* (1992) | `dracula_1992_poster.jpg` | Full illustrated theatrical poster, Gary Oldman featured in costume art; not a character still | 508 × 755 | IMP Awards poster page: https://www.impawards.com/1992/dracula_ver3.html · Image: https://www.impawards.com/1992/posters/dracula_ver3.jpg · Credit IMP Awards as poster archive/source. |

### `dracula_first_edition_1897.webp`

- Оригинал: `dracula_first_edition_1897.jpg`; 4177×5818 px.
- WebP: 1600×2229 px; 952.3 КБ.
- Истории: 08.

| *Dracula* (1897) | `dracula_first_edition_1897.jpg` | Full image of the genuine yellow cloth first-edition cover with red title; not a film poster | 4,177 × 5,818 | Wikimedia Commons file page: https://commons.wikimedia.org/wiki/File:Dracula-First-Edition-1897.jpg · Original: https://upload.wikimedia.org/wikipedia/commons/e/e0/Dracula-First-Edition-1897.jpg · Commons identifies the source as the British Library Board and marks the scan public domain. |

### `filmstrip-0190.webp`

- Оригинал: `filmstrip-0190.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 73.5 КБ.
- Истории: 12.

| `filmstrip-0190.jpg` | A20, кадр 0190 — Петер, кинолента слайда 12 | 1920×1080 | [Cap-That, страница кадра](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0190.jpg); [оригинальный JPEG](https://s3.us-west-1.wasabisys.com/cap-that.com/tv/what-we-do-in-the-shadows/movie/images/what-we-do(2014)_0190.jpg). Подлинный кадр фильма 2014 года, используется один раз. Оригинал без ретуши, кадрирование CSS; архив просит ссылку на страницу кадра, права отдельно не проверяли.

### `filmstrip-0255.webp`

- Оригинал: `filmstrip-0255.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 60.2 КБ.
- Истории: 20.

| `filmstrip-0255.jpg` | A20, кадр 0255 — трое за столом, кинолента слайда 12 | 1920×1080 | [Cap-That, страница кадра](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0255.jpg); [оригинальный JPEG](https://s3.us-west-1.wasabisys.com/cap-that.com/tv/what-we-do-in-the-shadows/movie/images/what-we-do(2014)_0255.jpg). Подлинный кадр фильма 2014 года, используется один раз. Оригинал без ретуши, кадрирование CSS; архив просит ссылку на страницу кадра, права отдельно не проверяли.

### `filmstrip-0265.webp`

- Оригинал: `filmstrip-0265.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 36.1 КБ.
- Истории: 09.

| `filmstrip-0265.jpg` | A20, кадр 0265 — Владислав, кинолента слайда 12 | 1920×1080 | [Cap-That, страница кадра](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0265.jpg); [оригинальный JPEG](https://s3.us-west-1.wasabisys.com/cap-that.com/tv/what-we-do-in-the-shadows/movie/images/what-we-do(2014)_0265.jpg). Подлинный кадр фильма 2014 года, используется один раз. Оригинал без ретуши, кадрирование CSS; архив просит ссылку на страницу кадра, права отдельно не проверяли.

### `filmstrip-0269.webp`

- Оригинал: `filmstrip-0269.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 44.7 КБ.
- Истории: 20.

| `filmstrip-0269.jpg` | A20, кадр 0269 — Дикон, кинолента слайда 12 | 1920×1080 | [Cap-That, страница кадра](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0269.jpg); [оригинальный JPEG](https://s3.us-west-1.wasabisys.com/cap-that.com/tv/what-we-do-in-the-shadows/movie/images/what-we-do(2014)_0269.jpg). Подлинный кадр фильма 2014 года, используется один раз. Оригинал без ретуши, кадрирование CSS; архив просит ссылку на страницу кадра, права отдельно не проверяли.

### `heinous-crime-defendant-00-14.webp`

- Оригинал: `heinous-crime-defendant-00-14.jpg`; 640×360 px.
- WebP: 640×360 px; 10.6 КБ.
- Истории: 03.

Полный кадр Heinous Crime (2004), 640×360. Источник видео: https://www.youtube.com/watch?v=puy_UyUptqo ; публикация Flicks: https://www.flicks.co.nz/news/top-ten-48hours-winners/ . Роль и таймкод указаны в подписи истории.

### `heinous-crime-judge-01-24.webp`

- Оригинал: `heinous-crime-judge-01-24.jpg`; 640×360 px.
- WebP: 640×360 px; 12.8 КБ.
- Истории: 03.

Полный кадр Heinous Crime (2004), 640×360. Источник видео: https://www.youtube.com/watch?v=puy_UyUptqo ; публикация Flicks: https://www.flicks.co.nz/news/top-ten-48hours-winners/ . Роль и таймкод указаны в подписи истории.

### `heinous-crime-jury-member-02-36.webp`

- Оригинал: `heinous-crime-jury-member-02-36.jpg`; 640×360 px.
- WebP: 640×360 px; 6.1 КБ.
- Истории: 03.

Полный кадр Heinous Crime (2004), 640×360. Источник видео: https://www.youtube.com/watch?v=puy_UyUptqo ; публикация Flicks: https://www.flicks.co.nz/news/top-ten-48hours-winners/ . Роль и таймкод указаны в подписи истории.

### `heinous-crime-lawyer-03-04.webp`

- Оригинал: `heinous-crime-lawyer-03-04.jpg`; 640×360 px.
- WebP: 640×360 px; 8.0 КБ.
- Истории: 03.

Полный кадр Heinous Crime (2004), 640×360. Источник видео: https://www.youtube.com/watch?v=puy_UyUptqo ; публикация Flicks: https://www.flicks.co.nz/news/top-ten-48hours-winners/ . Роль и таймкод указаны в подписи истории.

### `karen-oleary-police-closeup.webp`

- Оригинал: `karen-oleary-police-closeup.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 54.6 КБ.
- Истории: 17.

| `karen-oleary-police-closeup.jpg` | A18, крупный план Карен О’Лири в полицейской форме для слайда 10 | 1920×1080 | Кадр полнометражного фильма *What We Do in the Shadows* (2014) из [покадрового архива cap-that.com, кадр 3621](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_3621.jpg); [исходный JPEG](https://s3.us-west-1.wasabisys.com/cap-that.com/tv/what-we-do-in-the-shadows/movie/images/what-we-do(2014)_3621.jpg). Архив просит указывать ссылку на его страницу. Карен находится в центре кадра, её лицо и форма хорошо видны.

### `kickstarter-authors-2015-0012.webp`

- Оригинал: `kickstarter-authors-2015-0012.jpg`; 1680×1050 px.
- WebP: 1600×1000 px; 54.4 КБ.
- Истории: 28.

| A33 | `kickstarter-authors-2015-0012.jpg` | 1680×1050 | Слайд 17. Полный кадр браузерного захвата на 00:12 видео [What We Do In The Shadows — US Kickstarter Video](https://www.youtube.com/watch?v=jYqz3VgZG2k), связанного с [кампанией Kickstarter](https://www.kickstarter.com/projects/1423546688/what-we-do-in-the-shadows-the-american-release). Тайка Вайтити стоит слева в узорчатой куртке; Джемейн Клемент — справа в очках и тёмном костюме. Видны головы обоих авторов, вампирского грима нет. Чёрные полосы сохранены, ресайза и файлового кадрирования нет; это разрешение захвата браузера, а не исходное разрешение видео. Права повторного использования отдельно не подтверждены. |

### `laptop.webp`

- Оригинал: `laptop.jpg`; 4928×3280 px.
- WebP: 1600×1065 px; 85.0 КБ.
- Истории: 16.

| `laptop.jpg` | A08, Стю за ноутбуком с Виаго; отдельный ракурс Виаго для слайда 7 | 4928×3280 | [Kinopoisk image endpoint](https://avatars.mds.yandex.net/get-kinopoisk-image/1777765/5dacba24-1130-4771-b581-f0350ae68fb5/orig); подпись из материалов проекта: кадр фильма, © Unison Films. Исходный файл-кандидат; лицензию повторно не проверяли.

### `night.webp`

- Оригинал: `night.jpg`; 1000×666 px.
- WebP: 1000×666 px; 68.9 КБ.
- Истории: 07.
- Также общий визуальный материал обложки сайта.

| `night.jpg` | A12, ночной городской кадр для финального слайда | 1000×666 | [Пресс-фото KUNC / NPR](https://npr.brightspotcdn.com/legacy/sites/kunc/files/201502/PressPhoto.jpg); кредит из материалов проекта: KUNC / © Unison Films.

### `nosferatu_1922.webp`

- Оригинал: `nosferatu_1922.jpg`; 705×900 px.
- WebP: 705×900 px; 33.7 КБ.
- Истории: 12.

| *Nosferatu* (1922) | `nosferatu_1922.jpg` | Actual film still; Max Schreck as Count Orlok, alone, non-graphic | 705 × 900 | Wikimedia Commons file page: https://commons.wikimedia.org/wiki/File:Max_Schreck_as_Count_Orlok_in_Nosferatu_%E2%80%93_Eine_Symphonie_des_Grauens_(1922).jpg · Original: https://upload.wikimedia.org/wikipedia/commons/9/95/Max_Schreck_as_Count_Orlok_in_Nosferatu_%E2%80%93_Eine_Symphonie_des_Grauens_%281922%29.jpg · Public Domain Mark listed on page. |

### `party-costumes-film-2014.webp`

- Оригинал: `party-costumes-film-2014.jpg`; 635×390 px.
- WebP: 635×390 px; 20.6 КБ.
- Истории: 06, 21.

| `party-costumes-film-2014.jpg` | 635×390 | [The Dissolve, интервью](https://thedissolve.com/features/interview/923-jemaine-clement-and-taika-waititi-on-their-years-i/); [исходный JPEG](https://d2ycltig8jwwee.cloudfront.net/features/923/detail.402ca0fb.jpg). Подлинный кадр фильма 2014 года с Клементом и Вайтити в вампирских костюмах. На экране подписан «Кадр фильма · 2014»; иллюстрирует костюмы. Архивного фото реальной вечеринки не найдено. Разрешение источника умеренное; исходник сохранён целиком без увеличения файла. |

### `party-house-meeting-2014-0300.webp`

- Оригинал: `party-house-meeting-2014-0300.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 60.4 КБ.
- Истории: 14.

| `party-house-meeting-2014-0300.jpg` | 1920×1080 | [Cap-That, кадр 0300](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0300.jpg); [исходный JPEG](https://s3.us-west-1.wasabisys.com/cap-that.com/tv/what-we-do-in-the-shadows/movie/images/what-we-do(2014)_0300.jpg). Подлинный кадр фильма 2014 года, трое соседей за столом; не буквальное мытьё посуды. Архив просит ссылку на страницу кадра. |

### `peter-on-ship.webp`

- Оригинал: `peter-on-ship.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 100.5 КБ.
- Истории: 22.

| `peter-on-ship.jpg` | A10, кадр 0730 с Петером на палубе, слайд 13 | 1920×1080 | [Cap-That, кадр 0730](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0730.jpg). Подлинный кадр начальных титров; оригинал без ретуши и обрезки. Архив просит ссылку на страницу кадра; права отдельно не проверяли.

### `script-bts-2014.webp`

- Оригинал: `script-bts-2014.jpg`; 800×400 px.
- WebP: 800×400 px; 21.8 КБ.
- Истории: 13.

| A29 | `script-bts-2014.jpg` | 800×400 | Слайд 9. Закулисное фото из статьи [Monster Complex](https://www.monstercomplex.com/blog/making-what-we-do-in-the-shadows-behind-the-scenes-of-the-original-movie), [исходное изображение](https://images.squarespace-cdn.com/content/v1/5e613d28fefad366b93ece35/e1b06630-1c9f-4940-941e-2d7b1f316c78/What-We-Do-In-The-Shadows-BTS.jpg). Люди на фото не подписаны. Это контекст производства, а не визуальное доказательство того, что актёрам не показывали сценарий. CDN отдаёт WebP; локальная JPEG-копия сохранена с исходным размером и кадрированием. Права повторного использования не установлены. |

### `set-building-2014-0400.webp`

- Оригинал: `set-building-2014-0400.jpg`; 1680×1050 px.
- WebP: 1600×1000 px; 51.8 КБ.
- Истории: 19.

| A30 | `set-building-2014-0400.jpg` | 1680×1050 | Слайд 11. Кадр публичного видео Behind The Shadows о создании фильма 2014 года: [YouTube, фактический кадр 04:01](https://www.youtube.com/watch?v=l3B4yXLxSPE&t=241s). В павильоне участники группы поднимают большую окрашенную панель. Это полный кадр захвата браузера с чёрными полосами, не исходное разрешение видео; полосы сохранены, файлового кадрирования нет. Имя файла сохраняет согласованный маркер `0400`, фактическая метка кадра — 04:01. Видео опубликовано публичным репостом; права отдельно не подтверждены. |

### `set-empty-interior-2014.webp`

- Оригинал: `set-empty-interior-2014.jpg`; 1200×900 px.
- WebP: 1200×900 px; 81.8 КБ.
- Истории: 18.

| A35 | `set-empty-interior-2014.jpg` | 1200×900 | **Принято; полноразмерно проверено root.** Фото «Finished Set» из оригинального раздела фильма 2014 года в [портфолио Ra Vincent Workshop](https://www.ravincentworkshop.com/work-1); [исходное изображение](https://images.squarespace-cdn.com/content/v1/5bd830b9ebfc7f8841dba818/1540895246631-MWVCNFLWMJQKIKOMZLB5/img_5115.jpg?format=2500w). Пустой физический холл, лестница слева, открытая центральная дверь с креслом в глубине и часы справа; людей в комнате и соседних дверных проёмах нет. Портреты в рамах — часть декорации. Исходный WebP сохранён; JPEG преобразован в том же размере без кадрирования или увеличения. SHA-256 JPEG: `2ea9ae8d4cb560e758fb3802176e4db7dbff5c580389cdd1b3f3b63cea73a50f`. Старый кандидат `img_5116` с фигурой в глубине коридора отклонён и сохранён только во внутренних исследовательских материалах; аудитории не показывать. Права повторного использования не установлены. |

### `shadows-2019-promo.webp`

- Оригинал: `shadows-2019-promo.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 169.5 КБ.
- Истории: 30.

Официальный промокадр шестого сезона, © Disney: https://prensa.disneylatino.com/imagenes/what-we-do-in-the-shadows . В материалах источника отмечено редакционное использование; 2019 — год старта сериала, не дата кадра.

### `short-2005-clement-interview-0015.webp`

- Оригинал: `short-2005-clement-interview-0015.jpg`; 480×360 px.
- WebP: 480×360 px; 13.0 КБ.
- Истории: 04.

Кадр Interviews with Some Vampires (2005). Публичная запись: https://www.youtube.com/watch?v=_ess6DdPHaw ; каталог ACMI: https://www.acmi.net.au/works/178--what-we-do-in-the-shadows-interviews-with-some-vampires/ . Из существующего оригинала презентации: ранее убраны только боковые чёрные поля.

### `short-2005-viago-living-room-0530.webp`

- Оригинал: `short-2005-viago-living-room-0530.jpg`; 480×360 px.
- WebP: 480×360 px; 13.0 КБ.
- Истории: 05.

Кадр Interviews with Some Vampires (2005). Публичная запись: https://www.youtube.com/watch?v=_ess6DdPHaw ; каталог ACMI: https://www.acmi.net.au/works/178--what-we-do-in-the-shadows-interviews-with-some-vampires/ . Из существующего оригинала презентации: ранее убраны только боковые чёрные поля.

### `spinal_tap_1984_poster.webp`

- Оригинал: `spinal_tap_1984_poster.jpg`; 517×755 px.
- WebP: 517×755 px; 50.9 КБ.
- Истории: 08.

| *This Is Spinal Tap* (1984) | `spinal_tap_1984_poster.jpg` | Full illustrated theatrical poster; band group image, no sensitive content | 517 × 755 | IMP Awards poster page: https://www.impawards.com/1984/this_is_spinal_tap.html · Image: https://www.impawards.com/1984/posters/this_is_spinal_tap.jpg · Credit IMP Awards as poster archive/source. |

### `sundance.webp`

- Оригинал: `sundance.jpg`; 640×640 px.
- WebP: 640×640 px; 26.8 КБ.
- Истории: 02.

| `sundance.jpg` | A02, совместное фото Тайки Вайтити и Джемейна Клемента; также может обозначать этап 2014 года в таймлайне | 640×640 | Исходный кредит проекта: Courtney Young, 2014; [публикация изображения](https://worldoftaika.com/wp-content/uploads/2014/01/d5-young2.jpg). На снимке авторы на сцене; конкретное событие не подтверждено, поэтому не подписывать его как Sundance.

### `title-poster-en.webp`

- Оригинал: `title-poster-en.jpg`; 509×755 px.
- WebP: 509×755 px; 49.6 КБ.
- Истории: 26.

| A31 | `title-poster-en.jpg` | 509×755 | Слайд 15. Англоязычный постер новозеландского проката 2014 года; композиция с персонажами в гробах. [Архив IMP Awards](https://www.impawards.com/intl/new_zealand/2014/what_we_do_in_the_shadows_ver7.html), [изображение](https://www.impawards.com/intl/new_zealand/2014/posters/what_we_do_in_the_shadows_ver7.jpg). Файл без обрезки и увеличения; права на постер не установлены. |

### `title-poster-ru-2015.webp`

- Оригинал: `title-poster-ru-2015.jpg`; 1080×1543 px.
- WebP: 1080×1543 px; 246.1 КБ.
- Истории: 26.

| A32 | `title-poster-ru-2015.jpg` | 1080×1543 | Слайд 15. Русский прокатный постер 2015 года с лестничной композицией, зачёркнутым словом «сага», слоганом «Запрещено для оборотней» и датой 16.04.2015. Источник: [Kinoafisha, подборка постеров](https://www.kinoafisha.info/selections/komedii-pro-vampirov/), [страница фильма](https://www.kinoafisha.info/movies/8172119/), [изображение](https://static.kinoafisha.info/k/movie_posters/1080x1920/upload/movie_posters/9/1/1/8172119/fba17f8088780228c8df7b2a790da0aa.jpg). Исходное изображение без изменения размера и кадрирования; права на постер не установлены. |

### `title-trio.webp`

- Оригинал: `title-trio.jpg`; 1500×998 px.
- WebP: 1500×998 px; 118.9 КБ.
- Истории: 01, 25.
- Также общий визуальный материал обложки сайта.

| `title-trio.jpg` | A01, горизонтальный титульный кадр с Виаго, Диконом и Владиславом | 1500×998 | [GeekTyrant, публикация о фильме](https://geektyrant.com/news/what-we-do-in-the-shadows-watch-first-6-minutes-of-the-vampire-mockumentary); [исходный файл](https://images.squarespace-cdn.com/content/v1/51b3dc8ee4b051b96ceb10de/1414447235541-1LLXBIPRL8F8VOGSJQFX/image-asset.jpeg?format=1500w). В статье не указаны фотограф и правообладатель; подпись в презентации должна обозначать кадр фильма и сохранять эту оговорку до проверки прав.

### `tuatara-delicious-neck-2014.webp`

- Оригинал: `tuatara-delicious-neck-2014.jpg`; 760×925 px.
- WebP: 760×925 px; 124.4 КБ.
- Истории: 29.

Фото из обзора buzz and hum, 20.07.2014: https://buzzandhum.wordpress.com/2014/07/20/tuatara-delicious-neck/ . Подлинная бутылка, не официальный промоснимок.

### `vampires-1967.webp`

- Оригинал: `vampires-1967.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 80.2 КБ.
- Истории: 23.

| `vampires-1967.jpg` | A10c, групповая фотография с карточками, кадр 0746, слайд 13 | 1920×1080 | [Cap-That, кадр 0746](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0746.jpg). Подлинный кадр начальных титров; оригинал без ретуши и обрезки. Архив просит ссылку на страницу кадра; права отдельно не проверяли.

### `vampires-group.webp`

- Оригинал: `vampires-group.jpg`; 1920×1080 px.
- WebP: 1600×900 px; 164.3 КБ.
- Истории: 22.

| `vampires-group.jpg` | A10b, групповая фотография, кадр 0740, слайд 13 | 1920×1080 | [Cap-That, кадр 0740](https://www.cap-that.com/what-we-do-in-the-shadows/movie/index.php?image=what-we-do%282014%29_0740.jpg). Подлинный кадр начальных титров; оригинал без ретуши и обрезки. Архив просит ссылку на страницу кадра; права отдельно не проверяли.

### `viago-toast.webp`

- Оригинал: `viago-toast.jpg`; 4928×3280 px.
- WebP: 1600×1065 px; 108.8 КБ.
- Истории: 10, 27.

| `viago-toast.jpg` | A05, отдельный кадр Виаго для слайда о его характере | 4928×3280 | [KPBS, фото и подпись](https://www.kpbs.org/news/arts-culture/2015/02/20/what-we-do-shadows-sheds-light-modern-vampire-life); [исходный файл](https://cdn.kpbs.org/img/photos/2015/02/19/Taika_Waititi_WHAT_WE_DO_IN_THE_SHADOWS_Photo_Credit_Unison_Films.jpg). Страница KPBS подписывает изображение как Таика Вайтити в роли Виаго и указывает Paladin Pictures; имя файла несёт кредит Unison Films.

### `voice-vartanov.webp`

- Оригинал: `voice-vartanov.jpg`; 1500×1000 px.
- WebP: 1500×1000 px; 69.5 КБ.
- Истории: 27.

Александр Вартанов, фото PhotoXPress. Публикация: https://daily.afisha.ru/cinema/3647-kak-hardkornoe-russkoe-kino-sovpalo-s-tragediey-s-pskovskimi-shkolnikami/ .

### `wellington-paranormal-poster.webp`

- Оригинал: `wellington-paranormal-poster.jpg`; 1365×2048 px.
- WebP: 1365×2048 px; 177.1 КБ.
- Истории: 30.

Официальный промоарт второго сезона, Bell Media / New Zealand Documentary Board: https://www.bellmedia.ca/the-lede/tv/crave/wellington-paranormal/ . Год старта сериала — 2018, это не дата снимка.

