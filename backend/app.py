from ultralytics import YOLO
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
import cv2

app = FastAPI()

# Load model hasil training
model = YOLO("../runs/classify/train/weights/best.pt")

@app.post("/predict/image")
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    npimg = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    results = model(img)
    probs = results[0].probs

    class_id = int(probs.top1)
    confidence = float(probs.top1conf)
    class_name = results[0].names[class_id]

    return JSONResponse(content={
        "predicted_class": class_name,
        "confidence": confidence
    })
