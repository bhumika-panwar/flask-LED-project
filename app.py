from flask import Flask, render_template,Response,request
import serial
import time
ser = serial.Serial('COM3' , 9600)
ser.timeout= 1 
app = Flask(__name__)
def turnOn(device):
    print('Turn on-',device)
    ser.write(bytes(device,'UTF-8'))
def off():
    ser.write(str('off').encode())
def disconnect():
    ser.close()
@app.route("/", methods=['GET','POST'])
def index():
    dict=request.form.to_dict()
    if request.method=='POST':
        if 'red' in dict: turnOn('R')
        elif 'green' in dict: turnOn('G')
        elif 'yellow' in dict: turnOn('Y')
        elif 'light' in dict: turnOn('T')
        elif 'off' in dict: turnOn('L')
        elif 'dis' in dict: disconnect()
    return render_template('index.html')
if  __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)



