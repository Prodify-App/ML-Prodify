import tensorflow as tf

from transformers import AutoImageProcessor, AutoTokenizer, TFVisionEncoderDecoderModel
from utils.chat_completion import ChatCompletion

model_category_dict = {
    "elektronik": "vit_bert_elektronik"
}

class Predict:

    def __init__(self):

        encoder_pretrained = 'google/vit-base-patch16-224'
        decoder_pretrained = 'indolem/indobert-base-uncased'

        self.image_processor = AutoImageProcessor.from_pretrained(encoder_pretrained)
        self.tokenizer = AutoTokenizer.from_pretrained(decoder_pretrained)

        self.model_category_dict = {
            "elektronik": "vit_bert_elektronik"
        }


    def predict(self, pillow_image, category):
        
        with tf.device('/cpu:0'):
            model_path = f'models/{model_category_dict[category]}'
            model = TFVisionEncoderDecoderModel.from_pretrained(model_path)

            pixel_values = self.image_processor(pillow_image, return_tensors="tf").pixel_values
            generated_ids = model.generate(pixel_values)
            generated_text = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

        return generated_text


    def predict_improvement(self, generated_title):

        title_prompt = f'Fix this product title and make it compelling and eye catching "{generated_title}". Only answer with the title in Bahasa Indonesia'
        predicted_title = self.get_result(title_prompt)

        description_prompt = f'Write a description for product titled "{predicted_title}", make it three sentences long. Only answer with the description in Bahasa Indonesia'
        predicted_description = self.get_result(description_prompt)

        return predicted_title, predicted_description
    
     
    def get_result(self, prompt):
        messages = [
            {"role": "user", "content": prompt},
        ]

        results = ""
        for chunk in ChatCompletion.create(messages):
            results += chunk

        return results