from flask import Flask,request,render_template,url_for
from flask import jsonify
from facedetection import getimage
from werkzeug.utils import secure_filename
import os
import cv2

#PEOPLE_FOLDER = os.path.join('static', 'people_photo') 
#app = Flask(__name__)
app = Flask(__name__, static_url_path="", static_folder="static")
#app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route('/')

def my_form():
    return render_template('my-form.html')


@app.route('/',methods=['POST',"GET"])
# def look_up():
#     # results = get_comments(videoid)
#     channelid=request.form.get("channelid")
#     results = get_channelinfo(channelid)
#     return jsonify(results)
  
def look_up():
    # results = get_comments(videoid)
    file=request.files['file']
    name=secure_filename(file.filename)
    file.save(name)
    image = getimage([name])
    cv2.imwrite('static/annotated_image.png',image)
    img_url = url_for('static', filename='annotated_image.png')
    return render_template('results.html', new=img_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)