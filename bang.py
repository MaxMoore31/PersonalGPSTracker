from gpiozero import Servo
from time import sleep
from flask import Flask, request, abort

servo = Servo(17)
servo.min()

app=Flask(__name__)

@app.route('/bang', methods=['GET'])
def webhook():
    if request.method == 'GET':
        print('*BANG*')
        servo.max()
        return 'success', 200
        sleep(2)
        exit()
    else:
        abort(400)
        servo.min()

if __name__ == '__main__':
    app.debug = False
    app.run(host = '0.0.0.0', port = 5000)

