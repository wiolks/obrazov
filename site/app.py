from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key'

users = {'vitya38rus': '123'}
progress = {
    'vitya38rus': {'points': 100, 'level': 1, 'tests': 0, 'tasks': 0},
    '1st_Ch1ller': {'points': 1818, 'level': 9, 'tests': 9, 'tasks': 2},
    'sema228moris': {'points': 500, 'level': 5, 'tests': 0, 'tasks': 0},
    'WW': {'points': 1235, 'level': 6, 'tests': 11, 'tasks': 244},
    'rt2': {'points': 322, 'level': 4, 'tests': 2, 'tasks': 2},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['user'] = username
            flash('Вы успешно вошли в систему!', 'success')
            return redirect('/dashboard')
        else:
            flash('Неверный логин или пароль', 'danger')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    
    user = session['user']
    user_progress = progress.get(user, {'points': 0, 'level': 1, 'tests': 0, 'tasks': 0})
    
    return render_template('dashboard.html', 
                         username=user,
                         points=user_progress['points'],
                         level=user_progress['level'],
                         tests=user_progress['tests'],
                         tasks=user_progress['tasks'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Вы вышли из системы', 'info')
    return redirect('/')

@app.route('/tests')
def tests():
    if 'user' not in session:
        return redirect('/login')
    return render_template('tests.html')

@app.route('/tasks')
def tasks():
    if 'user' not in session:
        return redirect('/login')
    return render_template('tasks.html')

@app.route('/leaderboard')
def leaderboard():
    sorted_users = sorted(progress.items(), key=lambda x: x[1]['points'], reverse=True)
    return render_template('leaderboard.html', users=sorted_users)

@app.route('/math')
def math():
    if 'user' not in session:
        return redirect('/login')
    return render_template('math.html')

@app.route('/chim')
def chim():
    if 'user' not in session:
        return redirect('/login')
    return render_template('chim.html')

@app.route('/yes')
def yes():
    if 'user' not in session:
        return redirect('/login')
    return render_template('yes.html')

@app.route('/no')
def no():
    if 'user' not in session:
        return redirect('/login')
    return render_template('no.html')

if __name__ == '__main__':
    app.run(debug=True)
