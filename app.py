from flask import Flask, request, render_template, render_template_string
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def slang_meaning():
    if request.method == "GET":
        return render_template("input.html")
    elif request.method == "POST":
        input_slang = request.form['username'].upper()
        output = "Slang not found"
        with open('slangs.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[1] == input_slang:
                    output = row[2]
                    break
            
        return render_template('output.html', output=output , input_slang=input_slang)

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')

