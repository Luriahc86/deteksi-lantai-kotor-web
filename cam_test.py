import cv2
from ultralytics import YOLO

# Load model hasil training
model = YOLO(r"runs/classify/train3/weights/best.pt")

# Buka kamera (0 = default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Kamera tidak ditemukan")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Prediksi
    results = model(frame)
    probs = results[0].probs
    class_id = int(probs.top1)
    confidence = float(probs.top1conf)
    class_name = results[0].names[class_id]

    # Tampilkan hasil di frame
    label = f"{class_name} ({confidence*100:.1f}%)"
    cv2.putText(frame, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2)

    cv2.imshow("Deteksi Lantai Kotor", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
