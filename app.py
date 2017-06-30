from flask import Flask
from datetime import datetime

from fizzbuzz import fizzbuzz

app = Flask(__name__)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        pre {
            background: #CCCCCC
        }
        </style>
        <title>FizzBuzz</title>
    </head>
    <body>
        <h1>FizzBuzz</h1>
        <p>It is currently {time}.</p>

        <pre>
{result}
        </pre>
    </body>
    </html>
    """.format(time=the_time,
               # result="\n".join([fizzbuzz(i) for i in range(1, 101)]),
               result="\n".join(list(map(fizzbuzz, range(1, 101))))
               )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
