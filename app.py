'''
from flask import Flask, render_template, request, flash
import blog

app = Flask(__name__)
app.secret_key = "dumbfoundfuckalls"

@app.route("/")
def index():
    #flash("ENTER KEYWORD")
    return render_template("index.html")

@app.route("/article",methods=["POST","GET"])
def article():
    flash("The Keyword is " + str(request.form['name_input'])+".")
    return render_template("index.html")

'''

from cmd import PROMPT
from flask import Flask, render_template, request,flash
import config
import blog



def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.secret_key = "dumbfoundfuckalls"
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = blog.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')

        if 'form2' in request.form:
            prompt = request.form['blogSection']
            blogT = blog.generateBlogSections(prompt)
            blogSectionIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = blog.blogSectionExpander(prompt)
            blogExpanded = blogT.replace('\n', '<br>')


    return render_template('index.html', **locals())


@app.route('/welcomeToMyWorld', methods=["GET", "POST"])
def index2():
    #flash("ENTER KEYWORD")
    return render_template("index2.html")

@app.route("/article",methods=["POST","GET"])
def article():
    prompt=request.form['name_input']
    blogT = blog.generateBlogTopicsPipe(prompt)
    #flash("The Keyword is " + str(request.form['name_input'])+".")
    flash(str(blogT))
    return render_template("index2.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)