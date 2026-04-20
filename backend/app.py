from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'users.db')

# Initialize database
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS quiz_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT UNIQUE,
            budget TEXT,
            language TEXT,
            speciality TEXT,
            timeline TEXT,
            recommended_countries TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Expert-level recommendation engine
def calculate_recommendations(responses):
    scores = {"France": 0, "Allemagne": 0, "Belgique": 0, "Italie": 0, "Canada": 0}
    
    # Budget (weight: 3)
    budget = responses.get("budget", "")
    if budget == "tight":
        scores["France"] += 3
        scores["Allemagne"] += 4
        scores["Belgique"] += 2
        scores["Italie"] += 3
    elif budget == "medium":
        scores["France"] += 2
        scores["Belgique"] += 3
        scores["Canada"] += 1
    elif budget == "high":
        scores["Canada"] += 4
    
    # Language (weight: 3)
    language = responses.get("language", "")
    if language == "french":
        scores["France"] += 4
        scores["Belgique"] += 4
        scores["Canada"] += 1
    elif language == "english":
        scores["Canada"] += 4
        scores["Allemagne"] += 2
    elif language == "italian":
        scores["Italie"] += 4
    elif language == "mix":
        scores["Canada"] += 3
        scores["Belgique"] += 2
        scores["Allemagne"] += 1
    
    # Field of study (weight: 4 - MOST IMPORTANT)
    field = responses.get("field", "")
    field_map = {
        "tech_engineering": {"Allemagne": 5, "Canada": 4, "France": 2},
        "computer_science": {"Allemagne": 5, "Canada": 5, "France": 2},
        "art_design": {"Italie": 5, "France": 3, "Belgique": 2},
        "law": {"France": 4, "Belgique": 3, "Canada": 2},
        "medicine": {"France": 4, "Allemagne": 3, "Canada": 2},
        "business": {"France": 3, "Belgique": 3, "Canada": 4},
        "sciences": {"Allemagne": 4, "France": 3, "Italie": 2},
        "agriculture": {"Allemagne": 3, "France": 2, "Canada": 3},
        "humanities": {"France": 4, "Belgique": 3, "Italie": 2},
        "tourism": {"Italie": 4, "France": 3, "Belgique": 2},
    }
    if field in field_map:
        for country, bonus in field_map[field].items():
            scores[country] += bonus
    
    # Timeline (weight: 2)
    timeline = responses.get("timeline", "")
    if timeline == "short":
        scores["France"] += 2
        scores["Belgique"] += 2
    elif timeline == "long":
        scores["Canada"] += 3
        scores["Allemagne"] += 2
    
    # Post-graduation work (weight: 3)
    post_work = responses.get("post_work", "")
    if post_work == "stay":
        scores["Canada"] += 4
        scores["Allemagne"] += 3
        scores["France"] += 2
    elif post_work == "maybe":
        scores["France"] += 2
        scores["Belgique"] += 2
        scores["Canada"] += 2
    
    # Climate preference (weight: 1)
    climate = responses.get("climate", "")
    if climate == "warm":
        scores["Italie"] += 2
        scores["France"] += 1
    elif climate == "cold":
        scores["Canada"] += 2
        scores["Allemagne"] += 1
    
    # City size (weight: 1)
    city = responses.get("city", "")
    if city == "big":
        scores["Canada"] += 1
        scores["France"] += 1
    elif city == "cozy":
        scores["Italie"] += 1
    
    # Credential recognition (weight: 2)
    recognition = responses.get("recognition", "")
    if recognition == "global":
        scores["Canada"] += 2
        scores["Allemagne"] += 2
    elif recognition == "europe":
        scores["France"] += 2
        scores["Allemagne"] += 2
        scores["Belgique"] += 2
    
    # Academic level (weight: 2)
    academic = responses.get("academic_level", "")
    if academic == "excellent":
        scores["Canada"] += 3
        scores["Allemagne"] += 3
        scores["France"] += 1
    elif academic == "good":
        scores["Canada"] += 2
        scores["Allemagne"] += 2
        scores["France"] += 1
        scores["Belgique"] += 1
    elif academic == "average":
        scores["France"] += 2
        scores["Belgique"] += 2
        scores["Italie"] += 1
    elif academic == "acceptable":
        scores["France"] += 1
        scores["Belgique"] += 1
        scores["Italie"] += 1
    
    # Sort by score
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [{"country": c[0], "score": c[1]} for c in ranked]

# Routes

@app.route('/api/quiz/submit', methods=['POST'])
def submit_quiz():
    try:
        data = request.json
        user_id = data.get('user_id', f'user_{datetime.now().timestamp()}')
        
        recommendations = calculate_recommendations(data)
        recommended_str = json.dumps([r['country'] for r in recommendations[:3]])
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT OR REPLACE INTO quiz_responses 
            (user_id, budget, language, speciality, timeline, recommended_countries)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            data.get('budget'),
            data.get('language'),
            data.get('speciality'),
            data.get('timeline'),
            recommended_str
        ))
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'user_id': user_id,
            'recommendations': recommendations,
            'message': f"Top match: {recommendations[0]['country']}"
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/quiz/results/<user_id>', methods=['GET'])
def get_results(user_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('SELECT * FROM quiz_responses WHERE user_id = ?', (user_id,))
        row = c.fetchone()
        conn.close()
        
        if not row:
            return jsonify({'success': False, 'error': 'User not found'}), 404
        
        return jsonify({
            'success': True,
            'user_id': row[1],
            'budget': row[2],
            'language': row[3],
            'speciality': row[4],
            'timeline': row[5],
            'recommended_countries': json.loads(row[6])
        }), 200
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'message': 'Modzi Info API running'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
