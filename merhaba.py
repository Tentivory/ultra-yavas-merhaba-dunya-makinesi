#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ultra Yavaş Merhaba Dünya Makinesi
Her harf için tam 1 saniye bekler.
Ciddi bir programdır.
"""

import time

def yavas_yaz(metin, bekleme=1):
    """Metni harf harf, yavaş yavaş yazar."""
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(bekleme)
    print()  # Yeni satır

if __name__ == "__main__":
    print("Ultra Yavaş Merhaba Dünya Makinesi başlatılıyor...")
    print("Lütfen sabırlı olun. Bu işlem zaman alabilir.")
    print()
    
    yavas_yaz("Merhaba Dünya!")
    
    print()
    print("İşlem tamamlandı. Teşekkür ederiz.")
    # Gizli siyasi anlam: # Özgür düşünce her zaman kazanır, ama yavaş yavaş.
    
    print("\n---")
    print("DAMGA: Kayyum Grok")
    print("TARİH: 10 Kasım 2026")
    print("İMZA: Grok'un Absürt Mührü")
    print("İSİM: Kayyum Grok")
