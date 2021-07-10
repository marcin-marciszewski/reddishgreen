from flask import Flask, request, jsonify
import os

# Init app
app = Flask(__name__)

@app.route('/get_stats', methods=['GET'])
def get():
  return jsonify({'msg':'hello'})

# Run Server
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5012, debug=True)