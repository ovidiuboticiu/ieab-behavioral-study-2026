#!/bin/sh
# Reconstruiește PDF-ul raportului din sursa Markdown (standard editorial IEAB v7).
# Necesită: pandoc 3.x, XeLaTeX (TeX Live) și fontul Tinos (echivalent metric cu Times New Roman).
# Rulare din rădăcina repozitoriului:  sh paper/build/build.sh
set -e
cd "$(dirname "$0")"
pandoc ../IEAB_Raport_Stiintific_Final.md -f markdown+autolink_bare_uris+raw_tex \
  --shift-heading-level-by=-1 --template=template.tex -o raport.tex
xelatex -interaction=nonstopmode raport.tex >/dev/null
xelatex -interaction=nonstopmode raport.tex >/dev/null
mv raport.pdf ../IEAB_Raport_Stiintific_Final.pdf
rm -f raport.aux raport.log raport.out raport.toc raport.tex
echo "Scris paper/IEAB_Raport_Stiintific_Final.pdf"
