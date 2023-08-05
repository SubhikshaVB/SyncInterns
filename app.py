from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample users dictionary for login and signup demonstration (you should use a proper database in a real application)
users = {}

@app.route('/', methods=['GET', 'POST'])
def login_signup():
    if request.method == 'POST':
        if 'signup' in request.form:
            # Handle the signup form submission
            username = request.form['username']
            password = request.form['password']

            # Check if the username is already taken
            if username in users:
                return render_template('index.html', error='Username already taken. Please choose a different username.')

            # Create a new user account in the 'users' dictionary
            users[username] = password

            # Redirect to the dashboard page after successful signup
            return redirect(url_for('dashboard'))

        elif 'login' in request.form:
            # Handle the login form submission
            username = request.form['username']
            password = request.form['password']

            # Check if the provided credentials match any user in the 'users' dictionary
            if username in users and users[username] == password:
                # Redirect to the dashboard page upon successful login
                return redirect(url_for('dashboard'))

            # Redirect back to the login/signup page with an error message
            return render_template('index.html', error='Invalid username or password. Please try again.')

    # If it's a GET request or no form submission yet, render the login/signup page
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # You can add code here to handle the dashboard page logic (if needed)
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
