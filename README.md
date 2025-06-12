


# 🩺 HealthHacked: AI-Powered Symptom Checker & Triage Assistant

**HealthHacked** is a smart healthcare assistant that allows users to:
- Describe their symptoms in natural language
- Receive likely medical conditions with confidence scores
- Get urgency recommendations (e.g., rest at home, visit a GP, or go to the ER)
- Track symptoms over time and receive pattern-based follow-ups

Built for the **Hack4Health 2025 Hackathon** under the Advanced Division.

---

## 🔍 Problem Statement

Healthcare access is often delayed due to uncertainty and lack of awareness. People Google their symptoms, panic unnecessarily, or worse—ignore warning signs. **HealthHacked** bridges this gap by offering:
- AI-powered, interpretable suggestions
- Personalized triage decisions
- Symptom tracking and historical pattern recognition

---

## 💡 Key Features

### 🧠 AI Symptom Analysis
- NLP-based symptom extraction
- TF-IDF + Logistic Regression classifier
- Predicts possible conditions with confidence scores

### 🚨 Triage Recommendation
- Rule-based decision engine to recommend next steps:
  - Try rest & hydration
  - Book GP appointment
  - Seek ER immediately

### 📊 Symptom Tracker & Pattern Detector
- Logs symptom data per user
- Detects patterns like:
  - Recurrent headaches
  - Seasonal triggers
  - Worsening trends over time

---

## 🏗️ Architecture

```text
User Input → NLP Processing → Symptom Classifier →
Triage Engine → Recommendation + Storage →
Pattern Detection → Follow-up Advice
````

### 🧱 Tech Stack

| Layer         | Tech                                 |
| ------------- | ------------------------------------ |
| Backend       | FastAPI, scikit-learn, spaCy         |
| Frontend      | Handled by teammates (HTML/CSS + JS) |
| Database      | SQLite (MVP-friendly)                |
| Model Storage | Pickle (.pkl) for trained ML         |
| Hosting       | Render / Railway (free tiers)        |

---

## 📁 Folder Structure

```bash
HealthHacked/
├── app/
│   ├── main.py                # FastAPI app
│   ├── models/                # ML + triage logic
│   ├── services/              # NLP, recommendations
│   ├── api/                   # API routes
│   └── data/                  # Datasets
├── database/                  # SQLite DB
├── run.py                     # Entry point
├── requirements.txt
└── .gitignore
```

---

## 🧪 API Demo

### Endpoint: `POST /api/analyze-symptoms`

**Sample Input:**

```json
{
  "symptoms": "I have chest tightness and shortness of breath",
  "severity": 7,
  "duration": "2 days",
  "user_id": "demo_user"
}
```

**Sample Output:**

```json
{
  "predicted_conditions": [
    {"condition": "Angina", "confidence": 0.62},
    {"condition": "Heart Attack", "confidence": 0.25}
  ],
  "urgency": "Seek emergency care immediately",
  "next_steps": "Call emergency services or go to the nearest ER."
}
```

---

## ⏳ Timeline Breakdown (20-Day MVP)

| Week | Milestone                                               |
| ---- | ------------------------------------------------------- |
| 1    | FastAPI setup, dataset preprocessing, baseline ML model |
| 2    | API endpoints, triage logic, database integration       |
| 3    | Pattern detection, UI integration, deployment           |

---

## 👨‍💻 Contributors

* **AI & Backend** – [Hammad Malik](https://github.com/hammadmalik17)
* **Frontend** – KLN Sai Aditya & Ayushmaan Manish Kumar 

---

## 🚀 Try It Yourself

```bash
git clone https://github.com/your-username/HealthHacked.git
cd HealthHacked
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Visit: `http://127.0.0.1:8000/docs` to test the interactive API.

---

## ✅ Future Scope

* Migrate to advanced transformers (DistilBERT)
* Add real-time vitals via wearable API
* Multi-language symptom support
* Secure authentication + user dashboard

---

## 🏁 License

This project is built for educational and prototype purposes under the MIT License.

---

**Let’s hack health, one symptom at a time.** 💻💉


