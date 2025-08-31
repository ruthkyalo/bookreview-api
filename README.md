
#  Book Review REST API
A REST API for managing **books, reviews, and user authentication** built with **Python, Django, and Django REST Framework (DRF)**.  

The platform allows users to:  
- Sign up and authenticate with JWT.  
- Browse, search, and filter books.  
- Create reviews and rate books.  
- Like other users’ reviews.  
- Enforce permissions so users can only update/delete their own content.  



## Features

1. **Authentication**
   - JWT signup/login/profile
   - Update profile
   - Only authenticated users can access protected endpoints
   
2. **Books CRUD**
   - Create, Read, Update, Delete books
   - Search and order by title, author, rating, or date

3. **Reviews & Ratings**
   - Add reviews with ratings (1–5)
   - Like other users’ reviews
   - Owners can update/delete their reviews only

4. **Permissions**
   - Custom `IsOwnerOrReadOnly` permission
   - Public read-only; authenticated users can create
   - Only owners can edit/delete their own books/reviews

5. **Pagination & Filters**
   - Global pagination (5 items per page)
   - Search, filter, and ordering support for books and reviews

---

##  Technology

- **Python 3.12**
- **Django 5.x**
- **Django REST Framework**
- **Simple JWT** (for authentication)
- **PostgreSQL** / SQLite (dev)
- **django-filter** (for filters)
- **PythonAnywhere** (deployment)

---

##  Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<username>/bookreview-api.git
cd bookreview-api
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # used this on pythoneverywhere
venv\Scripts\activate      # on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file in the root folder:

```env
SECRET_KEY=my-secrete-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```
### 5. Make Migrations
Generate migration files for your models:
```bash
python manage.py makemigrations

```
### 6. Run Migrations
Apply migrations to set up the database:
```bash
python manage.py migrate
```

### 7. Start the Server
Run the local development server:
```bash
python manage.py runserver
```

---

##  Deployment (PythonAnywhere)

1. Upload code to `/home/<username>/bookreview-api/`
2. Create virtualenv with Python 3.12
3. Install requirements inside venv
4. Update `WSGI` file to load `.env`
5. Add your domain to `ALLOWED_HOSTS` in `settings.py`
6. Reload web app from PythonAnywhere dashboard

---

##  API Testing (using Postman)

###  Authentication

#### Register

```http
POST /api/auth/register/
```

Body:

```json
{
  "username": "johnm",
  "email": "john@example.com",
  "password": "StrongPassword123"
}
```

Response:

```json
{
  "id": 1,
  "username": "johnm",
  "email": "john@example.com"
}
```

#### Login (JWT)

```http
POST /api/auth/login/
```

Body:

```json
{
  "username": "johnm",
  "password": "StrongPassword123"
}
```

Response:

```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

#### Profile (GET/PUT)

```http
GET /api/auth/profile/
Authorization: Bearer <access_token>
```

---

### Books CRUD

* **`GET /api/books/`** → List all books

* **`POST /api/books/`** → Add a book (auth required)  
  Example request body:
  ```json
  {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "description": "A fantasy novel.",
    "rating": 5
  }


* **`GET /api/books/{id}/`** → Get details of one book

* **`PUT /api/books/{id}/`** → Update book (owner only)
  Example request body:

  ```json
  {
    "title": "Harry Potter and the Chamber of Secrets",
    "author": "J.K. Rowling",
    "description": "Second book in the Harry Potter series.",
    "rating": 4
  }
 
  ```

* **`DELETE /api/books/{id}/`** → Delete book (owner only)

Search & Ordering examples:

```
GET
/api/books/?search=Harry
/api/books/?ordering=-rating (sort the results by rating in descending order.)
```

---

###  Reviews

* `GET /api/reviews/` → List reviews
* `POST /api/reviews/` → Add review (auth required)
* `PUT/DELETE /api/reviews/{id}/` → Update/delete own review

---

##  Permissions & Validation Testing

### 1. Owner Permissions

* User A creates a book
* User B tries to update/delete →  `403 Forbidden`
* User A can update/delete →  Success

```http
PUT /api/books/1/
Authorization: Bearer <user_b_token>
```

Response:

```json
{"detail": "You do not have permission to perform this action."}
```

### 2. Review Validation

Valid review :

```json
{
  "book": 1,
  "rating": 5,
  "comment": "Great book!"
}
```

Invalid review :

```json
{
  "book": 1,
  "rating": 10,
  "comment": "Invalid rating"
}
```

Response:

```json
{
  "rating": ["Ensure this value is less than or equal to 5."]
}
```

---

##  Pagination & Filters

### Pagination

```http
GET /api/books/?page=1
```

Response:

```json
{
  "count": 12,
  "next": "http://127.0.0.1:8000/api/books/?page=2",
  "previous": null,
  "results": [...]
}
```

### Filtering

```http
GET /api/books/?rating=5
```

### Search

```http
GET /api/books/?search=Rowling
```

### Ordering

```http
GET /api/books/?ordering=-rating
```

---

##  Summary

This project demonstrates:

* DRF with JWT Authentication
* Permissions & Validation
* CRUD for Books & Reviews
* Pagination, Filtering, and Ordering
* Deployed live on PythonAnywhere

---

