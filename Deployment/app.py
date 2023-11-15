from flask import Flask , render_template , request
import numpy as np
import tensorflow as tf
import pandas as pd
from tensorflow.keras.preprocessing import image
import pickle
import os
import google.generativeai as palm
from flask import jsonify



app = Flask(__name__)

model = tf.keras.models.load_model('finetuned_inceptionv3_model.h5')

df=pd.read_csv('vitamins.csv')

palm.configure(api_key="AIzaSyAqGPICr190pACB8wijn7FMlSK5s5NXOCs")

with open('class_labels.txt', 'r') as file:
    class_labels = [line.strip() for line in file.readlines()]



#@app.route('/', methods=['GET'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,'uploads',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        img_path = filepath
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        print(img_array)
        img_array = np.expand_dims(img_array, axis=0)
        print(img_array)
        img_array /= 255.
        prediction = model.predict(img_array)
        predicted_class_index = np.argmax(prediction)
        predicted_class = class_labels[predicted_class_index]
        name=predicted_class
        if name in df['Name'].values:
            row = df.loc[df['Name'] == name]
            vitamins_data = []
            for col in df.columns:
                value = row[col].values[0]
                if isinstance(value, np.int64):
                    value = int(value)
                vitamins_data.append({col: str(value)})
            #vitamins=row.to_string(index=False)
            prompt = f"you are a Nutrition specialist , tell 2 Interseting facts about {name}"
            model_name='models/text-bison-001'
            palm_ans=(f"Few facts about {name}:")
            completion= palm.generate_text(
            model=model_name,
            prompt=prompt,
            temperature=0.3,
            max_output_tokens=80, )
            facts=str(completion.result)
            sol = [vitamins_data,facts]
            
            return jsonify(sol)
        else:    
            return jsonify("We don't have Nutrition Data or the Input is not trained yet, sorry!!!")

    return jsonify("The input image is not trained , we will work on it!! sorry")

if __name__ == '__main__':
    #app.run(port=3000,debug=True)
    app.run(debug = False, threaded = False)
