import os

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


model_urls = {
    "vit_bert_elektronik": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_elektronik.zip"
}

def download_models():

    model_root = 'models'
    os.mkdir(model_root)

    for name, url in model_urls.items():
        path = f'{model_root}/{name}'

        with urlopen(url) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(path)

    # return "OK"
        