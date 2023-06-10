import tensorflow as tf

from transformers import AutoImageProcessor, AutoTokenizer, TFVisionEncoderDecoderModel

if __name__ == "__main__":
    model_path = f'models/vit_bert_elektronik'
    print("Load")
    model = TFVisionEncoderDecoderModel.from_pretrained(model_path)
    print("Load Complete")
