from flask import Flask, request
from flask_cors import CORS
import pyautogui, argparse
parser = argparse.ArgumentParser(description='A server that closes a browser tab when it receives a certain URL.')
parser.add_argument('--TRIGGERURL', type=str, default='youtube.com/shorts',
                    help='Trigger URL')
args = parser.parse_args()
CORS(app := Flask(__name__))
@app.route('/report', methods=['POST'])
def report_url():
    data = request.get_json()
    print(f'Received URL: {data['url']}')
    if args.TRIGGERURL in data['url']: pyautogui.hotkey('alt', 'f4')
    return '', 204
if __name__ == '__main__':
    print(f'Running with --TRIGGERURL={args.TRIGGERURL}')
    app.run(port=5000)