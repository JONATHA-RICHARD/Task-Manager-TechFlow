from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []
next_id = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.json
    task = {
        "id": next_id,
        "title": data.get("title"),
        "description": data.get("description"),
        "status": "To Do",
        "priority": data.get("priority", "Normal")
    }
    next_id += 1
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    priority = request.args.get('priority')
    result = tasks
    if priority:
        result = [t for t in tasks if t["priority"] == priority]
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)

