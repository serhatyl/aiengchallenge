# 180 Günlük AI Engineering Öğrenme Günlüğü

Hedefim, mevcut yazılım ve frontend deneyimimi kullanarak AI Engineering alanına ilerlemek; Python ile LLM tabanlı uygulamalar geliştirmek, bunları test etmek ve güvenli biçimde çalıştırmak.

## İlerleme durumu

- **Tamamlanan:** Gün 1–8
- **Sıradaki:** Gün 9 — API anahtarını ortam değişkeninden güvenli biçimde okumak
- Her günün sonunda çıktıyı, takıldığım noktayı ve sonraki adımı kaydedeceğim.

## Gün gün çalışma kaydı

### Gün 1 — Çalışma ortamı ve depo

- Proje klasörünü ve Python sanal ortamı çalışma akışını oluşturdum.
- AI Engineering'e geçiş hedefimi ve öğrenme günlüğü tutma amacımı belirledim.
- **Çıktı:** Python proje iskeleti ve bağımlılık dosyaları.

### Gün 2 — `pathlib`, `dataclass` ve dosya işlemleri

- `Path` ile klasör/dosya yollarını yönetip dosya adı, uzantı ve boyut bilgilerini çıkardım.
- `dataclass` kullanarak dosya bilgilerini `FileInfo` nesnelerinde tuttum.
- Olmayan klasör ve dosya olmayan yol durumlarını ele aldım; örnek dosyalarla denedim.
- **Takıldığım nokta:** `Path` ile `FileInfo` nesnesini karıştırıp dosya tanımlama fonksiyonunu yanlış türde değerle çağırdım. Fonksiyonların girdi ve dönüş tiplerini kontrol ederek düzelttim.

### Gün 3 — Pydantic doğrulaması

- `ScanRequest`, `FileOutput` ve `ScanResponse` modelleriyle giriş/çıkış verilerini doğruladım.
- Alan sınırlarını `Field` ile tanımladım.
- **Takıldığım nokta:** `FileInfo.size` ile Pydantic modelindeki `size_bytes` alanı eşleşmedi. Dönüşüm sırasında alan adlarının modelle aynı olması gerektiğini öğrendim.

### Gün 4 — pytest ile test

- Dosya tanımlama ve klasör listeleme davranışları için pytest testleri yazdım.
- `tmp_path` fixture'ı ile geçici dosya ve klasörler oluşturdum.
- `file_catalog` import hatasında testin beklediği modül adıyla proje dosyasının adının uyuşmadığını tespit ettim.

### Gün 5 — FastAPI uç noktaları

- FastAPI uygulamasında `GET /health` ve `POST /ask` uç noktalarını oluşturdum.
- Swagger arayüzünde (`/docs`) iki endpoint'i deneyip yanıtları kontrol ettim.
- `/ask` şu aşamada gerçek bir LLM çağrısı yapmıyor; gelen soruyu örnek yanıt olarak geri döndürüyor.

### Gün 6 — Test ve lint akışı

- `pytest` testlerini ve Ruff kontrollerini yerel ortamda çalıştırdım.
- `requirements-dev.txt` içinde geliştirme araçlarını (`pytest`, `ruff`) temel bağımlılıklardan ayırdım.
- **Durum:** Kullanıcı bildirimiyle pytest ve Ruff bölümleri tamamlandı.

### Gün 7 — Haftalık gözden geçirme

- Servisi çalıştırıp `/health` ve `/ask` uçlarını Swagger üzerinden yeniden kontrol ettim.
- İlk haftada dosya işlemleri, Pydantic şemaları, testler, FastAPI ve lint konularını uyguladım.
- **Çıktı:** Çalışan yerel API iskeleti ve test edilebilir dosya kataloğu.

### Gün 8 — LLM API akışını anlama

- Bir LLM API kullanımında uygulamanın sağlayıcıya istek gönderdiğini, yanıt içinden üretilen metni aldığını ve kullanım/gecikme gibi bilgileri izleyebileceğini öğrendim.
- API anahtarının kaynak koda yazılmaması gerektiğini belirledim. Yerelde `.env` dosyası kullanılacaksa Git dışında tutulmalı; CI/CD ortamında platformun secret değişkenleri kullanılmalı.
- **Not:** Henüz sağlayıcı seçimi veya gerçek model çağrısı yapılmadı. Bu günün uygulama adımı, rehberlikle API akışının kavramsal olarak incelenmesiydi.

## Haftalık hedefler

### 1. hafta — Geliştirme zemini ve LLM temelleri

- Yerel Python servis iskeleti, testli yardımcı modüller ve ilk model çağrısına hazırlık.
- **Durum:** Gün 1–7 tamamlandı. Servis iskeleti hazır; gerçek model çağrısı sonraki günlerde yapılacak.

### 2. hafta — LLM API, istem tasarımı ve yapılandırılmış çıktı

- Dayanıklı, şema doğrulamalı ve ölçülebilir bir LLM API katmanı kurmak.
- **Durum:** Gün 8 tamamlandı; sıradaki çalışma Gün 9.

## Öğrenme notları

- API anahtarı bir sırdır: kaynak koda, README'ye, loglara veya repoya eklenmemelidir.
- `.env` yerel geliştirmede kullanılabilir; `.gitignore` içinde tutulmalıdır. CI/CD'de secret/environment variable mekanizması kullanılmalıdır.
- Pydantic doğrulama hatalarında beklenen alan adlarıyla üretilen verinin alan adlarını karşılaştırmalıyım.
- Bir fonksiyona yanlış nesne türü gönderildiğinde, çağrı zincirini ve tip sözleşmesini takip etmeliyim.

## Sonraki adım

**Gün 9:** API anahtarını ortam değişkeninden okuma düzenini kur. Anahtarın kendisini bu dosyaya veya sohbete yazma; yerel `.env` dosyasını Git dışında tut ve uygulama yapılandırmasını gizli değerlerden ayrı yönet.
