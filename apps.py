from flask import Flask, render_template,request
app = Flask(__name__)

import crwaling

@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/result' ,methods=['POST'])
def result():

    keyword = request.form['keyword']

    list_kor,list_eng,list_post = crwaling.kor(keyword)






    return render_template("result.html", len = len(list_kor) ,
                                          kor = list_kor ,
                                          eng = list_eng ,
                                          post = list_post )



if __name__ == '__main__':
    app.run()

