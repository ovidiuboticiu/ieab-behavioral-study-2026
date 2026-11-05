# Proveniență, cronologie, autorat și asistență AI — IEAB

## 1. Autor uman și răspundere

**Ovidiu Boticiu** este autorul uman al studiului. A coordonat cercetarea, a aprobat deciziile experimentale, a configurat și executat local rulările modelelor, a ales seturile de date raportate și își asumă răspunderea pentru interpretarea și publicarea concluziilor.

Autorul a identificat personal că proiectul anterior intrase într-un proces de auditare și control disproporționat față de sarcina experimentală. A decis oprirea acelei direcții și organizarea unui restart mai simplu. Aceasta este o **decizie documentată de conducere a cercetării**, nu o observație experimentală despre modelele testate și nici o concluzie a evaluatorilor AI care trebuie atribuită acestora.

## 2. Utilizarea instrumentelor AI

Au fost folosite **ChatGPT**, **Claude** și **Codex** în sarcini de clarificare conceptuală, proiectare și revizuire metodologică, implementare și verificare de cod, analiză numerică, audit al artefactelor și redactare. Claude a scris implementarea runnerului comportamental și testele asociate în faza restartului; Codex a realizat o recalculare separată în JavaScript și un audit științific documentar. Rolul AI a fost substanțial și nu se reduce la traducere sau corectură gramaticală.

Aceste instrumente **nu sunt coautori**. Nici acordul dintre mai multe sisteme AI, nici auditul Codex nu constituie peer review uman ori dovadă de independență a erorilor. Responsabilitatea pentru deciziile de cercetare și afirmațiile publicate aparține autorului uman.

## 3. Cronologia etapelor (ora locală România, unde este relevant)

| Dată | Etapă | Dovezi și limitări |
|---|---|---|
| În jur de **5 octombrie 2026** | Început aproximativ al cercetării, conform relatării autorului | Dată retrospectivă neconfirmată de un artefact contemporan; nu se prezintă ca dată Git. |
| **6 octombrie 2026, 19:06:16 (România)** | **Primul reper verificabil al proiectului IEAB original** | Commit `14e1ed32b48005ddbf69f708b9619620d5b75381`, „Initialize IEAB repository”, în `ovidiuboticiu/independent-evidence-aggregation-boundary`. |
| **6–31 octombrie 2026** | Dezvoltarea designului, a stimulilor și a infrastructurii în repository-ul original | Nu există date comportamentale IEAB în etapa veche; proiectul s-a blocat operațional. Vezi `PROJECT_CLOSURE_2026-10-31.md`. |
| **31 octombrie 2026** | Decizia autorului de a opri infrastructura disproporționată, fără a abandona cercetarea | Raportul de închidere documentează cauze distincte și limitele probelor; nu este un rezultat experimental. |
| **31 octombrie 2026** | Inițializarea repository-ului privat `ieab-restart` | Primul commit Git `0082aa64e…` și importul verificat al nucleului prin `48106108d…`. |
| **1–2 noiembrie 2026** | Teste offline, configurare locală, probă API neutră | Proba neutră din 2 noiembrie **nu** este apel comportamental IEAB. |
| **2 noiembrie 2026, 21:05:20** | Freeze v0.4.3, înregistrare Git | `e7f84e2fff5cefafeac1e4f2369e5242b14b3060`; ora commitului este convertită în fusul Europe/Bucharest. |
| **2 noiembrie 2026** | **Începutul colectării comportamentale propriu-zise IEAB Restart**, prima execuție completă Qwen3.5-4B | Raportul Qwen este datat 2 noiembrie; ora exactă a primei cereri nu poate fi confirmată independent din jurnalul brut v0.4.3 indisponibil. |
| **3 noiembrie 2026** | Documentarea celor trei rezultate v0.4.3 | Qwen3.5-4B, Gemma 4 E4B run2 și Ministral 3 8B; commit de conservare `07b3f9160…`. |
| **4 noiembrie 2026, 18:32:22** | Fixarea prospectivă în Git a predicțiilor v0.4.4 | Commit/tag `3f418bb6b11a04119508ada24a634c4df46c8708`. Repository-ul privat nu echivalează cu registru public independent. |
| **4 noiembrie 2026, 19:35:51** | Primul RUN_START conservat Qwen3.5-9B | Jurnalul brut v0.4.4; ulterior Gemma 12B, până în dimineața de 5 noiembrie. |
| **5 noiembrie 2026** | Închiderea colectării și auditul științific Codex | Commitul de conservare v0.4.4 `1e8a309…`; auditul și raportul în `12d8e7b…`. |

**Distincție:** este **un singur proiect IEAB**, cu o etapă inițială în octombrie și o continuare în `ieab-restart`. **6 octombrie** este primul început verificabil în Git; **31 octombrie** marchează decizia de reorganizare; **2 noiembrie** marchează debutul efectiv al colectării comportamentale. Marcajele Git și jurnalelor sunt dovezi documentare, nu atestări externe imuabile ale cronologiei.

## 4. Păstrarea rezultatelor și limite

Etapa v0.4.3 este exploratorie, inclusiv folosirea rularii 2 pentru Gemma E4B după un incident. Jurnalul incidentului și celelalte jurnale v0.4.3 nu au fost accesibile auditorului. Etapa v0.4.4 fixează H1–H4 anterior rulărilor păstrate; 3 predicții au fost susținute și 5 nu, conform regulilor prestabilite. Jurnalele v0.4.4 au fost confruntate cu exporturile, dar identitatea binară a runtime-ului nu a fost certificată extern.

Se publică numai subsetul de date, stimuli, protocol și cod necesar verificării concluziilor. Istoricul complet de dezvoltare rămâne în repository-ul privat, nemodificat. Lipsa unor jurnale nu trebuie acoperită prin reconstrucții fabricate sau prin afirmații despre independența evaluării.
