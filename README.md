Gas Utility Service Request System

A Django-based web application that allows customers to submit service requests for gas utilities, track their request status, and view account information. It also provides customer support representatives with tools to manage service requests efficiently.

🚀 Features

🔹 For Customers:

Submit a service request online.

Select the type of service request (e.g., gas leakage, meter issue, new connection, etc.).

Provide details and attach files for better assistance.

Track the status of submitted requests.

🔹 For Customer Support Representatives:

View all submitted requests.

Update the request status (Pending, In Progress, Resolved).

Manage customer support operations efficiently via Django Admin Panel.

🛠️ Installation & Setup

1️⃣ Clone the Repository

https://github.com/yourusername/mahir.git
cd mahir

2️⃣ Set Up Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

5️⃣ Create a Superuser (Admin Access)

python manage.py createsuperuser
# Enter Username, Email, and Password

6️⃣ Run the Django Server

python manage.py runserver

7️⃣ Access the Application

Customer Portal: http://127.0.0.1:8000/

Submit Request: http://127.0.0.1:8000/requests/new/

Track Requests: http://127.0.0.1:8000/requests/

Admin Panel: http://127.0.0.1:8000/admin/


![Screenshot 2025-03-27 213948](https://github.com/user-attachments/assets/0bb20c6f-9629-4168-9cd8-b17d37500f83)


![Screenshot 2025-03-27 214144](https://github.com/user-attachments/assets/12b33c39-34b0-4455-a4a8-45fc61a55b32)


![Screenshot 2025-03-27 214220](https://github.com/user-attachments/assets/0aac4632-f55b-4c12-bee4-4b7a7a371cce)


![Screenshot 2025-03-27 214647](https://github.com/user-attachments/assets/bf2b1021-b296-46e6-8b51-96a6d497d184)






