<a name="top"></a>

<div align="center">
  <h1> Accelerated batch processing of Audio with OpenAI's Whisper
</div>
Simple program to transcribe/translate multiple audio with Opena AI's Whisper software, but using the much faster and less resource intensive Ctranslate2 implementation (courtesy of WhisperX).

# Installation

> I recommend at least [Python 3.10+](https://www.python.org/downloads/release/python-31011/).
<details>
  <Summary>🔥INSTRUCTIONS🔥</Summary>

### Step 1 - Install CUDA
Go [HERE](https://developer.nvidia.com/cuda-toolkit-archive) and install CUDA 11.8.

### Step 2 - Obtain Repository
Download all the files and open the folder containing the ```.py``` file.

### Step 3 - Virtual Environment
Within that folder create a command prompt and then create a virtual environment:
```
python -m venv .
```
Activate the virtual environment:
```
.\Scripts\activate
```
> On Linux run ```source bin/activate```

### Step 4 - Upgrade pip
```
python -m pip install --upgrade pip
```

### Step 5 - Install PyTorch
Nvidia GPUs:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
> If you're not using an Nvidia GPU go [HERE](https://pytorch.org/get-started/locally/) to determine the correct command.

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
  <summary>🔥INSTRUCTIONS🔥</summary>
  
### Step 1 - Virtual Environment
> Open a command prompt in the folder you saved my files to and once again create a virtual environment.
```
.\Scripts\activate
```
> On Linux run ```source bin/activate```

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
