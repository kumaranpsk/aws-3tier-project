from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Arun", "role": "Cloud Engineer"},
    {"id": 2, "name": "Priya", "role": "DevOps Engineer"},
    {"id": 3, "name": "Kumar", "role": "Software Engineer"}
]


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS Employee Portal</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #eef2f7;
                margin: 0;
                padding: 40px;
            }
            .container {
                max-width: 750px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
            }
            h1 { color: #1565c0; }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 12px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }
            th { background: #1565c0; color: white; }
            .badge {
                background: #e3f2fd;
                padding: 6px;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AWS Employee Portal</h1>
            <p>My first AWS Cloud project!</p>
            <h2>Employee Directory</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Role</th>
                </tr>
                {% for employee in employees %}
                <tr>
                    <td>{{ employee.id }}</td>
                    <td>{{ employee.name }}</td>
                    <td><span class="badge">{{ employee.role }}</span></td>
                </tr>
                {% endfor %}
            </table>
            <p>Application status: Running</p>
            <p>Hosted on Amazon EC2</p>
        </div>
    </body>
    </html>
    """ .replace(
        "<!-- employee data -->",
        ""
    ) if False else render_employees()


def render_employees():
    from flask import render_template_string

    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS Employee Portal</title>
        <style>
            body { font-family: Arial; background: #eef2f7; padding: 40px; }
            main { max-width: 750px; margin: auto; background: white;
                   padding: 30px; border-radius: 12px; }
            h1 { color: #1565c0; }
            table { width: 100%; border-collapse: collapse; }
            th, td { padding: 12px; border-bottom: 1px solid #ddd; text-align: left; }
            th { background: #1565c0; color: white; }
        </style>
    </head>
    <body>
      <main>
        <h1>AWS Employee Portal</h1>
        <p>My first AWS Cloud project!</p>
        <h2>Employee Directory</h2>
        <table>
          <tr><th>ID</th><th>Name</th><th>Role</th></tr>
          {% for employee in employees %}
          <tr>
            <td>{{ employee.id }}</td>
            <td>{{ employee.name }}</td>
            <td>{{ employee.role }}</td>
          </tr>
          {% endfor %}
        </table>
        <p>Application status: Running</p>
        <p>Hosted on Amazon EC2</p>
      </main>
    </body>
    </html>
    """

    return render_template_string(template, employees=employees)


@app.route("/api/employees")
def employee_api():
    return jsonify(employees)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
