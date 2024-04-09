# Studying-API-OpenAI

EN-US
To use this project you need to download some packages, I'll leave them here, just paste them into the prompt:
    python -m venv projectname
    projectName\Scripts\activate
    pip install openai python-dotenv pydub instabot pillow

Understand what this means:
    from openai import OpenAI
    dotenv import load_dotenv
    import operating system

Right after going to the OpenAI website and make a key (API_KEY) and copy the key code, create a .env and put:
    OPENAI_API_KEY = "Paste key here"

Create a gitignore case for you to put on github or elsewhere like this:
    .env
    *.env

This way your key will not be shared.

-----------------------------------------------------------------------------------------------------------------------------------------------------

PT-BR
Para o uso desse projeto é necessario baixar alguns pacotes, vou deixar aqui apenas cole no prompt: 
    python -m venv nomeDoProjeto
    nomeDoProjeto\Scripts\activate
    pip install openai python-dotenv pydub instabot Pillow

Realize as importações: 
    from openai import OpenAI
    from dotenv import load_dotenv
    import os

Logo após vá ao site do OpenAI e faça uma chave (API_KEY) e copie o código da chave, crie um .env e coloque: 
    OPENAI_API_KEY = "Cole a chave aqui"

Crie um gitignore caso for você for colocar no github ou outro lugar assim: 
    .env
    *.env

Desta forma sua chave nao será compartilhada.
