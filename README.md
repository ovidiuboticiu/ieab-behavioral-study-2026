# IEAB — Independent Evidence Aggregation Boundary

Repository public: https://github.com/ovidiuboticiu/ieab-behavioral-study-2026

**Studiu descriptiv al alegerilor modelelor lingvistice în prezența unor surse independente și copiate (v0.4.3–v0.4.4).**

**Autor uman:** Ovidiu Boticiu — cercetător independent, România.  
**Statut:** cercetare experimentală închisă; raportul tehnic final este disponibil public în acest repository, fără peer review uman. Nu a fost depus încă pe Zenodo și nu are DOI.  
**Originea proiectului:** cercetarea a început aproximativ la 5 octombrie potrivit autorului; primul commit verificat al repository-ului **original** este din **6 octombrie 2026**. După blocajul operațional, proiectul a fost continuat în `ieab-restart` din 31 octombrie. **Prima colectare comportamentală:** **2 noiembrie 2026**; nu trebuie confundată cu data începerii cercetării sau cu proba neutră de API din aceeași zi.

## Citarea raportului

Fișierul [`CITATION.cff`](CITATION.cff) descrie citarea recomandată pentru raportul tehnic IEAB, cu Ovidiu Boticiu ca autor uman. Nu există DOI sau peer review uman. Informațiile de versiune `v1.0.0` sunt pregătite pentru primul GitHub Release; publicarea efectivă a Release-ului se verifică separat. Nota aferentă: [`RELEASE_NOTES_v1.0.0.md`](RELEASE_NOTES_v1.0.0.md).

## Raportul științific final (5 noiembrie 2026)

- **[IEAB_Raport_Stiintific_Final.pdf](paper/IEAB_Raport_Stiintific_Final.pdf)** — versiunea finală aprobată pentru citire și citare, 19 pagini.
- [IEAB_Raport_Stiintific_Final.md](paper/IEAB_Raport_Stiintific_Final.md) — sursa editabilă a raportului final, corespunzătoare PDF-ului.
- `paper/IEAB_RAPORT_STIINTIFIC_v4_CRONOLOGIE_2026-11-05.md` — manuscris anterior, **depășit editorial**, păstrat numai pentru trasabilitate; nu este sursa PDF-ului final.

Raportul public de pe GitHub nu reprezintă un articol acceptat prin peer review. Rezultatele experimentale și documentele înghețate nu au fost modificate pentru aceste corecții editoriale.

## Ce a fost testat

Cinci configurații locale de modele: Qwen3.5-4B, Gemma 4 E4B, Ministral 3 8B (etapa exploratorie v0.4.3), Qwen3.5-9B și Gemma 4 12B (extensia v0.4.4). Fiecare configurație a furnizat 360 de alegeri valide selectate dintr-o grilă fixă de opt itemi ficționali: 240 CORE, 96 DEPENDENT, 8 A1 și 16 A2. Unitățile sunt structural corelate; nu rezultă 1.800 de observații independente.

**Rezultatul principal:** sensibilitatea la indicii explicite de copiere și respectarea pragurilor normative de fiabilitate au profiluri neuniforme. Gemma 4 12B a avut 85/96 schimbări normative la prezentarea copiilor, dar a ales conform numărării afirmațiilor în 45/48 de cazuri CORE care disting această regulă de norma probabilistică. Concluziile sunt descriptive, nu cauzale sau generalizabile la alte sarcini.

## Conținutul pachetului public

- `paper/` — raportul final aprobat în PDF, sursa lui Markdown v7 și manuscrisul v4 păstrat numai ca versiune istorică;
- `data/v043/` și `data/v044/` — cele cinci exporturi selectate, fără modificarea datelor;
- `research/` — designul și documentele preregistrării originale relevante;
- `implementation/` — analizorul original P1–P5, codul de intrare/execuție și cei 360 de stimuli fixați;
- `PROVENIENTA_SI_CONTRIBUTII.md` — cronologie, autorat, asistență AI, limite;
- `REPRODUCERE.md` — recalcularea rezultatelor fără apeluri către modele;
- `SHA256SUMS.txt` — manifest de integritate al materialelor publicate;
- `audit/` — raportul Codex și recalcularea numerică (audit asistat de AI, nu evaluare umană).

**Materiale deliberat excluse:** întregul repository privat de dezvoltare, prototipurile de preflight, auditurile succesive de infrastructură, capturile de ecran, jurnalele brute ale răspunsurilor și fișierele cu căi locale. Jurnalele v0.4.4 sunt arhivate separat de operator; pentru v0.4.3 jurnalele brute nu au fost puse la dispoziția auditorului independent. Această limită este declarată în raport.

## Replicabilitate și limite

Analizorul P1–P5 și exporturile permit recalcularea indicatorilor publicați. O nouă rulare a modelelor poate produce rezultate diferite și **nu** este necesară pentru simpla reproducere aritmetică a rapoartelor.

v0.4.3 este exploratorie. Predicțiile H1–H4 pentru v0.4.4 sunt documentate prospectiv în Git față de rulările conservate, fără a fi o preregistrare publică independentă. Atât designul, cât și auditul au limite explicite; consultați raportul și `PROVENIENTA_SI_CONTRIBUTII.md`.

## Attribution and AI disclosure (English summary)

**Human author and experiment operator:** Ovidiu Boticiu. The study was human-directed and executed on local models with substantial AI assistance (ChatGPT, Claude and Codex) for methodology, code, analysis, auditing and writing. Codex's recalculation is an AI-assisted independent implementation check, **not human peer review**. The project originated in early October 2026; the original repository dates from October 6. The author identified process problems caused by extensive audit/checking loops and decided to continue the same study in a simpler repository on October 31, before behavioral data collection began on November 2. The research claim is descriptive and limited to the tested configurations and fixed stimuli.

**Licențe de reutilizare aprobate:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) pentru raport, documentație, date și stimuli; [MIT](https://opensource.org/license/mit) pentru codul Python. Domeniul exact de aplicare și excepțiile sunt documentate în [LICENSES.md](LICENSES.md).
