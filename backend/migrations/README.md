Single-database configuration for Flask.

	**How to set up a database from scratch?**
1. Clone the repository `meetingbook` to your local machine
	`git clone https://github.com/meetingbook/meetingbook`

2. Install a virtual environment if not done before:[virtualenv](https://virtualenv.pypa.io/en/latest/index.html)
Go to `backend` folder and install:
	`python3 -m venv <name_venv>`

3. Activate venv:
	`source <name_venv>/Scripts/activate`

4. Install all dependencies from `requirements.txt`: 
	`pip3 install -r requirements.txt`

5. Provide the `FLASK_APP` environment variable:
	`export FLASK_APP=server/app.py` or
	`set FLASK_APP=server/app.py`

6. Create a database:
		`flask db upgrade`

7. Well done!

	**How to create a new migration (version of the database)**
	(For example what should we do if we need to add a new table.)
1. Create a table using code. For example:
	```class GrumpyCat(db.Model):
    	__tablename__ = 'GrumpyCat'
    	cat_paw = db.Column(db.Integer, primary_key=True)
    	tail = db.Column(db.String(50), unique=True, nullable=False)
    	mustache = db.Column(db.String(500), nullable=False)```

2. To create migration use:
	`flask db migrate`

3. To apply changes to the table use:
	`flask db upgrade`

4. Well done!
