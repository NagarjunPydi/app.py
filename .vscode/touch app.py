from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')

    top_output = subprocess.check_output("top -b -n 1 | head -10", shell=True).decode('utf-8')

    return f"""
    <html>
        <head>
            <title>HTOP Endpoint</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; }}
                pre {{ background-color: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; }}
            </style>
        </head>
        <body>
            <h1>HTOP Endpoint</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time:</strong> {server_time}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
