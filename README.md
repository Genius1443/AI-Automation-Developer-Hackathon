
### AI & Automation Developer Hackathon Submission

---

## 📌 Overview

The **Prospect Research Agent** is an end-to-end AI + automation system that takes company website URLs, extracts relevant business information, and generates structured insights.

The system is designed to be **robust, scalable, and reliable**, handling real-world challenges such as missing data, dynamic websites, and API failures.

---

## 🎯 Key Features

* 🔗 Accepts company website URLs as input
* 🧠 Smart multi-page web scraping (About, Contact, Services)
* 🧹 HTML cleaning & token optimization
* 📧 Accurate email & phone extraction using regex (no hallucination)
* 🤖 AI-ready architecture with fallback (works even without API)
* 📊 Structured JSON output (strict schema compliance)
* 🌐 Live web application with API + UI
* ⚡ Handles edge cases and invalid URLs gracefully

---

## 🏗️ System Architecture

```
Input URL
   ↓
Smart Link Discovery
   ↓
Multi-Page Scraping
   ↓
Data Cleaning & Processing
   ↓
AI / Rule-Based Inference
   ↓
Validation Layer
   ↓
Structured JSON Output
   ↓
Web API + UI Display
```

---

## 🧪 Subtask 1 — Research Pipeline (Colab)

### 🔹 Function

```python
enrich_company(url: str) -> dict
```

### 🔹 Input

```json
[
  "https://example.com",
  "https://company.com"
]
```

### 🔹 Output (Strict JSON Schema)

```json
{
  "website_name": "",
  "company_name": "",
  "address": "",
  "mobile_number": "",
  "mail": [],
  "core_service": "",
  "target_customer": "",
  "probable_pain_point": "",
  "outreach_opener": ""
}
```

### ✅ Highlights

* Smart link filtering (avoids full-site scraping)
* Token-efficient processing
* Regex-based contact extraction (no AI hallucination)
* Guaranteed schema stability

---

## 🌐 Subtask 2 — Web Application

### 🔹 Backend (FastAPI)

| Endpoint   | Method | Description                      |
| ---------- | ------ | -------------------------------- |
| `/enrich`  | POST   | Enrich a company URL             |
| `/results` | GET    | Retrieve all processed companies |

---

### 🔹 Frontend (Streamlit)

#### 1. Enrich Section

* Input field for company URL
* "Enrich" button
* Displays structured output

#### 2. Results Section

* "Show All Results" button
* Displays dataset in table format

---

## ⚙️ Tech Stack

| Category      | Tools                   |
| ------------- | ----------------------- |
| Language      | Python                  |
| Scraping      | requests, BeautifulSoup |
| Parsing       | regex, tldextract       |
| Backend       | FastAPI                 |
| Frontend      | Streamlit               |
| Server        | Uvicorn                 |
| AI (Optional) | OpenAI API              |
| Deployment    | Render / Railway        |

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd prospect-research-agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### 🔹 Start Backend

```bash
uvicorn backend:app --reload
```

### 🔹 Start Frontend

```bash
streamlit run app.py
```

---

## 🌍 Deployment

* Backend deployed on: **Render / Railway**
* Frontend deployed on: **Streamlit Cloud / Render**

> No authentication required — publicly accessible.

---

## 🛡️ Reliability & Edge Case Handling

* Handles invalid URLs without crashing
* Returns default values for missing fields
* Avoids AI hallucination via regex-first extraction
* Works even if AI API fails (fallback logic)
* Limits scraping to relevant pages only

---

## 🧠 Design Decisions

* **Smart Scraping over brute force** → Efficient & scalable
* **Rule-based fallback system** → Ensures reliability under API failure
* **Strict schema enforcement** → Prevents JSON breakage
* **Lightweight stack** → Fast development and deployment

---

## 🧪 Testing Strategy

Tested across:

* Large enterprise websites
* Startup websites
* JS-heavy platforms
* Invalid/broken URLs

---

## 📊 Evaluation Readiness

✔ Works on unseen URLs
✔ Stable JSON output
✔ Clean UI rendering
✔ API endpoints functional
✔ Colab notebook fully executable

---

## 🚀 Future Enhancements

* JS rendering support (Playwright/Selenium)
* Advanced AI-based summarization
* Resume-to-company matching
* Data visualization dashboard

---

## 👨‍💻 Author

**Pavan Kalyan Sanampudi**
AI & Automation Developer Hackathon Participant

---

## 🏁 Final Note

This project emphasizes **real-world problem solving**, focusing on building a **reliable, end-to-end system** rather than isolated features.

> Designed to perform consistently under real constraints — just like production systems.

---
