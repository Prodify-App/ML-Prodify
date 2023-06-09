import os

from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


model_urls = {
    "vit_bert_aksesoris_fashion": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_aksesoris_fashion.zip",
    "vit_bert_buku_alat_tulis": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_buku_alat_tulis.zip",
    "vit_bert_elektronik": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_elektronik.zip",
    "vit_bert_fashion_bayi_anak": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_fashion_bayi_anak.zip",
    "vit_bert_fashion_muslim": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_fashion_muslim.zip",
    "vit_bert_fotografi": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_fotografi.zip",
    "vit_bert_handphone_aksesoris": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_handphone_aksesoris.zip",
    "vit_bert_hobi_koleksi": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_hobi_koleksi.zip",
    "vit_bert_ibu_bayi": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_ibu_bayi.zip",
    "vit_bert_jam_tangan": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_jam_tangan.zip",
    "vit_bert_kesehatan": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_kesehatan.zip",
    "vit_bert_komputer_aksesoris": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_komputer_aksesoris.zip",
    "vit_bert_makanan_minuman": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_makanan_minuman.zip",
    "vit_bert_olahraga_outdoor": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_olahraga_outdoor.zip",
    "vit_bert_otomotif": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_otomotif.zip",
    "vit_bert_pakaian_pria": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_pakaian_pria.zip",
    "vit_bert_pakaian_Wanita": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_pakaian_Wanita.zip",
    "vit_bert_perawatan_kecantikan": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_perawatan_kecantikan.zip",
    "vit_bert_perlengkapan_rumah": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_perlengkapan_rumah.zip",
    "vit_bert_sepatu_pria": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_sepatu_pria.zip",
    "vit_bert_sepatu_wanita": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_sepatu_wanita.zip",
    "vit_bert_souvenir_party_supplies": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_souvenir_party_supplies.zip",
    "vit_bert_tas_pria": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_tas_pria.zip",
    "vit_bert_tas_wanita": "https://github.com/Prodify-App/ML-Prodify/releases/download/trained_generation_model/vit_bert_tas_wanita.zip",
}

def download_models():

    model_root = 'models'

    if not os.path.exists(model_root):
        os.mkdir(model_root)

    curr_model = 1

    for name, url in model_urls.items():
        path = f'{model_root}/{name}'

        with urlopen(url) as zipresp:
            with ZipFile(BytesIO(zipresp.read())) as zfile:
                zfile.extractall(path)
        
        print(f"Download Completed: {curr_model}/{len(model_urls)}" )
        curr_model += 1
        