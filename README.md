# Django Portfolio Website

A professional portfolio website built with Django, featuring a clean and modern design with Bootstrap 5.

## Features

✨ **Complete Portfolio Website** with the following pages:
- **Home Page** - Showcase featured projects and top skills
- **About Page** - Professional background and experience
- **Projects Page** - Paginated list of all projects with filtering
- **Project Detail Pages** - Detailed view of individual projects
- **Skills Page** - Organized skills with proficiency levels
- **Resume Page** - Professional resume with download option
- **Contact Page** - Contact form for inquiries

🔐 **Built-in Features:**
- Django admin panel for content management
- User authentication system
- Contact form with database storage
- Responsive design with Bootstrap 5
- Image support for projects
- Project categorization by technologies
- Skill proficiency levels and categorization

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── portfolio/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       └── core/
│           ├── home.html
│           ├── about.html
│           ├── projects.html
│           ├── project_detail.html
│           ├── skills.html
│           ├── resume.html
│           └── contact.html
├── templates/
│   └── base.html
├── static/
│   └── (CSS, JS, images)
├── media/
│   └── projects/
└── venv/
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

1. **Activate Virtual Environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

4. **Create Superuser (Admin Account):**
   ```bash
   python manage.py createsuperuser
   ```
   - Username: admin
   - Email: admin@example.com
   - Password: (set your own)

5. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   - Website: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/

## Database Models

### Project
- **title** - Project name
- **description** - Detailed project description
- **image** - Project image
- **technologies** - Comma-separated list of technologies
- **project_url** - Link to live project
- **github_url** - Link to GitHub repository
- **featured** - Mark as featured project
- **created_at** - Creation date
- **updated_at** - Last update date

### Skill
- **name** - Skill name
- **proficiency** - Level (Beginner, Intermediate, Advanced, Expert)
- **category** - Skill category (Language, Framework, Tool, Other)
- **order** - Display order

### Contact
- **name** - Sender's name
- **email** - Sender's email
- **subject** - Message subject
- **message** - Message content
- **read** - Whether message has been read
- **created_at** - Submission date

## Using the Admin Panel

1. Navigate to http://localhost:8000/admin/
2. Log in with your superuser credentials
3. Manage:
   - **Projects** - Add, edit, delete projects
   - **Skills** - Manage your skills and proficiency levels
   - **Contacts** - View and manage contact form submissions

## Customization

### Add Your Information
1. Update contact information in the **Contact** template
2. Add your projects via the admin panel
3. Add your skills and proficiency levels
4. Update the **About** and **Resume** pages with your information

### Styling
- Modify CSS in `base.html`
- Use Bootstrap 5 classes for responsive design
- Add custom styles in the `<style>` tags

### Add Project Images
1. Place images in the `media/projects/` directory
2. Upload via admin panel as you create projects
3. Images will automatically be displayed on project pages

## Common Tasks

### Create a New Project
1. Go to Admin Panel → Projects → Add Project
2. Fill in all fields (image is optional)
3. Technologies should be comma-separated (e.g., "Django, React, PostgreSQL")
4. Check "Featured" to show on homepage

### Add Skills
1. Go to Admin Panel → Skills → Add Skill
2. Set proficiency level and category
3. Use order field to arrange skill display

### View Contact Submissions
1. Go to Admin Panel → Contacts
2. Click on a message to view full details
3. Check "read" to mark as read

## Technologies Used

- **Backend:** Django 4.2
- **Frontend:** Bootstrap 5
- **Database:** SQLite (development)
- **Image Processing:** Pillow
- **Styling:** Bootstrap 5 CSS

## Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Collect static files: `python manage.py collectstatic`
4. Use a production-grade database (PostgreSQL recommended)
5. Use a production server (Gunicorn, uWSGI)
6. Set up proper environment variables for SECRET_KEY

## Security Notes

⚠️ **Important for Development Only:**
- The SECRET_KEY is visible in settings.py (change in production)
- DEBUG is set to True (change to False in production)
- Use environment variables for sensitive data in production

## Troubleshooting

### Port Already in Use
If port 8000 is already in use, run:
```bash
python manage.py runserver 8001
```

### Database Reset
If you need to reset the database:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Missing Static Files
Run:
```bash
python manage.py collectstatic
```

## Future Enhancements

- [ ] Blog section for articles
- [ ] Dark mode toggle
- [ ] Search functionality
- [ ] Social media integration
- [ ] Email notifications for contact forms
- [ ] Project filtering by technology
- [ ] User profile system

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please contact through the contact form on the website.

---

**Happy coding!** 🚀
