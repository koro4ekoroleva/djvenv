import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

classes = ['шаурма', 'суши']
model = load_model('food_model.h5')
# file_content =
image = byte2image(file_content)

size = (160, 160)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
img_array = tf.keras.utils.img_to_array(image)
img_array = tf.expand_dims(img_array, 0)

predictions = model.predict_on_batch(img_array).flatten()
predictions = tf.nn.sigmoid(predictions)
predictions = tf.where(predictions < 0.5, 0, 1)

bot.send_message(message.chat.id, text=f'На этом фото скорее всего {classes[int(predictions)]}')