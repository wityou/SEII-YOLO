# 🛠️ Installation & Reproduction Guide (Windows + PyCharm)

This guide provides step-by-step instructions to set up the environment and run the **SEII-YOLO** model on a Windows system using **PyCharm**.

## 1. Prerequisites
Before you begin, ensure you have the following installed:
*   **Anaconda** or **Miniconda**: [Download Here](https://www.anaconda.com/download)
*   **PyCharm Community/Professional**: [Download Here](https://www.jetbrains.com/pycharm/download/)
*   **Git** (Optional, for cloning): [Download Here](https://git-scm.com/downloads)
*   **NVIDIA GPU Driver** (Optional, for GPU acceleration)

---

## 2. Environment Setup (Anaconda Prompt)

1.  **Clone or Download the Repository**
    *   Use Git: `git clone https://github.com/wityou/SEII-YOLO.git`
    *   Or download the ZIP file and extract it to a folder (e.g., `D:\Projects\SEII-YOLO`).

2.  **Open Anaconda Prompt**
    *   Press `Win` key, search for "Anaconda Prompt", and open it.

3.  **Create a Virtual Environment**
    Create a clean environment with Python 3.10:
    ```bash
    conda create -n seii-yolo python=3.10
    ```

4.  **Activate the Environment**
    ```bash
    conda activate seii-yolo
    ```

5.  **Install PyTorch (GPU Version)**
    *   *Note: Check your CUDA version using `nvidia-smi`. Below is for CUDA 11.8/12.x.*
    ```bash
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    ```
    *(If you only have CPU, use: `pip install torch torchvision torchaudio`)*

6.  **Install Other Dependencies**
    Navigate to your project directory and install requirements:
    ```bash
    cd /d D:\Projects\SEII-YOLO  # Change to your actual path
    pip install -r requirements.txt
    pip install -e .
    ```

---

## 3. Configuring PyCharm

1.  **Open Project**
    *   Launch PyCharm.
    *   Click **Open** and select the `SEII-YOLO` folder.

2.  **Select the Python Interpreter**
    *   Go to **File** > **Settings** (or `Ctrl+Alt+S`).
    *   Navigate to **Project: SEII-YOLO** > **Python Interpreter**.
    *   Click **Add Interpreter** > **Add Local Interpreter...**
    *   Select **Conda Environment**.
    *   Choose **Use existing environment**.
    *   In the dropdown, select the `seii-yolo` environment you just created.
        *   *If it doesn't appear, point the interpreter path to: `C:\Users\YourUser\anaconda3\envs\seii-yolo\python.exe`*
    *   Click **OK** to apply.

---

## 4. Running the Code

### To Train the Model
1.  In the PyCharm Project view (left panel), locate `train.py`.
2.  Right-click `train.py` and select **Run 'train'**.
    *   *Alternatively, open the Terminal tab in PyCharm (bottom) and type:*
        ```bash
        yolo detect train model=seii-yolo.yaml data=substation.yaml epochs=100 imgsz=640 device=0
        ```

### To Validate (Test)
1.  Locate `val.py`.
2.  Right-click `val.py` and select **Run 'val'**.
    *   *Terminal command:*
        ```bash
        yolo detect val model=runs/detect/train/weights/best.pt data=substation.yaml
        ```

### To Inference (Predict)
1.  Locate `predict.py`.
2.  Right-click `predict.py` and select **Run 'predict'**.
    *   *Terminal command:*
        ```bash
        yolo detect predict model=runs/detect/train/weights/best.pt source=datasets/test/images
        ```

---

## ✅ Verification
If the setup is correct, you should see the training progress bar or detection results in the PyCharm "Run" console. Results will be saved in the `runs/detect/` directory.
