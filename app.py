import os
from flask import Flask, render_template, request, redirect, url_for, send_file
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-002"

app = Flask(name)

@app.route("/")
def index():
return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
input_text = request.form["input_text"]
output_text = generate_text(input_text)
return render_template("results.html", output_text=output_text)

def generate_text(prompt):
model = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
return model.choices[0].text

@app.route("/download")
def download():
output_text = request.args.get("output_text")
file_name = "spravka-obosnovanie.docx"
create_document(file_name, output_text)
return send_file(file_name, as_attachment=True)

def create_document(file_name, text):
with open(file_name, "w", encoding="utf-8") as f:
f.write(text)

if name == "main":
app.run()
