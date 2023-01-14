from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)
app.debug = True


@app.route('/<string:pagename>')
def page(pagename):
    if pagename == 'home':
        return render_template('index.html')
    return render_template(pagename + '.html')

def write_to_file(data):
    with open('database.txt', 'a' ) as database:
        email = data['email']
        subject = data['subject'] 
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a' ) as database2:
        email = data['email']
        subject = data['subject'] 
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:    
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except: 
            return 'did not save to database'
    else:
        return redirect('/ooops.html')
    

        

if __name__ == '__main__':
    app.run()