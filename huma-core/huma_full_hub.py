from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template_string('''
        <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Humanledger Sovereign Hub</title>
                <style>
                    body { background: #0a0a0a; color: #00ff00; font-family: monospace; padding: 20px; }
                    .card { border: 1px solid #00ff00; padding: 15px; margin-bottom: 10px; border-radius: 8px; }
                    .header { text-align: center; color: gold; font-size: 20px; margin-bottom: 20px; }
                    .btn { display: block; width: 100%; padding: 10px; background: #004400; color: white; border: none; margin-top: 5px; text-decoration: none; text-align: center; }
                    .tax-bar { color: gray; font-size: 10px; text-align: right; }
                </style>
            </head>
            <body>
                <div class="header">TUNAPAC HUMANLEDGER HUB</div>
                
                <div class="card">
                    <strong>HUMALOTO: Saturday National</strong>
                    <div class="tax-bar">Next Draw: 18:00 | Rule: 1-90</div>
                    <button class="btn">Enter Stakes (15% Agent Comm)</button>
                </div>

                <div class="card">
                    <strong>HUMATUBE & AUDIO</strong>
                    <div class="tax-bar">HRC-Sub Active | HRC-Ad Enabled</div>
                    <button class="btn">Launch Media Stream</button>
                </div>

                <div class="card">
                    <strong>SOVEREIGN DNS & COMMS</strong>
                    <div class="tax-bar">huma:// DNS functional</div>
                    <button class="btn">Register .huma Name</button>
                </div>

                <div class="card">
                    <strong>MERCHANT & GRANT HUB</strong>
                    <div class="tax-bar">$H 10M Pool | Status: Production</div>
                    <button class="btn">Dev Dashboard</button>
                </div>
            </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
