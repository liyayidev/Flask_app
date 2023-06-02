from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'title': 'Halloween',
        'Author': 'J liyayi',
        'date': '20th may, 2002',
        'content': 'I was born in the month of may 2002'
    },
    {
        'title': 'juro',
        'Author': 'J liyayi 2',
        'date': '20th may, 2002',
        'content': 'I was born in the month'
    },
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts = posts)
    


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port= 7878)