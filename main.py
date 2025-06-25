import os

from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from threading import Thread
from printer_controller import print_file
from config import UPLOAD_FOLDER, PRINTERS
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
printers_conf = PRINTERS


@app.route("/")
def index():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ['gcode']


@app.route("/send_to_printer", methods = ['GET', 'POST'])
def print_with_printer():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("ошибка ???")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print("Файл не выбран.")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            for printer in printers_conf:
                if printer["status"] == "w":
                    printer["status"] = "p"
                    print("_____________________________________")
                    print(f"Printing on printer {printer["name"]}")
                    print(f"Using port {printer["port"]}")
                    print(f"File {app.config['UPLOAD_FOLDER'] + filename}")
                    th = Thread(target=print_file,args=(app.config['UPLOAD_FOLDER'] +"/"+ filename, printer["port"], printer["baud"],))
                    th.start()

    return redirect("/")
if __name__ == "__main__":
    app.run(port = 2000, host = "0.0.0.0")
