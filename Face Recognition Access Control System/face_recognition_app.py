import face_recognition
import cv2
import numpy as np
import os

known_faces_dir = "known_faces"
known_face_encodings = []
known_face_names = []

for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        image_path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        name = os.path.splitext(filename)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(name)

print(f"Yüklenen yüzler: {known_face_names}")

video_capture = cv2.VideoCapture(0)

if not video_capture.isOpened():
    print("Kamera açılamadı!")
    exit()

print("Kamera başlatıldı. Çıkmak için 'q' tuşuna basın.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Kare alınamadı!")
        break
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Kullanici taninamadi"
        access = "Giris yapilamiyor"
        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            access = "Giris basarili"
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        result_text = f"{name}, {access}"
        cv2.putText(frame, result_text, (left + 6, bottom - 6), font, 0.6, (255, 255, 255), 1)
    
    cv2.imshow('Yüz Tanıma', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()