import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import pyodbc as odbc
app = Flask(__name__)

con = odbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:5upducks.database.windows.net,1433;Database=5UPDucks;Uid=connorbell;Pwd=5upduck$;Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;')
cursor = con.cursor()

# isAuth = False

@app.route('/', methods=['GET', 'POST'])
def index():
   #  if isAuth == False:
      if request.method == 'POST':
         username = request.form['username']
         password = request.form['password']

         cursor.execute('EXEC dbo.InternLogin @username=?, @password=?', (username, password))
         isIntern = False
         try:
            rows = cursor.fetchall()
            if len(rows) != 0:
               print(rows)
               isIntern = True
               # isAuth = True
               return render_template('intern.html')
         finally:
            cursor.execute('EXEC dbo.ManagerLogin @username=?, @password=?', (username, password))
            isManager = False
            try:
               rows2 = cursor.fetchall()
               if len(rows2) != 0:
                  print(rows2)
                  isManager = True
                  # isAuth = True
                  return render_template('manager.html')
            except:
               print("No rows2 in result, no valid logins")
      return render_template('login.html')
    

@app.route('/intern', methods=['GET', 'POST'])
def intern():
   # if isAuth == False:
   #     return render_template('login.html')
   #print('Request for index page received')
   if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        resume = request.files['resume']
        
        # Save the resume file
        resume.save(resume.filename)
        
        # Perform further processing with the form data and resume file here
        
        return "Form submitted successfully!"
   # cursor.execute("SELECT * FROM dbo.demotable")

   # for row in cursor.fetchall():
   #      print(row)
    
#return render_template('index.html')
   return render_template('ThankYouPage.html')

@app.route('/manager', methods=['GET', 'POST'])
def manager():
   #  if isAuth == False:
   #     return render_template('login.html')
    if request.method == 'POST':
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            Department = request.files['Department'] 
            return "Form submitted successfully!"
    return render_template('manager.html')
    
    # Perform login verification here
    # Replace the following code with your login verification logic
    #if username == 'admin' and password == 'password' and button_type == "login-button1":
        # Set session or cookie to remember the logged-in state if needed
       # return redirect(url_for('home'))
    #else if username == 'admin' and password == 'password' and button_type == "login-button2":

    #else:
        #return render_template('login.html', error='Invalid username or password')


# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
