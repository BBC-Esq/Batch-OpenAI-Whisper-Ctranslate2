<a name="top"></a>

<div align="center">
  <h1> Accelerated batch processing of Audio with OpenAI's Whisper
</div>
Simple program to transcribe/translate multiple audio with Opena AI's Whisper software, but using the much faster and less resource intensive Ctranslate2 implementation (courtesy of WhisperX).

# Installation

> I recommend at least [Python 3.10+](https://www.python.org/downloads/release/python-31011/).
<details>
  <Summary>Instructions</Summary>

### Step 1 - Install CUDA
Go [HERE](https://developer.nvidia.com/cuda-toolkit-archive) and select the version of CUDA that you want to install.
> I highly recommend 11.8.0 since it's compatible with the most recent stable version of PyTorch.

### Step 2 - Obtain Repository
Download all the files of my repository to a folder of your choosing.

### Step 3 - Virtual Environment
* Open the folder containing my repository files.  Create a command prompt and create a virtual environment with this command:
```
python -m venv .
```
* Then "activate" the virtual environment:
```
.\Scripts\activate
```
### Step 4 - Upgrade pip
```
python -m pip install --upgrade pip
```

### Step 5 - Install PyTorch
* Nvidia GPUs:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
> If you did not install CUDA 11.8, you must go [HERE](https://pytorch.org/get-started/locally/) to determine the correct command.  Also, remember to change "pip3" to pip since we're working in the virtual environment.

### Step 6 - Install WhisperX
```
pip install git+https://github.com/m-bain/whisperx.git
```

### Step 7 - Install PySide6
```
pip install PySide6
```

</details>

# Usage
<details>
  <summary>Instructions</summary>
  
### Step 1 - Virtual Environment
> Open a command prompt in the folder you saved my files to and once again create a virtual environment.
```
.\Scripts\activate
```

### Step 2 - Run the Main Script
```
python whisper_batch_whisperx.py
```
> This will bring up the GUI and you should be able to figure it out from here.  The Whisper program should download any model you select to the default "cache" directory on your computer.

</details>

# Contact

All suggestions (positive and negative) are welcome.  "bbc@chintellalaw.com" or feel free to create an "issue" on Github or go to the "discussions" portion of this github.

<div align="center">
  <img src="https://github.com/BBC-Esq/Batch-OpenAI-Whisper-Ctranslate2/blob/main/example.png?raw=true" alt="Example Image">
</div>
