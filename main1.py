from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    text2 = request.form['text2']
    if request.form['action'] == 'plus':
        processed_text=add(int(text),int(text2))
    if request.form['action'] == 'minus':
        processed_text=subtract(int(text),int(text2))
    return str(processed_text)

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

if __name__ == '__main__':
     app.run(host='0.0.0.0')
