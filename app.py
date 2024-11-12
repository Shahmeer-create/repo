from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Simple message to be displayed on the browser
    message = "Hello, welcome to my simple app  by shahmeer !"
    
    # Check if the app is running in the correct directory
    if os.path.exists('/home/ubuntu/myapp'):
        message += "<br>The application is running in the correct directory good: /home/ubuntu/myapp"
    else:
        message += "<br>Warning: The application directory does not exist!"
    
    return message

if __name__ == '__main__':
    # Run the app on port 5000, available publicly
    app.run(host='0.0.0.0', port=5000)
