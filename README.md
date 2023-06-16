# Prodify Machine Learning Repository
## Dataset
We created our own dataset by scraping products data from e-commerce dataset. We scrapped **Shopee Indonesia products** using **Selenium Python** and collected around **160K+** product data. The dataset contains **product id, images, name, store, store id, main category, and sub category**. We published our dataset on [**Kaggle**](https://www.kaggle.com/datasets/adirizq/shopee-product-images).
## Models
We created two types of models, which are Product Category Classification Model and Title Generation Model.
### Product Category Classification Model
There is two kinds of product category classification model we create, first one is based on product image and the other one is based on product title. We will only explain the first one, because that is what we used in our Prodify Application. Here are the detail of our product category classification model based on image.

- Trained on our scrapped product dataset
- Built and trained using TensorFlow
- Using transfer learning technique
- Pre-trained MobileNetV2 was used for transer learning
- Deployed using TFLite

### Product Title Generation Model
The product title generation model was used to create product title using only the image of the product. Here are the detail of the model.

- Trained on our scrapped product dataset
- Built and trained using TensorFlow and Hugging Face
- Hugging Face provides the model architecture and pretrained model, while TensorFlow used for training
- Using Fine-tuning technique
- The architecture we used is VisionEncoderDecoder model
- We finetuned pre-trained [ViT](https://huggingface.co/google/vit-base-patch16-224) by Google as our Encoder and pre-trained BERT ([IndoBERT](https://huggingface.co/indolem/indobert-base-uncased) by Koto et al.) as our Decoder
- Deployed using Flask and Gunicorn
