# 🌐 Groupify – Smart Interest-Based Group Chat App

**Groupify** is a smart, real-time, interest-based group communication platform designed to connect users with like-minded people through dynamically recommended chat groups. Powered by Django and WebSockets, Groupify is your gateway to intelligent, evolving communities.

> 🔗 [Read the full dev blog here](https://abdullahwebs.github.io/groupifyblog/)

---

## 🚀 Features

- 🔥 **Smart Group Recommendations**  
  Dynamically suggests groups based on user interests, behavior, and trending topics.

- 📈 **Hot/Trending Groups**  
  Detects rapidly growing communities using growth rate analysis (not just total members).

- 🧠 **Picked For You**  
  Recommends groups based on behavior of similar users — not just random matching.

- 🔔 **Interest-Based Notifications**  
  Get notified instantly when something pops in your preferred topics.

- 📱 **Responsive & Clean UI**  
  Built with Bootstrap 5 and custom styling to ensure a smooth, modern experience.

- 💬 **Real-Time Messaging**  
  Powered by Django Channels & WebSockets for blazing-fast communication.

- 🔐 **JWT Authentication**  
  Secure login/signup flow using JSON Web Tokens.

---

## 🛠️ Built With

### Backend:
- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Django Channels** (WebSocket support)
- **JWT Authentication**
- **SQLite** (default dev DB)

### Frontend:
- **HTML5**
- **CSS3**
- **JavaScript (Vanilla)**
- **Bootstrap 5**

---

## 📸 Screenshots

> Check out visuals and deep dive into logic on the blog:  
🔗 [Groupify Blog](https://abdullahwebs.github.io/groupifyblog/)

---

## 📦 Installation (Local)

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/groupify.git
cd groupify
```

### 2. Create a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

---

## 🧠 How It Works (Quick Overview)

- **Recommendations**: Analyzes interests and active user behavior.
- **Trending Detection**: Calculates group growth rate weekly.
- **JWT Tokens**: Handles user sessions securely.
- **WebSocket Channels**: Powers real-time messaging.
- **Points & Profiles**: Every user has a dynamic, interest-based identity.

---

## 👨‍💻 Author

**Abdullah Hussain**  
📬 [Linkedin](https://www.linkedin.com/in/abdullah-hussain-194796357/)  
🐙 [GitHub](https://github.com/abdullahwebs)

---

## 📄 License

MIT License

---


