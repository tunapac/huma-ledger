from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <html>
            <head>
                <title>HumaTube - Sovereign Media</title>
                <style>
                    body { background: #121212; color: white; font-family: sans-serif; text-align: center; }
                    .header { padding: 20px; background: #880000; font-size: 24px; font-weight: bold; }
                    .search { margin: 20px; padding: 10px; width: 80%; border-radius: 5px; }
                    .btn { background: gold; color: black; padding: 15px; border: none; border-radius: 5px; font-weight: bold; }
                </style>
            </head>
            <body>
                <div class="header">HUMATUBE SOVEREIGN</div>
                <input type="text" class="search" placeholder="huma:// Search Machine...">
                <div style="margin-top: 50px;">
                    <button class="btn">Launch Saturday National Draw</button>
                </div>
                <p style="color: gray; margin-top: 100px;">Connected to 8G Mesh | huma://dns functional</p>
            </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
