# Yusuf Seçilmiş Carpet — çalışma notları (Claude için)

Bu dosya her oturumda okunur. Kullanıcı Türkçe konuşur; cevaplar Türkçe, kısa ve net olsun.

## Firma
- Gaziantep merkezli toptan halı tedarikçisi (üretici değil). Yurt içi ve ihracat.
- Adres: Başpınar OSB, Vali Muammer Güler Blv. OSB 2. Bölge No:28/A, 27600 Şehitkamil/Gaziantep
- Tel + WhatsApp (tek numara): +90 544 545 29 67 · yusufsecilmiscarpet@gmail.com · Instagram @yusufsecilmiscarpet
- İngilizce ve Arapça tercümanları var.

## Değişmez kurallar
- Sitede fiyat yok. Fiyat yalnızca WhatsApp'tan; hazır mesajda ürün kodu geçer.
- Kuruluş yılı veya tarih asla yazılmaz.
- Minimum sipariş yok. Sevkiyat her yöntemle, ayrı ücretli hizmet olarak yapılır.
- Logonun yazı tipi ve düzeni değiştirilmez.
- Hedef ülke uydurulmaz. Pazarlar: Arap bölgesi (Irak, Ürdün, Suriye, Tunus), Afrika, Türk dünyası, Rusya/Ukrayna/Belarus, Avrupa, Amerika, komşular.
- Altbilgide "Prod by Sand Code TR" → https://sandcodetr.com/ kalır.

## Teknik yapı
- Bağımlılıksız Node betiği: `node build.js` → `dist/` (6 dil: tr, en, ar, ru, fr, ka; ar sağdan sola).
- `node serve.js` veya `baslat.bat` → http://localhost:8080
- Veri: `data/site.json` (ayarlar, renkler, hero, yönlendirmeler), `data/categories.json` (16 kategori), `data/i18n/*.json` (arayüz metinleri), `data/products/*.json` (ürünler).
- Stil/JS: `src/css/style.css`, `src/js/main.js` (filtreler, galeri, dil hatırlama, WhatsApp formu).
- Görseller: `src/images/products/<kod>/`. Yeni foto ekledikten sonra `python3 tools/gorselleri-hazirla.py` çalıştır (m/ 1000px ve t/ 480px WebP kopyaları üretir; site bunları kullanır).
- Kök `index.html` ziyaretçinin tarayıcı diline göre otomatik yönlendirir (az/tk→tr; kk/ky/uz/tg/be/uk/hy→ru; diğerleri→en).
- SEO: hreflang + x-default, canonical, sitemap.xml, robots.txt, JSON-LD (Organization, Product, Breadcrumb, FAQ, Article).

## Ürün ekleme kuralları
- Kod = malzeme ön eki + sıradaki numara (PES, AKR, DKR, PP, CAMI…).
- Ürün kodu başlıkta YAZILMAZ; başlığın üstündeki küçük satırda ve WhatsApp mesajında durur.
- Başlıkta ayırt edici bilgi olur: tarak sayısı + malzeme (ör. "700 Tarak Polyester Halı").
- Cami halısı renk örneklerinde sadece renk adı yazar, kod yazmaz.
- Her ürün eklendikten sonra kullanıcıya zip değil, sayfanın ekran görüntüsü gösterilir.
- Ürün JSON alanları: code, category, material, colors[], sizes[], reeds, weight_gsm veya weight_text, backing, packing, name{6 dil}, desc{6 dil}, images[]; isteğe bağlı badge, home (ana sayfa "Yeni ürünler"), priority, contain, wide, labels[], videos[{file,poster}].
- Mevcut ürünler: AKR1, AKR2, CAMI1, DKR1–DKR7, DKR9, PES1–PES6, PP1.
- Kullanıcıdan yanıt bekleyen sorular: DKR4, DKR6, DKR7, DKR9, AKR2, CAMI1'in gerçek kodları; DKR1 etiketindeki malzeme; PP1 için "çöken" ne demek; CAMI1 ana sayfaya eklensin mi.

## Yayına alma
- Canlı repo: `yusufsecilmis27-code/yusuf-secilmis-carpet` (CNAME: yusufsecilmiscarpet.com), dal: `main`.
- `main` hem kaynak dosyaları hem de derlenmiş `dist/` içeriğini kökte tutar (GitHub Pages dal yayını).
- Akış: `node build.js` → `dist/` içeriğini repo köküne kopyala → commit → `git push origin main`.
- Yayın birkaç dakika sürer; tarayıcıda Ctrl+F5.
- Eski repo `yusufsecilmiscarpet.com` içindeki `yeni-site` dalı artık gereksiz.

## Sosyal medya
- Seçilen tarz: koyu lüks (siyah zemin #131210, altın #D9B868, Cormorant Garamond başlık + Manrope metin; Arapça Noto Naskh/Noto Sans Arabic).
- 5 gönderi (1080×1350) + 6 story (1080×1920), TR/EN/AR; Claude'daki "Yusuf Seçilmiş Carpet – Instagram gönderi ve story seti" tasarım tuvalinde.
