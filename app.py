from flask import Flask, request, jsonify
from trading_logic import execute_trade

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if not data or 'action' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    result = execute_trade(data['action'], data.get('symbol', 'XAUUSD'))
    return jsonify({"status": "success", "details": result})

if __name__ == '__main__':
    app.run(debug=True)
