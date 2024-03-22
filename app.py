from flask import Flask, render_template, request
from predictor import predict_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        file_path = "static/" + file.filename
        file.save(file_path)
        predicted_class = predict_image('/model_1.pickle', file_path)
        return render_template('result.html', image_file=file_path, predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
