# IEAB v0.4.3 — Amendament de execuție (DRAFT, o pagină)

**Data:** 2026-11-02 · **Stare:** DRAFT · NOT FROZEN · ZERO IEAB BEHAVIORAL DATA
**Bază:** `DESIGN_IEAB_v0.4.1.md` + `DESIGN_IEAB_v0.4.2_DRAFT.md`, ambele nemodificate. Acest text prevalează **numai** pentru regulile de execuție de mai jos. Știința (itemi, grilă, prompturi, schemă, setări, ordinea celor 360 de chei, analiză M1–M6, B1–B7) rămâne neschimbată.

## 1. De ce

Un apel către un model local, cu context nou, nu are efecte secundare. Un POST dublu nu strică datele. Singurul risc științific este **alegerea selectivă** între mai multe răspunsuri. Acesta se previne printr-o regulă fixată dinainte, nu prin blocarea endpointului. Regulile de blocaj din v0.4.1 §17.2/§17.4 și din v0.4.2 §2 (gate HELD/BLOCKED, barieră SEND_POSSIBLE, interdicția de retrimitere după rezultat incert) au oprit proiectul fără să protejeze o proprietate științifică.

## 2. Reguli noi (înlocuiesc v0.4.1 §17.1–17.4 și v0.4.2 §2, clasa D)

1. **Jurnal unic append-only** (JSONL) pentru fiecare model: fiecare cerere și fiecare răspuns brut, cu SHA-256 și oră, scrise și sincronizate pe disc înainte de pasul următor. Nimic nu se șterge sau rescrie.
2. **Primul răspuns complet contează.** Rezultatul unei chei este primul răspuns înregistrat cu HTTP 200 și modelul corect, clasificat VALID sau INVALID. Orice răspuns ulterior pentru aceeași cheie se păstrează și se raportează, dar nu se folosește niciodată.
3. **Retrimitere permisă doar fără răspuns complet.** O cheie trimisă, dar fără răspuns complet înregistrat (timeout, crash, server oprit), poate fi trimisă din nou la reluare. Fiindcă răspunsul eventual pierdut nu a fost văzut, nu există selecție. Numărul cheilor trimise de mai multe ori se raportează.
4. **Răspuns individual invalid** (v0.4.2 clasa B, neschimbat): final pentru cheia sa, fără retrimitere; rularea continuă.
5. **STOP sistemic** (v0.4.2 clasa C, neschimbat în spirit): model greșit în răspuns, HTTP ≠ 200, envelope ilizibil, eroare de transport sau pachet de intrare schimbat față de prima pornire. Răspunsul respectiv nu este rezultat științific. După corectare, rularea se reia de la aceeași cheie.
6. **Ordinea fixă.** Cheile se trimit în ordinea `schedule_v0.4.1.jsonl`, sărind doar cheile deja finalizate. `--limit N` oprește curat după N cereri; nu se regrupează pe condiții.
7. **Orbire.** Runnerul și `status` nu afișează alegerile. `export` refuză până când toate cele 360 de chei sunt finalizate. Operatorul nu deschide jurnalul brut în timpul colectării.
8. **Timeout: 120 s pe cerere**, identic cu setarea comună v0.4.1. Este un plafon tehnic, nu un criteriu comportamental: un timeout oprește rularea, iar cheia se retrimite la reluare (regula 3), deci nu reduce acoperirea.
9. **Un singur runner pe jurnal**, prin lock de sistem eliberat automat la moartea procesului (fără fișiere de blocaj de curățat manual).

## 3. Freeze ușor (înlocuiește cerințele de freeze din v0.4.1 §26, pentru execuție)

Înainte de primul `--send` cu stimuli IEAB: commit pe `main` cu runnerul, testele și acest amendament, plus un **tag Git** împins pe GitHub (de exemplu `ieab-v0.4.3-freeze`). Runnerul scrie în jurnal amprentele SHA-256 ale fișierelor de stimuli, ale programului și ale codului; orice schimbare ulterioară oprește rularea. Corectarea codului după start înseamnă versiune nouă și jurnal nou, cu raportarea celui vechi.

## 4. Ce nu se schimbă

Raportarea pe acoperire parțială din v0.4.2 §§3, 5, 6. Fără imputare, fără praguri post-hoc, fără folosirea alegerilor pentru a schimba prompturi, setări sau modele. Cele trei configurații folosesc același cod și aceleași setări.

## 5. Implementare și verificare

`implementation/behavioral_runner.py` + `implementation/test_behavioral_runner.py` (R1–R12, transport fals; plus calea HTTP reală verificată contra unui server local fals). Testele nu dovedesc comportamentul LM Studio real; primele chei reale (`--limit 10`) sunt verificarea tehnică, după care se citește doar `status`.
