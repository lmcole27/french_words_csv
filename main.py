from flask import Flask, render_template
import pandas as pd
import random as r

words = pd.read_csv("1000frenchwords.csv")
word_id = 999
word_list = [999]
back = 2

app = Flask(__name__)

@app.route('/')
def welcome():
    word_id = 999
    return render_template("french.html", words=words, word_id=word_id, back=back, word_list=word_list)

@app.route('/reset/')
def reset():
    word_id = 999
    word_list = [999]
    back = 2
    print(word_list)
    return render_template("french.html", words=words, word_id=word_id, back=back, word_list=word_list)

@app.route('/previous/<int:back>')
def previous(back):
    print(word_list)
    if len(word_list) < back:
        word_id = 999
        return render_template("french.html", words=words, word_id=word_id, back=back, word_list=word_list)
    else:
        word_id = word_list[-back]
        back += 1

    
    #print(words["French"][word_id])
    return render_template("french.html", words=words, word_id=word_id, back=back, word_list=word_list)

@app.route('/french/')
def new_word():
    word_id = r.randint(0,998)
    word_list.append(word_id)
    print(word_list)
    return render_template("french.html", words=words, word_id=word_id, back=2, word_list=word_list)

@app.route('/french/<int:word_id>')
def french(word_id):
    new_word = word_id
    return render_template("french.html", words=words, word_id=new_word, back=back, word_list=word_list)

@app.route('/english/<int:word_id>')
def english(word_id):
    new_word = word_id
    return render_template("english.html", words=words, word_id=new_word, back=back, word_list=word_list)




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)