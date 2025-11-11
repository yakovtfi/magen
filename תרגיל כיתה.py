import time
q = 100000
start = time.time()
for _ in range(q):pass
print("O(n):", round(time.time() - start, 5), "seconds")
start = time.time()
for _ in range(q):
 for _ in range(q):pass
print("O(n²):", round(time.time() - start, 5), "seconds")
from models.book import Book
from models.user import User
from typing import List, Optional
        return f"{user.name} returned '{book.title}'."
        
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library Management System</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>📚 Library Management</h1>

        <section>
            <h2>Available Books</h2>
            {% if books %}
                <ul>
                    {% for book in books %}
                        <li>
                            <strong>{{ book.title }}</strong> by {{ book.author }} ({{ book.isbn }})
                        </li>
                    {% endfor %}
                </ul>
            {% else %}
                <p>No books available.</p>
            {% endif %}
        </section>

        <section>
            <h2>Add New Book</h2>
            <form method="POST" action="/add_book">
                <input type="text" name="title" placeholder="Title" required>
                <input type="text" name="author" placeholder="Author" required>
                <input type="text" name="isbn" placeholder="ISBN" required>
                <button type="submit">Add Book</button>
            </form>
        </section>

        <section>
            <h2>Add New User</h2>
            <form method="POST" action="/add_user">
                <input type="text" name="name" placeholder="Name" required>
                <input type="text" name="id" placeholder="User ID" required>
                <button type="submit">Add User</button>
            </form>
        </section>

        <section>
            <h2>Borrow / Return Book</h2>
            <form method="POST" action="/borrow">
                <input type="text" name="user_id" placeholder="User ID" required>
                <input type="text" name="isbn" placeholder="Book ISBN" required>
                <button type="submit">Borrow</button>
            </form>

            <form method="POST" action="/return">
                <input type="text" name="user_id" placeholder="User ID" required>
                <input type="text" name="isbn" placeholder="Book ISBN" required>
                <button type="submit" class="return-btn">Return</button>
            </form>
        </section>
    </div>
</body>
</html>
        