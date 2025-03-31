from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
    {
        'id': 1 ,
        'title': 'Web Developer',
        'location': 'Monrovia, Liberia',
        'salary': '$2,000,000',
        'type' : 'Full-time'
    },
    {
        'id': 2,
        'title': 'Data Analysis',
        'location': 'Gbarnga, Liberia',
        'salary': '$1,500,000',
        'type': 'Full-time'
    },
    {
        'id': 3,
        'title': 'Data Scientist',
        'location': 'Ganta, Liberia',
        'salary': '$15,000',
        'type' :'Full-time'
    },
    {
        'id': 4,
        'title': 'Data Entry',
        'location': 'Buchanan, Liberia',
        'salary': '$15,000',
        'type': 'Full-time'
    }
]
@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)
    
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)