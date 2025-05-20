# web_app

🌟 Euphoria: A Productivity & Wellness Tracker Web App
Euphoria is a simple yet elegant web application built with Flask that helps users monitor their daily activities, manage tasks, take notes, and visualize their productivity—all in one place. It offers user registration, login, progress tracking with charts, a dynamic to-do list, and note-taking features, emphasizing both utility and aesthetic simplicity.

✨ Features
🔐 User Authentication: Register and securely log in to your account.

📊 Daily Progress Tracker:

Input time spent on activities like sleep, work, meals, chores, reading, and more.

Visualize your productivity breakdown via interactive Pie Charts using Chart.js.

✅ To-Do List:

Add tasks with unique IDs.

Mark them as done or delete.

Persistent through localStorage.

📝 Notes Section:

Write and save quick notes.

Persisted in localStorage.

📱 Responsive UI designed with basic CSS and styled forms.

🛠️ Technologies Used
Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Templating Engine: Jinja2

Charts: Chart.js

Data Persistence: LocalStorage (Tasks & Notes), Server (Progress data)

Forms: HTML Forms with POST requests

🧭 How to Use Euphoria
Navigate to the Homepage
You'll see two options: Log In or Register.

Create an Account
Use the Register button to sign up with a username and password.

Log In
Enter your credentials and click Log In to access the dashboard.

Track Your Day

Input hours for different activities.

Submit to visualize data in a Pie Chart.

Manage Your Tasks

Click + add task to create new tasks.

Mark them as Done! or Delete as needed.

Take Notes

Click Create in the Notes section to type quick notes.

Notes persist between sessions via localStorage.

Logout

Use the Log Out button to safely exit your session.

📌 Notes
User progress data is submitted to the backend.

Tasks and Notes are stored in the browser’s localStorage—visible only to the user on their current device.

