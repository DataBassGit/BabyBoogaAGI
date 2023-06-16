# BabyBoogaAGI

Porting BabyAGI to Oobabooba.

Original GPT-4 version:
https://github.com/yoheinakajima/babyagi

You need Oobabooga installed and running in order to use this. Oobabooga can be found here:

https://github.com/oobabooga/text-generation-webui

You need to modify the start-webui.bat to replace the server init with this line:

```shell
python server.py --listen --no-stream --api
```

You have to enter your pinecone API key in the main.py script. Your pinecone index dimensions must be 768 with cosine metric.

## Quickinstall

After cloning the repo, create a venv, conda or any other environment of your choice.

Then run:

```shell
python -m pip install -r requirements.txt
```

### For AMD GPUs

Run the command bellow before installing the requirements in you venv

```shell
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4.2
```

## Running

just run the `main.py` script