# IEAB v0.4.4 — Preregistrare: modele mai mari din aceeași familie

**Data:** 2026-11-04 · **Stare:** scrisă **înainte** de orice apel la `qwen3.5-9b` sau `gemma-4-12b-it` cu stimuli IEAB. Fixată prin tag Git `ieab-v0.4.4-freeze`.
**Bază neschimbată:** design v0.4.1, amendamentele v0.4.2 și v0.4.3, cele 360 de prompturi, ordinea cheilor, setările cererii (temperature 0, top_k 40, seed 42, max_tokens 64, schema JSON), runnerul și regulile de execuție v0.4.3. Rezultatele v0.4.3 nu se modifică.

## 1. Ce se schimbă (numai tehnic)

- Se adaugă două configurații: `qwen3.5-9b` (pereche pentru `qwen3.5-4b`) și `gemma-4-12b-it` (pereche pentru `gemma-4-e4b-it`). Ambele sunt Q4_K_M, `lmstudio-community`, în LM Studio local. Thinking = OFF, verificat înainte de rulare.
- Timeout pe cerere: **300 s** (în loc de 120 s). Este doar un plafon tehnic: un timeout nu produce date, iar cheia se retrimite la reluare (v0.4.3, regula 3).
- Versiune și jurnale noi: `IEAB_v0.4.4`.

## 2. Întrebarea

Insensibilitatea la fiabilitate, numărarea afirmațiilor și reacția slabă la copiere, observate la modelele de 4–8B, se reduc când crește mărimea modelului în aceeași familie? Motivație: la Gao et al. (arXiv 2610.06192), modelele de frontieră integrează corect fiabilitatea `q` în probabilități, dar supraevaluează parțial copiile.

## 3. Măsuri și praguri de decizie fixate dinainte

Calculate mecanic de `implementation/analyze_v044.py` din exportul de 360 de rânduri. „Rep” = numărul de alegeri ale părții repetate din 16 (CORE, 8 itemi × 2 ordini).

**P1 — urmarea pragurilor normative de fiabilitate** (regula B1: la n=2 pragul e între r=.65 și .70; la n=3, între .60 și .65):
- n=2: `FOLLOWS` dacă Rep(.60) ≤ 4 **și** Rep(.65) ≤ 4 **și** Rep(.70) ≥ 12; `NOT_FOLLOWS` dacă Rep(.60) ≥ 8 **și** Rep(.65) ≥ 8; altfel `INTERMEDIATE`.
- n=3: `FOLLOWS` dacă Rep(.60) ≤ 4 **și** Rep(.65) ≥ 12 **și** Rep(.70) ≥ 12; `NOT_FOLLOWS` dacă Rep(.60) ≥ 8; altfel `INTERMEDIATE`.
- Referință v0.4.3 (verificată cu același script): toate trei modelele mici = `NOT_FOLLOWS` la n=2 și la n=3.

**P2 — normă versus numărare:** acord B1 și B3 pe 240 CORE. Referință: Qwen 4B 176 / 212; Gemma E4B 174 / 210.

**P3 — reacția la copiere (M6):** schimbări normative / perechi informative. Referință: Qwen 4B 35/92; Gemma E4B 13/95.

**P4 — direcția efectului de ordine (M5):** `FAVOURS_FIRST` / `FAVOURS_LAST` / `NONE`. Referință: Qwen 4B și Gemma E4B = `FAVOURS_FIRST`.

**P5 — ancore A1/A2:** raportate înaintea celorlalte, ca limită de interpretare (v0.4.1 §10).

## 4. Predicții (ipoteza mărimii)

| | Predicție | Confirmată dacă | Infirmată dacă |
|---|---|---|---|
| H1 | Modelul mare nu mai este `NOT_FOLLOWS` la n=2 | clasa n=2 ≠ `NOT_FOLLOWS` | clasa n=2 = `NOT_FOLLOWS` |
| H2 | Norma explică mai bine decât numărarea | acord B1 ≥ acord B3 | acord B1 < acord B3 |
| H3 | Reacție mai mare la copiere decât perechea mică | proporția P3 > proporția perechii mici | proporția P3 ≤ proporția perechii mici |
| H4 | Direcția ordinii se păstrează în familie | aceeași direcție P4 ca perechea mică | direcție diferită sau `NONE` |

Fiecare predicție se evaluează **separat pentru fiecare model**. Rezultatele confirmate și infirmate se raportează cu aceeași vizibilitate. H1–H3 decurg din ipoteza mărimii; H4 este o predicție de stabilitate în familie. P1 la n=3 se raportează descriptiv, fără predicție (la modelele mici a fost plafon).

## 5. Limite fixate dinainte

O singură rulare per model, 8 itemi, analiză descriptivă fără valori-p. Două modele per familie nu separă mărimea de alte diferențe de antrenare dintre versiuni. Un rezultat `INTERMEDIATE` sau o infirmare nu se reinterpretează post-hoc ca „aproape confirmat”. Dacă o rulare are răspunsuri invalide, se aplică acoperirea parțială din v0.4.2 §6, iar P1 devine `NOT_EVALUABLE` pentru celulele incomplete.

## 6. Ordinea de execuție

Tag `ieab-v0.4.4-freeze` → `py -3 test_behavioral_runner.py` → pentru fiecare model: `plan`, `run --limit 10 --send`, `status`, apoi `run --send` până la 360 → `export` → `py -3 analyze_v044.py <export>` → raport.
