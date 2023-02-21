from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template('index.html')

@app.route("/<string:page_name>")
def aboutPage(page_name):
    return render_template(f'{page_name}')

""" @app.route("/login", methods=['POST','GET'])
def login():
    error=None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return log_the_user(request.form['username'])
        else:
            error = 'invalid username/password'
    return render_template('login.html', error = error) """

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            with open("database.txt", mode = "a") as db:
                for key,value in data.items():
                    db.write(f"{key}:{value}\n")
                db.close
            return redirect('thankyou.html')
        except:
            return "error"
        
def write_to_csv(data):
    with open("database.csv", mode = "a") as db:
            csv_writer = csv.writer(db,lineterminator='\n',delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([data['email'],data['subject'],data['message']])
            db.closesadf

""" @app.route("/about.html")
def aboutPage():
    return render_template('about.html')

@app.route("/components.html")
def componentsPage():
    return render_template('components.html')

@app.route("/thankyou.html")
def thankYouPage():
    return render_template('thankyou.html')

@app.route("/work.html")
def workPage():
    return render_template('work.html')

@app.route("/works.html")
def worksPage():
    return render_template('works.html')

@app.route("/contact.html")
def contactPage():
    return render_template('contact.html') """
