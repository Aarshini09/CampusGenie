# 🎓 CampusGenie

CampusGenie is a productivity tool built to help students manage academic chaos. It takes unstructured WhatsApp messages (like assignment updates), extracts the deadlines using AI, and adds them directly to your Android calendar.

---

## 👥 Team & Contributions

### 🎨 Vaibhav Singh (Frontend & UI)
* **UI Development:** Designed and built the screens for Home, Message Analysis, and Deadline Cards.
* **API Integration:** Connected the frontend button clicks to the backend APIs (`/analyze`, `/explain`) so the app actually works.
* **Error Handling:** Wrote the logic to show success/error messages (e.g., when a calendar event is added successfully).

### 🧠 Adarsh Mishra (Prompt Engineering & Logic)
* **Prompt Design:** Wrote the specific system prompts to make the AI understand casual Hinglish messages (e.g., "Kal submit karna hai").
* **Data Extraction:** Configured the LLM to return data in strict JSON format so the code can read dates and titles accurately.
* **Study Helper:** Created the logic for the "Topic Explanation" feature to break down complex concepts into simple bullet points.

### ⚙️ Antra Priyadarshini (Backend & Automation)
* **Server Setup:** Built the backend server (Flask/Node) to handle requests from the frontend.
* **Droidrun SDK:** Handled the Droidrun integration to trigger the native Android calendar intent (this opens the actual calendar app with details pre-filled).
* **LLM Connection:** Wrote the backend scripts to send user data to the AI API and fetch the response.
* **Pitch & Demo:** Recorded the demo video, explained the workflow, and handled the project presentation.

---

## 🚀 What it does
1.  **Smart Parsing:** You paste a message, and it finds the hidden deadlines.
2.  **One-Tap Calendar:** Uses Droidrun to add events to your phone's calendar instantly.
3.  **Topic Explainer:** Explains confusing study topics simply with examples.

---

## 🛠️ Tech Stack
* **Frontend:** HTML/CSS/JS
* **Backend:** Python (Flask) / Node.js
* **AI:** Gemini/OpenAI API
* **Tools:** Droidrun SDK
