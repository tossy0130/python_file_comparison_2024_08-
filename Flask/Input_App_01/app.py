from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input')

        # 判定ロジック
        if user_input:
            message = f'入力された値：{user_input}'
        else:
            message = '入力がありません。'

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
