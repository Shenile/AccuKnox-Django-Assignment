
# AccuKnox-Django-Assignment

## Overview

This project demonstrates the handling of Django signals using `post_save`. It includes examples of synchronous execution, same-thread execution, and transactional behavior.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shenile/AccuKnox-Django-Assignment.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd signals_assesment
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Run the server:**
   ```bash
   python manage.py runserver
   ```

## Running Tests

To run tests, use:
```bash
python manage.py test
```
