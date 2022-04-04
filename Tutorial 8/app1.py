from flask import Flask,request,render_template,url_for
from flask import jsonify
from facedetection import getimage
from werkzeug.utils import secure_filename
import os
import cv2
app = Flask(__name__)

@app.route('/')

def my_form():
    return render_template('my-form.html')


@app.route('/',methods=['POST'])
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
    cv2.imwrite('annotated_image.png', image)
    #img_url = url_for('static', filename='annotated_image.png')
    #print(img_url)
    okay=cv2.imread('annotated_image.png')
    #cv2.imwrite('annotated_image' + str(idx) + '.png', annotated_image)
    return render_template('results.html', new="okay")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)