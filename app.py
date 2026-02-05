from flask import *
import os

app = Flask(__name__)

# -----------------------------
# 그래프 파일 서빙 (유지)
# -----------------------------
@app.route('/graphs/<path:filename>')
def serve_graphs(filename):
    graph_path = os.path.join(os.getcwd(), 'os')
    return send_from_directory(graph_path, filename)

# -----------------------------
# 1️⃣ 홈 화면 (첫 페이지)
# -----------------------------
@app.route("/")
def home():
    return render_template("home.html")

# -----------------------------
# 2️⃣ 분석 페이지들 (base.html 사용)
# -----------------------------
@app.route("/overview")
def overview():
    return render_template("index.html")  # 개요 페이지

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/visualization")
def visualization():
    return render_template("visualization.html")

@app.route("/conclusion")
def conclusion():
    return render_template("conclusion.html")

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)