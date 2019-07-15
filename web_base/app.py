from flask import Flask,render_template
import requests
app = Flask(__name__)


# 주문 받는 방식
@app.route("/")

#무엇을 제공할지
def home():
    return render_template('home.html')



# 서버 자동 업뎃
if __name__ == "__main__":
    app.run(debug = True)