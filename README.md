# 🐦 Social Media API (Django + DRF + JWT)

A modular social media backend inspired by Twitter, built with **Django**, **Django REST Framework**, and **JWT Authentication**.  
This project provides user accounts, posts, likes, comments, and follow/unfollow functionality through clean RESTful APIs.

---

## 🚀 Features
- 🔑 **JWT Authentication** (Register, Login, Refresh token)
- 👤 User registration & profile management
- 📝 Post creation, listing, and deletion
- ❤️ Like/Unlike posts
- 💬 Comment on posts
- ➕ Follow/Unfollow users
- 🔍 Filtering & searching (using `django-filter`)

---

## 🛠️ Tech Stack
- [Django 5](https://www.djangoproject.com/) — Web framework
- [Django REST Framework](https://www.django-rest-framework.org/) — API framework
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/) — Authentication
- [Pillow](https://pillow.readthedocs.io/) — Image processing
- [django-filter](https://django-filter.readthedocs.io/) — Filtering support

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Create a virtual environment (Conda or venv)
conda create -n socialenv python=3.11 -y
conda activate socialenv

or

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Create a superuser (admin)
python manage.py createsuperuser

6. Start the development server
python manage.py runserver

🔑 API Endpoints
Authentication
.POST /api/accounts/register/ — Register a new user
.POST /api/token/ — Get JWT access & refresh token
.POST /api/token/refresh/ — Refresh access token

Posts
.GET /api/posts/ — List all posts
.POST /api/posts/ — Create a post
.DELETE /api/posts/<id>/ — Delete a post

Likes
.POST /api/likes/post/<post_id>/like/ — Like a post
.DELETE /api/likes/post/<post_id>/unlike/ — Unlike a post
.GET /api/likes/post/<post_id>/likes/ — List post likes

Comments
.POST /api/comments/post/<post_id>/comment/ — Add comment
.GET /api/comments/post/<post_id>/comments/ — List comments
.DELETE /api/comments/comment/<comment_id>/delete/ — Delete comment

Follows
.POST /api/follows/ — Follow a user
.DELETE /api/follows/<user_id>/ — Unfollow a user
.GET /api/follows/ — List current user follows
.GET /api/follows/followers/<user_id>/ — List followers of a user
.GET /api/follows/following/<user_id>/ — List who a user is following

📌 Requirements
Django==5.0.7              
djangorestframework==3.15.1 
djangorestframework-simplejwt==5.3.1  
Pillow==10.3.0               
django-filter==24.2          
psycopg2-binary==2.9.9        
python-decouple==3.8

📬 Testing with Postman
1.Import the API endpoints in Postman.
2.Register a new user or create one via Django admin.
3.Obtain a JWT token from /api/token/.
4.Add the token in Postman under Authorization → Bearer Token.
5.Test endpoints for posts, likes, comments, and follows.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
