from flask import Flask, request, Response, send_from_directory
import urllib.request
import os

app = Flask(__name__, static_folder='static')

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,*/*",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "Referer": "https://goszakup.gov.kz/ru/search/lots",
}

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/proxy')
def proxy():
    target = request.args.get('url', '')
    if not target.startswith('https://goszakup.gov.kz'):
        return {'error': 'Only goszakup.gov.kz allowed'}, 403
    try:
        req = urllib.request.Request(target, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        resp = Response(data, content_type='text/html; charset=utf-8')
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    except Exception as e:
        return {'error': str(e)}, 502

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port)
