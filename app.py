from flask import Flask, render_template, request
import re
from collections import defaultdict
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to parse log file and detect failed login attempts
def parse_log(file_path):
    failed_attempts = defaultdict(int)
    suspicious_ips = set()
    
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                failed_attempts[ip] += 1
                if failed_attempts[ip] > 5:
                    suspicious_ips.add(ip)
    
    return failed_attempts, suspicious_ips

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    suspicious = []
    
    if request.method == 'POST':
        file = request.files['logfile']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            failed_attempts, suspicious_ips = parse_log(file_path)
            
            results = [{'ip': ip, 'attempts': failed_attempts[ip]} for ip in failed_attempts]
            suspicious = list(suspicious_ips)
    
    return render_template('index.html', results=results, suspicious=suspicious)

if __name__ == '__main__':
    app.run(debug=True)
