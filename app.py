from flask import * 
import os

app = Flask(__name__) # app 객체 생성이 가장 먼저 와야 합니다.

# -----------------------------
# [추가] os 폴더 내의 그래프 파일을 직접 보여주는 라우트
# -----------------------------
@app.route('/graphs/<path:filename>')
def serve_graphs(filename):
    # 'os' 폴더의 경로를 지정 (현재 실행 경로 기준)
    graph_path = os.path.join(os.getcwd(), 'os')
    return send_from_directory(graph_path, filename)

# -----------------------------
# 메인 페이지 (홈 화면)
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

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
    app.run(host = '127.0.0.1', port = 5000, debug=True) # 개발 중엔 debug=True가 편합니다.