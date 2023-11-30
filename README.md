# Restaurant

### Prerequisites
1. python installed on your machine(3.8+)

### setting up the project
1. setup virtualenv
2. switch into the virtualenv
3. Install the required modules <code>pip install -r requirements.txt</code>
4. perform migrations <code>python manage.py makemigrations</code>
5. migrate the database <code>python manage.py migrate</code>

### run the project
1. run the project by running the command <code>python manage.py runserver</code>
2. By default the port is 8000 but if you want to run on another port enter the port number after the runserver ( e.g <code>python manage.py runserver 8001 </code> it runs the project on 8001 port )

### setting up virtual env in fedora
1. Run the command <code>python -m venv myenv</code> this command creates an virtual environment
2. Now activate the virtual environment <code>source myenv/bin/activate</code>
3. Install the required modules by running the command <code>pip install -r requirements.txt</code>

## DEMO
<code>http://rajeshkanugu.pythonanywhere.com/</code>
