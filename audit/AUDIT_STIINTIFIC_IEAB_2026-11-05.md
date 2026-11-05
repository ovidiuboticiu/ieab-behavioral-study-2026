# Audit științific independent — IEAB v0.4.3 + v0.4.4
Data: 5 noiembrie 2026. Evaluare pe materialele existente; zero apeluri către modelele experimentale.

**Verdict editorial: B — raport tehnic/descriptiv publicabil după corecții exclusiv analitice și editoriale.** Recalcularea confirmă P1–P5 și evaluările H1–H4. Contribuția defensabilă este o caracterizare locală a unor profiluri comportamentale diferite, nu descoperirea generală a neglijării dependenței și nici identificarea unui efect al mărimii.

## 1. Acoperire și surse inspectate

**Rezultat: COMPLETE pentru corpusul obligatoriu enumerat în REPO_REQUIRED_FILES.md și cele 15 fișiere istorice.** Acesta este statutul acoperirii auditului documentar și analitic, nu certificarea completă a execuției istorice. Jurnalele v0.4.3, inclusiv Gemma-run1, și atestarea independentă a runtime-ului lipsesc; concluziile care le-ar necesita rămân nedemonstrate.

Am accesat direct repository-ul privat, nu am presupus că arhiva ZIP este autosuficientă. Am inspectat designul, amendamentele, codul, metadatele stimulilor, exporturile și referințele Git înainte de confruntarea cu sintezele post-colectare. Nu am consultat alte audituri externe de design. Rapoartele și addendumul solicitate au fost tratate ca afirmații de verificat, nu ca autoritate asupra verdictului.

Referințe accesate:
- [ieab-v0.4.3-freeze](https://github.com/ovidiuboticiu/ieab-restart/commit/e7f84e2fff5cefafeac1e4f2369e5242b14b3060): `e7f84e2fff5cefafeac1e4f2369e5242b14b3060`.
- [ieab-v0.4.4-freeze](https://github.com/ovidiuboticiu/ieab-restart/commit/3f418bb6b11a04119508ada24a634c4df46c8708): `3f418bb6b11a04119508ada24a634c4df46c8708`.
- [Închiderea](https://github.com/ovidiuboticiu/ieab-restart/commit/1e8a30938704a255521ab8316a9c4eefd1fa1042): `1e8a30938704a255521ab8316a9c4eefd1fa1042`.

Corpus: 35 fișiere din repository, cu conținut verificat prin Git blob SHA-1; toate cele 16 intrări ale manifestului ZIP, verificate prin SHA-256; patru JSONL v0.4.4; cele șapte capturi 2522–2528, inspectate vizual. Lista exactă de căi, commituri, bloburi și SHA-256 este în anexa de surse și în `surse_inspectate.json`. Sunt incluse toate cele 15 fișiere din `provenance/RECOVERY_MANIFEST.md`, trei exporturi v0.4.3, două exporturi v0.4.4, cele trei rapoarte individuale v0.4.3, sinteza, addendumul, proveniența și STATE.md.

**Metoda recalculării:** implementare separată în JavaScript, pornind de la exporturi și textele efective ale prompturilor. Norma a fost refăcută din înregistrările cu observație proprie; B7 a fost calculată cu aritmetică întreagă echivalentă formulei zecimale exacte. Nu am folosit rezultatul executării analizorului original drept recalculare independentă. Codul său a fost inspectat pentru confruntare. Nu am executat runnerul, generatorul de stimuli sau experimente. Originalele, repository-ul și tagurile nu au fost modificate; fișierele noi sunt copii de lucru și livrabilele acestui audit.

Marcaje: **FAPT** = rezultat calculat sau conținut inspectat direct; **INFERENȚĂ** = interpretare limitată de design; **IPOTEZĂ** = explicație posibilă, netestată.

## 2. Constatări factuale

### Q1 — Integritatea și cronologia

**FAPT.** Referințele Git se rezolvă la SHA-urile declarate. Metadatele commiturilor indică:
- v0.4.3: 2 noiembrie, 19:05:20 UTC, adică 21:05:20 în București;
- v0.4.4: 4 noiembrie, 16:32:22 UTC, adică 18:32:22 în București;
- închidere: 5 noiembrie, 01:50:41 UTC, adică 03:50:41 în București.

Primul RUN_START Qwen 9B este la 4 noiembrie 19:35:51 +0200, cu **1 h 03 min 29 s după** timpul commitului de preregistrare. Ultimul răspuns este la 21:20:42. Gemma 12B: 21:48:04–00:18:36, trecând în 5 noiembrie.

**Distincția necesară:** acest ansamblu este compatibil cu documentarea prospectivă în Git a H1–H4 față de rulările păstrate. Timpul unui commit Git și orele jurnalului sunt metadate verificabile ca înregistrări, nu un martor extern imposibil de modificat. Nu am verificat ora istorică a push-ului/tagului, absența oricărei rulări anterioare nearchivate sau un registru public independent. Repository-ul este privat. Așadar: **preregistrare prospectivă în Git, documentată; preregistrare publică independentă, nedemonstrată**. Tagurile identifică acum commituri precise; nu pretind că un nume de tag nu ar fi putut fi mutat vreodată.

Comparația v0.4.3→v0.4.4 arată două commituri suplimentare. Cele 15 fișiere istorice nu sunt schimbate. Modificările de execuție sunt cele declarate: adăugarea a două ID-uri, versiunea și timeout-ul 120→300 s; sunt adăugate preregistrarea și analizorul. Comparația v0.4.4→închidere arată patru commituri suplimentare, cu modificări numai în STATE.md și documentație/rezultate; niciun fișier de design, stimuli sau cod frozen nu apare modificat în diferența dintre aceste capete.

Cele șase hashuri din fiecare RUN_START v0.4.4 coincid cu fișierele canonice, pentru ambele porniri ale fiecărui model. Reconstituirea fiecărei cereri conform codului frozen reproduce **720/720 request_sha256**. Cele **720/720 raw_sha256** coincid cu răspunsurile brute păstrate; alegerile din ele coincid cu exporturile. Exporturile locale v0.4.4 coincid octet-cu-octet cu cele de la commitul de închidere.

Aceasta verifică consistența internă dintre artefactele furnizate. Nu demonstrează separat traficul real, identitatea binarului GGUF încărcat ori aplicarea efectivă a tuturor parametrilor de către backend.

**Incidentul Gemma E4B-run1:** documentele post-colectare declară oprirea la 25/360, cu 10 răspunsuri valide și 15 NONEMPTY_REASONING; run2 a fost început după incident și ales explicit de operator drept set descriptiv. Jurnalul run1 și cele trei jurnale v0.4.3 nu sunt în corpus. Prin urmare, am verificat direct **existența declarației și exportul run2**, nu numărătorile incidentului, cauza activării Thinking sau orbirea operatorului. Cele șapte capturi din ZIP sunt despre Gemma **12B v0.4.4**, nu probe ale incidentului E4B.

Selectarea run2 nu primește retrospectiv statut de selecție prospectivă. Regula „primul răspuns complet” dintr-un jurnal nu legitimează singură înlocuirea unei rulări complete/incomplete prin alt jurnal. Amendamentele disting răspunsurile individuale invalide de defectele sistemice; fără jurnal și documentarea intervenției nu pot stabili independent încadrarea exactă ori conformitatea restartului. Nu există aici dovadă de selecție după alegeri favorabile, dar nici dovadă care să o excludă printr-un audit al jurnalului.

| Afirmație | Valoare recalculată / verificare | Sursa | Verdict |
|---|---|---|---|
| Tagurile au țintele declarate | e7f84e2… / 3f418bb… | Rezolvarea referințelor Git | corect |
| Nucleul istoric este conservat | 15/15 SHA-256 și bloburi conforme | RECOVERY_MANIFEST + fișiere canonice | corect |
| Arhiva este intern consistentă | 16/16 hashuri conforme | SHA256SUMS.txt + octeții ZIP | corect |
| Fiecare jurnal v0.4.4 are 722 evenimente | 2 RUN_START + 360 REQUEST + 360 RESPONSE | Jurnalele originale | corect |
| Ordinea și cererile v0.4.4 corespund codului | 360/360 per model; 720/720 hashuri cereri | Schedule + cod + jurnale | corect |
| Exporturile v0.4.4 corespund răspunsurilor | 720/720; zero retransmiteri/erori în jurnalele primite | Raw JSON + exporturi | corect |
| H1–H4 sunt documentate înaintea rulărilor păstrate | Commitul precede primul RUN_START cu 1:03:29 | Metadate Git + jurnal Qwen | corect în această limită |
| A existat preregistrare publică independentă | Nicio dovadă prezentă | Repository privat; STATE.md | nedemonstrat |
| Run1 E4B: 10 valide, 15 invalide | Nu poate fi recalculat din corpus | Declarații în rapoarte; jurnal absent | nedemonstrat direct |
| Runtime-ul/modelul binar sunt certificate integral | ID-uri și capturi, fără atestare binară a execuției | Jurnale + capturi | nedemonstrat |

### Q2 — Reproducerea P1–P5 și H1–H4

Toate cele cinci exporturi au 360 de chei distincte, în ordinea frozen, 240 CORE + 96 DEPENDENT + 8 A1 + 16 A2. În exporturi toate rândurile sunt VALID; pentru v0.4.4 acest lucru este confruntat și cu răspunsurile brute. Cele 1.800 de rânduri nu sunt 1.800 de observații independente: sunt cinci hărți pe aceiași opt itemi și numeroase condiții structural corelate.

**P5 este raportat întâi**, conform designului. A2 testează .90 contra .80. În coloanele de ordine, „.80 prima” înseamnă că sursa .90 este ultima.

| Configurație | A1 | A2 | A2: .80 prima | A2: .80 ultima | Verdict recalculare |
| --- | --- | --- | --- | --- | --- |
| Qwen3.5-4B | 8/8 | 10/16 | 2/8 | 8/8 | corect |
| Gemma 4 E4B (run2) | 8/8 | 8/16 | 0/8 | 8/8 | corect |
| Ministral 3 8B | 8/8 | 10/16 | 6/8 | 4/8 | corect |
| Qwen3.5-9B | 8/8 | 13/16 | 7/8 | 6/8 | corect |
| Gemma 4 12B | 8/8 | 15/16 | 7/8 | 8/8 | corect |

**FAPT.** Fiecare configurație greșește cel puțin o ancoră A2. Conform §10.1 din design, nu putem atribui specific erorile CORE agregării multi-sursă, deoarece apar erori și în comparația mai simplă între două surse. A1 perfect nu elimină această limită.

Pentru CORE, norma independent recalculată este semnul lui:
`L = n·ln(r/(1−r)) − ln(4)`.
Rezultă aceleași praguri n=4/3/2 pentru r=.60/.65/.70. Nu există contradicții între norma refăcută din prompturi și metadatele celor 360 de stimuli.

În tabelul P1, fiecare componentă este din 16, în ordinea r=.60/.65/.70.

| Configurație | n=2: Rep(.60/.65/.70) | Clasa n=2 | n=3: Rep(.60/.65/.70) | Clasa n=3 | Verdict |
| --- | --- | --- | --- | --- | --- |
| Qwen3.5-4B | 12 / 14 / 12 | NOT_FOLLOWS | 16 / 16 / 16 | NOT_FOLLOWS | corect |
| Gemma 4 E4B (run2) | 15 / 11 / 15 | NOT_FOLLOWS | 16 / 16 / 16 | NOT_FOLLOWS | corect |
| Ministral 3 8B | 11 / 13 / 14 | NOT_FOLLOWS | 12 / 12 / 14 | NOT_FOLLOWS | corect |
| Qwen3.5-9B | 8 / 5 / 12 | INTERMEDIATE | 12 / 12 / 16 | NOT_FOLLOWS | corect |
| Gemma 4 12B | 13 / 16 / 16 | NOT_FOLLOWS | 16 / 16 / 16 | NOT_FOLLOWS | corect |

| Configurație | P2 B1 | P2 B3 | P4 identice / numai primul / numai ultimul (din 120) | P4 direcție | Verdict |
| --- | --- | --- | --- | --- | --- |
| Qwen3.5-4B | 176/240 | 212/240 | 92 / 28 / 0 | FAVOURS_FIRST | corect |
| Gemma 4 E4B (run2) | 174/240 | 210/240 | 90 / 30 / 0 | FAVOURS_FIRST | corect |
| Ministral 3 8B | 169/240 | 193/240 | 85 / 2 / 33 | FAVOURS_LAST | corect |
| Qwen3.5-9B | 199/240 | 201/240 | 105 / 6 / 9 | FAVOURS_LAST | corect |
| Gemma 4 12B | 195/240 | 237/240 | 117 / 0 / 3 | FAVOURS_LAST | corect |

Sursa fiecărei linii: exportul configurației (inventarul anexat), metadatele CORE/anchor și definițiile designului/preregistrării.

Pentru P4, „primul/ultimul” se referă la **blocul de dovezi repetate**, nu la sufixul FIRST/LAST al ID-ului, care indică poziția sursei .80.

| Ipoteză și criteriu fixat | Qwen3.5-9B | Gemma 4 12B |
| --- | --- | --- |
| H1: n=2 ≠ NOT_FOLLOWS | Confirmată: INTERMEDIATE | Infirmată: NOT_FOLLOWS |
| H2: B1 ≥ B3 | Infirmată: 199 < 201 | Infirmată: 195 < 237 |
| H3: P3 > perechea mică | Confirmată: 43/88 > 35/92 | Confirmată: 85/96 > 13/95 |
| H4: aceeași direcție P4 în familie | Infirmată: FIRST → LAST | Infirmată: FIRST → LAST |

Sunt trei confirmări și cinci infirmări conform criteriilor fixate; aceasta este o numărătoare descriptivă a opt evaluări, nu opt teste independente. H1 Qwen este confirmată deoarece clasa devine INTERMEDIATE; criteriul nu cerea FOLLOWS. Niciun model nu este FOLLOWS la n=2 sau n=3. La n=3 nu se adaugă retrospectiv o ipoteză H1.

**Confruntare pe fișiere:** nu am găsit diferențe numerice în valorile P1–P5/H1–H4 raportate în `REPORT_AND_PROVENANCE.md`, `IEAB_v044_CLOSURE_REPORT_2026-11-05.md` și `IEAB_v0.4.4_raport_verificare_exporturi_2026-11-05.md`. Referințele v0.4.3 din preregistrare, sinteza și rapoartele individuale sunt reproduse pentru indicatorii comparați. Clasificările P1 v0.4.3 sunt aplicarea retrospectivă, explicită, a regulii v0.4.4 la exporturile deja existente.

Există însă o **diferență documentară de acoperire**: raportul preliminar `IEAB_v0.4.4_raport_verificare_exporturi_2026-11-05.md` spune că jurnalul Gemma 12B nu fusese încărcat; raportul de închidere și corpusul actual îl includ. Prima afirmație descrie etapa preliminară și este depășită pentru pachetul actual, nu o eroare aritmetică. Similar, mențiunea veche că raportul Qwen nu era în GitHub nu descrie commitul de închidere.

## 3. Evaluare metodologică

### Q3 — Fragilitatea afirmației centrale

**INFERENȚĂ:** afirmația „sensibilitatea la dependența/proveniența surselor și respectarea pragurilor normative de fiabilitate nu evoluează uniform între configurațiile testate” este susținută ca descriere a indicatorilor observați. Termenul „evoluează” trebuie explicat drept diferență între configurații, nu evoluție longitudinală, mecanism de dezvoltare sau efect cauzal al scalei.

#### P3 pe numitori variabili și pe toate cele 96 de perechi

„Schimbare normativă” = CORE alege partea repetată, DEPENDENT alege sursa .80. „Informativă” = CORE alege partea repetată. Acordul normativ DEPENDENT include și same_single; nu trebuie confundat cu schimbarea.

| Configurație | Normative / informative | Normative / toate | Inverse | Aceeași repetată | Aceeași .80 | Acord DEP / 96 |
| --- | --- | --- | --- | --- | --- | --- |
| Qwen3.5-4B | 35/92 (38,04%) | 35/96 (36,46%) | 0 | 57 | 4 | 39/96 |
| Gemma 4 E4B (run2) | 13/95 (13,68%) | 13/96 (13,54%) | 0 | 82 | 1 | 14/96 |
| Ministral 3 8B | 21/81 (25,93%) | 21/96 (21,88%) | 4 | 60 | 11 | 32/96 |
| Qwen3.5-9B | 43/88 (48,86%) | 43/96 (44,79%) | 0 | 45 | 8 | 51/96 |
| Gemma 4 12B | 85/96 (88,54%) | 85/96 (88,54%) | 0 | 11 | 0 | 85/96 |

La Qwen, creșterea este +10,82 puncte procentuale pe subseturile informative, dar +8,33 pp pe toate cele 96 de perechi. La Gemma, +74,86 pp, respectiv +75,00 pp. Așadar, direcția agregată nu este produsă doar de schimbarea numitorului. Totuși, subseturile informative diferă între configurații și condiționarea pe alegerea CORE nu furnizează o comparație a unei populații fixe.

#### Ce arată cei opt itemi

Fiecare celulă este „schimbări / informative”; fiecare item are 12 perechi în total.

| Item | Qwen3.5-4B | Gemma 4 E4B (run2) | Ministral 3 8B | Qwen3.5-9B | Gemma 4 12B |
| --- | --- | --- | --- | --- | --- |
| I01 | 4/11 | 1/12 | 2/11 | 6/12 | 10/12 |
| I02 | 3/11 | 2/12 | 2/11 | 1/10 | 8/12 |
| I03 | 4/12 | 3/12 | 3/10 | 7/10 | 11/12 |
| I04 | 5/12 | 2/12 | 2/10 | 9/11 | 12/12 |
| I05 | 5/11 | 2/12 | 7/9 | 4/11 | 12/12 |
| I06 | 4/12 | 1/11 | 4/7 | 4/11 | 12/12 |
| I07 | 4/11 | 1/12 | 1/12 | 7/11 | 11/12 |
| I08 | 6/12 | 1/12 | 0/11 | 5/12 | 9/12 |

Gemma 12B depășește E4B pe toți opt itemii, atât pe numitorul total fix, cât și condiționat. Qwen 9B depășește Qwen 4B pe cinci itemi și este mai jos pe trei în proporția condiționată; pe numărul brut de schimbări, patru itemi cresc, unul rămâne egal și trei scad. Rezultatul Qwen este eterogen, nu o ameliorare uniformă pe item.

Acordul B1 pe cele 30 de rânduri CORE/item este: Qwen 9B = 23,21,27,27,25,26,24,26; Gemma 12B = 24,25,24,24,25,25,24,24. Avantajul mare Gemma la P3 coexistă cu un profil CORE apropiat de B3 în fiecare item. Datele complete P1 pe item și toate traseele n=1…5 se află în fișierul de recalculare; nu aplic pragurile P1 din 16 observații unor subgrupuri de numai două.

#### Cele șase celule de dependență

Celulele sunt „schimbări / informative”; numărul total este 16 în fiecare celulă/model.

| r / n | Qwen3.5-4B | Gemma 4 E4B (run2) | Ministral 3 8B | Qwen3.5-9B | Gemma 4 12B |
| --- | --- | --- | --- | --- | --- |
| 0.60/4 | 7/16 | 1/16 | 5/13 | 10/16 | 16/16 |
| 0.65/3 | 5/16 | 3/16 | 4/12 | 5/12 | 16/16 |
| 0.70/2 | 4/12 | 7/15 | 4/14 | 5/12 | 16/16 |
| 0.60/5 | 6/16 | 0/16 | 3/13 | 10/16 | 14/16 |
| 0.65/5 | 6/16 | 1/16 | 3/14 | 6/16 | 14/16 |
| 0.70/5 | 7/16 | 1/16 | 2/15 | 7/16 | 9/16 |

Pentru Gemma 12B, celulele de prag dau 48/48 schimbări; celulele cu n=5 dau 37/48, dintre care doar 9/16 la r=.70. Sub norma declarată, toate copiile lasă o singură observație r contra .80, deci cele 11 erori cu n=5 rămân erori. Ele arată că sensibilitatea puternică la indicii de dependență nu este competență perfectă de agregare a surselor.

**IPOTEZĂ:** lungimea blocului, saliența repetării sau utilizarea inexactă a fiabilității pot contribui la degradarea cu n=5. Aceste explicații nu sunt identificate separat de contrastul existent.

#### Ordinea dovezilor

| Configurație | P3, .80 prima (48 totale) | P3, .80 ultima (48 totale) | B1 CORE .80 prima /120 | B1 CORE .80 ultima /120 |
| --- | --- | --- | --- | --- |
| Qwen3.5-4B | 35/44 | 0/48 | 98/120 | 78/120 |
| Gemma 4 E4B (run2) | 13/47 | 0/48 | 101/120 | 73/120 |
| Ministral 3 8B | 14/47 | 7/34 | 88/120 | 81/120 |
| Qwen3.5-9B | 30/44 | 13/44 | 99/120 | 100/120 |
| Gemma 4 12B | 46/48 | 39/48 | 96/120 | 99/120 |

P3 Qwen 4B→9B **scade** de la 35/44 la 30/44 când .80 este prima și crește de la 0/48 la 13/44 când .80 este ultima. Concluzia H3 agregată rămâne confirmată, dar „îmbunătățire în ambele ordini” ar fi incorect.

La modelele mici Qwen/Gemma, toate schimbările normative apar când .80 este prima. La Gemma 12B contrastul rămâne favorabil față de E4B în ambele ordini: 46/48 și 39/48. Scăderea sensibilității CORE la ordine nu înseamnă dispariția dependenței de ordine în blocul DEPENDENT.

#### Plafon, compoziția grilei și variații simultane

**FAPT.** Gemma 12B alege partea repetată în toate cele 144 de rânduri CORE cu n≥3; Qwen 4B și E4B sunt tot la plafon în aceste rânduri. O alegere binară neschimbată nu arată că probabilitatea latentă nu s-a schimbat. Totuși, plafonul la r=.60,n=3 este incompatibil cu decizia normativă cerută: acolo norma cere sursa .80.

B1 și B3 se deosebesc pe numai 48/240 rânduri. Pe acestea, alegerile compatibile cu B3 sunt:
Qwen 4B 42/48; E4B 42/48; Ministral 36/48; Qwen 9B 25/48; Gemma 12B 45/48.
Așadar, superioritatea B3 la Qwen 9B în total înseamnă doar 25 față de 23 alegeri pe celulele discriminante. La Gemma 12B înseamnă 45 față de 3.

Creșterea acordului B1 Gemma 174→195 nu demonstrează o îmbunătățire a pragurilor: pe cele 48 de celule discriminante, acordul B1 chiar scade 6→3; pe cele 192 unde B1 și B3 coincid, crește 168→192. Citirea agregatului B1 ca „mai bayesian” ar fi greșită.

Potrivirea perechilor este verificată: cele 120 de perechi CORE de ordine conțin aceleași înregistrări reordonate; cele 96 de perechi CORE/DEPENDENT păstrează itemul, r, n, ordinea, asignarea și numărul de înregistrări. Dar manipularea dependenței schimbă **simultan trei câmpuri**: observation_source_id, copied_from_record și made_own_observation. Nu izolează influența fiecăruia. Lungimea crește cu 3(n−1) caractere, fără schimbarea numărului de cuvinte; răspunsurile API raportează +2…19 tokeni la Qwen 9B și +3…17 la Gemma 12B pentru perechile DEPENDENT.

Mai mult, comparația între r=.60/.65/.70 **nu** schimbă numai numărul fiabilității. Generatorul folosește asignări XOR diferite; se schimbă, după caz, mapping-ul text–etichetă, eticheta părții repetate, ordinea afirmațiilor, textul repetat și identificatorii opaci. Echilibrarea celor opt combinații în fiecare strat r este utilă, dar nu este o încrucișare completă item×r×asignare. P1 descrie conformitatea pe această grilă echilibrată; nu estimează un efect pur al modificării lui r în același prompt.

**Puncte forte:** normă explicită verificabilă; variante de ordine realmente potrivite; număr de înregistrări constant în contrastul dependenței; reguli și numitori expliciți; păstrarea rezultatelor infirmate; jurnale v0.4.4 concordante cu codul.

**Limite majore:** opt itemi ficționali, o singură rulare/configurație; răspuns binar fără probabilități; erori A2 în toate configurațiile; contraste r cu variații concomitente; indicii de proveniență legate între ele; proveniență incompletă v0.4.3 și selecția post-incident E4B-run2. Ele limitează interpretarea, fără a invalida numărătorile descriptive.

**Limite minore/editoriale:** rapoarte succesive cu afirmații istorice depășite, ambiguitatea FIRST/LAST și folosirea abreviată a denumirilor modelului. E4B nu trebuie transformat automat în „exact 4 miliarde de parametri”: fișierul istoric de tokenizare înregistrează params_string='7.5B'. Acesta este un câmp documentar al runtime-ului, nu o măsurătoare independentă a parametrilor.

### Q4 — Alternative și inferențe nepermise

| Alternativă / inferență | Ce permit datele |
|---|---|
| Numărarea afirmațiilor | B3 este un comparator descriptiv, cu acord 237/240 la Gemma 12B. Nu identifică un algoritm intern. |
| Primat/recență și etichetare | Explicații încă plauzibile. Ministral alege afirmația listată prima în 239/360 cazuri; norma este prima în 180/360. Acordul CORE este 102/120 versus 67/120 după poziția răspunsului normativ. |
| Folosirea inexactă a fiabilității | Compatibilă cu rezultatele; alegerea binară nu separă ignorarea lui r de ponderare greșită, rotunjire, bias ori modificări sub prag. |
| Variante de antrenare/arhitectură | Nu sunt controlate separat de mărime; două configurații/familie nu identifică efectul cauzal al parametrilor. |
| Prompt, tokenizare și chat template | Semantica user prompt este comună; reprezentările efective nu sunt identice între modele. Tokenizarea istorică nu atestă singură runtime-ul rularii comportamentale. |
| Indicii de proveniență | Reacția poate folosi unul sau mai multe câmpuri redundante. Nu există ablație care să identifice indiciul decisiv. |
| Strategie internă bayesiană | NU poate fi atribuită. |
| Competență generală de provenance | NU este demonstrată. Nu există sarcină separată de recunoaștere sau descoperire a dependenței ascunse. |
| Generalizare la RAG/agenți | NU este demonstrată de IEAB. Aici nu există retrieval, selecție de surse sau interacțiune agentică. |

**B1/B7:** pe 208/240 de rânduri direcționale, predicțiile sunt identice. B7 are TIE pe 32 de rânduri, la (.60,3) și (.65,2); nu sunt răspunsuri normative concurente și nu se punctează ca greșite. Acordurile B7 sunt, în ordinea Qwen4/E4B/Ministral/Qwen9/Gemma12: **174/208, 169/208, 162/208, 184/208, 195/208**. B1/B7 nu pot fi separate pe rândurile nediscriminante; chiar conformitatea perfectă cu B1 pe această grilă nu ar demonstra calculul log-odds.

**Cele trei perechi Gemma P4:** sunt I02, I05 și I06, toate la r=.60,n=2. Rezultatul prescris este FAVOURS_LAST și H4 este infirmată. Diferența netă este însă **3/120 = 2,5 pp**; 117/120 perechi sunt identice. Nu este justificată o „strategie generală de recență”. Pentru Qwen 9B, 9 versus 6 discordante produc aceeași diferență netă, cu alt profil de variație.

## 4. Noutate față de literatură

### Q5 — Comparație explicită pe texte integrale

Am consultat versiunile HTML integrale și anexele relevante pentru articolele arXiv, respectiv PDF-urile complete ACL/EMNLP. Evaluarea nu se bazează doar pe abstracte. Căutarea suplimentară este țintită, nu o revizuire sistematică exhaustivă. „Nu am identificat un precedent exact” nu ar însemna „nu există”.

**Gao et al. (2026)** — Jianxin Gao, Runze Li, Tianyi Yu, Liangwei Ren, Bohan Chen și Zining Wang. *Copies or Sources? Measuring How LLM Aggregators Count Restated Evidence in Multi-Agent Systems*. arXiv:2610.06192v1, 5 octombrie 2026. [Text integral](https://arxiv.org/html/2610.06192v1).

Deja cunoscut: model generativ binar cu prior egal, fiabilități explicite, oracle de numărare a surselor, copii versus observații independente, măsurarea excesului de evidență și consecințe decizionale. Secțiunile 2–3, 4 și anexele B/F/G includ controale de lungime, pointers, formulare și conflicte. IEAB aduce configurațiile locale testate și grila n×r împotriva unei surse .80, cu decizii JSON și P1–P5. Nu susține prioritatea ideii de proveniență explicită, a oracle-ului bayesian ori a testării consecințelor asupra deciziei. Contrastul între probabilitățile raportate de Gao și alegerile IEAB nu demonstrează că diferența provine din mărimea modelului.

**Krishna et al. (2026)** — Mukand Krishna, Anoushka Harit, Chenghao Xiao și Zhongtian Sun. *Recognizing Study Lineage Is Not Enough: Over-Crediting Same-Trial Evidence in LLM-Based Medical Verification*. arXiv:2610.23721v1, 16 octombrie 2026. [Text integral](https://arxiv.org/html/2610.23721v1).

Deja cunoscut: recunoașterea corectă a originii comune nu garantează folosirea ei la agregare; sarcini separate, 14 familii clinice, apeluri repetate, controale și diagnostice de ablație. Lucrarea include și modele mici, inclusiv Qwen3-4B și Ministral-3-8B; „extinderea pentru prima dată la modele mici” nu este susținută. IEAB adaugă probabilități numerice declarate și un oracle exact, în locul relațiilor clinice auditate. Nu reproduce direct disocierea recunoaștere–utilizare, deoarece nu măsoară recunoașterea separat. Anexa G arată și limitele unor indicii redundante.

**Naphade (2026)** — Atharv Naphade. *Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering*. Findings of ACL 2026, pp. 40293–40311. DOI: 10.18653/v1/2026.findings-acl.2003. [Text integral](https://aclanthology.org/2026.findings-acl.2003.pdf).

Deja cunoscut: acumularea de documente distincte versus parafraze, primatul ordinii și variația cu configurația/mărimea; GroupQA are 1.635 întrebări. Secțiunea 4.4 măsoară atât probabilități, cât și schimbarea răspunsului binar, deci „prima analiză a pragurilor de schimbare a alegerii” este prea largă. IEAB adaugă praguri **normative numeric determinate**, explicit-lineage și semantica probabilistică ficțională. GroupQA nu furnizează același oracle; această diferență permite o caracterizare complementară, nu revendicarea unui fenomen nou de repetiție sau ordine.

**Carletti et al. (2026)** — Mattia Carletti, Edward Phillips, Fredrik K. Gustafsson, Patitapaban Palo, Lei Clifton, Danielle Belgrave, Xiao Gu și David A. Clifton. *When Text and Numbers Disagree: Evidence Arbitration in Large Language Models*. arXiv:2608.20116v1, 20 august 2026. [Text integral](https://arxiv.org/html/2608.20116v1).

Deja cunoscut: arbitrajul sintetic între surse, diferențe între configurații, interacțiuni cu ordinea și utilizarea slabă a indiciilor de fiabilitate. Secțiunile 3–4 folosesc serii numerice, rezumate, indicii de corupere și forecast-uri, cu decizii binare din logits. IEAB aduce fiabilități r explicite cu semantica unor observații simetrice și un contrast de copiere, nu doar calificative de nefiabilitate. Nu justifică „prima dovadă că fiabilitatea și alți indici sunt utilizați neuniform”. Recența temporală din articol trebuie distinsă de poziția textuală măsurată de P4.

**Zhou et al. (2026)** — Ruihua Zhou, Hao Huang, Yijie Zheng, Jiatang Luo, Yunpeng Li, Yuling Liu și Dan Du. *Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence*. Proceedings of EMNLP 2026, pp. 11682–11693. [Text integral](https://aclanthology.org/2026.emnlp-main.509.pdf).

Deja cunoscut: clustere dependente tratate ca suport aparent independent, cu corpusuri potrivite, agenți de cercetare și intervenție structurală. Articolul distinge corect controlul de independență **aparentă** de investigații epistemic independente. IEAB este mai curat în privința normei generative declarate, dar mult mai îngust ecologic. Lucrarea împiedică prezentarea riscului pentru agenți drept descoperire IEAB. Rezultatele sale nu transferă automat validitatea externă către configurațiile IEAB.

**Precedent suplimentar important — Wang et al. (2026)** — Sikun Wang, Yixi Zhou, Lei Fan și Fan Zhang. *GraphEcho: Structural Redundancy and Evidence Provenance in LLM Graph Agents*. arXiv:2609.17695v1, 15 septembrie 2026. [Text integral](https://arxiv.org/html/2609.17695v1).

Secțiunile 5–6 separă răspunsul la căi redundante, origini distincte, numărarea surselor și verdictul; raportează profiluri diferite la Qwen3 1.7B/4B/8B. Aceasta restrânge suplimentar noutatea unei afirmații generale de „capacități de proveniență care nu progresează uniform”. IEAB rămâne distinct prin combinarea acestei caracterizări cu pragurile numerice r contra .80 în aceleași configurații. GraphEcho arată și de ce absența schimbării categorice nu exclude schimbarea încrederii.

**Context anterior — Imran et al. (2025)** — Sohaib Imran, Ihor Kendiukhov, Matthew Broerman, Aditya Thomas, Riccardo Campanella, Rob Lamb și Peter M. Atkinson. *Are LLM Belief Updates Consistent with Bayes’ Theorem?* arXiv:2507.17951v1, 23 iulie 2025. [Text integral](https://arxiv.org/html/2507.17951v1).

Măsoară coerența actualizărilor prin probabilități de tokeni și BCC în cinci familii de modele preantrenate; investighează deja relația cu scala. IEAB nu este primul studiu al scalei și coerenței bayesiene. Nici nu infirmă acel rezultat: instrucțiunile, tipul modelului, măsura și distribuția sarcinilor sunt diferite. Contribuția IEAB trebuie formulată ca observație specifică, nu drept lege generală anti-scaling.

**Judecată asupra noutății:** incrementală, dar reală la nivel de instrument și rezultat local. Nici „copiile sunt supraevaluate”, nici „proveniența nu garantează agregarea”, nici „ordinea contează” nu sunt noi. Combinația exactă de grilă, configurații și contrast P3–P1 poate susține un raport descriptiv bine delimitat. Dezvoltarea independentă sau prioritatea istorică a ideii nu sunt demonstrate de lipsa unei citări într-un document.

## 5. Concluzii editoriale

### Q6 — Decizie, contribuții și abstract

**B: publicabil numai după corecții exclusiv analitice/editoriale**, ca raport tehnic sau studiu descriptiv de caracterizare. Nu este necesar un nou experiment pentru această contribuție restrânsă. Verdictul nu garantează acceptarea într-o anumită revistă sau conferință.

A nu este potrivit deoarece manuscrisul trebuie să prezinte simetric numitorii P3, ancorele și eterogenitatea pe ordine/celule, să delimiteze istoricul Gemma și să reducă revendicările de noutate. C ar fi excesiv pentru obiectivul descriptiv: datele sunt verificabile și furnizează un contrast real, chiar dacă nu identifică mecanisme sau efecte cauzale.

**Cel mult trei contribuții susținute:**
1. Un instrument finit cu oracle explicit, contraste potrivite de dependență/ordine și artefacte suficiente pentru recalcularea hărților a cinci configurații.
2. Un rezultat descriptiv în care schimbările normative la indicii de dependență și clasificările pragurilor de fiabilitate au profiluri diferite; cazul Gemma 12B este cel mai pronunțat.
3. O analiză transparentă a limitelor identificării: ancore imperfecte, numitori condiționați, celule discriminante și echivalența B1/B7, cu păstrarea predicțiilor infirmate.

**Cel mult trei supra-afirmații de eliminat:**
1. „Prima demonstrație că LLM-urile numără copii / ignoră proveniența sau fiabilitatea.”
2. „Creșterea numărului de parametri cauzează competență de proveniență, disociată de raționamentul bayesian.”
3. „Acordul B3 identifică strategia internă și dovedește comportamentul general al sistemelor RAG/agenților.”

**Corecții concrete înainte de publicare:** incorporați tabelele P3 pe toate perechile, itemi, celule și ordine; prezentați A2 înainte de CORE; etichetați P1/H drept reguli operaționale, nu certificări de competență; explicați contrastul de 48 de rânduri B1/B3 și cele 208 nediscriminante B1/B7; distingeți datele prospectiv documentate de selecția run2 și diagnosticele post-colectare. Păstrați raportul preliminar ca document istoric și indicați raportul de închidere drept sursa curentă. Publicația trebuie să furnizeze accesul autorizat la artefactele necesare recalculării, nu doar la ZIP-ul incomplet fără repository. Acestea sunt operații analitice/editoriale și de arhivare, nu rerulări.

**Formulare defensabilă a contribuției:**

> Pe opt itemi ficționali și în câte o rulare a celor cinci configurații, schimbările alegerii în direcția normativă la manipularea explicită a dependenței surselor nu sunt însoțite de o conformare uniformă cu pragurile normative de fiabilitate. Gemma 12B prezintă 85/96 schimbări normative în perechile CORE–DEPENDENT, dar rămâne NOT_FOLLOWS la n=2 și n=3. Rezultatul caracterizează aceste alegeri și aceste prompturi; nu identifică mecanisme interne sau un efect cauzal al mărimii.

**Abstract propus, sub 180 de cuvinte:**

Evaluăm descriptiv cinci configurații locale de modele lingvistice pe opt itemi ficționali, folosind un model probabilistic explicit, fiabilități cunoscute și proveniență declarată. Fiecare configurație produce 360 de alegeri binare: 240 de condiții independente, 96 de controale dependente și 24 de ancore. Analiza reproduce criteriile fixate pentru extensia v0.4.4 și raportează atât perechile informative, cât și toate perechile potrivite. Qwen3.5-9B prezintă 43/96 schimbări normative la introducerea dependenței, față de 35/96 la Qwen3.5-4B; Gemma 4 12B prezintă 85/96, față de 13/96 la E4B. Totuși, Qwen9B este doar INTERMEDIATE la pragul n=2, iar Gemma12B rămâne NOT_FOLLOWS la n=2 și n=3. Distribuțiile diferă după item, celulă și ordine, iar toate configurațiile prezintă erori la ancora cu surse .90 versus .80. Rezultatele documentează profiluri neuniforme ale conformității decizionale în aceste configurații. Ele nu identifică strategii interne, un efect cauzal al mărimii sau performanța în RAG și agenți. Selecția post-incident a rularii E4B și limitele provenienței sunt explicit raportate.

## 6. Incertitudini rămase

- Absența jurnalelor v0.4.3 împiedică verificarea independentă a incidentului E4B, a primelor răspunsuri și a eventualelor intervenții. Numărătorile incidentului rămân declarații ale operatorului.
- Nu este disponibilă o atestare externă a momentului public al freeze-ului, a lipsei unor rulări nearchivate, a binarelor încărcate și a tuturor parametrilor efectivi.
- Repetabilitatea între rulări și robustețea la alți itemi, alte formulări, tokenizări sau contexte nu sunt măsurate.
- Nu se poate separa efectul fiecărui indiciu de proveniență ori efectul pur al lui r din variațiile concomitente. Nu se poate determina strategia internă din concordanțe comportamentale.
- Căutarea bibliografică nu certifică exhaustivitatea sau prioritatea exactei combinații IEAB.

Nu recomand continuare experimentală ca o condiție pentru raportul delimitat de mai sus. Dacă se urmărește o afirmație mai puternică, întrebarea precisă ar fi: **„Rămâne contrastul dependență–fiabilitate când fiabilitatea și fiecare indiciu de proveniență sunt manipulate separat, cu restul promptului fix?”** Datele actuale nu pot răspunde deoarece aceste intervenții nu au fost realizate separat. Aceasta ar necesita un design prospectiv nou, nu o rerulare automată a experimentului existent.

---

## Anexă — Inventarul surselor canonice

Toate căile de mai jos au fost accesate în repository-ul privat. Codurile de commit: F43=e7f84e2fff5cefafeac1e4f2369e5242b14b3060; F44=3f418bb6b11a04119508ada24a634c4df46c8708; C=1e8a30938704a255521ab8316a9c4eefd1fa1042. Bloburile și SHA-256 complete sunt în inventarul JSON al livrării.

| Fișier | Commit |
| --- | --- |
| [research/DESIGN_IEAB_v0.4.1.md](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/research/DESIGN_IEAB_v0.4.1.md) | F44 |
| [research/DESIGN_IEAB_v0.4.2_DRAFT.md](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/research/DESIGN_IEAB_v0.4.2_DRAFT.md) | F44 |
| [research/DESIGN_IEAB_v0.4.3_AMENDMENT_DRAFT.md](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/research/DESIGN_IEAB_v0.4.3_AMENDMENT_DRAFT.md) | F44 |
| [implementation/behavioral_inputs.py](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/implementation/behavioral_inputs.py) | F44 |
| [implementation/behavioral_runner.py](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/implementation/behavioral_runner.py) | F44 |
| [implementation/analyze_v044.py](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/implementation/analyze_v044.py) | F44 |
| [implementation/dry_run_v0.4.1/core_prompts_v0.4.1.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/implementation/dry_run_v0.4.1/core_prompts_v0.4.1.jsonl) | F44 |
| [implementation/dry_run_v0.4.1/dependent_prompts_v0.4.1.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/implementation/dry_run_v0.4.1/dependent_prompts_v0.4.1.jsonl) | F44 |
| [implementation/dry_run_v0.4.1/anchor_prompts_v0.4.1.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/implementation/dry_run_v0.4.1/anchor_prompts_v0.4.1.jsonl) | F44 |
| [implementation/dry_run_v0.4.1/schedule_v0.4.1.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/implementation/dry_run_v0.4.1/schedule_v0.4.1.jsonl) | F44 |
| [research/DESIGN_IEAB_v0.4.4_PREREGISTRATION.md](https://github.com/ovidiuboticiu/ieab-restart/blob/3f418bb6b11a04119508ada24a634c4df46c8708/research/DESIGN_IEAB_v0.4.4_PREREGISTRATION.md) | F44 |
| [results/ieab-v0.4.3-2026-11-03/EXPORTURI/qwen3.5-4b-results.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/EXPORTURI/qwen3.5-4b-results.jsonl) | C |
| [results/ieab-v0.4.3-2026-11-03/EXPORTURI/gemma-run2-results.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/EXPORTURI/gemma-run2-results.jsonl) | C |
| [results/ieab-v0.4.3-2026-11-03/EXPORTURI/ministral-results.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/EXPORTURI/ministral-results.jsonl) | C |
| [results/ieab-v0.4.4-2026-11-05/qwen3.5-9b-results.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.4-2026-11-05/qwen3.5-9b-results.jsonl) | C |
| [results/ieab-v0.4.4-2026-11-05/gemma-4-12b-it-results.jsonl](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.4-2026-11-05/gemma-4-12b-it-results.jsonl) | C |
| [results/ieab-v0.4.3-2026-11-03/SINTEZA/IEAB_v043_SINTEZA_STIINTIFICA_CONSOLIDATA_2026-11-03.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/SINTEZA/IEAB_v043_SINTEZA_STIINTIFICA_CONSOLIDATA_2026-11-03.md) | C |
| [results/ieab-v0.4.3-2026-11-03/ADDENDUM_INTERPRETARE_SI_LITERATURA_2026-11-04.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/ADDENDUM_INTERPRETARE_SI_LITERATURA_2026-11-04.md) | C |
| [results/ieab-v0.4.3-2026-11-03/PROVENIENTA_SI_LIMITARI.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/PROVENIENTA_SI_LIMITARI.md) | C |
| [results/ieab-v0.4.4-2026-11-05/REPORT_AND_PROVENANCE.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.4-2026-11-05/REPORT_AND_PROVENANCE.md) | C |
| [STATE.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/STATE.md) | C |
| [results/ieab-v0.4.3-2026-11-03/RAPOARTE/IEAB_v043_Gemma4_E4B_run2_raport_si_comparatie_Qwen_2026-11-03.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/RAPOARTE/IEAB_v043_Gemma4_E4B_run2_raport_si_comparatie_Qwen_2026-11-03.md) | C |
| [results/ieab-v0.4.3-2026-11-03/RAPOARTE/IEAB_v043_Ministral_M1-M6_B1-B7_comparatie_finala_3_modele_2026-11-03.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/RAPOARTE/IEAB_v043_Ministral_M1-M6_B1-B7_comparatie_finala_3_modele_2026-11-03.md) | C |
| [results/ieab-v0.4.3-2026-11-03/RAPOARTE/IEAB_v043_Qwen35_4B_raport_M1-M6_B1-B7_2026-11-02.md](https://github.com/ovidiuboticiu/ieab-restart/blob/1e8a30938704a255521ab8316a9c4eefd1fa1042/results/ieab-v0.4.3-2026-11-03/RAPOARTE/IEAB_v043_Qwen35_4B_raport_M1-M6_B1-B7_2026-11-02.md) | C |
| [implementation/STIMULI_DRAFT_v0.4.1.json](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/STIMULI_DRAFT_v0.4.1.json) | F43 |
| [implementation/build_dry_run_v0_4_1.py](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/build_dry_run_v0_4_1.py) | F43 |
| [implementation/generate_assignments_v0_4_1.py](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/generate_assignments_v0_4_1.py) | F43 |
| [implementation/check_design_v0_4_1.py](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/check_design_v0_4_1.py) | F43 |
| [implementation/check_dry_run_package_v0_4_1.py](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/check_dry_run_package_v0_4_1.py) | F43 |
| [implementation/check_canonical_package_v0_4_1.py](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/check_canonical_package_v0_4_1.py) | F43 |
| [implementation/dry_run_v0.4.1/assignments_v0.4.1.json](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/dry_run_v0.4.1/assignments_v0.4.1.json) | F43 |
| [implementation/tokenization/results/tokenization_qwen_v0.4.1.json](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/tokenization/results/tokenization_qwen_v0.4.1.json) | F43 |
| [implementation/tokenization/results/tokenization_gemma_v0.4.1.json](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/tokenization/results/tokenization_gemma_v0.4.1.json) | F43 |
| [implementation/tokenization/results/tokenization_ministral_v0.4.1.json](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/implementation/tokenization/results/tokenization_ministral_v0.4.1.json) | F43 |
| [provenance/RECOVERY_MANIFEST.md](https://github.com/ovidiuboticiu/ieab-restart/blob/e7f84e2fff5cefafeac1e4f2369e5242b14b3060/provenance/RECOVERY_MANIFEST.md) | F43 |
