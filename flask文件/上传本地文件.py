from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        return 'file uploaded successfully'
    return render_template('upload.html')
if __name__ == '__main__':
    app.run(debug=True)
