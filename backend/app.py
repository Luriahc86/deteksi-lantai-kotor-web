from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import numpy as np
import cv2
import os
from ultralytics import YOLO

from . import models, database

# Inisialisasi
models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()
model = YOLO("../runs/classify/train/weights/best.pt")

# Dependency DB
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ✅ Prediksi & simpan riwayat
@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    results = model(img)
    probs = results[0].probs

    class_id = int(probs.top1)
    confidence = float(probs.top1conf)
    class_name = results[0].names[class_id]

    # Simpan file (opsional)
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(filepath, "wb") as f:
        f.write(contents)

    # Simpan ke DB
    new_pred = models.Prediction(
        filename=file.filename,
        predicted_class=class_name,
        confidence=confidence
    )
    db.add(new_pred)
    db.commit()
    db.refresh(new_pred)

    return JSONResponse(content={
        "id": new_pred.id,
        "filename": file.filename,
        "predicted_class": class_name,
        "confidence": confidence,
        "timestamp": str(new_pred.timestamp)
    })

# ✅ Ambil semua riwayat
@app.get("/history")
def get_history(db: Session = Depends(get_db)):
    data = db.query(models.Prediction).all()
    return data

# ✅ Hapus riwayat by ID
@app.delete("/history/{pred_id}")
def delete_history(pred_id: int, db: Session = Depends(get_db)):
    pred = db.query(models.Prediction).filter(models.Prediction.id == pred_id).first()
    if not pred:
        return JSONResponse(content={"error": "Data tidak ditemukan"}, status_code=404)
    db.delete(pred)
    db.commit()
    return {"msg": f"Riwayat dengan id={pred_id} berhasil dihapus"}
