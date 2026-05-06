# Django Portfolio Website - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Start the Development Server
Run the following command in the terminal:
```bash
source venv/bin/activate
python manage.py runserver
```

Then visit: **http://localhost:8000/**

### Step 2: Access the Admin Panel
Visit: **http://localhost:8000/admin/**

Login with:
- **Username:** admin
- **Password:** password123

### Step 3: Add Your Content
In the Admin Panel:
1. **Add Projects** - Click "Projects" → "Add Project"
2. **Add Skills** - Click "Skills" → "Add Skill"
3. **View Contacts** - Click "Contacts" to see messages

---

## 📝 Default Admin Credentials
- **Username:** admin
- **Email:** admin@example.com
- **Password:** password123

⚠️ **IMPORTANT:** Change this password immediately in production!

---

## 🎯 Main Website Pages

| Page | URL | What It Shows |
|------|-----|---------------|
| Home | `/` | Featured projects & top skills |
| About | `/about/` | Your professional background |
| Projects | `/projects/` | All your projects with pagination |
| Project Detail | `/projects/<id>/` | Single project details |
| Skills | `/skills/` | All skills organized by category |
| Resume | `/resume/` | Your professional resume |
| Contact | `/contact/` | Contact form for visitors |

---

## 🔧 Common Admin Tasks

### Add a New Project
1. Go to Admin → Projects
2. Click "Add Project"
3. Fill in:
   - **Title:** Project name
   - **Description:** What the project is about
   - **Image:** Optional project screenshot
   - **Technologies:** Comma-separated (e.g., "Django, React, PostgreSQL")
   - **Project URL:** Link to live project (optional)
   - **GitHub URL:** Link to repository (optional)
   - **Featured:** Check this to show on homepage
4. Click "Save"

### Add a Skill
1. Go to Admin → Skills
2. Click "Add Skill"
3. Fill in:
   - **Name:** Skill name
   - **Proficiency:** Select level
   - **Category:** Programming Language / Framework / Tool / Other
   - **Order:** Display order (lower numbers appear first)
4. Click "Save"

### Manage Contact Submissions
1. Go to Admin → Contacts
2. View all messages submitted through the contact form
3. Click on a message to view full details
4. Mark as "read" when you've responded

---

## 📂 File Structure

Important files you might want to edit:

```
portfolio/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── manage.py                    # Django management
│
├── portfolio/settings.py        # Configuration
├── portfolio/urls.py            # Main URL routes
│
├── core/
│   ├── models.py               # Database models
│   ├── views.py                # Page logic
│   ├── admin.py                # Admin configuration
│   └── templates/core/         # Page templates
│       ├── home.html
│       ├── about.html
│       ├── projects.html
│       ├── project_detail.html
│       ├── skills.html
│       ├── resume.html
│       └── contact.html
│
└── templates/base.html          # Base template (header/footer)
```

---

## 🎨 Customization Tips

### Change Colors
Edit the color variables in `templates/base.html`:
```css
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
}
```

### Update Contact Information
Edit `templates/core/contact.html`:
- Change email address
- Update phone number
- Modify location

### Customize About Page
Edit `templates/core/about.html`:
- Update your background
- Change journey/milestones
- Modify achievements

### Customize Resume
Edit `templates/core/resume.html`:
- Add your work experience
- Update education
- List your certifications

---

## 🛠️ Available Management Commands

```bash
# Create database tables
python manage.py migrate

# Create new superuser
python manage.py createsuperuser

# Make database changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Collect static files (for production)
python manage.py collectstatic

# Check for issues
python manage.py check

# Create empty database tables
python manage.py migrate --fake-initial

# Shell for testing
python manage.py shell
```

---

## 🐛 Troubleshooting

### Server won't start
- Check if port 8000 is available
- Activate virtual environment: `source venv/bin/activate`
- Run migrations: `python manage.py migrate`

### Can't log into admin
- Try password: `password123`
- Create new superuser: `python manage.py createsuperuser`

### Images not showing
- Ensure images are in `media/` directory
- Check file permissions
- Try uploading a test image via admin

### Static files missing
- Run: `python manage.py collectstatic`
- Check `settings.py` STATIC_URL configuration

---

## 📚 Learn More

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.0/)
- [Django Admin](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)

---

## ✅ Next Steps

1. ✓ Start the server
2. ✓ Log into admin panel
3. ✓ Add your first project
4. ✓ Add your skills
5. ✓ Update About page
6. ✓ Customize colors/styling
7. ✓ Deploy to production (when ready)

Happy building! 🎉
