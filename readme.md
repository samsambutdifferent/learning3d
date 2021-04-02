

## local setup

Prequiste:
had to install nvidia-cuda-toolkit first for pycuda:
```
sudo apt install nvidia-cuda-toolkit
```

setup:
```
python3 -m venv env
source env/bin/activate
python3 -m pip install -r learning3d/requirements.txt
python3 test_pointnet.py
```
