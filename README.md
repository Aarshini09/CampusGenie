# 🎓 CampusGenie - AI Academic Assistant

![HTML5](https://img.shields.io/badge/Frontend-HTML5-orange?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/Style-CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/Script-JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-green?style=for-the-badge&logo=flask&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Gemini%20Pro-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Droidrun](https://img.shields.io/badge/Automation-Droidrun-red?style=for-the-badge)

> **"Turning WhatsApp Chaos into Calendar Clarity."**

**CampusGenie** is a smart student productivity tool designed to solve the problem of missed deadlines hidden in hundreds of WhatsApp messages. It uses GenAI to parse informal text and Droidrun automation to sync events directly to the Android Calendar.

---

## 🏗️ How It Works (The Flow)
1.  **Input:** User pastes a messy WhatsApp message (e.g., *"Kal maths ka assignment submit karna hai aur 18 ko quiz hai"*).
2.  **Processing:** The backend sends this text to our **Fine-Tuned LLM** (Gemini) with custom prompt engineering.
3.  **Extraction:** The AI converts the text into structured JSON data (Title, Date, Time, Priority).
4.  **Action:** The app uses **Droidrun SDK** to instantly open the native Calendar app with all details pre-filled.

---

## 🌟 Key Features

### 1. 🧠 Smart Message Analysis
Unlike basic regex, our AI understands **Hinglish** and context. It extracts:
* **Summaries:** Short, actionable tasks.
* **Deadlines:** Converts "tomorrow" or "next Friday" into actual dates.
* *Powered by custom Prompt Engineering.*

### 2. 📅 One-Tap Droidrun Sync
We integrated the **Droidrun SDK** to bridge the gap between web and native Android.
* No manual typing required.
* Click "Add to Calendar" -> Event Saved.

### 3. 📚 Topic Simplifier
Stuck on a complex topic? Just type it in.
* Get explanations in simple student-friendly language.
* Includes real-world examples.

---

## 👥 Meet the Team

### 🎨 Vaibhav Singh (Frontend & UI Lead)
* **Architecture:** Designed the responsive Mobile-First UI using HTML/CSS/JS.
* **Integration:** Connected the frontend to backend REST APIs (`/analyze`, `/explain`) for real-time data fetching.
* **UX Logic:** Implemented error handling and success states for the Droidrun trigger.

### 🧠 Adarsh (AI & Prompt Architect)
* **Prompt Engineering:** Designed "System Instructions" to handle unstructured Hinglish inputs and force strict JSON outputs.
* **Logic Design:** Built the core logic for deadline extraction and context understanding.
* **Education Module:** Created the prompts for the "Topic Explainer" engine.

### ⚙️ Antra (Backend & Automation Lead)
* **Backend Core:** Developed the Flask server to handle API requests and route them to the AI model.
* **Droidrun Integration:** Implemented the critical Droidrun SDK logic to trigger native Android intents.
* **Product Demo:** Scripted and recorded the project pitch and demonstration video.

---

## 🛠️ Tech Stack & Tools

| Component | Technology |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript (ES6) |
| **Backend** | Python (Flask), Node.js |
| **AI Model** | Google Gemini Pro / OpenAI API |
| **Automation** | Droidrun SDK |
| **Version Control** | GitHub |

---

## 🔮 Future Scope
* **WhatsApp Bot:** Integrating directly into WhatsApp so users don't even need to copy-paste.
* **Voice Commands:** Adding voice-to-text for adding tasks.
* **Notifications:** Reminder alerts before the deadlines.

---

### 💻 Installation (Run Locally)

```bash
# Clone the repository
git clone [https://github.com/YourUsername/CampusGenie-backend.git](https://github.com/YourUsername/CampusGenie-backend.git)

# Navigate to directory
cd CampusGenie-backend

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
