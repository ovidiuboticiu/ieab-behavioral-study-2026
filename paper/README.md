# Raportul IEAB — versiuni și statut

**Raportul științific final aprobat:** [IEAB_Raport_Stiintific_Final.pdf](IEAB_Raport_Stiintific_Final.pdf) (5 noiembrie 2026; ediția corectată v1.0.1, 18 pagini). Acesta este documentul recomandat pentru citire și citare.

**Sursa text a versiunii finale:** [IEAB_Raport_Stiintific_Final.md](IEAB_Raport_Stiintific_Final.md) (versiunea v7 după corecțiile editoriale și paginare). Acest fișier conține și instrucțiuni de machetare pentru PDF.

**Versiune anterioară:** `IEAB_RAPORT_STIINTIFIC_v4_CRONOLOGIE_2026-11-05.md` — păstrată fără modificări pentru istoricul editorial, dar **înlocuită de v7**; nu se recomandă citarea acesteia în locul raportului final.

**Licență:** CC BY 4.0 (pentru raport și sursele documentare), conform [LICENSES.md](../LICENSES.md). Nu s-au modificat designul, datele experimentale sau ipotezele preregistrate. Documentul este un raport tehnic descriptiv făcut public pe GitHub, nu o publicație evaluată prin peer review uman și nu un depozit Zenodo cu DOI.

## Corectura editorială v1.0.1 (22 noiembrie 2026)

PDF-ul a fost regenerat din aceeași sursă, după o verificare pagină cu pagină față de standardul editorial IEAB v7. Au fost corectate numai defecte de formatare:

- un rând care depășea marginea din dreapta (codul commitului de închidere) și acoladele rămase din conversie în jurul unui alt cod de commit;
- spații albe mari la final de pagină și titluri rămase izolate la baza paginii (4.2, Bibliografie);
- linkurile din bibliografie, care nu erau active;
- etichetele „Tabel. N.” înlocuite cu „Tabelul N.”, conform standardului; lățimea coloanelor din Tabelul 7;
- spațierea textului principal adusă exact la 1,5 rânduri.

Textul, cifrele, tabelele, rezultatele și concluziile nu au fost modificate; o comparație cuvânt cu cuvânt între cele două PDF-uri arată doar diferențe de paginare, despărțire în rânduri și eticheta tabelelor. Numărul de pagini a scăzut de la 19 la 18. Ediția v1.0.0 rămâne disponibilă neschimbată la eticheta git `v1.0.0`.

PDF-ul se poate reconstrui din sursă cu `sh paper/build/build.sh` (pandoc, XeLaTeX, fontul Tinos, echivalent metric cu Times New Roman).
