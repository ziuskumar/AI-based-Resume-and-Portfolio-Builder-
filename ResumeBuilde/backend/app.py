from flask import Flask, request, jsonify
from resume_generator import generate_resume

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    resume, cover_letter = generate_resume(data)

    return jsonify({
        "resume": resume,
        "cover_letter": cover_letter
    })

if __name__ == "__main__":
    app.run(debug=True)
