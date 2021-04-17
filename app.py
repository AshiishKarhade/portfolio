from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

def write_data(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    #msg = Message(subject, sender=email, recipients=["akarhade5@gmail.com"])
    #msg.body = message
    #mail.send(msg)
    with open('database.txt', 'a') as f:
        f.write("email:{}, subject:{}, message:{} \n".format(email, subject, email))

@app.route('/submit_form', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        data = request.form.to_dict()
        write_data(data)
        return render_template('thankyou.html')
    else:
        return "form not submitted"


@app.route('/<string:page_name>')
def page(page_name="/"):
    try:
        return render_template(page_name)
    except:
        return redirect('/')


def before_request():
    app.jinja_env.cache = {}

if __name__=="__main__":
    app.before_request(before_request)
    app.run(debug=True)

