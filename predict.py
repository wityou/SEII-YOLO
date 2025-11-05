from ultralytics import YOLO

model_name = 'yolo11n.pt'
image_name = './assets/000056_contrast.jpg'
model = YOLO(model_name)  # Replace with the desired model scale
model.predict(
    source=image_name,
    # source=0,
    # imgsz=640,
    show=True,
    # save=True,
    # name = 'pre_sub'  #model_name[:-3]+'-'+image_name[:-4]
)