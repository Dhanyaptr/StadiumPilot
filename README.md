# 🏟️ StadiumPilot AI

An AI-powered smart stadium assistant designed for the FIFA World Cup 2026. StadiumPilot AI helps visitors navigate the stadium, locate facilities, understand stadium rules, and receive accessibility assistance through a natural conversational interface.

---

## 📌 Challenge Vertical

**Smart Stadium Assistant**

This solution focuses on improving the match-day experience by providing an intelligent assistant that guides visitors inside the stadium using natural language conversations.

---

## ✨ Features

### 🧭 Smart Navigation
- Multi-turn conversations
- Parking-to-section navigation
- Remembers user context
- Provides entrance, gate, and walking time

Example:
```
User: I'm at Parking Lot 50A
Bot: Which section are you trying to reach?
User: 110
Bot: Head to Entrance P11 through North Gate. Walking time is approximately 5 minutes.
```

---

### 🍔 Food Court Assistance

Provides information about:

- Food court location
- Nearby section
- Available menu
- Opening hours

---

### 🚻 Restroom Assistance

Provides:

- Nearest restroom
- Restroom ID
- Nearby section

---

### 🏥 Medical Assistance

Provides:

- Medical center location
- Emergency assistance point

---

### 🛍 Merchandise Store

Provides information about:

- Official merchandise store
- Jerseys
- Scarves
- Souvenirs
- Gifts

---

### 📖 Stadium Rules

Supports questions like:

- Can I bring outside food?
- Are cameras allowed?
- Can I carry a backpack?
- Is smoking allowed?
- Can I re-enter the stadium?
- Are pets allowed?

---

### ♿ Accessibility Assistance

Supports:

- Wheelchair seating
- Accessible restrooms
- Elevators
- Hearing assistance

---

### 🤖 Intelligent Conversation

The chatbot automatically detects user intent and responds appropriately.

Supported intents include:

- Navigation
- Food
- Restrooms
- Medical
- Merchandise
- Stadium Rules
- Accessibility
- Unknown questions

---

## 🛠 Tech Stack

### Frontend

- React
- Vite
- CSS

### Backend

- FastAPI
- Python

### AI

- Groq API
- Llama 3.3 70B Versatile

### Data Storage

JSON datasets

---

## 📂 Project Structure

```
backend/
frontend/
dataset/
models/
services/
tests/
README.md
requirements.txt
```

---

## ⚙️ How It Works

1. User sends a message.
2. ChatService detects the user's intent.
3. Depending on the intent:
   - Navigation
   - Facility
   - Rule
   - Accessibility
4. Relevant information is retrieved from JSON datasets.
5. PromptBuilder creates a structured prompt.
6. Gemini generates a natural language response.
7. Response is displayed in the chat interface.

---

## 🧠 System Architecture

```
User
   │
   ▼
React Frontend
   │
   ▼
FastAPI Backend
   │
   ▼
ChatService
   │
   ├── Navigation Service
   ├── Facility Service
   ├── Rules Service
   └── Accessibility Service
            │
            ▼
       Prompt Builder
            │
            ▼
      Gemini AI
```

---

## 📊 Datasets

The project uses JSON datasets containing:

- Stadium
- Parking
- Entrances
- Sections
- Routes
- Facilities
- Rules
- Accessibility

---

## 🚀 Running the Project

### Backend

```bash
pip install -r requirements.txt

uvicorn backend.app:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📝 Assumptions

- Stadium information is stored locally in JSON files.
- Navigation is based on predefined routes.
- Users provide valid parking IDs and section numbers.
- Internet connectivity is available for AI responses.

---

## 🔮 Future Improvements

- Live crowd density
- Indoor maps
- QR code seat navigation
- Voice assistant
- Multi-language support
- Real-time parking availability
- Live match updates
- Emergency alerts

---

## 👩‍💻 Author

**Dhanya**

Developed as part of an AI-powered Smart Stadium Assistant challenge.