# Olympic History Athletes API

## Setup

### Environment Variables
Setup the environments variables:
<code>
    <p>DJANGO_SETTINGS_MODULE=olympic_history_athletes.envs.dev;
    <p>KAGGLE_USERNAME={kaggle_username};
    <p>KAGGLE_KEY={kaggle_key}
</code>
obs: To generate Kaggle credentials: https://github.com/Kaggle/kaggle-api

### Running Migrations
After created your <b>virtual environment with virtualenv</b>, in the directory of the project enter the commands:
<code>
<p>pip install -r requirements.txt
<p>python manage.py makemigrations
<p>python manage.py migrate
<p>python manage.py runserver
</code>
obs: The database still without data

### Tasks
To run the routine to get the csv from Kaggle and populate the database, it necessary run the command:
<p><code>python manage.py process_tasks</code>
<p>The tasks will be schedule to run everyday inserting 50 new objects.


<h2>Methods</h2>
<p>
<h3>Update</h3>
To UPDATE some object use the PUT http method:
<p>PUT https://olympic-history-athletes.herokuapp.com/api/{category}/{id}/

<p>Example:
<p>PUT https://olympic-history-athletes.herokuapp.com/api/sport/1
<p>payload:
<p><code>{"name": "car"}</code>

<h3>Delete</h3>
To DELETE some object use the DELETE http method:
<p>DELETE https://olympic-history-athletes.herokuapp.com/api/{category}/{id}/

<p>Example:
<p>DELETE https://olympic-history-athletes.herokuapp.com/api/sport/1

<h3>Insert</h3>
To CREATE some object use the DELETE http method:
<p>POST https://olympic-history-athletes.herokuapp.com/api/{category}

<p>Example:
<p>POST https://olympic-history-athletes.herokuapp.com/api/sport
<p>payload:
<p><code>{"name": "test"}</code>


<h2>Filtering Attributes</h2>
To filter attribute make a request to endpoint /api/<category>?name=<attribute>

<p>Example:
<p>https://olympic-history-athletes.herokuapp.com/api/sport/?name=Judo


<h2>Filtering Athletes</h2>
To filter athlete make a request to endpoint /api/athletes_search?<params>
<p>Not work searching by the parameter id, just for the name.
<p>It's able to put multiple filter.
<p>Example:
<p>https://olympic-history-athletes.herokuapp.com/api/athletes_search?medal=Silver&season=Summer

<h3>Available filters:</h3>
<ul>
  <li>games</li>
  <li>team</li>
  <li>season</li>
  <li>city</li>
  <li>sport</li>
  <li>event</li>
  <li>medal</li>
</ul>
