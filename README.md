# Polls App

A Django-based polling application that allows users to create and participate in polls. The app includes user authentication, role-based access control, and a password reset functionality using Django Allauth.

## Features
- User authentication with Django Allauth
- Role-based access control (Student, Boss, Employer)
- Create, update, and delete polls
- Vote on polls
- View poll results
- Password reset functionality

## Installation

### Prerequisites
Make sure you have the following installed:
- Python (>=3.8)
- Django (>=4.0)
- PostgreSQL (or SQLite for development)
- Virtualenv (optional but recommended)

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/amahadnejad/Polls_App.git
   cd Polls_App
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

The app should now be accessible at `http://127.0.0.1:8000/`.

## Usage
- Register or log in using Django Allauth.
- Depending on your assigned role, create or vote on polls.
- View poll results and manage polls if you have the appropriate permissions.

## Configuration
### Environment Variables
Create a `.env` file in the project root and define the following variables:
```
SECRET_KEY=your_secret_key_here
DEBUG=True  # Set to False in production
```

### Admin Panel
Access the Django admin panel at `/admin/` to manage users and polls.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your fork and submit a pull request.

## Contact
For any questions, reach out via [GitHub Issues](https://github.com/amahadnejad/Polls_App/issues).

