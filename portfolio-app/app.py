from flask import Flask, render_template, request, redirect
import boto3
import os

app = Flask(__name__)
BUCKET_NAME = "leandro-ec2-s3-bucket"
s3 = boto3.client('s3')  # usa IAM Role da EC2

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # Lista arquivos do bucket
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    files = []
    if 'Contents' in response:
        files = [obj['Key'] for obj in response['Contents']]
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        local_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(local_path)
        # Faz upload automático para o S3
        s3.upload_file(local_path, BUCKET_NAME, file.filename)
    return redirect('/')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
