import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
   #print('Request for index page received')
   if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume = request.files['resume']
        
        # Save the resume file
        resume.save(resume.filename)
        
        # Perform further processing with the form data and resume file here
        
        return "Form submitted successfully!"
    
#return render_template('index.html')
   return render_template('intern.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#@app.route('/hello', methods=['POST'])
"""
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))
       """


if __name__ == '__main__':
   app.run()
