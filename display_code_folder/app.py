from flask import Flask,url_for,render_template,request
import spacy 
from spacy import displacy

nlp = spacy.load('../display_code_folder/Model_3')
import json

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)


# def analyze_text(text):
# 	return nlp(text)

@app.route('/')
def index():
	# raw_text = "Bill Gates is An American Computer Scientist since 1986"
	# docx = nlp(raw_text)
	# html = displacy.render(docx,style="ent")
	# html = html.replace("\n\n","\n")
	# result = HTML_WRAPPER.format(html)

	return render_template('index.html')


@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		docx = nlp(raw_text)
		colors = {"POLITICS": "linear-gradient(90deg, #aa9cfc, #fc9ce7)",
				  "FOOD": "linear-gradient(90deg, #33ACFF , #33C7FF)",
				  "ENTERTAINMENT": "linear-gradient(90deg, #FFC300 , #FFB833 )",
				  "TECH": "linear-gradient(90deg, #FF5733 , #FFB833 )" }
		options = {"ents": ["POLITICS","FOOD","ENTERTAINMENT","TECH"], "colors": colors}
		html = displacy.render(docx,style="ent",options=options)
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

	return render_template('result.html',rawtext=raw_text,result=result)


@app.route('/previewer')
def previewer():
	return render_template('previewer.html')

@app.route('/preview',methods=["GET","POST"])
def preview():
	if request.method == 'POST':
		newtext = request.form['newtext']
		result = newtext

	return render_template('preview.html',newtext=newtext,result=result)


if __name__ == '__main__':
	app.run(debug=True)