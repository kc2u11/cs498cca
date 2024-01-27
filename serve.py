from flask import Flask, request
import subprocess
import socket 

app = Flask(__name__)
seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():
    return str(socket.gethostname())

@app.route('/', methods=['POST'])
def run_stress_program():
    
    print('Processing python file')
    # Create a separate process
    http_server_process = subprocess.Popen(['python', 'stress_cpu.py'])
    print('Done triggering  python file')

    return str('Completed POST')

if __name__ == '__main__':
    app.run(debug=True)
