from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.template_global()
def format_number(number):
    return '{:,.0f}'.format(number)


@app.route('/')
def index():
    url = "https://vipact.api.mgtv.com/api/v1/act/vote/charlist?" \
          "ticket=ECCD14A505A832A193A51AF986EFA46A&" \
          "act_name=20230414cf2023&count=50&" \
          "invoker=mobile-zhifubao&" \
          "_dx_seq_id=237d2264-5e02-f487-2da8-624c02231881&v=v4"

    response = requests.get(url)
    data = json.loads(response.text)
    contestants = data['data']['character_list']

    return render_template('index.html', contestants=contestants, rank=0)


if __name__ == '__main__':
    app.run()
