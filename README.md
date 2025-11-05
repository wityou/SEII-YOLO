# SEII-YOLO
SII-YOLO11：An Improved algorithm for substation Infrared Image recognition
# Usage
## Install Dependencies
```
git clone https://github.com/wityou/SEII-YOLO.git
cd SEII-YOLO
wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl
conda create -n SEII-YOLO python=3.11
conda activate SEII-YOLO
pip install -r requirements.txt
pip install -e .
```
## Training
Use the following code to train the SEII-YOLO models. Make sure the model configuration file path and the coco dataset configuration file are correct in train.py.
```python
python train.py
```
## Prediction
Use the following code to perform object detection using the SEII-YOLO models. Make sure to replace with the desired model in file.
```python
python predict.py
```
