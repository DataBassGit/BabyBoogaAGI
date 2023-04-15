# BabyBoogaAGI
Porting BabyAGI to Oobabooba.

Development of this project has moved to a new repo: https://github.com/DataBassGit/BigBoogaAGI

The scope of the project has grown, and so the name has grown too.


Original GPT-4 version:
https://github.com/yoheinakajima/babyagi

You need Oobabooga installed and running in order to use this. Oobabooga can be found here:

https://github.com/oobabooga/text-generation-webui

You need to modify the start-webui.bat to replace the server init with this line:
python server.py --auto-devices --listen --no-stream

This change disables the web interface.


You have to enter your pinecone API key in the main.py script. Your pinecone index dimensions must be 768.
