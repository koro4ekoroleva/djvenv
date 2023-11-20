from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageOps
# import tensorflow as tf
from tensorflow import keras, nn
from tensorflow.python import ops
from keras.models import load_model
import numpy as np


menu = menu = [{"title": 'Главная', "url": "hello"},
                {"title": 'Помощь', "url": "help"},
        {"title": "Разработчик", "url": "me"}]


# classes = ['шаурма', 'суши']
# model = load_model('ml/mysite/model/my_model.h5')
# img_height = 160
# img_width = 160
#
#
# def upload_file(f):
#     with open(f"ml/mysite/model/imgs/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#
#
# def ml(image):
#     img = tf.keras.utils.load_img(
#         image, target_size=(img_height, img_width)
#     )
#     img_array = tf.keras.utils.img_to_array(img)
#     img_array = tf.expand_dims(img_array, 0)
#     predictions = model.predict(img_array)
#     score = tf.nn.softmax(predictions[0])
#     return f"'На этом фото скорее всего {classes[np.argmax(score)]} с вероятностью {100 * np.max(score)} процентов."
#
#     # size = (160, 160)
#     # image = Image.open(image)
#     # image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
#     # img_array = keras.utils.img_to_array(image)
#     # img_array = expand_dims(img_array, 0)
#     # predictions = model.predict_on_batch(img_array).flatten()
#     # predictions = nn.sigmoid(predictions)
#     # predictions = tensorflow.where(predictions < 0.5, 0, 1)
#
# def index(request):
#     if request.method == "POST":
#         return render(request, 'index.html')
#         upload_file(request.FILES['ml_photo'])
#     elif request.method == "GET":
#         return render(request, 'index.html')
#         img_address = "ml/mysite/model/imgs/" + request.FILES['ml_photo'].name
#         print(img_address)
#         ml(img_address)



def index(request):
    return render(request, 'index.html')

def about_me(request):
    return render(request, "about_me.html")
