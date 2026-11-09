# 180 Günlük AI Engineering Öğrenme Günlüğü

Hedefim, mevcut yazılım ve frontend deneyimimi kullanarak AI Engineering alanına ilerlemek; Python ile LLM tabanlı uygulamalar geliştirmek, bunları test etmek ve güvenli biçimde çalıştırmak.

## İlerleme durumu

- **Tamamlanan:** Gün 1–12 (Gün 12 şema üretimi başarılı; hata durumu ayrıca doğrulanmadı)
- **Sıradaki:** Gün 13 — timeout, retry, rate limit ve kullanıcıya dönük hata davranışı
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
- O sırada `/ask` gerçek bir LLM çağrısı yapmıyor, gelen soruyu örnek yanıt olarak geri döndürüyordu.

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

### Gün 9 — API anahtarını güvenli yapılandırma

- `python-dotenv` paketini kurup `requirements.txt` içine kaydettim.
- `OPENAI_API_KEY` değerini yerel `.env` dosyasından yükledim; `.env` zaten `.gitignore` içinde tutuluyor.
- Anahtarın değerini yazdırmadan yalnızca yüklenip yüklenmediğini kontrol ettim.
- CI/CD'de anahtarın platformun secret değişkenleri olarak saklanacağını öğrendim; bu proje için GitHub Actions henüz kurulmadı.

## Haftalık hedefler

### 1. hafta — Geliştirme zemini ve LLM temelleri

- Yerel Python servis iskeleti, testli yardımcı modüller ve ilk model çağrısına hazırlık.
- **Durum:** Gün 1–7 tamamlandı. Servis iskeleti ve ilk haftanın değerlendirmesi hazır.

### 2. hafta — LLM API, istem tasarımı ve yapılandırılmış çıktı

- Dayanıklı, şema doğrulamalı ve ölçülebilir bir LLM API katmanı kurmak.
- **Durum:** Gün 8–10 tamamlandı.

## Öğrenme notları

- API anahtarı bir sırdır: kaynak koda, README'ye, loglara veya repoya eklenmemelidir.
- `.env` yerel geliştirmede kullanılabilir; `.gitignore` içinde tutulmalıdır. CI/CD'de secret/environment variable mekanizması kullanılmalıdır.
- Pydantic doğrulama hatalarında beklenen alan adlarıyla üretilen verinin alan adlarını karşılaştırmalıyım.
- Bir fonksiyona yanlış nesne türü gönderildiğinde, çağrı zincirini ve tip sözleşmesini takip etmeliyim.

### Gün 10 — İlk model çağrısı

- OpenAI Python istemcisi ve Responses API ile `/ask` endpoint'inden gerçek model çağrısı yaptım.
- İlk denemede `input="f{request.question}"` yazdığım için soru modele ulaşmadı; bunu `input=request.question` olarak düzelttim.
- Model: `gpt-4.1-mini`
- Soru: “Türkiye'nin başkenti neresi?”
- Yanıt: “Türkiye'nin başkenti Ankara'dır.”
- Gecikme: **3606.43 ms**
- Kullanım: **39 girdi tokenı**, **10 çıktı tokenı**, **49 toplam token**
- **Çıktı:** `/ask` artık kullanıcı sorusunu modele gönderiyor ve yanıt, gecikme ile token kullanımını döndürüyor.
- İkinci deneme sorusu: “Bana frontend'den AI Engineering'e geçiş için neler yapmam gerektiğini açıklar mısın?”
- Model; matematik, Python, ML/DL, veri bilimi, portföy ve araçlar gibi genel geçiş önerileri verdi. Yanıtta bu kullanıcının zaten frontend geliştiricisi ve orta seviye Python geliştiricisi olduğu yeterince hesaba katılmadı; bu, sonraki prompt denemelerinde iyileştirilecek bir gözlem.
- İkinci deneme gecikmesi: **4140.82 ms**
- İkinci deneme kullanımı: **50 girdi tokenı**, **381 çıktı tokenı**, **431 toplam token**

### Gün 11 — Talimatların çıktıya etkisini karşılaştırma

- Aynı model ve aynı soruyla üç deneme yaptım; system talimatındaki biçim, kişiselleştirme ve ölçülebilirlik beklentilerini değiştirdim.
- **Deneme 1 — kısa yanıt:** En fazla üç madde talimatına rağmen yanıt üç madde oldu, ancak uzun ve genel kaldı. **5,150.33 ms**, 59 girdi / 218 çıktı / 277 toplam token.
- **Deneme 2 — kişiselleştirme:** Üç somut adım istedi; yanıt yine TensorFlow/PyTorch, Pandas/NumPy ve Kaggle gibi genel ML önerileri ağırlıklıydı. Frontend deneyimini belirgin bir avantaja çevirmedi. **3,032.8 ms**, 89 girdi / 254 çıktı / 343 toplam token.
- **Deneme 3 — ölçülebilir plan:** Aylara bölünmüş uzun bir plan ve ölçülebilir çıktılar üretti; ancak kullanıcının LLM, RAG ve AI ürünleri odağı yerine klasik ML/DL, kurs ve sertifika konularını gereğinden fazla öne çıkardı. **6,882.34 ms**, 82 girdi / 853 çıktı / 935 toplam token.
- **Öğrendiğim:** System talimatı yanıtın uzunluğunu ve yapısını etkiliyor. Genel “kişiselleştir” demek yeterli değil; kullanıcı bağlamını ve kapsam dışı konuları açıkça belirtmek gerekiyor. Daha uzun yanıt daha iyi hizalanmış yanıt anlamına gelmiyor.
- **Kontrol notu:** Üç denemede soruyu ve modeli sabit tuttum. Kullanılan system talimatlarını ayrıca deney günlüğünde saklamalıyım ki sonuçlar tekrarlanabilsin.
- **Çıktı:** Üç farklı talimatla karşılaştırmalı model yanıtları ve gecikme/token ölçümleri.

### Gün 12 — Yapılandırılmış çıktı ve Pydantic şeması

- Model yanıtını `AskResponse` Pydantic şemasına göre üretmek için Responses API'nin yapılandırılmış çıktı akışını kullandım.
- Başarılı denemede JSON yanıtı `answer` ve `key_points` alanlarına uydu.
- Soru: “Türkiye'nin başkenti neresidir?”
- Yanıt: “Türkiye'nin başkenti Ankara'dır.” Önemli nokta: Ankara, Türkiye'nin idari başkentidir.
- Gecikme: **3098.02 ms**
- Kullanım: **89 girdi tokenı**, **29 çıktı tokenı**, **118 toplam token**
- **Hata davranışı:** Kodda beklenen yapı parse edilemezse `parsed is None` kontrolüyle HTTP 502 dönmesi eklendi; bu hata yolu henüz ayrıca çalıştırılıp doğrulanmadı.
- **Çıktı:** `/ask` endpoint'inden şemaya uygun cevap ve önemli noktalar.

## Sonraki adım

**Gün 13:** LLM çağrısı için timeout ve geçici hatalarda retry davranışını ele al; rate limit ve sağlayıcı hatalarını kullanıcıya anlaşılır biçimde döndür. Sırları ve teknik detayları hata yanıtına koyma.
