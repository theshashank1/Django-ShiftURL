﻿# Django-ShiftURL
## ShiftURL: A Django Short URL Application

This is a Django application for creating and managing short URLs. With ShiftURL, you can shorten long URLs and share them easily.

**Features:**

* Shorten long URLs
* Customize short URLs (optional)
* Track clicks on shortened URLs (optional - functionality not currently implemented)
* Manage shortened URLs (optional - functionality not currently implemented)

**Getting Started:**

1. **Prerequisites:**
    * Python 3.x (https://www.python.org/downloads/)
    * pip (usually comes bundled with Python)
2. **Setup Virtual Environment (recommended):**
    * Create a virtual environment: `python -m venv .venv` (activate using your OS specific command)
    * Activate the virtual environment
3. **Install Dependencies:**
    * `pip install django`
    * (Optional for additional features)
        * `pip install django-hitcount` (for tracking clicks)
4. **Clone this repository (or copy files):**
    * (If using Git) `git clone https://...` (replace with your repository URL)
5. **Start the project:**
    * Navigate to the project directory (ShiftURL)
    * Run `python manage.py migrate` to create database tables (if applicable)
    * Run `python manage.py runserver` to start the development server

**Project Structure:**

* `shortURL`: Main Django app for managing short URLs
* `templates`: Contains HTML templates for the application (if applicable)
    * `init.py`: An empty file to mark the directory as a package
* `db.sqlite3`: Database file (if using SQLite) - might be replaced with actual database configuration
* `demo.json` (potential): Demo data for testing purposes (if applicable)
* `flights.db` (unclear purpose): Might be unrelated to the application or a leftover file
* `manage.py`: Django management script
* `README.md`: This file (you're reading it!)
* `Scratches and Consoles` (potential): This directory might contain scratch work or console logs - you can clean it up if not needed

**Next Steps:**

* Explore the code within the `shortURL` app.
* Customize the application to fit your needs (adding features, modifying behavior).
* Refer to the Django documentation (https://docs.djangoproject.com/en/5.0/) for further guidance.

**Note:**

* This readme assumes the application is currently under development and some functionalities (like click tracking and URL management) might not be implemented yet based on the provided directory structure.

**Feel free to contribute!**

This is an open-source project. If you have any questions, suggestions, or want to contribute to the development, feel free to reach out!
