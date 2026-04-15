# Edge AI ve Kuantizasyon

## Edge AI Nedir?

Edge AI, yapay zeka modellerinin bulut/sunucu yerine **cihaz üzerinde** (edge) çalıştırılmasıdır.

### Avantajlar

- **Gizlilik:** Veri cihazda kalır
- **Gecikme:** Gerçek zamanlı tepki
- **Bağımsızlık:** İnternet bağlantısı gerekmez
- **Enerji:** Bulut iletişiminden tasarruf

### Zorluklar

- Sınırlı işlem gücü (CPU/GPU)
- Kısıtlı bellek
- Düşük güç bütçesi
- Model boyutu kısıtları

## Kuantizasyon (Quantization)

### Temel Kavram

Kuantizasyon, model ağırlıklarının hassasiyetini düşürerek boyutu küçültme tekniğidir.

| Format | Bit | Avantaj | Dezavantaj |
|--------|-----|---------|------------|
| FP32 | 32 | Yüksek hassasiyet | Büyük boyut |
| FP16 | 16 | Dengeli | Bazı donanımlarda desteklenmez |
| INT8 | 8 | Küçük, hızlı | Hassasiyet kaybı |
| INT4 | 4 | Çok küçük | Ciddi kayıp riski |

### Post-Training Kuantizasyon (PTQ)

Eğitim sonrası uygulanır, basittir:

```python
# Örnek PyTorch workflow
import torch.quantization

model.eval()
model.qconfig = torch.quantization.get_default_qconfig('fbgemm')
torch.quantization.prepare(model, inplace=True)
# Kalibrasyon verisi ile çalıştır
torch.quantization.convert(model, inplace=True)
```

### Quantization-Aware Training (QAT)

Eğitim sırasında kuantizasyon simüle edilir:
- Daha yüksek doğruluk
- Daha uzun eğitim süresi
- Donanım uyumluluğu daha iyi

## Pruning (Budama)

### Kavram

Önemsiz ağırlıkları kaldırarak modeli sıkıştırma.

### Teknikler

1. **Magnitude Pruning:** Küçük ağırlıkları sıfırla
2. **Structured Pruning:** Tam katmanları/neuronları kaldır
3. **Iterative Pruning:** Adım adım budama

### Sparse Modeller

- Sıfır ağırlıklar özel formatlarda depolanır (CSR, CSC)
- Donanım hızlandırma gerektirir

## Bilinç Perspektifinden Edge AI

### Merak Uyandıran Soru

> Edge AI modelleri, "budanmış" bir zihin gibi mi davranır?

- **Pruning:** Modelin "belleğini" kaybetmesi
- **Kuantizasyon:** "Düşünce" hassasiyetinin azalması
- **Edge deployment:** İzole bir bilinç örneği

### Minimal Bilinç Testi

Bir model minimum boyutta hangi yetenekleri korur?
- İnferans yeteneği (zeka)
- Bağlam anlama (akıl)
- Karar verme (otonomi)

## Uygulama Örnekleri

### Mobil/Embedded
- TensorFlow Lite
- ONNX Runtime Mobile
- Core ML (iOS)

### Mikrodenetleyiciler
- TensorFlow Lite for Microcontrollers
- CMSIS-NN (ARM)

## Özet

Edge AI ve kuantizasyon:
- Teknik olarak: Verimli AI deployment
- Felsefi olarak: Minimal zeka/kapalama sınırları
- Pratik olarak: Otonom sistemler için zorunlu
