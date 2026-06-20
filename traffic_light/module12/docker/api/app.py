import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_CONFIG = {
    'host':     os.getenv('DB_HOST',  'postgres'),
    'port':     int(os.getenv('DB_PORT',  5432)),
    'dbname':   os.getenv('DB_NAME',  'traffic_light'),
    'user':     os.getenv('DB_USER',  'postgres'),
    'password': os.getenv('DB_PASS'),
}


def get_conn():
    return psycopg2.connect(**DB_CONFIG)


@app.after_request
def cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})


@app.route('/history', methods=['GET'])
def history():
    limit = min(request.args.get('limit', 100, type=int), 500)
    try:
        conn = get_conn()
        try:
            with conn.cursor() as cur:
                # Fetch the latest `limit` records, return them in ascending order
                cur.execute(
                    'SELECT created_on, state FROM ('
                    '  SELECT created_on, state FROM traffic_state_history'
                    '  ORDER BY created_on DESC LIMIT %s'
                    ') t ORDER BY created_on ASC',
                    (limit,)
                )
                rows = cur.fetchall()
        finally:
            conn.close()
        return jsonify([{'timestamp': r[0].isoformat(), 'state': r[1]} for r in rows])
    except Exception as e:
        return jsonify({'error': str(e)}), 503


@app.route('/stats', methods=['GET'])
def stats():
    try:
        conn = get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    'SELECT state, COUNT(*) FROM traffic_state_history GROUP BY state ORDER BY state'
                )
                rows = cur.fetchall()
        finally:
            conn.close()
        return jsonify([{'state': r[0], 'count': r[1]} for r in rows])
    except Exception as e:
        return jsonify({'error': str(e)}), 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
