# Face Recognition Access Control System

## Description
Bu proje, webcam kullanarak gerçek zamanlı yüz tanıma yapan basit bir giriş kontrol sistemidir. Sistem, önceden tanımlanmış kişilerin yüzlerini tanıyarak güvenli giriş sağlar. Tanınan kişiler için "Giriş başarılı" mesajı gösterilirken, tanınmayan kişiler için "Giriş yapılamıyor" uyarısı verilir.

## Özellikler
- Gerçek zamanlı yüz tanıma
- Çoklu yüz tanıma desteği
- Basit ve kullanıcı dostu arayüz
- Anlık görsel geri bildirim
- Kolay kurulum ve yapılandırma

## Gereksinimler

Programı çalıştırmak için aşağıdaki kütüphanelere ihtiyaç vardır:

```
face_recognition==1.3.0
opencv-python==4.8.0.76
numpy==1.24.3
```

Gereksinimleri yüklemek için:

```
pip install -r requirements.txt
```

## Kullanım

1. `known_faces` klasörüne tanınmasını istediğiniz kişilerin fotoğraflarını ekleyin.
   - Fotoğraf dosyalarının adları kişilerin isimleri olmalıdır (örn. `Tarik.jpeg`, `Emir.jpeg`).
   - Fotoğraflarda yüzler net bir şekilde görünmelidir.

2. Programı çalıştırın:

```
python face_recognition_app.py
```

3. Webcam açılacak ve yüz tanıma işlemi başlayacaktır.
   - Tanınan kişiler için: "[İsim], Giriş başarılı" mesajı gösterilir.
   - Tanınmayan kişiler için: "Kullanıcı tanınamadı, Giriş yapılamıyor" mesajı gösterilir.

4. Programdan çıkmak için 'q' tuşuna basın.

## Not

Bu program, yüz tanıma için `face_recognition` kütüphanesini kullanmaktadır. Bu kütüphane, dlib kütüphanesine bağlıdır ve kurulumu bazı sistemlerde zor olabilir. Windows'ta kurulum yaparken sorun yaşarsanız, Visual C++ Build Tools ve CMake yüklemeniz gerekebilir. 