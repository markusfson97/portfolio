# Markus portfolio – hemsida

Personlig portfolio för foto och film (Markus Fredriksson). Markus skriver på svenska, kort och slarvigt – svara på svenska, enkelt.

## Struktur
- `template.html` – själva sidan (HTML, CSS, JS). **Redigera här**, aldrig i `index.html`.
- `index.html` – byggd fil, en enda fil med alla bilder inbakade (base64). Skapas av `build.py`.
- `update.py` – läser bildmapparna i `../` (Markus hemsida), gör webbversioner av nya bilder till `img/p/`, skriver `active.json` och kör `build.py`.
- `build.py` – bygger `index.html` från `template.html` + bilderna i `img/p/f` + `img/me.jpg`.
- `order.json` – önskad ordning per kategori (`portratt`, `action`, `alla`). Bilder som inte står med hamnar sist.
- `img/me.jpg` – profilbilden (Kyoto).

## När Markus skriver "uppdatera"
Kör `pip install pillow` en gång, sedan `python3 update.py`. Den läser:
- `../Portraits` → fliken Portraits (prefix inget)
- `../Action sports` → fliken Action sports (prefix `a_`)
- `../Alla` → visas BARA under fliken All (prefix `x_`)
Raderade bilder försvinner, nya läggs till. Håll `index.html` under ~16 MB.

## Innehåll på sidan
- Topp: logga "Ligatur" (MF, inline SVG i h1) + Markus egen text + showreel (YouTube `_z1ZGzL__C8`).
- Om mig: bild till vänster, "Hey, I'm Markus!"-text till höger, sen rutor: 10,000+ photos delivered, 100+ film projects, Worldwide, Clients (bubbla med 8 kundlogos), Drone certified (bubbla: FPV/cinematic, EASA-approved, all-day aerial filming, national coverage, serious about safety).
- Flikar: All, Action sports, Videos, Portraits. Videos = 6 YouTube-kort (lista `VIDEOS` i template.html, med visningar och roller). Titeln på `GYmlskunkAk` är okänd ("Rezdar" som platshållare).
- Kontakt: "Let's work together" + mejl.
- Färger: marin `#040322`, blå `#0297DE`, orange `#FC734D`, med blå/orange glöd och korn (affischkänsla).
- Mörkt läge som standard, ljust via knappen. Mobilanpassad (sticky filterrad, 2 kolumner).

## YouTube
Inbäddade spelare fungerar bara på en riktig webbadress (http/https, inte claude.ai och inte file://).
`CAN_EMBED` i template.html styr det. På GitHub Pages spelas showreel och videor direkt på sidan.

## Publicering
Planen är GitHub Pages: repo `markusfson97/portfolio` (Markus behöver skapa det), Pages från `main` / root.
Lägg till `.nojekyll`. Det som ska ligga i repot är `index.html` (resten kan också ligga där).
