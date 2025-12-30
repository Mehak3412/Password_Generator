from flask import Flask, request, jsonify
from generator import password_generator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

generator = password_generator()

# ✅ HOME ROUTE (serves frontend)
@app.route("/")
def home():
    return app.send_static_file("index.html")

# ✅ API ROUTE (handles password generation)
@app.route("/generate", methods=["POST"])
def generate_password():
    data = request.json

    length = data.get("length", 12)
    count = data.get("count", 1)
    use_uppercase = data.get("use_uppercase", True)
    use_digits = data.get("use_digits", True)
    use_symbols = data.get("use_symbols", True)
    exclude_similar = data.get("exclude_similar", False)

    if count == 1:
        password = generator.generate(
            length=length,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_symbols=use_symbols,
            exclude_similar=exclude_similar
        )
        return jsonify({"passwords": [password]})

    passwords = generator.generate_multiple(
        count=count,
        length=length,
        use_uppercase=use_uppercase,
        use_digits=use_digits,
        use_symbols=use_symbols,
        exclude_similar=exclude_similar
    )

    return jsonify({"passwords": passwords})

if __name__ == "__main__":
    app.run(debug=True)
