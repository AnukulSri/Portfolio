from flask import Flask,render_template,url_for,redirect,request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def Projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['Email']
        message = request.form['Textarea1']
        phone_no = request.form['phone']
    return redirect(url_for('db',nm=name,em=email,msg=message,ph=phone_no))


@app.route('/db/<string:nm>/<string:em>/<string:msg>/<string:ph>')
def db(nm,em,msg,ph):
    
    conn= mysql.connector.connect(
        host = 'localhost',
        user = 'sqluser',
        password = 'password',
        database = 'Portfolio'
     )
    mycursor = conn.cursor()
    mycursor.execute(
        'insert into viewer (Name,Email,Message,phone) VALUES (%s,%s,%s,%s)',(nm,em,msg,ph)
    )
    conn.commit()
    conn.close()
    return redirect(url_for('contact'))
if __name__ =='__main__':
    app.run(debug=True)