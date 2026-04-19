# Katkıda Bulunma Rehberi (Contributing)

Bu projeye katkıda bulunduğunuz için teşekkürler! AGI ve bilinç araştırmaları alanında birlikte çalışalım.

## Katkı Türleri

- 📝 **Yeni teoriler ve analizler** - `teorik_kavramlar/` klasörüne
- ⚙️ **Teknik dökümanlar** - `mimari_ve_optimizasyon/` klasörüne  
- 🐍 **Kod ve simülasyonlar** - `simulasyonlar_ve_kod/` klasörüne
- 🐛 **Hata düzeltmeleri** - Herhangi bir dosya için
- 📚 **Kaynak ve referanslar** - Mevcut dosyaları genişletme

## Katkı Adımları

### 1. Repo'yu Fork'layın

GitHub üzerinden bu repoyu kendi hesabınıza fork'layın.

### 2. Yerel Kopya Oluşturun

```bash
git clone https://github.com/KULLANICI_ADINIZ/AGI-Bilinc-Arastirmalari.git
cd AGI-Bilinc-Arastirmalari
```

### 3. Branch Oluşturun

```bash
git checkout -b ozellik/konu-adi
# veya
git checkout -b fix/hata-aciklamasi
```

### 4. Değişikliklerinizi Yapın

- Markdown dosyaları için: Açıklayıcı başlıklar ve yapılandırılmış içerik
- Python dosyaları için: Docstring ve tip ipuçları ekleyin
- Yeni klasörler için: README.md ekleyin

### 5. Commit Edin

```bash
git add .
git commit -m "feat: yeni teori eklendi - zeka tanımı"
```

**Commit mesaj formatı:**
- `feat:` Yeni özellik/icerik
- `fix:` Hata düzeltmesi
- `docs:` Dokümantasyon güncellemesi
- `refactor:` Kod yapılandırma
- `test:` Test ekleme

### 6. Push ve Pull Request

```bash
git push origin ozellik/konu-adi
```

GitHub'da Pull Request (PR) oluşturun.

## İçerik Standartları

### Markdown Dosyaları

```markdown
# Başlık

## Alt Başlık

Açıklayıcı paragraflar...

### Bölümler

- Maddeli liste
- Tablolar kullanın
- Kod blokları ekleyin

## Kaynaklar

- [Yazar, Yıl] - Başlık
```

### Python Kodu

- PEP 8 stiline uygun
- Docstring zorunlu
- Tip ipuçları (typing) önerilir
- Yorumlar açıklayıcı olmalı

Örnek:
```python
def function_name(param: str) -> bool:
    """
    Fonksiyon açıklaması.
    
    Args:
        param: Parametre açıklaması
        
    Returns:
        Dönüş değeri açıklaması
    """
    return True
```

## Kod İnceleme Süreci

1. **Otomatik kontroller:**
   - Markdown linting
   - Python syntax check

2. **Manuel inceleme:**
   - İçerik doğruluğu
   - Kaynak gösterimi
   - Dil ve anlatım

3. **Onay ve merge:**
   - En az 1 onay gerekli
   - Çatışma (conflict) çözümü

## Topluluk Kuralları

- Saygılı ve yapıcı olun
- Farklı görüşlere açık olun
- Akademik dürüstlük gösterin
- Kaynak belirtmeyi unutmayın

## İletişim

- Sorular için: GitHub Issues
- Tartışmalar için: GitHub Discussions
- Özel konular: [E-posta / iletişim bilgisi]

## Katkıcılar

Projeye katkıda bulunan herkese teşekkürler!

---

*"Birlikte daha anlamlı sorular soruyoruz."*
