from flask import Flask, render_template,request

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')
\
@app.route('/submit',methods=['POST'])
def submit_form():

    name = request.form['name']
    email = request.form['email']

    #process your inputs here, for simplicity, just returning them
    result = f'Name: {name}, Email:{email}'

    return render_template('index.html', result = result)

app.run(debug=True)