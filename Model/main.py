from flask import Flask, render_template, request
import os
import model

UPLOAD_FOLDER = "/home/sai-vamsi-ogety/fastapi_model1/static/text-files/"
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      text_location = os.path.join(UPLOAD_FOLDER,f.filename)
      f.save(text_location)
      with open(text_location,"r") as file:
        content = file.readlines()

      entities = model.entities(content[0])
      return render_template('index.html',content = content, entities = entities)


    return render_template('index.html',content= None)


if __name__ == '__main__':

   app.run(debug = True)