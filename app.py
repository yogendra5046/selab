from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# In-memory task storage
tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task")
    if task_name:
        tasks.append({"id": len(tasks) + 1, "name": task_name})
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/api/tasks", methods=["POST"])
def add_task_api():
    data = request.json
    if "name" in data:
        task = {"id": len(tasks) + 1, "name": data["name"]}
        tasks.append(task)
        return jsonify(task), 201
    return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
