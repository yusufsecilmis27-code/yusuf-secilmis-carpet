#!/usr/bin/env python3
"""Ürün fotoğraflarından hızlı açılan küçük kopyalar üretir.

Her src/images/products/<kod>/<dosya> için:
  m/<dosya-adı>.webp  — en fazla 1000 px (ürün sayfasındaki büyük görsel)
  t/<dosya-adı>.webp  — en fazla 480 px  (katalog kartı ve küçük resimler)
Yeni fotoğraf ekledikten sonra çalıştırın: python3 tools/gorselleri-hazirla.py
Gereken: pip install pillow
"""
import os, sys
from PIL import Image, ImageOps

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src', 'images', 'products')
SIZES = {'m': (1000, 78), 't': (480, 72)}
made = 0
for code in sorted(os.listdir(ROOT)):
    d = os.path.join(ROOT, code)
    if not os.path.isdir(d):
        continue
    for f in sorted(os.listdir(d)):
        if not f.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        src = os.path.join(d, f)
        stem = os.path.splitext(f)[0]
        for key, (px, q) in SIZES.items():
            out = os.path.join(d, key, stem + '.webp')
            if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(src):
                continue
            os.makedirs(os.path.dirname(out), exist_ok=True)
            im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
            im.thumbnail((px, px))
            im.save(out, 'WEBP', quality=q, method=6)
            made += 1
print(f'{made} küçük görsel üretildi.')
