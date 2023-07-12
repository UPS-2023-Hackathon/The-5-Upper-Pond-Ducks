import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
import pyodbc as odbc
app = Flask(__name__)

con = odbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:5upducks.database.windows.net,1433;Database=5UPDucks;Uid=connorbell;Pwd=5upduck$;Encrypt=yes;TrustServerCertificate=yes;Connection Timeout=30;')
cursor = con.cursor()

@app.route('/')
def index():
   print('Request for index page received')

   '''cursor.execute("SELECT * FROM dbo.demotable")

   for row in cursor.fetchall():
        print(row)'''

   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
