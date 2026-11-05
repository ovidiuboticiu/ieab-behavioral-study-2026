# Reproducerea aritmetică a rezultatelor IEAB

Aceste instrucțiuni **nu trimit cereri către modele** și nu refac experimentele; ele citesc cele cinci exporturi JSONL păstrate.

## Cerințe

- Python 3 instalat, fără pachete externe pentru analizorul `analyze_v044.py`.
- Fișierele originale din `implementation/dry_run_v0.4.1/` (în special `core_prompts_v0.4.1.jsonl`, `dependent_prompts_v0.4.1.jsonl` și `anchor_prompts_v0.4.1.jsonl`).
- Cele cinci exporturi complete cu câte 360 de rânduri `VALID`.

Din rădăcina repository-ului, în Windows PowerShell:

```powershell
py -3 .\implementation\analyze_v044.py .\data\v043\qwen3.5-4b-results.jsonl .\data\v043\gemma-run2-results.jsonl .\data\v043\ministral-results.jsonl .\data\v044\qwen3.5-9b-results.jsonl .\data\v044\gemma-4-12b-it-results.jsonl
```

Scriptul afișează **P1–P5** pentru fiecare configurație, inclusiv denominatoarele. Pragurile de decizie H1–H4 sunt în `research/DESIGN_IEAB_v0.4.4_PREREGISTRATION.md` și au fost fixate înaintea rulărilor v0.4.4 păstrate. Pentru v0.4.3, clasificarea P1 este o aplicare retrospectivă a acelorași criterii și nu o preregistrare istorică pentru acele modele.

Celelalte diagnostice M1–M6/B1–B7 sunt explicate în design și în raportul științific; recalcularea separată Codex se află în `audit/recalculare_independenta.json`. Fișierul JSON este un rezultat, **nu codul sursă** al recalculării Codex.

## Ce NU certifică această verificare

- Repetabilitatea alegerilor la o nouă execuție.
- Configurația binară exactă a modelului și parametrii efectivi din LM Studio.
- Validitatea inferențelor cauzale sau generalizarea la alte modele.
- Existența unei preregistrări publice independente.

Pentru v0.4.4, amprentele jurnalelelor brute sunt consemnate în rapoartele de proveniență; jurnalele nu sunt incluse în subsetul public minimal. Pentru v0.4.3, jurnalele nu au fost disponibile auditului Codex.
