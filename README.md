# LeadFlow CRM

LeadFlow CRM is a Lead Management System built with Django and Django REST Framework. It enables organizations to manage leads efficiently with role-based access, activity tracking, notes, and REST APIs.

---

## Features

### Authentication
- Secure Login & Logout
- Django Authentication System

### Role-Based Access
- Admin Dashboard
- Member Dashboard
- Admin can manage all leads
- Members can access only assigned leads

### Lead Management
- Create Lead
- View Lead
- Update Lead
- Delete Lead
- Assign Lead to Team Member
- Lead Status Management

### Lead Collaboration
- Add Notes
- Activity Timeline
- Track Lead Updates

### Dashboard
- Total Leads
- New Leads
- Won Leads
- Lost Leads
- Lead Analytics Chart

### Search & Filters
- Search by Name
- Filter by Status
- Pagination

### REST API
- List Leads
- Create Lead
- Update Lead
- Delete Lead

### Responsive UI
- Bootstrap 5
- Mobile Friendly
- Professional CRM Dashboard

---

## Tech Stack

- Python 3
- Django
- Django REST Framework
- Bootstrap 5
- SQLite
- HTML5
- CSS3
- JavaScript

---

## Project Structure

```
LeadFlow/
│
├── accounts/
├── activity/
├── api/
├── dashboard/
├── leads/
├── static/
├── templates/
├── LeadFlow/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/yourusername/LeadFlow.git

cd LeadFlow

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/leads/ | Get all leads |
| POST | /api/leads/ | Create lead |
| GET | /api/leads/<id>/ | Get single lead |
| PUT | /api/leads/<id>/ | Update lead |
| DELETE | /api/leads/<id>/ | Delete lead |

---

## User Roles

### Admin

- Manage all leads
- Assign leads
- Update/Delete leads
- View dashboard
- Access API

### Member

- View assigned leads
- Add notes
- View activity history

---

## Running Tests

```bash
python manage.py test
```

---

## AI Usage

ChatGPT was used to assist with project planning, UI improvements, Django REST Framework implementation, debugging, and documentation. All architectural decisions, feature implementation, testing, and final project customization were completed and verified during development.

---

## Future Improvements

- Email Notifications
- CSV Import/Export
- Dashboard Analytics
- File Attachments
- Lead Reminders

---

## Author

Aditya Raj

Built for the Digital Heroes Full Stack Developer Assessment.