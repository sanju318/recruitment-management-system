# recruitment-management-system

A Django-based backend system that streamlines the recruitment process — from job posting and candidate management to interview scheduling and status tracking. Built with Django and Django REST Framework (DRF), this system is designed to handle real-world recruitment workflows efficiently.


 ====> **Features**

 User Authentication – Signup/login system with OTP verification.

 Role Management – Admin, recruiter, and candidate roles with access control.

 Job Posting – Create and manage job listings.

 Resume Uploads – Candidates can submit resumes via the system.

 Interview Scheduling – Schedule and track interview dates with status updates.

 Admin Panel – Manage all data via Django’s built-in admin dashboard.

 API Tested with Postman – All endpoints are tested using Postman collections.




====> **Tools & Technologies**

| Category            | Tools & Frameworks                     |
| ------------------- | -------------------------------------- |
| **Backend**         | Django, Django REST Framework (DRF)    |
| **Database**        | SQLite (development), MySQL (optional) |
| **API Testing**     | Postman                                |
| **Authentication**  | OTP + Password-based                   |
| **Version Control** | Git                                    |



====> **Authentication System**

OTP generation for secure signups

timezone.now() used to track OTP expiry

Passwords are hashed using make_password() for security


====> **API Endpoints**

All endpoints are tested using Postman.
Some key routes:

POST /signup/ – User registration with OTP

POST /login/ – Authenticated user login

POST /job/ – Create a new job post

GET /candidate/ – List all candidates

POST /interview/ – Schedule interview for candidate



====> **How to Run the Project ?**


git clone https://github.com/yourusername/recruitment-management-system.git

cd recruitment-management-system/RMS

python -m venv venv

 Windows use : venv\Scripts\activate , IOS : source venv/bin/activate  

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

====> **Admin**

python manage.py createsuperuser

====> **Testing**

All APIs tested using Postman.

File uploads and OTP login fully verified.




