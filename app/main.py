from os.path import join
from shutil import rmtree
from tempfile import mkdtemp
from werkzeug.utils import secure_filename
from flask import Flask, request
import textract

app = Flask(__name__)


@app.route('/textract', methods=['POST'])
def create():
    upload = request.files['file']
    temp_dir = mkdtemp()
    filename = secure_filename(upload.filename)
    file_path = join(temp_dir, filename)
    upload.save(file_path)
    text = textract.process(file_path)
    rmtree(temp_dir)
    return text


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True)
