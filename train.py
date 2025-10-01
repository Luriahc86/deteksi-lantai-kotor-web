from ultralytics import YOLO

# 1. Load model YOLOv8 classification (pretrained)
#    Pilihan: yolov8n-cls.pt (paling ringan), yolov8s-cls.pt (lebih akurat), dst.
model = YOLO("yolov8n-cls.pt")

# 2. Training
model.train(
    data="dataset",    # folder dataset
    epochs=20,
    imgsz=224,
    batch=16,
    device="cpu"       # pakai CPU
)

# 3. Setelah training, model terbaik tersimpan di:
# runs/classify/train/weights/best.pt
