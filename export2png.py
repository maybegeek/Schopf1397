#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ziel: Telegram Sticker.

transparent, png, eine Seite genau 512px, die andere zumindest kleiner-gleich 512px.
"""

import os
import glob
import subprocess
import fontforge

svg_path = 'SVGS'
png_path = 'PNGS-TELEGRAM'

if not os.path.exists(svg_path):
    os.makedirs(svg_path)
if not os.path.exists(png_path):
    os.makedirs(png_path)

F = fontforge.open("Schopf1397.ttf")
for name in F:
    filename = name + ".svg"
    F[name].export(svg_path + '/' + filename)

filesSVG = [f for f in glob.glob(svg_path + '/' + "*.svg")]
for f in filesSVG:
    dateiname = os.path.splitext(os.path.basename(f))[0]
    f_svg_height = subprocess.check_output(['inkscape', '--query-height', f])
    f_svg_width = subprocess.check_output(['inkscape', '--query-width', f])
    if int(float(f_svg_height)) > 0 and int(float(f_svg_width)) > 0 :
        if int(float(f_svg_height)) > int(float(f_svg_width)) :
            subprocess.check_call(['inkscape', '--export-area-drawing', '-e', png_path + '/' + dateiname + '-telegram.png', '-h', '512', f])
        else :
            subprocess.check_call(['inkscape', '--export-area-drawing', '-e', png_path + '/' + dateiname + '-telegram.png', '-w', '512', f])
