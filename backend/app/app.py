from flask import Flask, render_template

app = Flask(__name__)

@app.route('/admin/login')
def admin_login():
    return render_template('frontend/admin/login.html')  # This renders login.html from the /templates/admin folder

if __name__ == '__main__':
    app.run(debug=True)