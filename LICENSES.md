# Licențe și domeniul lor de aplicare — IEAB

**Decizie aprobată de autor la 5 noiembrie 2026:** documentele, raportul, datele și stimulii sunt publicate sub **CC BY 4.0**, iar codul Python sub **MIT**. Sunt două licențe diferite, aplicate pe categorii de fișiere, nu o licență unică pentru întregul repository.

## 1. CC BY 4.0 (SPDX: CC-BY-4.0)

Se aplică următoarelor fișiere/directoare:
- `paper/`: raportul PDF final, sursa Markdown corespunzătoare și versiunile editoriale istorice;
- `data/`: toate cele cinci exporturi JSONL;
- `research/`: designul, amendamentele și preregistrarea;
- `implementation/dry_run_v0.4.1/`: stimuli, asignări și ordinea planificată (`.json` / `.jsonl`);
- `audit/`: rapoartele și rezultatele de recalculare asistată AI, în măsura drepturilor aplicabile;
- `README.md`, `PROVENIENTA_SI_CONTRIBUTII.md`, `REPRODUCERE.md`, `SHA256SUMS.txt` și `LICENSES.md`.

**Licență:** https://creativecommons.org/licenses/by/4.0/legalcode  
**Notificare:** [LICENSE-CONTENT-CC-BY-4.0.md](LICENSE-CONTENT-CC-BY-4.0.md)

Reutilizarea este permisă, inclusiv comercial, cu atribuire corectă, referința la licență și indicarea modificărilor. Aceasta nu oferă drepturi asupra materialelor terților care nu aparțin autorului.

## 2. MIT (SPDX: MIT)

Se aplică exclusiv codului Python păstrat în `implementation/`, în prezent:
- `implementation/analyze_v044.py`
- `implementation/behavioral_inputs.py`
- `implementation/behavioral_runner.py`

**Textul licenței:** [LICENSE-CODE-MIT.txt](LICENSE-CODE-MIT.txt)

La redistribuirea codului ori a unor porțiuni substanțiale ale sale, trebuie păstrate notificarea de copyright și licența MIT. Fișierele de intrare JSON/JSONL din același director nu intră sub MIT; acestea sunt CC BY 4.0.

## 3. Atribuire și asistență AI

**Autorul uman și operatorul experimentului:** Ovidiu Boticiu (Independent Researcher, Romania). Instrumentele ChatGPT, Claude și Codex au fost utilizate substanțial pentru proiectare, programare, analiză, verificare și redactare. Descrierea contribuțiilor se află în `PROVENIENTA_SI_CONTRIBUTII.md`; acest fapt nu constituie certificare peer review uman.

Mențiunea CC BY 4.0 sau MIT este o declarație de permisiune numai pentru drepturile pe care titularul le poate acorda. Conținutul bibliografic citat, mărcile și materialele provenite de la terți nu sunt relicențiate prin acest fișier. Nu se acordă nicio garanție privind completitudinea dovezilor experimentale.

## 4. Pentru Zenodo

La o eventuală depunere care conține atât cod, cât și documentație/date, se vor declara **ambele licențe** (CC-BY-4.0 și MIT), cu trimitere la această mapare. Înregistrarea Zenodo nu este încă publicată și nu are DOI.
