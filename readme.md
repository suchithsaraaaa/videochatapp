# 🎥 Awesome Video Chat App

Welcome to the **Awesome Video Chat App**!  
A modern, beautifully designed, full-featured video conferencing platform for all your professional and personal needs.

---

![Hero Banner](static/img/video_conference.svg)

## 🚀 Features

- **🧑‍💻 User Authentication**
  - Secure sign up, login, and logout
  - Beautiful animated UI for all auth screens

- **📹 Video Conferencing**
  - Easy “New Meeting” creation
  - Join with Room ID
  - Real-time video & audio using [ZegoCloud UIKit](https://www.zegocloud.com/)
  - Up to 50 users per room

- **✨ Modern Aesthetics**
  - Animated glassmorphic cards for all actions
  - Responsive design with dark mode
  - SVG graphics & avatars for a friendly, professional feel

- **🔒 Safe & Secure**
  - CSRF protection
  - Password confirmation for sign up

- **🌙 Dark Mode**
  - One-click toggle, smooth transitions

---

## 📸 Demo

![App Demo](static/img/demo_screenshot.png)

---

## 🏗️ Project Structure

```
videochatapp/
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       ├── video_conference.svg
│       └── avatar_placeholder.png
├── videoconference_app/
│   ├── templates/
│   │   ├── index.html
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── joinroom.html
│   └── ...
├── manage.py
└── README.md
```

---

## 🖼️ Screenshots

<div align="center">
  <img src="static/img/demo_dashboard.png" alt="Dashboard" width="400"/>
  <img src="static/img/demo_join.png" alt="Join Room" width="400"/>
  <img src="static/img/demo_darkmode.png" alt="Dark Mode" width="400"/>
</div>

---

## 🛠️ Tech Stack

- **Backend:** Python (Django)
- **Frontend:** HTML5, CSS3 (Poppins font, glassmorphism, animated cards)
- **Video Engine:** [ZegoCloud UIKit](https://www.zegocloud.com/)
- **Icons:** Font Awesome
- **UI Graphics:** SVG, PNG illustrations

---

## 💻 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/suchithsaraaaa/videochatapp.git
cd videochatapp
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Collect static files

```bash
python manage.py collectstatic
```

### 4. Run the server

```bash
python manage.py runserver
```

---

## 📝 Customization

- **Branding:** Replace SVG/PNG files in `static/img/` with your own.
- **ZegoCloud Keys:** Update `videocall.html` with your own `appID` and `serverSecret`.

---

## 🤝 Contributing

Contributions are welcome!  
Open an issue or submit a pull request for new features, bugfixes, or design tweaks.

---

## 📄 License

MIT License

---

<div align="center">
  <img src="static/img/video_conference.svg" alt="Video Conference" width="120"/><br>
  <b>Built with ❤️ by suchithsaraaaa</b>
</div>
