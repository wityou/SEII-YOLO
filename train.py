from ultralytics import YOLO

model = YOLO('yolo11n-CBAM.yaml')

# Train the model
results = model.train(
  data='VOC.yaml',
  epochs=1000,
  batch=32,
  imgsz=640,
  # scale=0.9,  # S:0.9; M:0.9; L:0.9; X:0.9
  # mosaic=1.0,
  mixup=0.15,  # S:0.05; M:0.15; L:0.15; X:0.2
  copy_paste=0.15,  # S:0.15; M:0.4; L:0.5; X:0.6
  # name='SUBv11-CBAM14-1000',
  patience=50,
  # amp=False,
  workers=0,
  # device="0",
)

# Evaluate model performance on the validation set
# metrics = model.val()

# Perform object detection on an image
# results = model("assets/bus.jpg")
# results[0].show()

