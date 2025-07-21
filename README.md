# 💼 Recruitment Management System (RMS)

A scalable and secure **Django + Django REST Framework**-based backend system designed to streamline and automate the recruitment lifecycle — from **job postings** and **resume collection** to **interview scheduling** and **candidate tracking**.

## 📌 Business Overview

The Recruitment Management System (RMS) provides companies and hiring teams with an efficient way to manage the recruitment pipeline through role-based access and automated processes. Key stakeholders include:

- **Admins**: Full control over users, roles, and recruitment data.
- **Recruiters**: Can create job posts, review candidates, and schedule interviews.
- **Candidates**: Can sign up, upload resumes, and track application progress.

## ✨ Key Features

| Category                 | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| 🔐 **User Authentication** | OTP-based signup and secure password login system                           |
| 👥 **Role Management**      | Supports Admin, Recruiter, and Candidate roles with RBAC                    |
| 📄 **Job Posting**         | Recruiters can create, update, and delete job listings                      |
| 📎 **Resume Uploads**      | Candidates can upload and manage their resumes                             |
| 📅 **Interview Scheduling**| Interviews can be scheduled and tracked by recruiters                       |
| 🧭 **Status Tracking**     | Admins and recruiters can monitor candidate progress                        |
| 📊 **Admin Panel**         | Centralized data control via Django Admin dashboard                         |
| 🔍 **Postman Tested APIs** | All APIs validated through real-world testing using Postman                 |

## 🛠️ Tech Stack

| Layer               | Tools & Technologies                         |
|---------------------|-----------------------------------------------|
| **Backend**         | Django, Django REST Framework (DRF)           |
| **Authentication**  | OTP System, Hashed Passwords                  |
| **Database**        | SQLite (for dev), MySQL (for production use)  |
| **API Testing**     | Postman                                       |
| **Version Control** | Git                                           |
| **Environment**     | Python 3.8+                                   |

## 🔒 Authentication System

- **OTP-Based Signup**: Generated OTP stored in DB with expiry using `timezone.now()`
- **Password Security**: Passwords hashed using Django’s `make_password()`
- **Token Authentication (optional)**: Can integrate DRF’s token or JWT for sessionless auth

## 🚀 API Endpoints (Sample)

| Method | Endpoint           | Description                            |
|--------|--------------------|----------------------------------------|
| POST   | `/signup/`         | Register user with OTP verification    |
| POST   | `/login/`          | Login with username and password       |
| POST   | `/job/`            | Create a new job post                  |
| GET    | `/candidate/`      | List all registered candidates         |
| POST   | `/interview/`      | Schedule an interview for a candidate  |

## 🧩 Project Structure

```bash
recruitment-management-system/
├── RMS/                        # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── main_app/                   # Core app for roles, jobs, interviews
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── media/                      # Resume and file uploads
├── static/                     # Static files (if used)
├── requirements.txt            # Python dependencies
└── manage.py
```



## 🛠️ Project Setup Guide

**1. Clone the Repository**
```bash
git clone https://github.com/yourusername/recruitment-management-system.git
cd recruitment-management-system/RMS
```

**2. Create Virtual Environment**
```bash
python -m venv venv
```

**3. Activate Virtual Environment**
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

**4. Install Dependencies**
```bash
pip install -r ../requirements.txt
```

**5. Database Setup**
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Run the Server**
```bash
python manage.py runserver
```


## 🔑 Create Admin User
```bash
python manage.py createsuperuser
```
Visit `http://127.0.0.1:8000/admin/` to log in with admin credentials.


## 🧭 Future Enhancements

- Frontend integration (React/Angular)
- Notification system (email/SMS for interview updates)
- Candidate shortlisting & offer letter automation

## 🤝 Contributing

Contributions are welcome! Please fork the repository and open a pull request with your updates.  

## 📄 License

MIT License – feel free to use, modify, and distribute with attribution.




