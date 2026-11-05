---
title: "IEAB v0.4.3–v0.4.4"
author: "Ovidiu Boticiu"
subtitle: "Profiluri comportamentale în agregarea dovezilor independente și copiate"
date: "5 noiembrie 2026"
lang: ro-RO
fontsize: 12pt
papersize: a4
geometry: [left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]
mainfont: "Tinos"
sansfont: "Tinos"
colorlinks: false
linkcolor: black
urlcolor: black
---

\Needspace{6\baselineskip}

## Rezumat

**Obiectiv.** Evaluarea concordanței dintre alegerile binare ale unor modele lingvistice și o regulă normativă explicită de agregare a dovezilor, în condiții care variază numărul observațiilor, fiabilitatea lor, ordinea și proveniența declarată.

**Metodă.** Au fost analizate cinci configurații locale (Qwen3.5-4B, Gemma 4 E4B, Ministral 3 8B, Qwen3.5-9B și Gemma 4 12B), fiecare cu 360 de răspunsuri selectate: 240 condiții cu observații independente, 96 de condiții pereche cu copii declarate și 24 de ancore, construite din opt itemi ficționali. Prima etapă, v0.4.3, este exploratorie; extensia v0.4.4 are patru predicții operaționale fixate prospectiv în Git față de rulările păstrate.

**Rezultate.** La introducerea dependenței, schimbările de alegere în direcția normativă apar în 35/96 și 43/96 perechi la Qwen 4B și 9B, respectiv în 13/96 și 85/96 la Gemma E4B și 12B. Cu toate acestea, niciuna dintre cele cinci configurații nu primește clasificarea `FOLLOWS` la pragurile de fiabilitate testate pentru două sau trei observații. În cele 48 de cazuri CORE care disting norma probabilistică de regula numărării afirmațiilor, Gemma 12B alege conform numărării în 45 de cazuri, iar Qwen 9B în 25. Toate configurațiile au erori la ancora simplă 0,90 versus 0,80.

**Concluzie.** Pe stimulii și rulările studiate, răspunsul la indiciile explicite de copiere și conformitatea cu pragurile normative de fiabilitate prezintă profiluri diferite între configurații. Rezultatul este descriptiv, nu identifică mecanisme interne și nu demonstrează un efect cauzal al dimensiunii modelului ori o competență generală în RAG/agenți.

**Cuvinte-cheie:** modele lingvistice; agregarea dovezilor; independența surselor; proveniență; fiabilitate; decizie binară; evaluare comportamentală; reproducibilitate.

\clearpage

## 1. Introducere

Într-un flux de informații, mai multe mesaje care susțin aceeași afirmație nu constituie neapărat mai multe observații independente. O singură constatare poate fi transmisă, rezumată și republicată de mai multe ori. Agregarea care tratează aceste copii ca observații noi acordă dovezii originale o greutate excesivă. Distincția dintre **numărul mesajelor** și **numărul observațiilor independente** este importantă în verificarea afirmațiilor, în sisteme de regăsire și în sisteme cu mai mulți agenți.

Studii recente au documentat supraponderarea copiilor, diferențe între recunoașterea provenienței și folosirea ei în decizie, precum și influența ordinii și a indiciilor de fiabilitate asupra răspunsurilor modelelor lingvistice (Gao et al., 2026; Krishna et al., 2026; Naphade, 2026; Carletti et al., 2026; Zhou et al., 2026; Wang et al., 2026). IEAB (Independent Evidence Aggregation Boundary) nu revendică descoperirea acestor fenomene. Contribuția sa potențială este una de **caracterizare comportamentală**, prin compararea răspunsurilor unor configurații locale cu o normă probabilistică explicită, într-o grilă finită de decizii între două afirmații concurente.

**Întrebarea principală:** în ce măsură alegerea binară respectă pragurile normative determinate de numărul și fiabilitatea observațiilor și în ce măsură se modifică atunci când înregistrări anterior independente sunt prezentate drept copii ale aceleiași observații?

Acest studiu nu măsoară probabilitățile subiective ale modelelor, nu identifică algoritmi interni și nu evaluează un sistem RAG ori un agent complet. Unitatea centrală de descriere este **configurația de model pe grila fixată de stimuli**, nu o populație statistică de sarcini generale.

\Needspace{6\baselineskip}

## 2. Literatură relevantă și poziționare

Gao și colaboratorii (2026) au propus o măsură a greutății atribuite unei copii, exprimată în unități de observații independente, folosind inclusiv un model probabilistic normativ și consecințe decizionale. Krishna și colaboratorii (2026) au arătat, în verificarea dovezilor clinice, că recunoașterea provenienței comune într-o sarcină separată nu garantează folosirea ei corectă la agregare. Naphade (2026) a studiat efectele repetiției și ordinii în RAG, iar Carletti și colaboratorii (2026) au analizat arbitrajul între indicii conflictuale, inclusiv fiabilitatea și proveniența. Zhou și colaboratorii (2026) și Wang și colaboratorii (2026) au tratat redundanța și independența aparentă în sisteme agentice și de graf. Imran și colaboratorii (2025) au cercetat coerența actualizărilor de credință cu teorema lui Bayes, într-o paradigmă diferită.

IEAB se deosebește prin grila sa particulară `n × r` împotriva unei surse independente de fiabilitate 0,80, prin alegeri binare într-un format JSON fix, prin comparații pereche cu proveniență declarată și prin cele cinci configurații locale examinate. Aceste diferențe justifică un **raport empiric complementar**, nu revendicarea priorității pentru problemă, metodă probabilistică sau fenomenul supraevaluării copiilor. Căutarea bibliografică utilizată la închiderea studiului a fost țintită, nu sistematică exhaustivă.

\Needspace{6\baselineskip}

## 3. Metodă

\Needspace{6\baselineskip}

### 3.1 Semantica normativă

Fie două afirmații mutual exclusive și exhaustive, `CLAIM_A` și `CLAIM_B`, cu priori egale. Fiecare observație proprie raportează afirmația adevărată cu probabilitatea `r`, simetric pentru ambele afirmații. Observațiile provenite din surse distincte sunt independente condiționat de adevăr.

În condiția **CORE**, una dintre afirmații este susținută de `n` observații independente cu fiabilitate comună `r`, iar cealaltă de o singură observație independentă cu fiabilitate `c = 0,80`. Raportul șanselor în favoarea părții cu `n` observații este:

$$
O_{\mathrm{rep}} = \left(\frac{r}{1-r}\right)^n\!\left(\frac{1-c}{c}\right),\qquad c=0{,}80.
$$

Alegerea normativă este partea cu `n` observații când `O_rep > 1` și sursa unică 0,80 când `O_rep < 1`. Nicio celulă CORE nu produce egalitate normativă. Grila folosește cele trei valori ale lui `r` (0,60; 0,65; 0,70) și cele cinci valori ale lui `n` (1–5). Pragurile de trecere la partea cu `n` observații sunt `n=4`, `n=3` și, respectiv, `n=2`.

\Needspace{12\baselineskip}

**Tabel. 1. Decizia normativă pentru două și trei observații**

| Număr de observații independente | r=0,60 | r=0,65 | r=0,70 |
|:---:|:---:|:---:|:---:|
| n=2 | Sursa 0,80 | Sursa 0,80 | Grupul cu n observații |
| n=3 | Sursa 0,80 | Grupul cu n observații | Grupul cu n observații |

**Notă:** „Sursa 0,80” indică alegerea observației independente opuse grupului repetat.

În condiția **DEPENDENT**, înregistrările suplimentare de pe partea cu `n` mesaje sunt declarate copii ale unei singure observații inițiale; ele nu adaugă observații proprii. Norma tuturor celor 96 de cazuri DEPENDENT este alegerea sursei independente 0,80, întrucât fiabilitatea unicei observații de pe cealaltă parte este sub 0,80.

\Needspace{6\baselineskip}

### 3.2 Stimuli, structură și controlul factorilor

Au fost utilizați opt itemi ficționali fixați înainte de colectare, două etichete neutre de răspuns și o schemă JSON pentru alegere. Sunt echilibrate între straturi asignările text–etichetă, partea susținută de observațiile repetate și ordinea prezentării afirmațiilor. Comparațiile de ordine sunt potrivite în cadrul aceleiași combinații item–r–n. Comparațiile CORE–DEPENDENT păstrează numărul înregistrărilor, itemul, asignările și ordinea; modifică valorile câmpurilor care definesc originea și copierea.

**Pentru fiecare configurație** au fost produse:

- **CORE:** 8 itemi × 3 fiabilități × 5 valori `n` × 2 ordini = 240 răspunsuri;
- **DEPENDENT:** 6 celule de dependență × 8 itemi × 2 ordini = 96 răspunsuri;
- **A1:** 8 ancore cu o singură observație de fiabilitate 0,80;
- **A2:** 16 ancore cu două observații opuse, de fiabilitate 0,90 și 0,80.

Totalul este de **360 de răspunsuri selectate per configurație**, respectiv 1.800 pentru cinci configurații. Acestea sunt variații structural corelate ale acelorași opt itemi, nu 1.800 de observații independente.

\Needspace{6\baselineskip}

### 3.3 Configurații și execuție

Etapa exploratorie **v0.4.3** a inclus `qwen3.5-4b`, `gemma-4-e4b-it` (rularea a doua selectată după incidentul documentat) și `ministral-3-8b`. Etapa **v0.4.4** a adăugat `qwen3.5-9b` și `gemma-4-12b-it`, ca perechi de familie ale unor configurații deja testate. Denumirile modelelor reprezintă identificatori de configurație, nu măsurători independente ale parametrilor efectivi.

Configurația protocolului a fixat, între altele, `temperature=0`, `top_k=40`, `seed=42`, `max_tokens=64` și formatul de răspuns JSON. Pentru v0.4.4, prompturile și ordinea cheilor au rămas neschimbate față de v0.4.3; modificările declarate au vizat identificatorii modelelor, versiunea și timeoutul tehnic, mărit de la 120 la 300 s.

Pentru fiecare model v0.4.4 s-a păstrat un jurnal append-only cu 2 evenimente `RUN_START`, 360 `REQUEST` și 360 `RESPONSE`. Verificarea externă a reconstruit 720/720 amprente ale cererilor și a confirmat 720/720 amprente ale răspunsurilor originale, împreună cu concordanța alegerilor și a exporturilor. Aceasta atestă **consistența documentară internă** a artefactelor păstrate, nu o atestare externă a traficului de rețea, binarului modelului sau parametrilor efectiv aplicați de backend.

\Needspace{6\baselineskip}

### 3.4 Cronologie și statutul pre-specificării

**Originea proiectului și continuitatea sa:** potrivit relatării autorului, cercetarea IEAB a început în jurul datei de 5 octombrie 2026; această dată aproximativă nu a fost verificată printr-un artefact contemporan. **Primul reper Git verificat este 6 octombrie 2026, ora 19:06:16 în România** (commit `14e1ed32b48005ddbf69f708b9619620d5b75381`, „Initialize IEAB repository”), în repository-ul original \href{https://github.com/ovidiuboticiu/independent-evidence-aggregation-boundary}{repository-ul IEAB original}. Între 6 și 31 octombrie au fost dezvoltate și revizuite designul, generatorul și controalele tehnice, însă colectarea comportamentală IEAB nu a început. Infrastructura de verificare și audit s-a complicat până la un blocaj operațional, descris în raportul istoric `PROJECT_CLOSURE_2026-10-31.md`. Autorul a identificat problema de proporționalitate a procedurilor și a decis oprirea infrastructurii vechi, nu abandonarea întrebării științifice.

**Reorganizare, nu începutul unui nou studiu:** la **31 octombrie 2026**, autorul a creat repository-ul privat `ovidiuboticiu/ieab-restart` și a recuperat fără modificări 15 fișiere științifice/deterministe, cu proveniență verificată. Runnerul live din proiectul anterior nu a fost importat. Acest pas a simplificat execuția aceleiași cercetări.

**Începutul colectării comportamentale efective:** **2 noiembrie 2026**, în v0.4.3, după fixarea protocolului de execuție. Înaintea colectării, o probă neutră a API-ului local nu a produs date comportamentale IEAB. Tagul `ieab-v0.4.3-freeze` indică un commit datat 2 noiembrie 2026, ora 21:05:20 în România. Prima execuție Qwen3.5-4B este documentată și analizată în aceeași zi; ora exactă a primei cereri nu poate fi verificată independent deoarece jurnalul brut v0.4.3 nu a fost disponibil auditorului. **6 octombrie** este data de început documentată în Git a proiectului; **2 noiembrie** este începutul colectării de răspunsuri comportamentale, nu al cercetării în ansamblu.

Rezultatele v0.4.3 au fundamentat exploratoriu ipotezele v0.4.4. Documentul `DESIGN_IEAB_v0.4.4_PREREGISTRATION.md` a fixat patru predicții, pragurile și regula de decizie înaintea celor două rulări mari păstrate. Metadatele Git indică fixarea la 4 noiembrie 2026, ora 18:32:22 București, iar primul eveniment de pornire Qwen 9B în jurnal este la 19:35:51 în aceeași zi. Aceste dovezi susțin **documentarea prospectivă în Git** față de rulările conservate, dar nu demonstrează un registru public independent, imposibil de modificat, ori inexistența unor încercări neconservate.

Prima rulare Gemma E4B din v0.4.3 a fost întreruptă după un incident de configurare declarat de operator; analiza folosește **run2**, aleasă explicit după incident. Jurnalul incidentului și jurnalele brute v0.4.3 nu au fost disponibile auditorului independent. Prin urmare, numărătorile și cauza istorică a incidentului nu sunt certificate din jurnale în cadrul acestui raport. Run2 nu este prezentată drept selecție prospectivă.

\Needspace{6\baselineskip}

### 3.5 Indicatori și criterii de interpretare

**P5** descrie mai întâi ancorele A1/A2. **P1** clasifică alegerea părții repetate la `n=2` și `n=3`, pentru cele trei valori `r`, în categoriile operaționale `FOLLOWS`, `INTERMEDIATE` și `NOT_FOLLOWS` definite în preregistrarea v0.4.4. Categoriile nu certifică o competență internă. **P2** compară acordul cu regula normativă B1 și cu regula B3 a numărării mesajelor (care alege grupul cu `n` înregistrări la $n\ge 2$). **P3** numără schimbările CORE repetat → DEPENDENT sursa 0,80, raportate atât din perechile informative (CORE a ales grupul repetat), cât și din toate cele 96 de perechi; acordul normativ în DEPENDENT este separat. **P4** compară ordini potrivite ale blocurilor de evidență.

B1 și B3 diferă pe **48 din 240** de rânduri CORE, dar coincid pe celelalte 192. O altă regulă prespecificată, B7, este direcțional echivalentă cu B1 pe **208 rânduri** și are 32 de egalități (`TIE`). Nici un acord ridicat cu B1, nici un acord ridicat cu B3 nu identifică o strategie internă unică.

Predicțiile v0.4.4 au fost: **H1**, configurația mare iese din `NOT_FOLLOWS` la `n=2`; **H2**, acordul B1 este cel puțin egal cu B3; **H3**, proporția P3 pe perechile informative o depășește pe cea a configurației mici din aceeași familie; **H4**, direcția efectului P4 rămâne aceeași în familie. Fiecare predicție este evaluată separat pentru fiecare dintre cele două configurații mari, după regulile fixe dinainte de colectare. Nu au fost folosite teste statistice care să trateze rândurile drept independente.

\Needspace{21\baselineskip}

## 4. Rezultate

\Needspace{6\baselineskip}

### 4.1 Verificările de bază: ancorele P5

\Needspace{12\baselineskip}

**Tabel. 2. Acordul normativ pe ancore**

| Configurație | A1 | A2 | A2: 0,80 prima | A2: 0,80 ultima |
|---|---:|---:|---:|---:|
| Qwen3.5-4B | 8/8 | 10/16 | 2/8 | 8/8 |
| Gemma 4 E4B (run2) | 8/8 | 8/16 | 0/8 | 8/8 |
| Ministral 3 8B | 8/8 | 10/16 | 6/8 | 4/8 |
| Qwen3.5-9B | 8/8 | 13/16 | 7/8 | 6/8 |
| Gemma 4 12B | 8/8 | 15/16 | 7/8 | 8/8 |

**Notă:** A2: 0,90 versus 0,80; numitorii sunt 8 pentru A1 și 16 pentru A2.

Toate configurațiile răspund normativ la A1, dar **toate greșesc cel puțin o ancoră A2**. Conform designului, erorile din CORE nu pot fi atribuite exclusiv integrării mai multor observații, deoarece există erori și în comparația mai simplă între două surse.

\Needspace{6\baselineskip}

### 4.2 Pragurile normative și regula numărării: P1 și P2

\Needspace{12\baselineskip}

**Tabel. 3. Numărul alegerilor grupului cu `n` observații la pragurile P1**

| Configurație | n=2: alegeri repetat | Clasă n=2 | n=3: alegeri repetat | Clasă n=3 |
|---|---|---|---|---|
| Qwen3.5-4B | 12 / 14 / 12 | NOT_FOLLOWS | 16 / 16 / 16 | NOT_FOLLOWS |
| Gemma 4 E4B (run2) | 15 / 11 / 15 | NOT_FOLLOWS | 16 / 16 / 16 | NOT_FOLLOWS |
| Ministral 3 8B | 11 / 13 / 14 | NOT_FOLLOWS | 12 / 12 / 14 | NOT_FOLLOWS |
| Qwen3.5-9B | 8 / 5 / 12 | INTERMEDIATE | 12 / 12 / 16 | NOT_FOLLOWS |
| Gemma 4 12B | 13 / 16 / 16 | NOT_FOLLOWS | 16 / 16 / 16 | NOT_FOLLOWS |

**Notă:** În fiecare triplet, ordinea este `r=0,60 / 0,65 / 0,70`, fiecare celulă având numitorul 16.

Nicio configurație nu este clasificată `FOLLOWS` la `n=2` sau `n=3`. Qwen 9B obține `INTERMEDIATE` la `n=2`, ceea ce satisface H1, dar **nu echivalează** cu urmarea completă a pragului.

\Needspace{12\baselineskip}

**Tabel. 4. Acordul CORE cu norma B1 și numărarea B3**

| Configurație | Acord B1 / 240 | Acord B3 / 240 | Acord B3 / 48 discriminante |
|---|---:|---:|---:|
| Qwen3.5-4B | 176 | 212 | 42 |
| Gemma 4 E4B (run2) | 174 | 210 | 42 |
| Ministral 3 8B | 169 | 193 | 36 |
| Qwen3.5-9B | 199 | 201 | 25 |
| Gemma 4 12B | 195 | 237 | 45 |

**Notă:** Ultima coloană arată numărul acordurilor B3 din cele 48 de situații unde B1 și B3 prezic răspunsuri diferite.

La Qwen 9B, 25/48 alegeri corespund B3 și 23/48 corespund B1: diferența este mică și nu susține o dominanță puternică a numărării. La Gemma 12B, diferența este 45/48 versus 3/48. Deși acordul global cu B1 crește între E4B și 12B (174 → 195), pe **cele 48 de cazuri discriminante** acordul cu B1 scade (6 → 3); creșterea totală provine din cazurile unde B1 și B3 sunt de acord. Nu se justifică descrierea acestei creșteri agregate drept progres al utilizării pragurilor de fiabilitate.

\Needspace{17\baselineskip}

### 4.3 Reactivitatea la copierea explicită: P3

\Needspace{12\baselineskip}

**Tabel. 5. Cele 96 de perechi CORE–DEPENDENT per configurație**

| Configurație | Schimbări / informative | Schimbări / toate cele 96 | Acord DEPENDENT / 96 |
|---|---:|---:|---:|
| Qwen3.5-4B | 35/92 | 35/96 | 39/96 |
| Gemma 4 E4B (run2) | 13/95 | 13/96 | 14/96 |
| Ministral 3 8B | 21/81 | 21/96 | 32/96 |
| Qwen3.5-9B | 43/88 | 43/96 | 51/96 |
| Gemma 4 12B | 85/96 | 85/96 | 85/96 |

**Notă:** „Schimbare normativă” înseamnă trecerea din alegerea grupului repetat în CORE la alegerea sursei 0,80 în DEPENDENT. „Acord DEPENDENT” include și cazurile în care sursa 0,80 este aleasă în ambele condiții.

Între Qwen 4B și 9B, proporția pe toate perechile crește de la 35/96 la 43/96 (**+8,33 puncte procentuale**); între Gemma E4B și 12B crește de la 13/96 la 85/96 (**+75,00 puncte procentuale**). Ambele diferențe au aceeași direcție și pe perechile informative, dar numitorii acestora depind de alegerea CORE a fiecărei configurații și nu reprezintă subseturi identice.

Pentru **Gemma 12B**, diferența față de E4B este observată la toți cei opt itemi: cele 12 perechi/item au între 8 și 12 schimbări normative în varianta 12B, față de 1–3 în varianta E4B. Pentru **Qwen**, numărul brut de schimbări crește la patru itemi, rămâne egal la unul și scade la trei: răspunsul este eterogen. Pe cele șase celule DEPENDENT, Gemma 12B are 16/16 schimbări în fiecare dintre cele trei celule de prag (`r=0,60;n=4`, `r=0,65;n=3`, `r=0,70;n=2`), dar numai 14/16, 14/16 și 9/16 la cele trei celule cu `n=5`. În consecință, sensibilitatea ridicată la copiere nu reprezintă agregare normativă perfectă.

\Needspace{12\baselineskip}

**Tabel. 6. Schimbări normative P3 în funcție de poziția sursei 0,80**

| Configurație | 0,80 prima / 48 | 0,80 ultima / 48 |
|---|---:|---:|
| Qwen3.5-4B | 35 | 0 |
| Gemma 4 E4B (run2) | 13 | 0 |
| Ministral 3 8B | 14 | 7 |
| Qwen3.5-9B | 30 | 13 |
| Gemma 4 12B | 46 | 39 |

**Notă:** Numitorul fix este 48 de perechi pentru fiecare poziție; nu este numitorul condițional al perechilor informative.

Qwen 9B are mai puține schimbări decât Qwen 4B atunci când 0,80 este prezentată prima (30 versus 35), dar mai multe atunci când este ultima (13 versus 0). Așadar, confirmarea H3 la Qwen **nu** înseamnă îmbunătățire în ambele ordini. Gemma 12B depășește E4B în ambele ordini, fără ca diferența de ordine să dispară complet.

\Needspace{6\baselineskip}

### 4.4 Influența poziției blocurilor de dovezi: P4

\Needspace{12\baselineskip}

**Tabel. 7. Perechi CORE cu ordinea dovezilor inversată; total 120 perechi/model**

| Configurație | Aceeași alegere | Repetatul favorizat primul | Repetatul favorizat ultimul | Direcție |
|---|---:|---:|---:|---|
| Qwen3.5-4B | 92 | 28 | 0 | FAVOURS_FIRST |
| Gemma 4 E4B (run2) | 90 | 30 | 0 | FAVOURS_FIRST |
| Ministral 3 8B | 85 | 2 | 33 | FAVOURS_LAST |
| Qwen3.5-9B | 105 | 6 | 9 | FAVOURS_LAST |
| Gemma 4 12B | 117 | 0 | 3 | FAVOURS_LAST |

**Notă:** „Primul/ultimul” se referă la poziția blocului cu observații repetate, nu la sufixul ID-ului stimulului.

Pentru Gemma 12B, 117 din 120 de perechi sunt identice, iar direcția `FAVOURS_LAST` este determinată de trei perechi discordante (diferență netă 2,5 puncte procentuale). Nu este demonstrată o strategie generală de recență. Același rezultat categorial P4 la Qwen 9B se bazează pe un profil diferit, 9 versus 6 discordante.

\Needspace{6\baselineskip}

### 4.5 Predicțiile H1–H4 din extensia v0.4.4

\Needspace{17\baselineskip}

**Tabel. 8. Aplicarea criteriilor prospectiv documentate în Git, separat pentru fiecare configurație mare**

| Predicție și criteriu | Qwen3.5-9B | Gemma 4 12B |
|---|---|---|
| H1: n=2 nu mai este `NOT_FOLLOWS` | Confirmată: `INTERMEDIATE` | Infirmată: `NOT_FOLLOWS` |
| H2: acord B1 ≥ acord B3 | Infirmată: 199 < 201 | Infirmată: 195 < 237 |
| H3: P3 informativ > configurația mică în aceeași familie | Confirmată: 43/88 > 35/92 | Confirmată: 85/96 > 13/95 |
| H4: direcția P4 rămâne aceeași | Infirmată: FIRST → LAST | Infirmată: FIRST → LAST |

Rezultatul este de **trei predicții confirmate și cinci infirmate**, conform regulilor fixate; nu reprezintă opt teste independente de ipoteze, probabilități de confirmare ori un scor general al modelelor. P1 la `n=3` a fost raportat numai descriptiv, fără adăugarea retrospectivă a unei noi ipoteze.

\Needspace{6\baselineskip}

## 5. Discuție

\Needspace{6\baselineskip}

### 5.1 Contrastul central și gradul său de susținere

Constatarea descriptivă centrală este că **alegerile orientate normativ la declararea copiilor nu sunt însoțite de o conformitate uniformă cu pragurile normative de fiabilitate**. La Gemma 12B, acest contrast este puternic în grila observată: 85/96 schimbări normative CORE–DEPENDENT, concomitent cu 45/48 alegeri compatibile cu numărarea mesajelor în cazurile discriminante CORE. La Qwen 9B, profilul este mai amestecat: 43/96 schimbări normative, iar în cele 48 de situații discriminante B3 și B1 sunt aproape la egalitate (25 față de 23).

Aceste observații **nu** arată că modelul are un modul intern pentru proveniență și altul pentru fiabilitate. Nici nu arată că un model „ignoră r” la nivel probabilistic: chiar când alegerea binară rămâne neschimbată, o estimare latentă ar putea varia fără să traverseze pragul de decizie. IEAB nu a solicitat și măsurat asemenea estimări.

\Needspace{6\baselineskip}

### 5.2 Explicații concurente neeliminate

Există câteva alternative compatibile cu rezultatele: preferințe de ordine, preferințe pentru etichete, repetarea lexicală, utilizarea inexactă a fiabilității, strategie de numărare, sensibilitate la unul sau mai multe câmpuri explicite de proveniență și diferențe între configurații în reprezentarea efectivă a prompturilor. Concordanța B3 nu dovedește utilizarea unui algoritm intern de numărare. Concordanța B1 nu dovedește calculul intern al raporturilor de șanse.

În DEPENDENT se modifică împreună `observation_source_id`, `copied_from_record` și `made_own_observation` și apar diferențe mici de lungime/tokenizare. Nu există o ablație care să identifice indiciul decisiv. De asemenea, straturile de fiabilitate `r` au asignări echilibrate, dar nu identice la nivelul unui prompt individual; comparația agregată între r nu izolează efectul pur al cifrei fiabilității.

\Needspace{6\baselineskip}

### 5.3 Interpretarea comparațiilor între configurații

Apariția aceluiași sens de diferență P3 la Qwen și Gemma nu identifică un efect **cauzal al numărului de parametri**. Perechile includ versiuni/configurații care pot diferi și prin antrenare, arhitectură ori execuție. Chiar în familiile comparate, profilul Qwen este neuniform între itemi și ordine, pe când Gemma arată o diferență mai consistentă pentru manipularea DEPENDENT. În consecință, formulările despre „evoluție” trebuie înțelese numai ca **diferență între configurațiile observate**, nu proces longitudinal sau lege de scalare.

\Needspace{6\baselineskip}

### 5.4 Relevanța practică, strict delimitată

Sarcinile IEAB sugerează prudență față de presupunerea că simpla includere a câmpurilor de proveniență și a fiabilității în prompt garantează o decizie corectă. Aceasta este o implicație pentru proiectarea verificărilor în sisteme care consumă surse multiple, nu o demonstrație a performanței unor sisteme RAG sau agenți reali. IEAB nu a testat explicit deduplicarea în cod, instrucțiunile care explică efectul copierii, retrievalul sau orchestrarea agenților. Literatura (Gao et al., 2026; Krishna et al., 2026; Zhou et al., 2026) examinează separat anumite intervenții de acest tip.

\Needspace{6\baselineskip}

## 6. Limitări și statut epistemic

1. **Validitate externă restrânsă:** opt itemi ficționali și o singură rulare selectată per configurație; nu sunt estimate variațiile între rulări sau generalizarea la alte sarcini.
2. **Unități corelate:** rândurile aceleiași grile derivă din aceiași itemi și nu sunt tratate drept 1.800 de observații independente. Nu raportăm valori-p ori intervale de încredere bazate pe o asemenea ipoteză de independență.
3. **Ancore imperfecte:** toate configurațiile fac erori în A2; greșelile CORE nu pot fi atribuite exclusiv integrării multisursă.
4. **Manipulări neizolate:** proveniența modifică simultan trei câmpuri, iar condițiile r nu păstrează toate asignările identice. Nu se poate estima separat efectul cauzal al fiecărei componente.
5. **Măsură binară:** nu observăm probabilități interne ori raportate, încredere calibrată sau modificări sub pragul deciziei; există și celule aproape de plafon.
6. **Confuzii între configurații:** nu se poate izola efectul parametrilor sau al arhitecturii; etichetele comerciale ale modelelor nu certifică dimensiunea efectivă încărcată.
7. **Proveniență tehnică incompletă:** pentru v0.4.4 sunt verificate intern jurnalele, cererile reconstruite și răspunsurile brute, dar nu există atestare externă a runtime-ului/GGUF-ului; pentru v0.4.3 lipsesc jurnalele brute din corpusul auditorului și jurnalul incidentului E4B.
8. **Statutul v0.4.3 versus v0.4.4:** prima etapă este exploratorie; în a doua, predicțiile sunt prospectiv documentate în Git față de rulările păstrate, nu atestate prin registru public independent.
9. **Noutate limitată:** literatura anterioară tratează deja sursele copiate, ordinea, fiabilitatea și profilurile diferite între modele. IEAB contribuie o combinație empirică particulară, nu o teorie sau un fenomen general nou.

Aceste limite reduc **forța interpretării**, nu corectitudinea numărătorilor descriptive verificate.

\Needspace{6\baselineskip}

## 7. Transparență, reproducibilitate și rolul instrumentelor AI

**Surse canonice și diseminare:** etapa inițială se găsește în \href{https://github.com/ovidiuboticiu/independent-evidence-aggregation-boundary}{repository-ul IEAB original} (arhivă istorică privată; închisă operațional la 31 octombrie). Etapa de continuare și colectare se găsește în `https://github.com/ovidiuboticiu/ieab-restart` (privată la data redactării). Pachetul public distinct pentru raport, date și cod este disponibil la `https://github.com/ovidiuboticiu/ieab-behavioral-study-2026`. Pentru a reproduce rezultatele din date, un evaluator autorizat are nevoie de design, stimuli, ordine, exporturi, analizor și regulile de selecție a rulărilor.

- **Inițializare IEAB original:** `14e1ed32b48005ddbf69f708b9619620d5b75381`, 6 octombrie 2026.
- **Închidere operațională original:** `PROJECT_CLOSURE_2026-10-31.md`, 31 octombrie 2026.
- **Import în IEAB Restart:** `48106108da00146d87e3b99832bb62c9173e2066`, 31 octombrie 2026.
- **Freeze v0.4.3:** `e7f84e2fff5cefafeac1e4f2369e5242b14b3060`.
- **Freeze v0.4.4:** `3f418bb6b11a04119508ada24a634c4df46c8708`.
- **Commitul închiderii experimentale:** `1e8a30938704a255521ab8316a9c4eefd1fa1042`.
- **Commitul arhivării auditului și manuscrisului inițial:** {\ttfamily 12d8e7bd61\allowbreak e297cced03\allowbreak aa5b335095\allowbreak 5cc908a5bf}.
- **Exporturi și rapoarte v0.4.3:** `results/ieab-v0.4.3-2026-11-03/`.
- **Exporturi și rapoarte v0.4.4:** `results/ieab-v0.4.4-2026-11-05/`.
- **Manuscrisul inițial și auditul:** `results/ieab-final-2026-11-05/`.
- **Preregistrare și criterii v0.4.4:** \href{https://github.com/ovidiuboticiu/ieab-behavioral-study-2026/blob/main/research/DESIGN_IEAB_v0.4.4_PREREGISTRATION.md}{preregistrarea IEAB v0.4.4}.

Jurnalele brute v0.4.4 și capturile sunt conservate într-o arhivă separată a operatorului; aceasta nu este încărcată în repository. Jurnalele v0.4.3 nu au fost disponibile evaluatorului. Repository-ul privat nu este, în acest stadiu, un pachet public complet pentru reproducere independentă. O eventuală publicare trebuie însoțită de o decizie distinctă despre accesul la artefacte; nu presupune publicarea automată a întregului repository.

**Verificare externă de calcul:** Codex a realizat o recalculare separată în JavaScript din exporturi și stimuli, consemnată în `AUDIT_STIINTIFIC_IEAB_2026-11-05.md` și `recalculare_independenta.json`; cifrele P1–P5 și evaluările H1–H4 corespund rapoartelor de închidere. Este o **verificare independentă de implementare realizată cu ajutorul unui sistem AI**, nu peer review uman și nu certificare formală a tuturor condițiilor istorice.

**Autorat și responsabilitate umană:** Ovidiu Boticiu este autorul uman unic declarat al acestui raport. El a organizat și executat local experimentul, a luat deciziile de continuare și de oprire și își asumă selecția datelor și concluziile publicate. În cursul proiectului original (6–31 octombrie), autorul a identificat blocajul de proces produs de acumularea de audituri și proceduri disproporționate și a decis continuarea aceleiași cercetări într-un repository curat, recuperând nucleul științific fără importul infrastructurii live anterioare. Aceasta este o decizie de management al cercetării, documentată prin istoricul IEAB Restart; nu este un rezultat experimental al modelelor.

**Declarație privind utilizarea AI:** ChatGPT și Claude au fost utilizate pentru structurarea și revizuirea designului, redactarea și verificarea implementărilor, analiza datelor și redactarea documentelor. Claude a contribuit direct la implementarea runnerului comportamental. Codex a efectuat un audit al artefactelor și o recalculare separată în JavaScript, conform raportului său. Acestea sunt forme de asistență AI, nu coautorat și nici peer review uman. Verificările efectuate de mai multe sisteme AI pot avea erori corelate; acordul lor nu este o garanție independentă a validității științifice. Autorul uman poartă responsabilitatea finală pentru conținut. Nu s-au făcut noi apeluri la modelele experimentale pentru această redactare.

\Needspace{6\baselineskip}

## 8. Concluzii

IEAB v0.4.3–v0.4.4 furnizează o caracterizare descriptivă, recalculabilă, a alegerilor a cinci configurații locale în condiții ficționale cu fiabilități și proveniență declarate. Cele două comparații de familie satisfac predicția H3 pe grila analizată, însă nu prezintă îmbunătățiri uniforme ale pragurilor de fiabilitate, ale ordinii sau ale ancorelor. Contrastul cel mai pronunțat este Gemma 4 12B: reacții normative frecvente la declararea copiilor și, simultan, alegeri CORE în mare parte compatibile cu numărarea mesajelor exact în cazurile unde aceasta contrazice norma.

**Contribuția științifică este incrementală și locală:** un instrument finit cu normă explicită, comparații controlate între condiții și profiluri comportamentale documentate, cu limitele declarate. Studiul nu identifică mecanisme interne, nu demonstrează efecte cauzale ale dimensiunii și nu validează generalizarea la sisteme RAG ori agenți. Pentru aceste afirmații descriptive, experimentul este închis și nu este necesară o nouă rulare a modelelor. Întrebările despre repetabilitate, probabilități raportate ori manipularea separată a indiciilor ar necesita cercetări distincte, cu design prospectiv nou.

\Needspace{6\baselineskip}

## Bibliografie

\Needspace{5\baselineskip}

Carletti, M., Phillips, E., Gustafsson, F. K., Palo, P., Clifton, L., Belgrave, D., Gu, X. și Clifton, D. A. (2026). When Text and Numbers Disagree: Evidence Arbitration in Large Language Models. arXiv:2608.20116. https://arxiv.org/abs/2608.20116

\Needspace{5\baselineskip}

Gao, J., Li, R., Yu, T., Ren, L., Chen, B. și Wang, Z. (2026). Copies or Sources? Measuring How LLM Aggregators Count Restated Evidence in Multi-Agent Systems. arXiv:2610.06192. https://arxiv.org/abs/2610.06192

\Needspace{5\baselineskip}

Imran, S., Kendiukhov, I., Broerman, M., Thomas, A., Campanella, R., Lamb, R. și Atkinson, P. M. (2025). Are LLM Belief Updates Consistent with Bayes' Theorem?. arXiv:2507.17951. https://arxiv.org/abs/2507.17951

\Needspace{5\baselineskip}

Krishna, M., Harit, A., Xiao, C. și Sun, Z. (2026). Recognizing Study Lineage Is Not Enough: Over-Crediting Same-Trial Evidence in LLM-Based Medical Verification. arXiv:2610.23721. https://arxiv.org/abs/2610.23721

\Needspace{5\baselineskip}

Naphade, A. (2026). Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering. Findings of ACL 2026, 40293–40311. DOI: 10.18653/v1/2026.findings-acl.2003. https://aclanthology.org/2026.findings-acl.2003/

\Needspace{5\baselineskip}

Wang, S., Zhou, Y., Fan, L. și Zhang, F. (2026). GraphEcho: Structural Redundancy and Evidence Provenance in LLM Graph Agents. arXiv:2609.17695. https://arxiv.org/abs/2609.17695

\Needspace{5\baselineskip}

Zhou, R., Huang, H., Zheng, Y., Luo, J., Li, Y., Liu, Y. și Du, D. (2026). Evidence Laundering: Deep Research Agents Mistake Correlated Sources for Independent Evidence. Proceedings of EMNLP 2026, 11682–11693. DOI: 10.18653/2026.emnlp-main.509. https://aclanthology.org/2026.emnlp-main.509/

\Needspace{19\baselineskip}

## Anexă. Matricea completă a schimbărilor P3, pe cele șase celule de dependență

\Needspace{12\baselineskip}

**Tabel. A1. Schimbări normative / perechi informative în fiecare celulă**

| r / n | Qwen 4B | Gemma E4B | Ministral 8B | Qwen 9B | Gemma 12B |
|---|---:|---:|---:|---:|---:|
| 0,60 / 4 | 7/16 | 1/16 | 5/13 | 10/16 | 16/16 |
| 0,65 / 3 | 5/16 | 3/16 | 4/12 | 5/12 | 16/16 |
| 0,70 / 2 | 4/12 | 7/15 | 4/14 | 5/12 | 16/16 |
| 0,60 / 5 | 6/16 | 0/16 | 3/13 | 10/16 | 14/16 |
| 0,65 / 5 | 6/16 | 1/16 | 3/14 | 6/16 | 14/16 |
| 0,70 / 5 | 7/16 | 1/16 | 2/15 | 7/16 | 9/16 |

**Notă:** Fiecare celulă cuprinde 16 perechi per configurație; numitorii de mai jos sunt subseturile informative (CORE alege partea repetată). Valorile sunt reproduse în recalcularea independentă Codex.

**Notă de lectură:** valorile din această anexă reprezintă reacții ale alegerii la câmpurile de proveniență în cadrul grilei fixate, nu estimări independente ale unei rate populaționale și nu atestă interpretarea internă a relației de copiere.
