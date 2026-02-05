# Flask에서 필요한 모든 기능을 가져옴
# (render_template, request, redirect 등 포함)
from flask import * 

# Flask 앱 객체 생성
# __name__은 현재 파일이 실행되는 위치를 Flask에게 알려주는 역할
app = Flask(__name__)

# -----------------------------
# 메인 페이지 (홈 화면)
# 주소: http://127.0.0.1:5000/
# -----------------------------
@app.route("/")
def index():  # templates 폴더 안의 index.html 파일을 화면에 보여줌
    return render_template("index.html")

# -----------------------------
# 분석 페이지
# 주소: http://127.0.0.1:5000/analysis
# -----------------------------
@app.route("/analysis")
def analysis():
    # analysis.html 템플릿을 렌더링
    return render_template("analysis.html")

# -----------------------------
# 데이터 설명 페이지
# 주소: http://127.0.0.1:5000/data
# -----------------------------
@app.route("/data")
def data():
    # data.html 파일을 웹 페이지로 반환
    return render_template("data.html")

# -----------------------------
# 시각화 페이지
# 주소: http://127.0.0.1:5000/visualization
# -----------------------------
@app.route("/visualization")
def visualization():
     # visualization.html을 브라우저에 출력
    return render_template("visualization.html")

# -----------------------------
# 결론 페이지
# 주소: http://127.0.0.1:5000/conclusion
# -----------------------------
@app.route("/conclusion")
def conclusion():
     # conclusion.html 화면 표시
    return render_template("conclusion.html")

# -----------------------------
# 팀 소개 페이지
# 주소: http://127.0.0.1:5000/team
# -----------------------------
@app.route("/team")
def team():
    # team.html을 렌더링
    return render_template("team.html")

# -----------------------------
# 이 파일을 직접 실행했을 때만 서버 실행
# -----------------------------
if __name__ == "__main__":
    # debug=True
    # - 코드 수정 시 서버 자동 재시작
    # - 에러 발생 시 상세한 오류 화면 제공
    app.run(host = '127.0.0.1', port = 5000, debug=False)
    