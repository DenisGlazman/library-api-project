from flask import Flask, request, jsonify

app = Flask(__name__)

books = []
users = []

@app.route("/")
def home():
    return jsonify({"message": "Library API is running"}), 200

# ---------- BOOKS ----------

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books), 200

@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.json
    if not new_book.get("title") or not new_book.get("author"):
        return jsonify({"error": "Missing title or author"}), 400

    if any(b["id"] == new_book["id"] for b in books):
        return jsonify({"error": "Book already exists"}), 400

    new_book["is_borrowed"] = False
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    updated = request.json
    for book in books:
        if book["id"] == book_id:
            book.update(updated)
            return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    if any(b["id"] == book_id for b in books):
        books = [b for b in books if b["id"] != book_id]
        return jsonify({"message": "Book deleted"}), 200
    return jsonify({"error": "Book not found"}), 404

# ---------- USERS ----------

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users", methods=["POST"])
def add_user():
    new_user = request.json
    if not new_user.get("name"):
        return jsonify({"error": "Missing name"}), 400
    new_user["id"] = new_user.get("id", len(users) + 1)
    new_user["borrowed_books"] = []
    if any(u["id"] == new_user["id"] for u in users):
        return jsonify({"error": "User already exists"}), 400
    users.append(new_user)
    return jsonify(new_user), 201

# ---------- LOAN ----------

@app.route("/loan", methods=["POST"])
def loan_book():
    data = request.json
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    user = next((u for u in users if u["id"] == user_id), None)
    book = next((b for b in books if b["id"] == book_id), None)

    if not user or not book:
        return jsonify({"error": "User or book not found"}), 404
    if book["is_borrowed"]:
        return jsonify({"error": "Book already borrowed"}), 400

    book["is_borrowed"] = True
    user["borrowed_books"].append(book_id)
    return jsonify({"message": "Book loaned"}), 200

# ---------- RETURN ----------

@app.route("/return", methods=["POST"])
def return_book():
    data = request.json
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    user = next((u for u in users if u["id"] == user_id), None)
    book = next((b for b in books if b["id"] == book_id), None)

    if not user or not book:
        return jsonify({"error": "User or book not found"}), 404
    if book_id not in user["borrowed_books"]:
        return jsonify({"error": "Book not borrowed by user"}), 400

    book["is_borrowed"] = False
    user["borrowed_books"].remove(book_id)
    return jsonify({"message": "Book returned"}), 200

if __name__ == "__main__":
    app.run(debug=True)
