from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

app = Flask(__name__)

dic = {0 : 'The Picture is not Clear(Blurry Picture', 1 : 'This is Clear Picture', 
2 : 'Picture is not Allinged in Right Direction', 3 : 'This is not a Human Picture or the Picture is Blank'}

model = load_model('DenseNet201.hdf5')

model.make_predict_function()

def predict_label(img_path):
	i = image.load_img(img_path, target_size=(224, 224))
	i = image.img_to_array(i)/255.0
	i = i.reshape(1, 224, 224, 3)
	p = np.argmax(model.predict_generator(i), axis=-1) 
	return dic[p[0]]

# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Image Recoginition API..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)