import sys
path = '/Users/chaithanyakota/Code/project/final-env/lib/python3.11/site-packages'
# For example: /path/to/your/project/venv/lib/python3.11/site-packages 

sys.path.append(path)

import cv2
import os
from werkzeug.utils import secure_filename
from flask import Flask,request,render_template


UPLOAD_FOLDER = '/Users/chaithanyakota/Code/project/static/uploads'
#               '/path/to/your/project/static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def make_sketch(img):
    grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(grayed)
    blurred = cv2.GaussianBlur(inverted, (19, 19), sigmaX=0, sigmaY=0)
    final_result = cv2.divide(grayed, 255 - blurred, scale=256)
    return final_result


@app.route('/',)
def home():
        return render_template('index.html')
        
              
@app.route('/sketch',methods=['POST'])
def sketch():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        img = cv2.imread(UPLOAD_FOLDER+'/'+filename)
        sketched_img = make_sketch(img)
        
        sketched_img_name = filename.split('.')[0]+"_sketch.jpg"
        
        _ = cv2.imwrite(UPLOAD_FOLDER+'/'+sketched_img_name, sketched_img)
        return render_template('index.html',original_img_name=filename,sketch_img_name=sketched_img_name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
    