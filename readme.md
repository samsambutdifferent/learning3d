

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



## compute instance notebook set up

first need to request GPU quota increase


setup compute engine
```
export IMAGE_FAMILY="pytorch-latest-gpu"
export ZONE="us-west1-b"
export INSTANCE_NAME="pcr-instance-1"

gcloud compute instances create $INSTANCE_NAME \
  --zone=$ZONE \
  --image-family=$IMAGE_FAMILY \
  --image-project=deeplearning-platform-release \
  --maintenance-policy=TERMINATE \
  --accelerator="type=nvidia-tesla-v100,count=1" \
  --metadata="install-nvidia-driver=True" \
  --preemptible

```

connect (will create ssh key)
```
export PROJECT_ID="pcr1-309610"
export ZONE="us-west1-b"
export INSTANCE_NAME="pcr-instance-1"
gcloud compute ssh --project $PROJECT_ID --zone $ZONE \
  $INSTANCE_NAME -- -L 8080:localhost:8080
```





