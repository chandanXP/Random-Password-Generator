from flask import Flask,  render_template, url_for
import random
import string

app = Flask(__name__)


def gen():
    pass_range = ''
    for i in range(10):
        if i == 5:
            pass_range = pass_range + '@'
        elif i < 5:
            pass_range = pass_range + random.choice(string.ascii_letters)
        elif i > 5:
            pass_range = pass_range + str(random.randint(0, 9))

    pass_range = pass_range.capitalize()
    print(pass_range)
    return pass_range


@app.route('/', )
def index():
    # pass_word = gen()

    # print(pass_word)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)


