from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def showProjects():
    return render_template('projects.html')

@app.route('/resume')
def showResume():
    return render_template('my-resume.html')

if __name__ == "__main__":
    app.run(debug=True)