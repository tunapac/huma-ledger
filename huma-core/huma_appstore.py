from flask import Flask, render_template_string, make_response

app = Flask(__name__)

# Your new Identity Portal HTML with the Verification Console
HUB_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background:#000; color:#fff; font-family:sans-serif; text-align:center; padding:20px; }
        .mint-section { background:#111; border:2px solid #222; border-radius:20px; padding:30px; box-shadow:0 10px 30px rgba(0,0,0,0.5); }
        .mint-title { color:gold; letter-spacing:3px; font-weight:bold; margin-bottom:20px; }
        input { background:#000; border:1px solid #444; color:#0f0; padding:15px; width:80%; border-radius:10px; margin-bottom:20px; text-align:center; }
        button { background:gold; color:#000; border:none; padding:15px 30px; border-radius:10px; font-weight:bold; width:80%; cursor:pointer; }
        #statusConsole { display:none; margin-top:20px; text-align:left; font-family:monospace; font-size:11px; color:#0f0; background:#050505; padding:15px; border:1px solid #003300; border-radius:10px; }
    </style>
</head>
<body>
    <div class="mint-section">
        <div class="mint-title">TUNAPAC IDENTITY PORTAL</div>
        <input type="text" id="bioHash" placeholder="ENTER BIOMETRIC HASH">
        <button id="mintBtn" onclick="startVerification()">MINT $HUMA IDENTITY</button>
        
        <div id="statusConsole">
            > INITIALIZING POH PROTOCOL...<br>
            > SCANNING LAGOS NODE #001...<br>
            <div id="loadLine"></div>
        </div>
    </div>

    <script>
    function startVerification() {
        const btn = document.getElementById('mintBtn');
        const console = document.getElementById('statusConsole');
        const hash = document.getElementById('bioHash').value;
        if(!hash) { alert("Enter Hash"); return; }

        btn.disabled = true;
        btn.innerHTML = "VERIFYING...";
        console.style.display = "block";

        let lines = [
            "> CONNECTING TO PI BLOCKCHAIN...",
            "> AUTHENTICATING GENESIS ARTIFACT...",
            "> ACCESS GRANTED: ARCHITECT 001",
            "> SYNCHRONIZING WITH HUMANLEDGER..."
        ];

        let i = 0;
        let interval = setInterval(() => {
            if(i < lines.length) {
                document.getElementById('loadLine').innerHTML += lines[i] + "<br>";
                i++;
            } else {
                clearInterval(interval);
                btn.style.background = "#4cd964";
                btn.innerHTML = "IDENTITY MINTED";
            }
        }, 1200);
    }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    response = make_response(render_template_string(HUB_HTML))
    # This line tells the browser: "DO NOT SAVE THIS PAGE, ALWAYS FETCH NEW CODE"
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
