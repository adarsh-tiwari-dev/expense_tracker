# 💰 Expense Tracker (Django + DRF)

A full-stack Expense Tracker web application built using **Django** and **Django REST Framework** to manage daily expenses efficiently.

---

## 🚀 Features

* 🔐 User Authentication (Login/Register)
* ➕ Add, Edit, Delete Expenses
* 📊 Track daily/monthly expenses
* 🏷️ Categorize expenses (Food, Travel, Bills, etc.)
* 📈 REST API support using DRF
* 🗄️ SQLite database (can be upgraded to PostgreSQL)

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Frontend:** HTML, CSS (can be extended to React)
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
expense_tracker/
│── manage.py
│── expense_tracker/      # Main project folder
│── app_name/             # Django app
│── db.sqlite3
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/adarsh-tiwari-dev/expense_tracker.git
cd expense_tracker
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate virtual environment

```
# Windows
venv\Scripts\activate

# Git Bash / Linux / Mac
source venv/Scripts/activate
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Run migrations

```
python manage.py migrate
```

### 6️⃣ Run server

```
python manage.py runserver
```

---

## 🌐 API Endpoints (Sample)

* `GET /api/expenses/` → Get all expenses
* `POST /api/expenses/` → Add expense
* `PUT /api/expenses/<id>/` → Update expense
* `DELETE /api/expenses/<id>/` → Delete expense

---

## 📸 Future Improvements

* 📱 Add frontend using React
* ☁️ Deploy on AWS / Render
* 📊 Advanced analytics dashboard
* 🔔 Notifications & alerts

---

## 👨‍💻 Author

**Adarsh Tiwari**

* 🎓 Computer Science Engineer (2025)
* 💼 Aspiring Data Scientist
* 🔗 GitHub: https://github.com/adarsh-tiwari-dev

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
