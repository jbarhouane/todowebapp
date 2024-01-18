from flask import Flask, render_template
from flask import request, redirect, url_for
from task_manager import TaskManager
from database import Database

app = Flask(__name__)

# Initialize database and task manager
db = Database('todo.db')
task_manager = TaskManager(db)

@app.route('/')
def index():
    tasks = task_manager.display_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        description = request.form['description']
        priority = request.form['priority']
        task_manager.add_task(int(priority), description)
        return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task_manager.remove_task(task_id)
    return redirect(url_for('index'))

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
