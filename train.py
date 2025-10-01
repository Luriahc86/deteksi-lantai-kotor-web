from ultralytics import YOLO

# 1. Load model YOLOv8 classification (pretrained)
#    Pilihan: yolov8n-cls.pt (paling ringan), yolov8s-cls.pt (lebih akurat), dst.
model = YOLO("yolov8n-cls.pt")

# 2. Training
model.train(
    data="dataset",    # folder dataset (subfolder = kelas)
    epochs=20,         # jumlah epoch training
    imgsz=224,         # ukuran input gambar
    batch=16,          # jumlah batch
    device=0           # pakai GPU (0) kalau ada, atau -1 untuk CPU
)

# 3. Setelah training, model terbaik tersimpan di:
# runs/classify/train/weights/best.pt
