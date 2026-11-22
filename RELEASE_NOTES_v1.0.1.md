# IEAB v1.0.1 — editorial correction of the report PDF

**Date:** 22 November 2026

This release changes only the formatting of the Romanian report `paper/IEAB_Raport_Stiintific_Final.pdf`. Data, stimuli, code, analyses, results and conclusions are unchanged.

## Changes

- Regenerated the PDF from the same Markdown source after a page-by-page check against the IEAB v7 editorial standard.
- Fixed a line exceeding the right margin and leftover braces around a commit hash.
- Removed large blank areas and isolated headings at page bottoms.
- Made the bibliography links clickable.
- Renamed table labels from "Tabel. N." to "Tabelul N." and widened a column in Table 7.
- Set the body line spacing exactly to 1.5 lines. The report now has 18 pages instead of 19.
- Added `paper/build/` (template and build script) so the PDF can be rebuilt from source.

A word-by-word comparison of the text of both PDFs shows only pagination, line-breaking and table-label differences. The v1.0.0 edition remains available unchanged at the `v1.0.0` tag.
